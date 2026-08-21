import streamlit as st
import sqlite3
import pandas as pd
import datetime
from datetime import date, timedelta
import json
import time
import os
import io
import contextlib
import urllib.request
import hashlib
import random

# ==========================================
# ページ基本設定
# ==========================================
st.set_page_config(
    page_title="TechMaster for Business | 非エンジニアのためのAI・DX・セキュリティ・Python即答マスター",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

TECH_DB_PATH = "tech_master.db"

# ==========================================
# クラウド自動同期エンジン (PC ⇄ スマホ)
# ==========================================
CLOUD_SYNC_API = "https://api.restful-api.dev/objects"
CLOUD_HEADERS = {"Content-Type": "application/json", "User-Agent": "TechMasterApp/1.0"}

def get_sync_key_hash(sync_key: str) -> str:
    if not sync_key:
        return ""
    return hashlib.sha256(sync_key.strip().lower().encode("utf-8")).hexdigest()[:16]

def init_tech_db():
    if not os.path.exists(TECH_DB_PATH):
        try:
            import generate_tech_master_data
            generate_tech_master_data.init_and_seed_tech_master_db(TECH_DB_PATH)
        except Exception:
            pass

def get_user_state_kv(key: str, default: str = "") -> str:
    try:
        init_tech_db()
        conn = sqlite3.connect(TECH_DB_PATH)
        c = conn.cursor()
        c.execute("SELECT value FROM user_state WHERE key = ?", (key,))
        row = c.fetchone()
        conn.close()
        return str(row[0]) if row and row[0] else default
    except Exception:
        return default

def save_user_state_kv(key: str, value: str):
    try:
        init_tech_db()
        conn = sqlite3.connect(TECH_DB_PATH)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO user_state (key, value) VALUES (?, ?)", (key, str(value)))
        conn.commit()
        conn.close()
    except Exception:
        pass

def export_tech_progress_json():
    conn = sqlite3.connect(TECH_DB_PATH)
    data = {
        "version": "1.0",
        "app": "tech_master",
        "exported_at": datetime.datetime.now().isoformat(),
        "tech_terms": pd.read_sql_query("SELECT id, term, repetitions, interval_days, ease_factor, next_review_date, mistake_count FROM tech_terms", conn).to_dict("records"),
        "meeting_scenarios": pd.read_sql_query("SELECT id, title, repetitions, interval_days, ease_factor, next_review_date, mistake_count FROM meeting_scenarios", conn).to_dict("records"),
        "tradeoffs": pd.read_sql_query("SELECT id, title, repetitions, interval_days, ease_factor, next_review_date, mistake_count FROM tradeoffs", conn).to_dict("records"),
        "study_logs": pd.read_sql_query("SELECT card_id, rating, is_correct, reviewed_at, item_type FROM study_logs", conn).to_dict("records"),
        "study_time_logs": pd.read_sql_query("SELECT study_date, seconds, category, item_count, created_at FROM study_time_logs", conn).to_dict("records")
    }
    conn.close()
    return json.dumps(data, ensure_ascii=False, indent=2)

def merge_and_import_tech_progress(data: dict) -> tuple[bool, str]:
    try:
        conn = sqlite3.connect(TECH_DB_PATH)
        cursor = conn.cursor()
        
        # 1. tech_terms マージ
        if "tech_terms" in data:
            for item in data["tech_terms"]:
                cursor.execute("""
                UPDATE tech_terms 
                SET repetitions = MAX(repetitions, ?), 
                    interval_days = MAX(interval_days, ?), 
                    ease_factor = ?, 
                    next_review_date = COALESCE(?, next_review_date), 
                    mistake_count = MAX(mistake_count, ?)
                WHERE term = ? OR id = ?
                """, (item.get("repetitions", 0), item.get("interval_days", 0), item.get("ease_factor", 2.5), item.get("next_review_date"), item.get("mistake_count", 0), item.get("term"), item.get("id")))

        # 2. meeting_scenarios マージ
        if "meeting_scenarios" in data:
            for item in data["meeting_scenarios"]:
                cursor.execute("""
                UPDATE meeting_scenarios 
                SET repetitions = MAX(repetitions, ?), 
                    interval_days = MAX(interval_days, ?), 
                    ease_factor = ?, 
                    next_review_date = COALESCE(?, next_review_date), 
                    mistake_count = MAX(mistake_count, ?)
                WHERE title = ? OR id = ?
                """, (item.get("repetitions", 0), item.get("interval_days", 0), item.get("ease_factor", 2.5), item.get("next_review_date"), item.get("mistake_count", 0), item.get("title"), item.get("id")))

        # 3. tradeoffs マージ
        if "tradeoffs" in data:
            for item in data["tradeoffs"]:
                cursor.execute("""
                UPDATE tradeoffs 
                SET repetitions = MAX(repetitions, ?), 
                    interval_days = MAX(interval_days, ?), 
                    ease_factor = ?, 
                    next_review_date = COALESCE(?, next_review_date), 
                    mistake_count = MAX(mistake_count, ?)
                WHERE title = ? OR id = ?
                """, (item.get("repetitions", 0), item.get("interval_days", 0), item.get("ease_factor", 2.5), item.get("next_review_date"), item.get("mistake_count", 0), item.get("title"), item.get("id")))

        # 4. study_time_logs 合算マージ
        if "study_time_logs" in data:
            cursor.execute("SELECT created_at FROM study_time_logs WHERE created_at IS NOT NULL")
            existing_time_logs = {r[0] for r in cursor.fetchall()}
            for item in data["study_time_logs"]:
                c_at = item.get("created_at")
                if c_at and c_at not in existing_time_logs:
                    cursor.execute("""
                    INSERT INTO study_time_logs (study_date, seconds, category, item_count, created_at)
                    VALUES (?, ?, ?, ?, ?)
                    """, (item.get("study_date"), item.get("seconds", 0.0), item.get("category", "tech"), item.get("item_count", 1), c_at))
                    existing_time_logs.add(c_at)

        conn.commit()
        conn.close()
        return True, "🎉 クラウドとローカルの学習進捗・時間が正常に同期されました！"
    except Exception as e:
        return False, f"同期エラー: {str(e)}"

def push_tech_to_cloud(sync_key: str, cloud_obj_id: str = None) -> str:
    try:
        if not sync_key:
            return ""
        key_hash = get_sync_key_hash(sync_key)
        export_dict = json.loads(export_tech_progress_json())
        
        payload = {
            "name": f"tech_sync_{key_hash}",
            "data": {
                "sync_key": sync_key,
                "sync_key_hash": key_hash,
                "updated_at": time.time(),
                "progress_data": export_dict
            }
        }
        
        if cloud_obj_id:
            url = f"{CLOUD_SYNC_API}/{cloud_obj_id}"
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=CLOUD_HEADERS, method="PUT")
            try:
                with urllib.request.urlopen(req, timeout=6) as res:
                    return cloud_obj_id
            except Exception:
                pass
                
        req = urllib.request.Request(CLOUD_SYNC_API, data=json.dumps(payload).encode("utf-8"), headers=CLOUD_HEADERS, method="POST")
        with urllib.request.urlopen(req, timeout=6) as res:
            obj = json.loads(res.read().decode("utf-8"))
            new_id = obj["id"]
            return new_id
    except Exception:
        return ""

def pull_tech_from_cloud(cloud_obj_id: str) -> tuple[bool, str]:
    try:
        if not cloud_obj_id:
            return False, "クラウドIDが指定されていません"
        url = f"{CLOUD_SYNC_API}/{cloud_obj_id}"
        req = urllib.request.Request(url, headers=CLOUD_HEADERS, method="GET")
        with urllib.request.urlopen(req, timeout=6) as res:
            obj = json.loads(res.read().decode("utf-8"))
            progress_data = obj.get("data", {}).get("progress_data")
            if progress_data:
                return merge_and_import_tech_progress(progress_data)
            return False, "データが空でした"
    except Exception as e:
        return False, f"エラー: {str(e)}"

def trigger_tech_cloud_sync():
    sync_key = st.session_state.get("tech_sync_key", "")
    cloud_id = st.session_state.get("tech_sync_id", "")
    if sync_key:
        new_id = push_tech_to_cloud(sync_key, cloud_id)
        if new_id and new_id != cloud_id:
            st.session_state.tech_sync_id = new_id
            save_user_state_kv("tech_sync_id", new_id)

def record_tech_study_time(seconds, category="tech", item_count=1):
    try:
        init_tech_db()
        today_str = date.today().isoformat()
        now_str = datetime.datetime.now().isoformat()
        sec = max(0.5, float(seconds))
        conn = sqlite3.connect(TECH_DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO study_time_logs (study_date, seconds, category, item_count, created_at)
        VALUES (?, ?, ?, ?, ?)
        ''', (today_str, sec, category, item_count, now_str))
        conn.commit()
        conn.close()
        trigger_tech_cloud_sync()
    except Exception:
        pass

def get_tech_study_stats():
    init_tech_db()
    today_str = date.today().isoformat()
    conn = sqlite3.connect(TECH_DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(seconds), SUM(item_count) FROM study_time_logs WHERE study_date = ?", (today_str,))
    t_row = cursor.fetchone()
    today_sec = float(t_row[0]) if t_row and t_row[0] else 0.0
    today_items = int(t_row[1]) if t_row and t_row[1] else 0
    
    cursor.execute("SELECT SUM(seconds), SUM(item_count) FROM study_time_logs")
    tot_row = cursor.fetchone()
    total_sec = float(tot_row[0]) if tot_row and tot_row[0] else 0.0
    total_items = int(tot_row[1]) if tot_row and tot_row[1] else 0
    
    cursor.execute("SELECT DISTINCT study_date FROM study_time_logs WHERE seconds >= 10 ORDER BY study_date DESC")
    study_dates = [datetime.datetime.strptime(r[0], "%Y-%m-%d").date() for r in cursor.fetchall()]
    
    streak = 0
    curr_d = date.today()
    if study_dates:
        if study_dates[0] == curr_d:
            streak = 1
            idx = 1
            check_d = curr_d - timedelta(days=1)
            while idx < len(study_dates) and study_dates[idx] == check_d:
                streak += 1
                idx += 1
                check_d -= timedelta(days=1)
        elif study_dates[0] == curr_d - timedelta(days=1):
            streak = 1
            idx = 1
            check_d = curr_d - timedelta(days=2)
            while idx < len(study_dates) and study_dates[idx] == check_d:
                streak += 1
                idx += 1
                check_d -= timedelta(days=1)
                
    cursor.execute("SELECT COUNT(*) FROM tech_terms WHERE repetitions >= 3")
    mastered_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM tech_terms")
    total_terms_count = cursor.fetchone()[0]
    
    conn.close()
    return {
        "today_sec": today_sec,
        "today_items": today_items,
        "total_sec": total_sec,
        "total_items": total_items,
        "streak": streak,
        "mastered_count": mastered_count,
        "total_terms_count": total_terms_count
    }

# ==========================================
# 忘却曲線 (SM-2 + 秒数連動 Smart SRS)
# ==========================================
def calculate_smart_srs(repetitions, interval_days, ease_factor, mistake_count, elapsed_sec, is_correct=True):
    if not is_correct:
        new_ef = max(1.3, ease_factor - 0.2)
        new_reps = 0
        new_interval = 1
        rating = 1
        label = "⚠️ 復習要 (明日再出題)"
        detail = f"想起失敗 / 所要時間: {elapsed_sec}秒 ➔ 間隔を1日にリセット"
    else:
        if elapsed_sec <= 3.0:
            rating = 4
            ef_delta = 0.15
            label = "⚡ 瞬発即答 (完璧！)"
        elif elapsed_sec <= 7.0:
            rating = 3
            ef_delta = 0.0
            label = "🟢 スムーズな想起"
        else:
            rating = 2
            ef_delta = -0.15
            label = "🟡 想起に時間を要した"
            
        new_ef = max(1.3, ease_factor + ef_delta)
        new_reps = repetitions + 1
        
        if new_reps == 1:
            new_interval = 1
        elif new_reps == 2:
            new_interval = 3 if rating >= 3 else 2
        else:
            multiplier = new_ef * (1.2 if rating == 4 else 1.0)
            new_interval = max(int(interval_days * multiplier), interval_days + 1)
            
        detail = f"想起成功 (所要: {elapsed_sec}秒) ➔ 次回復習: {new_interval}日後 (EF: {new_ef:.2f})"
        
    next_date = (date.today() + timedelta(days=new_interval)).isoformat()
    return new_reps, new_interval, new_ef, next_date, rating, label, detail

# ==========================================
# サイドバー & クラウド同期 UI
# ==========================================
init_tech_db()

query_params = st.query_params
q_sync = query_params.get("sync")
q_id = query_params.get("id")

if "tech_sync_key" not in st.session_state:
    st.session_state.tech_sync_key = q_sync if q_sync else get_user_state_kv("tech_sync_key", "")
if "tech_sync_id" not in st.session_state:
    st.session_state.tech_sync_id = q_id if q_id else get_user_state_kv("tech_sync_id", "")

if "tech_sync_initialized" not in st.session_state:
    st.session_state.tech_sync_initialized = True
    if st.session_state.tech_sync_id:
        pull_tech_from_cloud(st.session_state.tech_sync_id)

st.sidebar.title("👔 TechMaster OS")
st.sidebar.caption("非エンジニアのための AI・DX・セキュリティ・Python 即戦力マスター")

# クラウド同期パネル
with st.sidebar.expander("☁️ 端末クラウド自動同期 (PC ⇄ スマホ)", expanded=(not bool(st.session_state.tech_sync_key))):
    if not st.session_state.tech_sync_key:
        st.markdown("<div style='font-size:0.85rem; color:#475569; margin-bottom:8px;'>合言葉を決めて入力すると、PCとスマホで<b>学習時間と進捗が全自動で合算・同期</b>されます！</div>", unsafe_allow_html=True)
        in_sync_key = st.text_input("🔑 合言葉 (同期キー)", placeholder="例: tanaka-dx-2026", key="in_tech_sync_key")
        if st.button("🚀 同期を開始する", type="primary", use_container_width=True):
            if in_sync_key.strip():
                st.session_state.tech_sync_key = in_sync_key.strip()
                save_user_state_kv("tech_sync_key", in_sync_key.strip())
                new_c_id = push_tech_to_cloud(in_sync_key.strip())
                st.session_state.tech_sync_id = new_c_id
                save_user_state_kv("tech_sync_id", new_c_id)
                st.query_params["sync"] = in_sync_key.strip()
                st.query_params["id"] = new_c_id
                st.success("🎉 クラウド自動同期が有効化されました！")
                st.rerun()
    else:
        st.markdown(f"<div style='background-color:#dcfce7; color:#15803d; padding:6px 12px; border-radius:6px; font-weight:bold; font-size:0.9rem; margin-bottom:8px;'>🟢 自動同期中: <code>{st.session_state.tech_sync_key}</code></div>", unsafe_allow_html=True)
        st.caption("📱 **スマホでこのURLを開くだけで自動同期完了:**")
        share_url = f"?sync={st.session_state.tech_sync_key}&id={st.session_state.tech_sync_id}"
        st.code(share_url, language="text")
        
        sc1, sc2 = st.columns(2)
        with sc1:
            if st.button("🔄 今すぐ同期", use_container_width=True):
                if st.session_state.tech_sync_id:
                    pull_tech_from_cloud(st.session_state.tech_sync_id)
                push_tech_to_cloud(st.session_state.tech_sync_key, st.session_state.tech_sync_id)
                st.success("同期完了！")
                st.rerun()
        with sc2:
            if st.button("🔌 同期解除", use_container_width=True):
                st.session_state.tech_sync_key = ""
                st.session_state.tech_sync_id = ""
                save_user_state_kv("tech_sync_key", "")
                save_user_state_kv("tech_sync_id", "")
                if "sync" in st.query_params:
                    del st.query_params["sync"]
                if "id" in st.query_params:
                    del st.query_params["id"]
                st.rerun()

menu = st.sidebar.radio(
    "🧭 学習メニュー",
    [
        "🧩 Python 初級〜実務 4択クイズ特訓 (選択式)",
        "💻 Python 実践コード入力テスト道場 (入力式)",
        "🐍 Python 超入門〜実務マスター (用語カード)",
        "🗂️ 例え話で学ぶ！用語 Smart SRS (忘却曲線)",
        "🛡️ 会議・商談 リアル想定問答プラクティス",
        "⚖️ どっちを選ぶ？ 2択トレードオフ判断ドリル",
        "⚡ 打ち合わせ直前 30秒カンペ (チートシート)",
        "⌨️ 略語・IT用語 スペリング＆タイピング特訓",
        "🔀 5大分野 インターリービング実戦シャッフル",
        "📊 学習進捗ダッシュボード ＆ 💾 バックアップ"
    ]
)

# ==========================================
# 統計ヘッダー表示
# ==========================================
stats = get_tech_study_stats()
t_min = int(stats["today_sec"] // 60)
t_sec = int(stats["today_sec"] % 60)
tot_min = int(stats["total_sec"] // 60)

header_html = f"""<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:14px 20px; box-shadow:0 2px 4px rgba(0,0,0,0.03); margin-bottom:20px; display:flex; justify-content:space-around; align-items:center; flex-wrap:wrap; gap:12px;">
<div style="text-align:center;">
<div style="font-size:0.8rem; color:#64748b; font-weight:bold;">⏱️ 本日の学習時間</div>
<div style="font-size:1.3rem; font-weight:800; color:#0284c7;">{t_min}分 {t_sec}秒 <span style="font-size:0.9rem; color:#64748b;">({stats['today_items']}問)</span></div>
</div>
<div style="text-align:center;">
<div style="font-size:0.8rem; color:#64748b; font-weight:bold;">⏳ 累計学習時間</div>
<div style="font-size:1.3rem; font-weight:800; color:#1e293b;">{tot_min}分 <span style="font-size:0.9rem; color:#64748b;">({stats['total_items']}問)</span></div>
</div>
<div style="text-align:center;">
<div style="font-size:0.8rem; color:#64748b; font-weight:bold;">🔥 継続ストリーク</div>
<div style="font-size:1.3rem; font-weight:800; color:#ea580c;">{stats['streak']} 日連続</div>
</div>
<div style="text-align:center;">
<div style="font-size:0.8rem; color:#64748b; font-weight:bold;">🧠 定着済み用語</div>
<div style="font-size:1.3rem; font-weight:800; color:#16a34a;">{stats['mastered_count']} / {stats['total_terms_count']} 語</div>
</div>
</div>"""
st.markdown(header_html, unsafe_allow_html=True)

# ==========================================
# 0. 🧩 Python 初級〜実務 4択クイズ特訓 (選択式)
# ==========================================
if menu == "🧩 Python 初級〜実務 4択クイズ特訓 (選択式)":
    st.title("🧩 Python 初級〜実務 4択クイズ特訓 (選択式)")
    st.caption("スマホ片手でサクサク解ける！基本文法、コードの実行結果予測、データ型、Pandasの使い方まで、四択クイズで直感的にマスターできます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    try:
        df_quizzes = pd.read_sql_query("SELECT * FROM python_quiz_questions", conn)
    except Exception:
        import seed_python_quizzes
        seed_python_quizzes.init_and_seed_python_quizzes(TECH_DB_PATH)
        df_quizzes = pd.read_sql_query("SELECT * FROM python_quiz_questions", conn)
    conn.close()

    if len(df_quizzes) == 0:
        st.info("クイズデータを読み込み中です。少々お待ちください。")
    else:
        lvl_list = ["🌟 全レベルから出題 (推奨)"] + list(df_quizzes["level"].unique())
        sel_lvl = st.selectbox("🎯 レベルを選択してください：", lvl_list, key="sel_quiz_level")

        if sel_lvl == "🌟 全レベルから出題 (推奨)":
            quiz_df = df_quizzes.sort_values("id")
        else:
            quiz_df = df_quizzes[df_quizzes["level"] == sel_lvl].sort_values("id")

        if "pq_idx" not in st.session_state or st.session_state.pq_idx >= len(quiz_df):
            st.session_state.pq_idx = 0
            st.session_state.pq_answered = False
            st.session_state.pq_selected = None

        q_item = quiz_df.iloc[st.session_state.pq_idx]

        st.caption(f"クイズ特訓中：残り {len(quiz_df) - st.session_state.pq_idx} / {len(quiz_df)} 問（対象全 {len(quiz_df)} 問）")
        st.progress((st.session_state.pq_idx + 1) / len(quiz_df))

        if "pq_start_time" not in st.session_state or st.session_state.get("pq_current_id") != q_item["id"]:
            st.session_state.pq_start_time = time.time()
            st.session_state.pq_current_id = int(q_item["id"])
            st.session_state.pq_answered = False
            st.session_state.pq_selected = None

        code_snippet_html = ""
        if q_item.get("code_snippet") and str(q_item["code_snippet"]).strip():
            code_snippet_html = f"""<pre style="background:#1e293b; color:#38bdf8; padding:14px; border-radius:8px; font-family:monospace; font-size:1.05rem; margin:12px 0;">{q_item['code_snippet']}</pre>"""

        quiz_q_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #8b5cf6; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
<span style="background:#ede9fe; color:#6d28d9; padding:4px 12px; border-radius:16px; font-size:0.85rem; font-weight:bold;">{q_item['level']}</span>
<span style="font-size:0.9rem; color:#64748b;">第 {st.session_state.pq_idx + 1} 問 / {len(quiz_df)}</span>
</div>
<h3 style="color:#0f172a; margin-top:0; font-size:1.35rem; line-height:1.5;">❓ {q_item['question']}</h3>
{code_snippet_html}
<div style="font-size:1.0rem; color:#64748b;">
👉 正しい選択肢を1つ選んでください：
</div>
</div>"""
        st.markdown(quiz_q_html, unsafe_allow_html=True)

        raw_opts = [o.strip() for o in str(q_item["options"]).split(",") if o.strip()]
        correct_ans = str(q_item["correct_answer"]).strip()

        if not st.session_state.get("pq_answered", False):
            # 2列グリッドで押しやすく配置
            q_c1, q_c2 = st.columns(2)
            for i, opt in enumerate(raw_opts):
                target_col = q_c1 if (i % 2 == 0) else q_c2
                with target_col:
                    if st.button(opt, key=f"pq_opt_{q_item['id']}_{i}", use_container_width=True):
                        st.session_state.pq_selected = opt
                        st.session_state.pq_answered = True
                        st.session_state.pq_elapsed = max(0.1, round(time.time() - st.session_state.pq_start_time, 1))
                        st.rerun()
        else:
            user_choice = str(st.session_state.get("pq_selected", "")).strip()
            is_right = (user_choice.lower() == correct_ans.lower()) or (user_choice in correct_ans) or (correct_ans in user_choice)
            res_bg = "#f0fdf4" if is_right else "#fef2f2"
            res_bdr = "#16a34a" if is_right else "#dc2626"
            res_title = "🎉 完璧！正解です！" if is_right else "⚠️ 惜しい！別の選択肢です。"

            quiz_res_html = f"""<div style="background:{res_bg}; border:2px solid {res_bdr}; padding:20px; border-radius:10px; margin-bottom:16px;">
<div style="font-size:1.25rem; font-weight:bold; color:{res_bdr}; margin-bottom:8px;">{res_title}</div>
<div style="font-size:1.05rem; color:#334155; margin-bottom:10px;">
あなたの回答: <b>{user_choice}</b> ｜ 正解: <b style="color:#15803d;">{correct_ans}</b>
</div>
<hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">
<div style="font-size:1.0rem; color:#1e293b; line-height:1.7;">
💡 <b>解説:</b> {q_item['explanation']}
</div>
</div>"""
            st.markdown(quiz_res_html, unsafe_allow_html=True)

            record_tech_study_time(float(st.session_state.get("pq_elapsed", 3.0)), "python_quiz", 1)

            if st.button("⭕️ 次のクイズへ進む ➡️", type="primary", use_container_width=True):
                st.session_state.pq_idx = (st.session_state.pq_idx + 1) % len(quiz_df)
                st.session_state.pq_answered = False
                st.session_state.pq_selected = None
                st.session_state.pq_start_time = time.time()
                st.rerun()

# ==========================================
# 1. 💻 Python 実践コード入力テスト道場
# ==========================================
elif menu == "💻 Python 実践コード入力テスト道場 (入力式)":
    st.title("💻 Python 実践コード入力テスト道場 (初級〜実務)")
    st.caption("実際にキーボードでPythonの基本コードを書いて、実行＆判定する実践トレーニングです。穴埋め・コード入力でプログラミングの指の記憶を定着させます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    try:
        df_code_tests = pd.read_sql_query("SELECT * FROM python_code_tests", conn)
    except Exception:
        import seed_python_code_tests
        seed_python_code_tests.init_and_seed_code_tests(TECH_DB_PATH)
        df_code_tests = pd.read_sql_query("SELECT * FROM python_code_tests", conn)
    conn.close()

    if len(df_code_tests) == 0:
        st.info("コードテストデータを読み込み中です。少々お待ちください。")
    else:
        lvl_list = ["🌟 全問にチャレンジ (推奨)"] + list(df_code_tests["level"].unique())
        sel_lvl = st.selectbox("🎯 レベルを選択してください：", lvl_list, key="code_test_level_sel")

        if sel_lvl == "🌟 全問にチャレンジ (推奨)":
            test_df = df_code_tests.sort_values("id")
        else:
            test_df = df_code_tests[df_code_tests["level"] == sel_lvl].sort_values("id")

        if "ct_idx" not in st.session_state or st.session_state.ct_idx >= len(test_df):
            st.session_state.ct_idx = 0
            st.session_state.ct_submitted = False
            st.session_state.ct_user_code = ""

        q_card = test_df.iloc[st.session_state.ct_idx]

        st.caption(f"コードテスト中：残り {len(test_df) - st.session_state.ct_idx} / {len(test_df)} 問（対象全 {len(test_df)} 問）")
        st.progress((st.session_state.ct_idx + 1) / len(test_df))

        if "ct_start_time" not in st.session_state or st.session_state.get("ct_current_id") != q_card["id"]:
            st.session_state.ct_start_time = time.time()
            st.session_state.ct_current_id = int(q_card["id"])
            st.session_state.ct_submitted = False
            st.session_state.ct_user_code = ""

        q_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #3b82f6; padding:22px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
<span style="background:#dbeafe; color:#1e40af; padding:4px 12px; border-radius:16px; font-size:0.85rem; font-weight:bold;">{q_card['level']}</span>
<span style="font-size:0.9rem; color:#64748b;">問題 {st.session_state.ct_idx + 1} / {len(test_df)}</span>
</div>
<h3 style="color:#0f172a; margin-top:0; font-size:1.35rem;">{q_card['title']}</h3>
<div style="font-size:1.15rem; font-weight:bold; color:#1e293b; line-height:1.6; background:#f8fafc; padding:16px; border-radius:8px; border-left:4px solid #3b82f6; margin-bottom:12px;">
📝 <b>お題:</b> {q_card['instruction']}
</div>
</div>"""
        st.markdown(q_html, unsafe_allow_html=True)

        with st.expander("💡 ヒント（クリックで開く）"):
            st.info(q_card["hint"])

        with st.form(key=f"ct_form_{q_card['id']}"):
            u_code = st.text_area(
                "⌨️ Pythonコードを入力してください:",
                value=st.session_state.get("ct_user_code", ""),
                height=100,
                placeholder="ここにコードを入力...",
                key=f"code_input_field_{q_card['id']}"
            )
            c1, c2 = st.columns([2, 1])
            with c1:
                b_check = st.form_submit_button("🔥 判定＆実行する", type="primary", use_container_width=True)
            with c2:
                b_clear = st.form_submit_button("🧹 クリア", use_container_width=True)

        if b_clear:
            st.session_state.ct_user_code = ""
            st.session_state.ct_submitted = False
            st.rerun()

        if b_check:
            st.session_state.ct_user_code = u_code
            st.session_state.ct_submitted = True
            st.session_state.ct_elapsed = max(0.1, round(time.time() - st.session_state.ct_start_time, 1))
            st.rerun()

        if st.session_state.get("ct_submitted", False):
            user_raw = st.session_state.get("ct_user_code", "").strip()
            target_raw = str(q_card["canonical_code"]).strip()

            def normalize_code(c):
                lines = [l.strip() for l in c.strip().split("\n") if l.strip()]
                norm = "\n".join(lines).replace("'", '"').replace(" ", "")
                return norm

            is_correct = (normalize_code(user_raw) == normalize_code(target_raw))

            exec_output = ""
            exec_error = ""
            try:
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    test_scope = {
                        "name": "太郎",
                        "first_name": "太郎",
                        "last_name": "山田",
                        "score": 85,
                        "fruits": ["りんご", "バナナ"],
                        "items": ["商品A", "商品B", "商品C"],
                        "user": {"name": "田中", "age": 30},
                        "numbers": [1, 2, 3, 4, 5],
                        "calc": lambda: 100
                    }
                    exec(user_raw, test_scope)
                exec_output = buffer.getvalue().strip()
            except Exception as e:
                exec_error = str(e)

            res_bg = "#f0fdf4" if is_correct else "#fef2f2"
            res_bdr = "#16a34a" if is_correct else "#dc2626"
            res_title = "🎉 完璧！正解です！" if is_correct else "⚠️ 惜しい！コードを確認しましょう。"

            res_html = f"""<div style="background:{res_bg}; border:2px solid {res_bdr}; padding:20px; border-radius:10px; margin-bottom:16px;">
<div style="font-size:1.25rem; font-weight:bold; color:{res_bdr}; margin-bottom:8px;">{res_title}</div>
<div style="margin-bottom:8px; font-size:1.0rem; color:#1e293b;">
<b>あなたのコード:</b>
<pre style="background:#ffffff; border:1px solid #cbd5e1; padding:10px; border-radius:6px; font-family:monospace; margin:4px 0;">{user_raw if user_raw else '(未入力)'}</pre>
</div>
<div style="margin-bottom:8px; font-size:1.0rem; color:#1e293b;">
<b>模範正解コード:</b>
<pre style="background:#f0fdf4; border:1px solid #86efac; color:#15803d; padding:10px; border-radius:6px; font-family:monospace; font-weight:bold; margin:4px 0;">{target_raw}</pre>
</div>
<hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">
<div style="font-size:0.95rem; color:#334155; line-height:1.6;">
💡 <b>解説:</b> {q_card['explanation']}
</div>
</div>"""
            st.markdown(res_html, unsafe_allow_html=True)

            if exec_output:
                st.markdown(f"**▶️ 実行結果（出力）:**")
                st.code(exec_output, language="text")
            elif exec_error:
                st.markdown(f"**⚠️ 実行時エラー:**")
                st.error(exec_error)

            record_tech_study_time(float(st.session_state.get("ct_elapsed", 4.0)), "code_test", 1)

            if st.button("⭕️ 次のコード問題へ進む ➡️", type="primary", use_container_width=True):
                st.session_state.ct_idx = (st.session_state.ct_idx + 1) % len(test_df)
                st.session_state.ct_submitted = False
                st.session_state.ct_user_code = ""
                st.session_state.ct_start_time = time.time()
                st.rerun()

# ==========================================
# 2. 🐍 Python 超入門〜実務マスター (用語カード)
# ==========================================
elif menu == "🐍 Python 超入門〜実務マスター (用語カード)":
    st.title("🐍 Python 超入門〜実務マスター (初心者特化カリキュラム)")
    st.caption("プログラミング完全初心者・文系ビジネスパーソン向け！変数やデータ型などの最初の一歩から、Excel自動化・Pandas・スクレイピングまで段階別にマスターできます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_py = pd.read_sql_query("SELECT * FROM tech_terms WHERE category LIKE '%Python%'", conn)
    conn.close()

    py_cats = ["🌟 全レベルを順番に学習 (推奨)"] + list(df_py["category"].unique())
    sel_py_cat = st.selectbox("🎯 学習レベルを選択してください：", py_cats, key="sel_py_level")

    if sel_py_cat == "🌟 全レベルを順番に学習 (推奨)":
        target_py_df = df_py.sort_values("id")
    else:
        target_py_df = df_py[df_py["category"] == sel_py_cat].sort_values("id")

    if len(target_py_df) == 0:
        st.info("対象のPython用語がありません。")
    else:
        if "py_idx" not in st.session_state or st.session_state.py_idx >= len(target_py_df):
            st.session_state.py_idx = 0
            st.session_state.py_revealed = False

        card = target_py_df.iloc[st.session_state.py_idx]

        st.caption(f"Python特訓中：残り {len(target_py_df) - st.session_state.py_idx} / {len(target_py_df)} 語（対象全 {len(target_py_df)} 語）")
        st.progress((st.session_state.py_idx + 1) / len(target_py_df))

        if "py_start_time" not in st.session_state or st.session_state.get("py_current_id") != card["id"]:
            st.session_state.py_start_time = time.time()
            st.session_state.py_current_id = int(card["id"])
            st.session_state.py_revealed = False

        status_lbl = "🌱 未学習" if card["repetitions"] == 0 else f"🔄 復習中 (Lv{card['repetitions']} / 間隔:{card['interval_days']}日)"

        # 表側カード
        front_card_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #10b981; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<span style="background:#d1fae5; color:#065f46; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{card['category']}</span>
<span style="font-size:0.9rem; color:#64748b;">{status_lbl}</span>
</div>
<div style="font-size:2.2rem; font-weight:800; color:#0f172a; margin-bottom:4px;">{card['term']}</div>
<div style="font-size:1.1rem; color:#64748b; margin-bottom:14px;">【 読み: <b>{card['reading']}</b> 】 ｜ 英語: <i>{card['english_full']}</i></div>
<div style="font-size:1.15rem; color:#334155; line-height:1.6; background:#f0fdf4; padding:16px; border-radius:8px; border-left:4px solid #10b981;">
🤔 <b>このPython用語の「日常の例え話」と「実務での使いどころ」は何でしょうか？</b>
</div>
</div>"""
        st.markdown(front_card_html, unsafe_allow_html=True)

        if not st.session_state.py_revealed:
            if st.button("💡 答え・日常の例え・公式定義・コード例を見る", type="primary", use_container_width=True):
                st.session_state.py_elapsed = max(0.1, round(time.time() - st.session_state.py_start_time, 1))
                st.session_state.py_revealed = True
                st.rerun()
        else:
            official_def_section = ""
            if card.get("official_definition") and str(card["official_definition"]).strip():
                official_def_section = f"""<div style="background:#f8fafc; border:1px solid #cbd5e1; border-left:4px solid #475569; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
<div style="font-size:0.85rem; font-weight:bold; color:#475569; margin-bottom:4px;">📖 正確な公式定義:</div>
<div style="font-size:1.0rem; line-height:1.6; color:#1e293b;">{card['official_definition']}</div>
</div>"""

            back_card_html = f"""<div style="background:#fffbeb; border:1px solid #fef3c7; border-left:6px solid #f59e0b; padding:22px; border-radius:12px; margin-bottom:16px;">
<h3 style="color:#b45309; margin-top:0; font-size:1.3rem;">💡 中学生でもわかる日常の例え話:</h3>
<div style="font-size:1.2rem; line-height:1.7; color:#1e293b; font-weight:bold; background:#ffffff; padding:16px; border-radius:8px; border:2px solid #fde68a; margin-bottom:16px;">
{card['metaphor']}
</div>
{official_def_section}
<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:4px solid #2563eb; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
<div style="font-size:0.85rem; font-weight:bold; color:#1d4ed8; margin-bottom:4px;">👔 実務・ビジネスでの活用メリット（なぜ必要なのか？）:</div>
<div style="font-size:1.0rem; line-height:1.6; color:#1e293b;">{card['business_impact']}</div>
</div>
<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4px solid #16a34a; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
<div style="font-size:0.85rem; font-weight:bold; color:#15803d; margin-bottom:4px;">🗣️ 打ち合わせ・開発現場で使える実践フレーズ:</div>
<div style="font-size:1.05rem; line-height:1.6; color:#14532d; font-weight:bold;">{card['meeting_phrase']}</div>
</div>
<div style="background:#fef2f2; border:1px solid #fecaca; border-left:4px solid #dc2626; padding:12px 16px; border-radius:8px;">
<div style="font-size:0.85rem; font-weight:bold; color:#b91c1c; margin-bottom:4px;">⚠️ 初心者がやりがちなミス・注意点:</div>
<div style="font-size:0.95rem; line-height:1.6; color:#991b1b;">{card['pitfall_warning']}</div>
</div>
</div>"""
            st.markdown(back_card_html, unsafe_allow_html=True)

            elapsed_sec = float(st.session_state.get("py_elapsed", 3.0))
            st_reps, st_inv, st_ef, st_next_date, st_rating, st_lbl, st_detail = calculate_smart_srs(
                int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]),
                int(card["mistake_count"]), elapsed_sec, is_correct=True
            )

            record_tech_study_time(elapsed_sec, "python_curriculum", 1)

            if st.button("⭕️ 次のPython用語へ進む ➡️", type="primary", use_container_width=True):
                conn = sqlite3.connect(TECH_DB_PATH)
                c = conn.cursor()
                c.execute("""
                UPDATE tech_terms 
                SET repetitions = repetitions + 1, interval_days = ?, ease_factor = ?, next_review_date = ?
                WHERE id = ?
                """, (st_inv, st_ef, st_next_date, int(card["id"])))
                conn.commit()
                conn.close()

                st.session_state.py_idx += 1
                st.session_state.py_revealed = False
                st.session_state.py_start_time = time.time()
                st.rerun()

# ==========================================
# 3. 🗂️ 例え話で学ぶ！用語 Smart SRS
# ==========================================
elif menu == "🗂️ 例え話で学ぶ！用語 Smart SRS (忘却曲線)":
    st.title("🗂️ 例え話で学ぶ！用語 Smart SRS (忘却曲線)")
    st.caption("小難しいIT定義ではなく『日常の例え話』と『打ち合わせで使える神質問』で、非エンジニアでも直感的に本質が脳に焼き付きます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_terms = pd.read_sql_query("SELECT * FROM tech_terms", conn)
    conn.close()

    today_str = date.today().isoformat()

    f_col1, f_col2 = st.columns([1.5, 1])
    with f_col1:
        cat_list = ["すべて"] + list(df_terms["category"].unique())
        sel_cat = st.selectbox("🏷️ 分野カテゴリー", cat_list, key="term_srs_cat")
    with f_col2:
        scope = st.selectbox("🎯 出題範囲", ["本日の復習待ち ＋ 未学習（推奨）", "全用語から特訓", "苦手用語（ミス多）集中特訓"], key="term_srs_scope")

    filtered_df = df_terms if sel_cat == "すべて" else df_terms[df_terms["category"] == sel_cat]
    if scope == "本日の復習待ち ＋ 未学習（推奨）":
        due_terms = filtered_df[(filtered_df["next_review_date"] <= today_str) | (filtered_df["repetitions"] == 0)].sort_values(["mistake_count", "next_review_date"], ascending=[False, True])
    elif scope == "苦手用語（ミス多）集中特訓":
        due_terms = filtered_df[filtered_df["mistake_count"] > 0].sort_values("mistake_count", ascending=False)
    else:
        due_terms = filtered_df.sample(frac=1, random_state=42) if len(filtered_df) > 0 else filtered_df

    if len(due_terms) == 0:
        st.success(f"🎉 素晴らしい！「{sel_cat}」の復習待ち用語はすべて完了しています！")
        st.balloons()
    else:
        if "srs_term_idx" not in st.session_state or st.session_state.srs_term_idx >= len(due_terms):
            st.session_state.srs_term_idx = 0
            st.session_state.srs_term_revealed = False

        card = due_terms.iloc[st.session_state.srs_term_idx]
        
        st.caption(f"学習中：残り {len(due_terms) - st.session_state.srs_term_idx} / {len(due_terms)} 語（対象全 {len(filtered_df)} 語）")
        st.progress((st.session_state.srs_term_idx + 1) / len(due_terms))

        if "srs_term_start_time" not in st.session_state or st.session_state.get("srs_term_current_id") != card["id"]:
            st.session_state.srs_term_start_time = time.time()
            st.session_state.srs_term_current_id = int(card["id"])
            st.session_state.srs_term_elapsed = 0.0
            st.session_state.srs_term_revealed = False

        status_lbl = "🌱 未学習" if card["repetitions"] == 0 else f"🔄 復習中 (Lv{card['repetitions']} / 間隔:{card['interval_days']}日)"
        if card["repetitions"] >= 4:
            status_lbl = f"🏆 定着済み (Lv{card['repetitions']} / 間隔:{card['interval_days']}日)"

        # 表側カード (Question)
        front_card_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #0284c7; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
<span style="background:#e0f2fe; color:#0369a1; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{card['category']}</span>
<span style="font-size:0.9rem; color:#64748b;">{status_lbl}</span>
</div>
<div style="font-size:2.2rem; font-weight:800; color:#0f172a; margin-bottom:4px;">{card['term']}</div>
<div style="font-size:1.1rem; color:#64748b; margin-bottom:14px;">【 読み: <b>{card['reading']}</b> 】 ｜ 英語: <i>{card['english_full']}</i></div>
<div style="font-size:1.15rem; color:#334155; line-height:1.6; background:#f8fafc; padding:16px; border-radius:8px; border-left:4px solid #0284c7;">
🤔 <b>この用語の本質・例え話と、実務でのメリットは何でしょうか？</b>（頭の中で0.5秒で思い浮かべてください）
</div>
</div>"""
        st.markdown(front_card_html, unsafe_allow_html=True)

        if not st.session_state.srs_term_revealed:
            if st.button("💡 答え・例え話・公式定義・神質問を見る (Enter / Space)", type="primary", use_container_width=True):
                st.session_state.srs_term_elapsed = max(0.1, round(time.time() - st.session_state.srs_term_start_time, 1))
                st.session_state.srs_term_revealed = True
                st.rerun()
        else:
            # 裏側カード
            official_def_section = ""
            if card.get("official_definition") and str(card["official_definition"]).strip():
                official_def_section = f"""<div style="background:#f8fafc; border:1px solid #cbd5e1; border-left:4px solid #475569; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
<div style="font-size:0.85rem; font-weight:bold; color:#475569; margin-bottom:4px;">📖 正確な公式定義（打ち合わせ・資料用）:</div>
<div style="font-size:1.0rem; line-height:1.6; color:#1e293b;">{card['official_definition']}</div>
</div>"""

            back_card_html = f"""<div style="background:#fffbeb; border:1px solid #fef3c7; border-left:6px solid #f59e0b; padding:22px; border-radius:12px; margin-bottom:16px;">
<h3 style="color:#b45309; margin-top:0; font-size:1.3rem;">💡 中学生でもわかる日常の例え話:</h3>
<div style="font-size:1.2rem; line-height:1.7; color:#1e293b; font-weight:bold; background:#ffffff; padding:16px; border-radius:8px; border:2px solid #fde68a; margin-bottom:16px;">
{card['metaphor']}
</div>
{official_def_section}
<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:4px solid #2563eb; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
<div style="font-size:0.85rem; font-weight:bold; color:#1d4ed8; margin-bottom:4px;">👔 ビジネスインパクト（なぜ会社に必要なのか？）:</div>
<div style="font-size:1.0rem; line-height:1.6; color:#1e293b;">{card['business_impact']}</div>
</div>
<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4px solid #16a34a; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
<div style="font-size:0.85rem; font-weight:bold; color:#15803d; margin-bottom:4px;">🗣️ 打ち合わせでそのまま使える「神質問フレーズ」:</div>
<div style="font-size:1.05rem; line-height:1.6; color:#14532d; font-weight:bold;">{card['meeting_phrase']}</div>
</div>
<div style="background:#fef2f2; border:1px solid #fecaca; border-left:4px solid #dc2626; padding:12px 16px; border-radius:8px;">
<div style="font-size:0.85rem; font-weight:bold; color:#b91c1c; margin-bottom:4px;">⚠️ 地雷注意点（知ったかぶりNGポイント）:</div>
<div style="font-size:0.95rem; line-height:1.6; color:#991b1b;">{card['pitfall_warning']}</div>
</div>
</div>"""
            st.markdown(back_card_html, unsafe_allow_html=True)

            elapsed_sec = float(st.session_state.get("srs_term_elapsed", 3.0))
            st_reps, st_inv, st_ef, st_next_date, st_rating, st_lbl, st_detail = calculate_smart_srs(
                int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]),
                int(card["mistake_count"]), elapsed_sec, is_correct=True
            )
            sf_reps, sf_inv, sf_ef, sf_next_date, sf_rating, sf_lbl, sf_detail = calculate_smart_srs(
                int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]),
                int(card["mistake_count"]), elapsed_sec, is_correct=False
            )

            srs_info_html = f"""<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:6px solid #16a34a; padding:12px 18px; border-radius:8px; margin-bottom:16px;">
<span style="font-weight:bold; color:#15803d;">🧠 忘却曲線判定: {st_lbl}</span>
<div style="font-size:0.9rem; color:#334155; margin-top:4px;">{st_detail}</div>
</div>"""
            st.markdown(srs_info_html, unsafe_allow_html=True)

            def submit_term_srs(reps, interval, ef, next_date, mistakes_delta, rating, is_correct):
                record_tech_study_time(elapsed_sec, "term_srs", 1)
                conn = sqlite3.connect(TECH_DB_PATH)
                c = conn.cursor()
                new_m = max(0, int(card["mistake_count"]) + mistakes_delta)
                c.execute("""
                UPDATE tech_terms 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE id = ?
                """, (reps, interval, ef, next_date, new_m, int(card["id"])))
                c.execute("""
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                VALUES (?, ?, ?, ?, 'term_srs')
                """, (int(card["id"]), rating, is_correct, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()

                st.session_state.srs_term_idx += 1
                st.session_state.srs_term_revealed = False
                st.session_state.srs_term_start_time = time.time()
                st.rerun()

            a_col1, a_col2 = st.columns([1.5, 1])
            with a_col1:
                if st.button(f"⭕️ 次の用語へ ({st_inv}日後に再出題 ➡️)", type="primary", use_container_width=True):
                    submit_term_srs(st_reps, st_inv, st_ef, st_next_date, 0, st_rating, 1)
            with a_col2:
                if st.button("❌ 苦手リストに追加して明日復習", use_container_width=True):
                    submit_term_srs(sf_reps, sf_inv, sf_ef, sf_next_date, 1, sf_rating, 0)

# ==========================================
# 4. 🛡️ 会議・商談 リアル想定問答プラクティス
# ==========================================
elif menu == "🛡️ 会議・商談 リアル想定問答プラクティス":
    st.title("🛡️ 会議・商談 リアル想定問答プラクティス (攻防切り返し)")
    st.caption("役員からの無茶振りや、受託ベンダーからの高額提案に対して、0.5秒で最もプロフェッショナルに切り返す反射神経を鍛えます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_scenarios = pd.read_sql_query("SELECT * FROM meeting_scenarios", conn)
    conn.close()

    if "ms_idx" not in st.session_state or st.session_state.ms_idx >= len(df_scenarios):
        st.session_state.ms_idx = 0
        st.session_state.ms_revealed = False

    s_card = df_scenarios.iloc[st.session_state.ms_idx]
    
    st.caption(f"シナリオ特訓中：残り {len(df_scenarios) - st.session_state.ms_idx} / {len(df_scenarios)} 件")
    st.progress((st.session_state.ms_idx + 1) / len(df_scenarios))

    if "ms_start_time" not in st.session_state or st.session_state.get("ms_current_id") != s_card["id"]:
        st.session_state.ms_start_time = time.time()
        st.session_state.ms_current_id = int(s_card["id"])
        st.session_state.ms_revealed = False

    scenario_card_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #7c3aed; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
<span style="background:#f5f3ff; color:#6d28d9; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{s_card['category']}</span>
<span style="font-size:0.9rem; color:#64748b;">相手: <b>{s_card['counterpart']}</b></span>
</div>
<h3 style="color:#0f172a; margin-top:0; font-size:1.4rem;">🎯 場面: {s_card['title']}</h3>
<div style="background:#faf5ff; border:1px solid #e9d5ff; border-left:5px solid #7c3aed; padding:18px; border-radius:8px; margin-top:14px; margin-bottom:14px;">
<div style="font-size:0.9rem; font-weight:bold; color:#6b21a8; margin-bottom:6px;">🗣️ 相手の発言:</div>
<div style="font-size:1.25rem; font-weight:bold; color:#1e1b4b; line-height:1.6;">
「{s_card['counterpart_statement']}」
</div>
</div>
<div style="font-size:1.05rem; color:#475569;">
🤔 <b>あなたなら、どのように切り返しますか？</b>（相手を不快にさせず、リスクを防ぎ、主導権を握るベストな返しを考えてください）
</div>
</div>"""
    st.markdown(scenario_card_html, unsafe_allow_html=True)

    if not st.session_state.ms_revealed:
        if st.button("💡 プロフェッショナルの模範回答 ＆ 解説を見る", type="primary", use_container_width=True):
            st.session_state.ms_elapsed = max(0.1, round(time.time() - st.session_state.ms_start_time, 1))
            st.session_state.ms_revealed = True
            st.rerun()
    else:
        best_resp_html = f"""<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:6px solid #16a34a; padding:22px; border-radius:12px; margin-bottom:16px;">
<h3 style="color:#15803d; margin-top:0; font-size:1.3rem;">🌟 模範切り返しフレーズ:</h3>
<div style="font-size:1.2rem; line-height:1.7; color:#14532d; font-weight:bold; background:#ffffff; padding:16px; border-radius:8px; border:1px solid #86efac; margin-bottom:16px;">
{s_card['best_response']}
</div>
<h4 style="color:#0369a1; margin-top:0;">🎯 会議で主導権を握るポイント:</h4>
<div style="font-size:1.05rem; line-height:1.6; color:#1e293b;">
{s_card['key_point']}
</div>
</div>"""
        st.markdown(best_resp_html, unsafe_allow_html=True)

        elapsed_ms_sec = float(st.session_state.get("ms_elapsed", 4.0))
        record_tech_study_time(elapsed_ms_sec, "meeting_scenarios", 1)

        if st.button("⭕️ 次の想定問答へ ➡️", type="primary", use_container_width=True):
            st.session_state.ms_idx = (st.session_state.ms_idx + 1) % len(df_scenarios)
            st.session_state.ms_revealed = False
            st.session_state.ms_start_time = time.time()
            st.rerun()

# ==========================================
# 5. ⚖️ どっちを選ぶ？ 2択トレードオフ判断ドリル
# ==========================================
elif menu == "⚖️ どっちを選ぶ？ 2択トレードオフ判断ドリル":
    st.title("⚖️ どっちを選ぶ？ 2択トレードオフ判断ドリル (意思決定マトリクス)")
    st.caption("「RAG vs ファインチューニング」「ゼロトラスト vs VPN」「請負 vs 準委任」など、実務で最も問われる技術選定の判断軸を瞬間的にジャッジする訓練です。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_tradeoffs = pd.read_sql_query("SELECT * FROM tradeoffs", conn)
    conn.close()

    if "to_idx" not in st.session_state or st.session_state.to_idx >= len(df_tradeoffs):
        st.session_state.to_idx = 0
        st.session_state.to_answered = False
        st.session_state.to_selected_opt = None

    t_item = df_tradeoffs.iloc[st.session_state.to_idx]
    
    st.caption(f"意思決定ドリル中：残り {len(df_tradeoffs) - st.session_state.to_idx} / {len(df_tradeoffs)} 件")
    st.progress((st.session_state.to_idx + 1) / len(df_tradeoffs))

    if "to_start_time" not in st.session_state or st.session_state.get("to_current_id") != t_item["id"]:
        st.session_state.to_start_time = time.time()
        st.session_state.to_current_id = int(t_item["id"])
        st.session_state.to_answered = False

    tradeoff_card_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #ea580c; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">
<div style="font-size:0.9rem; color:#c2410c; font-weight:bold; margin-bottom:4px;">⚖️ 意思決定テーマ:</div>
<h2 style="color:#0f172a; margin-top:0; font-size:1.6rem;">{t_item['title']}</h2>
<div style="font-size:1.25rem; font-weight:bold; color:#1e293b; line-height:1.6; background:#fff7ed; padding:18px; border-radius:8px; border-left:5px solid #ea580c; margin-bottom:16px;">
💬 {t_item['scenario']}
</div>
<div style="font-size:1.05rem; color:#475569; font-weight:bold;">
👉 この要件に対して、最も適した技術・アプローチはどっち？
</div>
</div>"""
    st.markdown(tradeoff_card_html, unsafe_allow_html=True)

    if not st.session_state.to_answered:
        c1, c2 = st.columns(2)
        with c1:
            if st.button(f"🅰️ {t_item['option_a']}", use_container_width=True, key="btn_opt_a"):
                st.session_state.to_selected_opt = t_item["option_a"]
                st.session_state.to_answered = True
                st.session_state.to_elapsed = max(0.1, round(time.time() - st.session_state.to_start_time, 1))
                st.rerun()
        with c2:
            if st.button(f"🅱️ {t_item['option_b']}", use_container_width=True, key="btn_opt_b"):
                st.session_state.to_selected_opt = t_item["option_b"]
                st.session_state.to_answered = True
                st.session_state.to_elapsed = max(0.1, round(time.time() - st.session_state.to_start_time, 1))
                st.rerun()
    else:
        is_correct = (st.session_state.to_selected_opt == t_item["correct_option"])
        res_bg = "#f0fdf4" if is_correct else "#fef2f2"
        res_border = "#16a34a" if is_correct else "#dc2626"
        res_title = "🎉 正解！完璧な意思決定です！" if is_correct else "⚠️ 惜しい！別の判断軸を確認しましょう。"
        
        tradeoff_res_html = f"""<div style="background:{res_bg}; border:2px solid {res_border}; padding:22px; border-radius:12px; margin-bottom:16px;">
<h3 style="color:{res_border}; margin-top:0; font-size:1.3rem;">{res_title}</h3>
<div style="font-size:1.15rem; color:#1e293b; margin-bottom:10px;">
あなたの選択: <b>{st.session_state.to_selected_opt}</b> ｜ 正解: <b style="color:#15803d;">{t_item['correct_option']}</b>
</div>
<hr style="border:none; border-top:1px solid #e2e8f0; margin:12px 0;">
<h4 style="color:#0369a1; margin-top:0;">💡 現場での明確な判断理由（トレードオフ）:</h4>
<div style="font-size:1.1rem; line-height:1.7; color:#334155;">
{t_item['decision_reason']}
</div>
</div>"""
        st.markdown(tradeoff_res_html, unsafe_allow_html=True)

        record_tech_study_time(float(st.session_state.get("to_elapsed", 4.0)), "tradeoffs", 1)

        if st.button("⭕️ 次の意思決定ドリルへ ➡️", type="primary", use_container_width=True):
            st.session_state.to_idx = (st.session_state.to_idx + 1) % len(df_tradeoffs)
            st.session_state.to_answered = False
            st.session_state.to_start_time = time.time()
            st.rerun()

# ==========================================
# 6. ⚡ 打ち合わせ直前 30秒カンペ (チートシート)
# ==========================================
elif menu == "⚡ 打ち合わせ直前 30秒カンペ (チートシート)":
    st.title("⚡ 打ち合わせ直前 30秒カンペ (チートシート)")
    st.caption("会議の5分前にスマホでサクッと確認できる実務支援ツールです。必須用語、地雷質問、NG発言をパッとチェックできます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_cheat = pd.read_sql_query("SELECT * FROM cheat_sheets", conn)
    conn.close()

    sel_theme = st.selectbox("🎯 会議テーマを選択", df_cheat["theme"].tolist())
    c_row = df_cheat[df_cheat["theme"] == sel_theme].iloc[0]

    cheat_card_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #2563eb; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:20px;">
<h2 style="color:#0f172a; margin-top:0; font-size:1.5rem;">📋 {c_row['theme']}</h2>
<div style="margin-top:16px; background:#eff6ff; border:1px solid #bfdbfe; padding:18px; border-radius:8px; margin-bottom:16px;">
<h3 style="color:#1d4ed8; margin-top:0; font-size:1.15rem;">📌 今日絶対に出てくる必須キーワード 5選:</h3>
<div style="font-size:1.05rem; line-height:1.8; color:#1e293b; white-space:pre-line; font-weight:bold;">
{c_row['must_know_terms']}
</div>
</div>
<div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:18px; border-radius:8px; margin-bottom:16px;">
<h3 style="color:#15803d; margin-top:0; font-size:1.15rem;">🚨 相手に絶対に確認すべき「地雷質問（突っ込みポイント）」:</h3>
<div style="font-size:1.05rem; line-height:1.8; color:#14532d; white-space:pre-line; font-weight:bold;">
{c_row['trap_questions']}
</div>
</div>
<div style="background:#fef2f2; border:1px solid #fecaca; padding:18px; border-radius:8px;">
<h3 style="color:#dc2626; margin-top:0; font-size:1.15rem;">⚠️ 知ったかぶりNGポイント（恥をかかないための注意点）:</h3>
<div style="font-size:1.0rem; line-height:1.7; color:#991b1b;">
{c_row['ng_behavior']}
</div>
</div>
</div>"""
    st.markdown(cheat_card_html, unsafe_allow_html=True)

# ==========================================
# 7. ⌨️ 略語・IT用語 スペリング＆タイピング特訓
# ==========================================
elif menu == "⌨️ 略語・IT用語 スペリング＆タイピング特訓":
    st.title("⌨️ 略語・IT用語 スペリング＆タイピング特訓")
    st.caption("英語略語（RAG, SaaS, EDR, WBS等）やキーワードを実際にキーボードで入力し、文字単位Diffで運動記憶に焼き付けます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_terms = pd.read_sql_query("SELECT * FROM tech_terms", conn)
    conn.close()

    if "type_idx" not in st.session_state or st.session_state.type_idx >= len(df_terms):
        st.session_state.type_idx = 0
        st.session_state.type_submitted = False
        st.session_state.type_input = ""

    t_card = df_terms.iloc[st.session_state.type_idx]
    
    st.caption(f"タイピング特訓中：残り {len(df_terms) - st.session_state.type_idx} / {len(df_terms)} 語")
    st.progress((st.session_state.type_idx + 1) / len(df_terms))

    target_word = str(t_card["correct_answer"]).strip()

    typing_q_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #059669; padding:24px; border-radius:12px; margin-bottom:16px;">
<div style="font-size:0.9rem; color:#059669; font-weight:bold; margin-bottom:6px;">🏷️ {t_card['category']}</div>
<div style="font-size:1.3rem; font-weight:bold; color:#0f172a; line-height:1.6; background:#f0fdf4; padding:16px; border-radius:8px; border-left:5px solid #059669; margin-bottom:12px;">
💬 {t_card['quiz_sentence']}
</div>
<div style="font-size:0.95rem; color:#64748b;">
💡 <b>ヒント（日常の例え）:</b> {t_card['metaphor'][:60]}...
</div>
</div>"""
    st.markdown(typing_q_html, unsafe_allow_html=True)

    with st.form(key=f"type_form_{st.session_state.type_idx}"):
        u_in = st.text_input("⌨️ 正しい用語名・略語を入力してください:", value=st.session_state.get("type_input", ""), placeholder="例: RAG, SaaS, ゼロトラスト...", key=f"t_in_field_{st.session_state.type_idx}")
        b_submit = st.form_submit_button("🔥 判定する (Enter)", type="primary", use_container_width=True)

    if b_submit:
        st.session_state.type_input = u_in
        st.session_state.type_submitted = True
        st.rerun()

    if st.session_state.get("type_submitted", False):
        user_val = st.session_state.get("type_input", "").strip()
        is_exact = (user_val.lower() == target_word.lower()) or (user_val in target_word)
        
        diff_bg = "#f0fdf4" if is_exact else "#fef2f2"
        diff_border = "#16a34a" if is_exact else "#dc2626"
        res_text = "🎉 完璧！正解です！" if is_exact else "⚠️ 惜しい！正解を確認しましょう。"
        
        typing_res_html = f"""<div style="background:{diff_bg}; border:2px solid {diff_border}; padding:18px 22px; border-radius:10px; margin-bottom:16px;">
<div style="font-weight:bold; font-size:1.1rem; color:#0f172a; margin-bottom:6px;">{res_text}</div>
<div style="font-size:1.05rem; color:#334155;">
あなたの入力: <code>{user_val}</code> ｜ 正解: <b style="color:#15803d;">{target_word}</b> ({t_card['english_full']})
</div>
</div>"""
        st.markdown(typing_res_html, unsafe_allow_html=True)

        record_tech_study_time(3.0, "typing", 1)

        if st.button("⭕️ 次のタイピング問題へ ➡️", type="primary", use_container_width=True):
            st.session_state.type_idx = (st.session_state.type_idx + 1) % len(df_terms)
            st.session_state.type_submitted = False
            st.session_state.type_input = ""
            st.rerun()

# ==========================================
# 8. 🔀 5大分野 インターリービング実戦シャッフル
# ==========================================
elif menu == "🔀 5大分野 インターリービング実戦シャッフル":
    st.title("🔀 5大分野 インターリービング実戦シャッフル")
    st.caption("AI、DX、セキュリティ、Python、Web基礎、見積もり・契約の全分野からランダム出題され、実務現場での『瞬時の引き出し力』を極限まで高めます。")

    conn = sqlite3.connect(TECH_DB_PATH)
    df_all_terms = pd.read_sql_query("SELECT * FROM tech_terms", conn)
    conn.close()

    if "il_term_ids" not in st.session_state or len(st.session_state.il_term_ids) != len(df_all_terms):
        st.session_state.il_term_ids = df_all_terms["id"].sample(frac=1, random_state=int(time.time()) % 1000).tolist()
        st.session_state.il_idx = 0
        st.session_state.il_answered = False
        st.session_state.il_selected = None

    if st.session_state.il_idx >= len(st.session_state.il_term_ids):
        st.session_state.il_term_ids = df_all_terms["id"].sample(frac=1, random_state=int(time.time()) % 1000).tolist()
        st.session_state.il_idx = 0
        st.session_state.il_answered = False
        st.session_state.il_selected = None

    curr_term_id = st.session_state.il_term_ids[st.session_state.il_idx]
    il_card = df_all_terms[df_all_terms["id"] == curr_term_id].iloc[0]
    
    st.caption(f"交差シャッフル中：残り {len(st.session_state.il_term_ids) - st.session_state.il_idx} / {len(st.session_state.il_term_ids)} 語")
    st.progress((st.session_state.il_idx + 1) / len(st.session_state.il_term_ids))

    il_q_html = f"""<div style="background:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #8b5cf6; padding:24px; border-radius:12px; margin-bottom:16px;">
<div style="font-size:0.9rem; color:#8b5cf6; font-weight:bold; margin-bottom:6px;">🏷️ {il_card['category']}</div>
<div style="font-size:1.3rem; font-weight:bold; color:#0f172a; line-height:1.6; background:#f5f3ff; padding:18px; border-radius:8px; border-left:5px solid #8b5cf6; margin-bottom:16px;">
❓ {il_card['quiz_sentence']}
</div>
<div style="font-size:1.0rem; color:#64748b;">
💡 <b>日常の例え:</b> {il_card['metaphor']}
</div>
</div>"""
    st.markdown(il_q_html, unsafe_allow_html=True)

    opts = [o.strip() for o in str(il_card["quiz_options"]).split(",") if o.strip()]
    correct_ans = str(il_card["correct_answer"]).strip()
    
    if not st.session_state.get("il_answered", False):
        st.write("**正しい用語を選択してください：**")
        o_cols = st.columns(len(opts))
        for i, opt in enumerate(opts):
            with o_cols[i]:
                if st.button(opt, key=f"il_btn_{il_card['id']}_{i}", use_container_width=True):
                    st.session_state.il_selected = opt
                    st.session_state.il_answered = True
                    st.rerun()
    else:
        user_choice = str(st.session_state.get("il_selected", "")).strip()
        is_right = (user_choice.lower() == correct_ans.lower()) or (user_choice in correct_ans) or (correct_ans in user_choice)
        bg = "#f0fdf4" if is_right else "#fef2f2"
        bdr = "#16a34a" if is_right else "#dc2626"
        res_t = "🌟 正解です！" if is_right else "⚠️ 惜しい！別の用語です。"
        
        il_res_html = f"""<div style="background:{bg}; border:2px solid {bdr}; padding:20px; border-radius:10px; margin-bottom:16px;">
<div style="font-size:1.2rem; font-weight:bold; color:{bdr}; margin-bottom:6px;">{res_t}</div>
<div style="font-size:1.05rem; color:#334155;">
あなたの回答: <b>{user_choice}</b> ｜ 正解: <b style="color:#15803d;">{correct_ans}</b> ({il_card['english_full']})
</div>
<hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">
<div style="font-size:0.95rem; color:#1e293b; line-height:1.6;">
👔 <b>ビジネスインパクト:</b> {il_card['business_impact']}
</div>
</div>"""
        st.markdown(il_res_html, unsafe_allow_html=True)

        record_tech_study_time(2.0, "interleaving", 1)

        if st.button("⭕️ 次のシャッフル問題へ ➡️", type="primary", use_container_width=True):
            st.session_state.il_idx += 1
            st.session_state.il_answered = False
            st.session_state.il_selected = None
            st.rerun()

# ==========================================
# 9. 📊 学習進捗ダッシュボード ＆ 💾 バックアップ
# ==========================================
elif menu == "📊 学習進捗ダッシュボード ＆ 💾 バックアップ":
    st.title("📊 学習進捗ダッシュボード ＆ 💾 バックアップ")
    
    conn = sqlite3.connect(TECH_DB_PATH)
    df_terms = pd.read_sql_query("SELECT * FROM tech_terms", conn)
    df_time = pd.read_sql_query("SELECT * FROM study_time_logs", conn)
    conn.close()

    d_col1, d_col2 = st.columns(2)
    with d_col1:
        st.markdown("### 🏷️ 分野別の定着状況")
        cat_stats = df_terms.groupby("category").agg(
            総用語数=("id", "count"),
            定着済み=("repetitions", lambda x: (x >= 3).sum()),
            復習中=("repetitions", lambda x: ((x > 0) & (x < 3)).sum()),
            未学習=("repetitions", lambda x: (x == 0).sum())
        ).reset_index()
        st.dataframe(cat_stats, use_container_width=True, hide_index=True)

    with d_col2:
        st.markdown("### 💾 ワンクリック進捗バックアップ & 復元")
        json_data = export_tech_progress_json()
        st.download_button(
            label="💾 学習進捗データをダウンロード (JSON)",
            data=json_data,
            file_name=f"tech_master_progress_{date.today().isoformat()}.json",
            mime="application/json",
            use_container_width=True
        )

        uploaded = st.file_uploader("📤 JSONファイルをアップロードして復元", type=["json"])
        if uploaded is not None:
            try:
                content = json.loads(uploaded.read().decode("utf-8"))
                ok, msg = merge_and_import_tech_progress(content)
                if ok:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)
            except Exception as e:
                st.error(f"ファイル読み込みエラー: {e}")
