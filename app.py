import streamlit as st
import sqlite3
import pandas as pd
import datetime
import os
import re
import time
import json
from dictionary_data import DICTIONARY_DATA
from chunks_data import CHUNKS_DATA
from pop_culture_data import POP_CULTURE_DATA
from pattern_practice_data import PATTERN_PRACTICE_DATA

# --- ページ設定 ---
st.set_page_config(
    page_title="🇪🇸 スペイン語 1年マスター学習システム",
    page_icon="🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- カスタムスタイル (サイドバーの行間・余白拡大) ---
st.markdown("""
<style>
/* サイドバーメニューの行間・余白をゆったり広げる */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 10px !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] > label {
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    padding-left: 12px !important;
    padding-right: 12px !important;
    margin-bottom: 8px !important;
    font-size: 1.05rem !important;
    line-height: 1.7 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease;
}
section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    background-color: rgba(2, 132, 199, 0.08) !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] > label > div:last-child {
    line-height: 1.7 !important;
    padding-left: 8px !important;
}
</style>
""", unsafe_allow_html=True)

DB_PATH = "spanish_learning.db"

def init_user_state():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_state (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')
    conn.commit()
    conn.close()

def get_last_lesson_idx():
    try:
        init_user_state()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM user_state WHERE key = 'last_lesson_idx'")
        row = cursor.fetchone()
        conn.close()
        return int(row[0]) if row else 0
    except Exception:
        return 0

def save_last_lesson_idx(idx):
    try:
        init_user_state()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO user_state (key, value) VALUES ('last_lesson_idx', ?)", (str(idx),))
        conn.commit()
        conn.close()
    except Exception:
        pass

def init_dict_db():
    if not os.path.exists(DB_PATH):
        import generate_113_lessons
        generate_113_lessons.seed_database()
        generate_113_lessons.seed_dictionary_database()
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dictionary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        reading TEXT NOT NULL,
        pos TEXT NOT NULL,
        meanings TEXT NOT NULL,
        examples TEXT NOT NULL,
        category TEXT NOT NULL,
        conjugation TEXT,
        repetitions INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        ease_factor REAL DEFAULT 2.5,
        next_review_date TEXT,
        mistake_count INTEGER DEFAULT 0,
        created_at TEXT
    )
    ''')
    cursor.execute("PRAGMA table_info(dictionary)")
    cols = [c[1] for c in cursor.fetchall()]
    if "conjugation" not in cols:
        try:
            cursor.execute("ALTER TABLE dictionary ADD COLUMN conjugation TEXT")
        except Exception:
            pass
    cursor.execute("SELECT COUNT(*) FROM dictionary WHERE examples LIKE '%単語分解%'")
    breakdown_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM dictionary WHERE examples LIKE '%【%'")
    katakana_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM dictionary WHERE conjugation IS NOT NULL AND conjugation != ''")
    valid_conj_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM dictionary")
    count = cursor.fetchone()[0]
    conn.close()

    if count < len(DICTIONARY_DATA) or valid_conj_count < 100 or breakdown_count < 100 or katakana_count < 100 or "repetitions" not in cols:
        import generate_113_lessons
        generate_113_lessons.seed_dictionary_database()

def get_dict_df(query="", category="すべて"):
    init_dict_db()
    conn = sqlite3.connect(DB_PATH)
    if query.strip():
        q = f"%{query.strip()}%"
        if category == "すべて":
            df = pd.read_sql_query('''
            SELECT * FROM dictionary
            WHERE word LIKE ? OR reading LIKE ? OR meanings LIKE ? OR examples LIKE ?
            ORDER BY word ASC
            ''', conn, params=(q, q, q, q))
        else:
            df = pd.read_sql_query('''
            SELECT * FROM dictionary
            WHERE (word LIKE ? OR reading LIKE ? OR meanings LIKE ? OR examples LIKE ?) AND category = ?
            ORDER BY word ASC
            ''', conn, params=(q, q, q, q, category))
    else:
        if category == "すべて":
            df = pd.read_sql_query("SELECT * FROM dictionary ORDER BY id ASC", conn)
        else:
            df = pd.read_sql_query("SELECT * FROM dictionary WHERE category = ? ORDER BY id ASC", conn, params=(category,))
    conn.close()

    if not df.empty:
        for col in ["id", "repetitions", "interval_days", "mistake_count"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        if "ease_factor" in df.columns:
            df["ease_factor"] = pd.to_numeric(df["ease_factor"], errors="coerce").fillna(2.5).astype(float)
    return df

def init_chunks_db():
    if not os.path.exists(DB_PATH):
        import generate_113_lessons
        generate_113_lessons.seed_chunks_database()
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chunk TEXT NOT NULL,
        reading TEXT NOT NULL,
        category TEXT NOT NULL,
        meaning TEXT NOT NULL,
        example TEXT NOT NULL,
        grammar_point TEXT NOT NULL,
        repetitions INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        ease_factor REAL DEFAULT 2.5,
        next_review_date TEXT,
        mistake_count INTEGER DEFAULT 0
    )
    ''')
    cursor.execute("SELECT COUNT(*) FROM chunks WHERE example LIKE '%【%'")
    chk_katakana_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM chunks")
    count = cursor.fetchone()[0]
    conn.close()
    if count < len(CHUNKS_DATA) or chk_katakana_count < len(CHUNKS_DATA):
        import generate_113_lessons
        generate_113_lessons.seed_chunks_database()

def get_chunks_df(category="すべて"):
    init_chunks_db()
    conn = sqlite3.connect(DB_PATH)
    if category == "すべて":
        df = pd.read_sql_query("SELECT * FROM chunks ORDER BY id ASC", conn)
    else:
        df = pd.read_sql_query("SELECT * FROM chunks WHERE category = ? ORDER BY id ASC", conn, params=(category,))
    conn.close()
    if not df.empty:
        for col in ["id", "repetitions", "interval_days", "mistake_count"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        if "ease_factor" in df.columns:
            df["ease_factor"] = pd.to_numeric(df["ease_factor"], errors="coerce").fillna(2.5).astype(float)
    return df

def init_pop_culture_db():
    if not os.path.exists(DB_PATH):
        import generate_113_lessons
        generate_113_lessons.seed_pop_culture_database()
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pop_culture (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        work TEXT NOT NULL,
        character TEXT NOT NULL,
        category TEXT NOT NULL,
        spanish TEXT NOT NULL,
        reading TEXT NOT NULL,
        japanese TEXT NOT NULL,
        breakdown TEXT NOT NULL,
        grammar_point TEXT NOT NULL
    )
    ''')
    cursor.execute("SELECT COUNT(*) FROM pop_culture")
    count = cursor.fetchone()[0]
    conn.close()
    if count < len(POP_CULTURE_DATA):
        import generate_113_lessons
        generate_113_lessons.seed_pop_culture_database()

def get_pop_culture_df(category="すべて"):
    init_pop_culture_db()
    conn = sqlite3.connect(DB_PATH)
    if category == "すべて":
        df = pd.read_sql_query("SELECT * FROM pop_culture ORDER BY id ASC", conn)
    else:
        df = pd.read_sql_query("SELECT * FROM pop_culture WHERE category = ? ORDER BY id ASC", conn, params=(category,))
    conn.close()
    return df

def init_cards_db():
    if not os.path.exists(DB_PATH):
        import generate_113_lessons
        generate_113_lessons.seed_database()
        generate_113_lessons.seed_dictionary_database()
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        lesson_title TEXT NOT NULL,
        content TEXT NOT NULL,
        title TEXT NOT NULL,
        sentence TEXT NOT NULL,
        options TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        hint TEXT,
        explanation TEXT,
        repetitions INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        ease_factor REAL DEFAULT 2.5,
        next_review_date TEXT,
        mistake_count INTEGER DEFAULT 0,
        created_at TEXT
    )
    ''')
    cursor.execute("SELECT COUNT(*) FROM cards")
    count = cursor.fetchone()[0]
    conn.close()
    if count < 113:
        import generate_113_lessons
        generate_113_lessons.seed_database()

def get_cards_df():
    init_cards_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM cards ORDER BY id ASC", conn)
    conn.close()
    if not df.empty:
        for col in ["id", "repetitions", "interval_days", "mistake_count"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        if "ease_factor" in df.columns:
            df["ease_factor"] = pd.to_numeric(df["ease_factor"], errors="coerce").fillna(2.5).astype(float)
    return df

def init_logs_db():
    if not os.path.exists(DB_PATH):
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS study_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER,
        rating INTEGER,
        is_correct INTEGER,
        reviewed_at TEXT,
        item_type TEXT DEFAULT 'grammar'
    )
    ''')
    cursor.execute("PRAGMA table_info(study_logs)")
    cols = [c[1] for c in cursor.fetchall()]
    if "item_type" not in cols:
        try:
            cursor.execute("ALTER TABLE study_logs ADD COLUMN item_type TEXT DEFAULT 'grammar'")
        except Exception:
            pass

    # 学習時間記録テーブル (日付ごとの学習秒数・問題数・カテゴリ)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS study_time_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        study_date TEXT NOT NULL,
        seconds REAL NOT NULL,
        category TEXT NOT NULL,
        item_count INTEGER DEFAULT 1,
        created_at TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def record_study_time(seconds, category="general", item_count=1):
    try:
        init_logs_db()
        today_str = date.today().isoformat()
        now_str = datetime.datetime.now().isoformat()
        sec = max(0.5, float(seconds))
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO study_time_logs (study_date, seconds, category, item_count, created_at)
        VALUES (?, ?, ?, ?, ?)
        ''', (today_str, sec, category, item_count, now_str))
        conn.commit()
        conn.close()
    except Exception:
        pass

def get_user_study_stats():
    init_logs_db()
    today_str = date.today().isoformat()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. 本日の学習時間 (秒) & 問題数
    cursor.execute("SELECT SUM(seconds), SUM(item_count) FROM study_time_logs WHERE study_date = ?", (today_str,))
    t_row = cursor.fetchone()
    today_sec = float(t_row[0]) if t_row and t_row[0] else 0.0
    today_items = int(t_row[1]) if t_row and t_row[1] else 0
    
    # 2. 累計学習時間 (秒) & 累計問題数
    cursor.execute("SELECT SUM(seconds), SUM(item_count) FROM study_time_logs")
    tot_row = cursor.fetchone()
    total_sec = float(tot_row[0]) if tot_row and tot_row[0] else 0.0
    total_items = int(tot_row[1]) if tot_row and tot_row[1] else 0
    
    # 3. 連続学習日数 (ストリーク)
    cursor.execute("SELECT DISTINCT study_date FROM study_time_logs ORDER BY study_date DESC")
    dates_rows = [r[0] for r in cursor.fetchall()]
    conn.close()
    
    streak = 0
    if dates_rows:
        cur_d = date.today()
        if dates_rows[0] == cur_d.isoformat():
            streak = 1
            check_d = cur_d - timedelta(days=1)
            for d_str in dates_rows[1:]:
                if d_str == check_d.isoformat():
                    streak += 1
                    check_d -= timedelta(days=1)
                else:
                    break
        elif dates_rows[0] == (cur_d - timedelta(days=1)).isoformat():
            streak = 1
            check_d = cur_d - timedelta(days=2)
            for d_str in dates_rows[1:]:
                if d_str == check_d.isoformat():
                    streak += 1
                    check_d -= timedelta(days=1)
                else:
                    break
                    
    return {
        "today_seconds": today_sec,
        "today_items": today_items,
        "total_seconds": total_sec,
        "total_items": total_items,
        "streak_days": streak
    }

def get_daily_study_time_df(days=7):
    init_logs_db()
    today = date.today()
    date_list = [(today - timedelta(days=i)).isoformat() for i in range(days - 1, -1, -1)]
    
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query('''
    SELECT study_date, SUM(seconds) as total_seconds, SUM(item_count) as total_items
    FROM study_time_logs
    WHERE study_date >= ?
    GROUP BY study_date
    ''', conn, params=(date_list[0],))
    conn.close()
    
    res = []
    lookup = {row["study_date"]: row for _, row in df.iterrows()}
    for d_str in date_list:
        d_obj = datetime.date.fromisoformat(d_str)
        day_label = d_obj.strftime("%m/%d")
        if d_str in lookup:
            m = round(lookup[d_str]["total_seconds"] / 60.0, 1)
            cnt = int(lookup[d_str]["total_items"])
        else:
            m = 0.0
            cnt = 0
        res.append({"日付": day_label, "学習時間 (分)": m, "完了問数": cnt})
    return pd.DataFrame(res)

def get_logs_df():
    init_logs_db()
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM study_logs", conn)
    conn.close()
    if not df.empty:
        for col in ["id", "card_id", "rating", "is_correct"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
    return df

def export_progress_json():
    conn = sqlite3.connect(DB_PATH)
    data = {
        "version": "1.0",
        "exported_at": datetime.datetime.now().isoformat(),
        "cards": pd.read_sql_query("SELECT id, lesson_title, repetitions, interval_days, ease_factor, next_review_date, mistake_count FROM cards", conn).to_dict("records"),
        "dictionary": pd.read_sql_query("SELECT id, word, repetitions, interval_days, ease_factor, next_review_date, mistake_count FROM dictionary", conn).to_dict("records"),
        "chunks": pd.read_sql_query("SELECT id, chunk, repetitions, interval_days, ease_factor, next_review_date, mistake_count FROM chunks", conn).to_dict("records"),
        "study_logs": pd.read_sql_query("SELECT card_id, rating, is_correct, reviewed_at, item_type FROM study_logs", conn).to_dict("records"),
        "study_time_logs": pd.read_sql_query("SELECT study_date, seconds, category, item_count, created_at FROM study_time_logs", conn).to_dict("records")
    }
    conn.close()
    return json.dumps(data, ensure_ascii=False, indent=2)

def import_progress_json(json_str):
    try:
        data = json.loads(json_str)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 1. cards の進捗復元
        if "cards" in data:
            for item in data["cards"]:
                cursor.execute('''
                UPDATE cards 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE lesson_title = ? OR id = ?
                ''', (item.get("repetitions", 0), item.get("interval_days", 0), item.get("ease_factor", 2.5), item.get("next_review_date"), item.get("mistake_count", 0), item.get("lesson_title"), item.get("id")))
                
        # 2. dictionary の進捗復元
        if "dictionary" in data:
            for item in data["dictionary"]:
                cursor.execute('''
                UPDATE dictionary 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE word = ? OR id = ?
                ''', (item.get("repetitions", 0), item.get("interval_days", 0), item.get("ease_factor", 2.5), item.get("next_review_date"), item.get("mistake_count", 0), item.get("word"), item.get("id")))

        # 3. chunks の進捗復元
        if "chunks" in data:
            for item in data["chunks"]:
                cursor.execute('''
                UPDATE chunks 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE chunk = ? OR id = ?
                ''', (item.get("repetitions", 0), item.get("interval_days", 0), item.get("ease_factor", 2.5), item.get("next_review_date"), item.get("mistake_count", 0), item.get("chunk"), item.get("id")))

        # 4. study_logs の復元
        if "study_logs" in data:
            cursor.execute("DELETE FROM study_logs")
            for item in data["study_logs"]:
                cursor.execute('''
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                VALUES (?, ?, ?, ?, ?)
                ''', (item.get("card_id", 0), item.get("rating", 4), item.get("is_correct", 1), item.get("reviewed_at"), item.get("item_type", "grammar")))

        # 5. study_time_logs の復元
        if "study_time_logs" in data:
            cursor.execute("DELETE FROM study_time_logs")
            for item in data["study_time_logs"]:
                cursor.execute('''
                INSERT INTO study_time_logs (study_date, seconds, category, item_count, created_at)
                VALUES (?, ?, ?, ?, ?)
                ''', (item.get("study_date"), item.get("seconds", 0.0), item.get("category", "general"), item.get("item_count", 1), item.get("created_at")))

        conn.commit()
        conn.close()
        return True, "🎉 進捗データが正常に復元されました！"
    except Exception as e:
        return False, f"復元中にエラーが発生しました: {str(e)}"

def calculate_sm2(repetitions, interval_days, ease_factor, quality):
    q_mapped = {1: 1, 2: 3, 3: 4, 4: 5}[quality]
    new_ef = ease_factor + (0.1 - (5 - q_mapped) * (0.08 + (5 - q_mapped) * 0.02))
    if new_ef < 1.3:
        new_ef = 1.3
    if quality == 1:
        new_reps = 0
        new_interval = 1
    else:
        new_reps = repetitions + 1
        if new_reps == 1:
            new_interval = 1
        elif new_reps == 2:
            new_interval = 6 if quality >= 3 else 3
        else:
            new_interval = int(interval_days * new_ef)
            if quality == 2:
                new_interval = max(1, int(new_interval * 0.8))
            elif quality == 4:
                new_interval = int(new_interval * 1.3)
    next_date = date.today() + timedelta(days=new_interval)
    return new_reps, new_interval, new_ef, next_date.isoformat()

def calculate_smart_srs(reps, interval, ease_factor, mistake_count, elapsed_sec, days_since_last_review, is_correct, pos=""):
    """
    想起時間(秒) + 経過日数 + 単語難易度・ミス履歴 + 正誤 を統合したAI忘却曲線アルゴリズム
    """
    if not is_correct:
        new_reps = 0
        new_interval = 1
        new_ef = max(1.3, ease_factor - 0.20)
        base_rating = 1
        next_date = (date.today() + timedelta(days=1)).isoformat()
        rating_label = "🔴 要復習 (Again: 明日復習)"
        analysis_detail = "❌ 不正解のため、明日もう一度出題して記憶を強化します。"
        return new_reps, new_interval, new_ef, next_date, base_rating, rating_label, analysis_detail

    # 1. 想起スピード評価 (Response Time)
    difficulty_penalty = min(0.25, mistake_count * 0.04)
    
    if elapsed_sec < 2.5:
        base_rating = 4  # Easy: 即答
        speed_badge = "⚡ 即答 (2.5秒未満)"
    elif elapsed_sec <= 5.0:
        base_rating = 3  # Good: スムーズ
        speed_badge = "🟢 スムーズ (2.5〜5.0秒)"
    else:
        base_rating = 2  # Hard: 迷いあり
        speed_badge = "🟡 迷いあり (5.0秒以上)"

    # 2. 経過時間ボーナス (忘却耐性)
    lapse_bonus = 1.0
    overdue_days = max(0, days_since_last_review - interval)
    if overdue_days > 0 and base_rating >= 3:
        lapse_bonus = 1.0 + min(0.4, (overdue_days / max(1, interval)) * 0.15)

    # 3. Ease Factor の更新
    ef_delta = (0.1 - (5 - base_rating) * (0.08 + (5 - base_rating) * 0.02)) - difficulty_penalty
    new_ef = max(1.3, ease_factor + ef_delta)

    # 4. 復習間隔の算出
    if reps == 0:
        new_reps = 1
        new_interval = 1 if base_rating <= 2 else (2 if base_rating == 3 else 3)
    elif reps == 1:
        new_reps = 2
        new_interval = 2 if base_rating <= 2 else (4 if base_rating == 3 else 6)
    else:
        new_reps = reps + 1
        mult = new_ef * (1.3 if base_rating == 4 else (1.0 if base_rating == 3 else 0.7)) * lapse_bonus
        new_interval = max(1, int(round(interval * mult)))

    next_date = (date.today() + timedelta(days=new_interval)).isoformat()
    rating_label = f"{speed_badge} ➔ Lv.{new_reps} ({new_interval}日後)"
    
    analysis_detail = f"⏱️ 想起時間: <b>{elapsed_sec:.1f}秒</b> ({speed_badge})"
    if lapse_bonus > 1.0:
        analysis_detail += f" ＋ 🌟 <b>忘却耐性ボーナス(x{lapse_bonus:.2f})</b> (予定より+{overdue_days}日経過)"
    if mistake_count > 0:
        analysis_detail += f" ＋ ⚠️ 過去ミス({mistake_count}回)"

    return new_reps, new_interval, new_ef, next_date, base_rating, rating_label, analysis_detail

# --- サイドバーナビゲーション ---
st.sidebar.title("🇪🇸 Español SRS")
st.sidebar.caption("全113課文法 & 220語+単語忘却曲線マスター")

# --- 全テーブルの初期化とスキーマ自動同期 ---
init_user_state()
init_cards_db()
init_dict_db()
init_chunks_db()
init_pop_culture_db()
init_logs_db()

# --- サイドバー モチベーションステータス ---
study_stats = get_user_study_stats()
streak_d = study_stats["streak_days"]
today_m = int(study_stats["today_seconds"] // 60)
today_s = int(study_stats["today_seconds"] % 60)
total_h = round(study_stats["total_seconds"] / 3600.0, 1)
streak_text = f"🔥 {streak_d}日連続学習中！" if streak_d > 0 else "🌱 今日からスタート！"

st.sidebar.markdown(f'''
<div style="background-color:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px; border-radius:8px; margin-bottom:14px;">
    <div style="font-weight:bold; color:#15803d; font-size:0.95rem; margin-bottom:4px;">{streak_text}</div>
    <div style="display:flex; justify-content:space-between; font-size:0.85rem; color:#334155;">
        <span>⏱️ 今日: <b>{today_m}分{today_s}秒</b></span>
        <span>⏳ 累計: <b>{total_h}時間</b></span>
    </div>
</div>
''', unsafe_allow_html=True)

menu = st.sidebar.radio(
    "メニューを選択",
    [
        "📖 文法レッスン (全113課)",
        "🔀 全113課 インターリービング文法シャッフル (実戦)",
        "⚡ 瞬間パターンプラクティス (瞬間西作文)",
        "🧩 最重要チャンクマスター (50選 / Smart SRS)",
        "🎬 映画・ドラマ・アニメ名セリフ (Sentence Mining)",
        "🗂️ 単語フラッシュカード (Smart Timer SRS)",
        "🔍 単語帳＆実用辞書 (220語+)",
        "📐 文法公式＆活用マスター",
        "📝 文法復習セッション (SRS)",
        "📊 学習ダッシュボード",
        "📚 カリキュラム・単語一覧",
        "📈 学習ログ・履歴分析"
    ]
)

# 1. 📖 文法レッスン (全113課)
if menu == "📖 文法レッスン (全113課)":
    st.title("📖 スペイン語 体系的学習レッスン")
    cards_df = get_cards_df()
    
    if len(cards_df) == 0:
        st.warning("⚠️ データベースを読み込み中...")
    else:
        if "current_lesson_idx" not in st.session_state:
            st.session_state.current_lesson_idx = get_last_lesson_idx()
            
        st.session_state.current_lesson_idx = max(0, min(st.session_state.current_lesson_idx, len(cards_df) - 1))
        card = cards_df.iloc[st.session_state.current_lesson_idx]
        
        last_saved = get_last_lesson_idx()
        if last_saved > 0 and st.session_state.current_lesson_idx == last_saved:
            st.info(f"📍 前回の続き（第 {last_saved + 1} 課）から再開しています")
        
        c_cat, c_les = st.columns(2)
        with c_cat:
            categories = list(cards_df["category"].unique())
            cat_idx = categories.index(card["category"]) if card["category"] in categories else 0
            sel_cat = st.selectbox("📚 章を選択してジャンプ", categories, index=cat_idx)
            if sel_cat != card["category"]:
                first_idx = cards_df[cards_df["category"] == sel_cat].index[0]
                st.session_state.current_lesson_idx = int(first_idx)
                save_last_lesson_idx(int(first_idx))
                st.rerun()
                
        with c_les:
            cat_cards = cards_df[cards_df["category"] == sel_cat]
            les_list = list(cat_cards["lesson_title"])
            cur_les_idx_in_cat = les_list.index(card["lesson_title"]) if card["lesson_title"] in les_list else 0
            sel_lesson = st.selectbox("📑 レッスンを選択", les_list, index=cur_les_idx_in_cat)
            if sel_lesson != card["lesson_title"]:
                target_idx = cards_df[cards_df["lesson_title"] == sel_lesson].index[0]
                st.session_state.current_lesson_idx = int(target_idx)
                save_last_lesson_idx(int(target_idx))
                st.rerun()

        nav_prev, nav_info, nav_next = st.columns(3)
        with nav_prev:
            if st.button("⬅️ 前のレッスン", disabled=(st.session_state.current_lesson_idx == 0), use_container_width=True, key="btn_nav_prev_top"):
                st.session_state.current_lesson_idx -= 1
                save_last_lesson_idx(st.session_state.current_lesson_idx)
                st.rerun()
        with nav_info:
            progress_val = (st.session_state.current_lesson_idx + 1) / len(cards_df)
            st.progress(progress_val, text=f"進捗: {st.session_state.current_lesson_idx + 1} / {len(cards_df)} 課")
        with nav_next:
            if st.button("次のレッスン ➡️", disabled=(st.session_state.current_lesson_idx >= len(cards_df) - 1), use_container_width=True, key="btn_nav_next_top"):
                st.session_state.current_lesson_idx += 1
                save_last_lesson_idx(st.session_state.current_lesson_idx)
                st.rerun()

        st.divider()
        st.subheader(f"💡 第 {st.session_state.current_lesson_idx + 1} 課: {card['lesson_title']}")
        st.caption(f"カテゴリー: {card['category']}")
        
        lesson_content_html = f'<div style="background-color:#f8fafc; border-left:5px solid #0284c7; padding:18px; border-radius:8px; font-size:1.1rem; line-height:1.8; color:#1e293b;">{card["content"]}</div>'
        st.markdown(lesson_content_html, unsafe_allow_html=True)
        
        st.write("")
        st.markdown("### ✍️ 理解度チェック問題")
        st.write(f"問題: {card['title']}")
        
        disp_sent = card["sentence"].replace("[___]", "＿＿＿＿")
        st.markdown(f'<div style="background-color:#f1f5f9; padding:14px; border-radius:6px; font-size:1.25rem; font-weight:bold;">{disp_sent}</div>', unsafe_allow_html=True)
        
        options = [opt.strip() for opt in card["options"].split(",")]
        cols = st.columns(len(options))
        for i, opt in enumerate(options):
            if cols[i].button(f"{i+1}. {opt}", key=f"less_opt_{i}_{card['id']}", use_container_width=True):
                is_cor = (opt.strip().lower() == card["correct_answer"].strip().lower())
                record_study_time(3.0, "grammar", 1)
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute('''
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                VALUES (?, ?, ?, ?, 'grammar')
                ''', (int(card["id"]), 4 if is_cor else 1, 1 if is_cor else 0, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()
                if is_cor:
                    st.success(f"🎉 正解です！ (正解: {card['correct_answer']})")
                else:
                    st.error(f"❌ 不正解です。 (正解は: {card['correct_answer']})")
                st.info(f"💡 解説: {card['explanation']}")

        st.divider()
        b_prev, b_spacer, b_next = st.columns(3)
        with b_prev:
            if st.button("⬅️ 前のレッスンに戻る", disabled=(st.session_state.current_lesson_idx == 0), use_container_width=True, key="btn_nav_prev_bottom"):
                st.session_state.current_lesson_idx -= 1
                save_last_lesson_idx(st.session_state.current_lesson_idx)
                st.rerun()
        with b_next:
            if st.button("次のレッスンに進む ➡️", disabled=(st.session_state.current_lesson_idx >= len(cards_df) - 1), use_container_width=True, key="btn_nav_next_bottom"):
                st.session_state.current_lesson_idx += 1
                save_last_lesson_idx(st.session_state.current_lesson_idx)
                st.rerun()

# 2. 🔀 全113課 インターリービング文法シャッフル (実戦)
elif menu == "🔀 全113課 インターリービング文法シャッフル (実戦)":
    st.title("🔀 全113課 インターリービング文法シャッフル")
    st.caption("認知科学で実証された「交互配置学習 (Interleaving)」により、全113課の様々な文法・時制をランダムに出題！「いまどの文法を使うべきか？」の瞬時見極め力を鍛えます。")
    
    cards_df = get_cards_df()
    
    col_mode1, col_mode2 = st.columns([1, 1])
    with col_mode1:
        shuffle_count = st.selectbox("🎯 出題問題数", [10, 20, 30, "全問エンドレス"], index=0, key="interleave_count")
    with col_mode2:
        shuffle_filter = st.selectbox("🏷️ 対象範囲", ["全113課すべてからシャッフル", "初級文法 (第1〜40課)", "中級・過去形・未来 (第41〜80課)", "上級・接続法・応用 (第81〜113課)"], key="interleave_filter")
        
    if "interleave_deck" not in st.session_state or st.button("🔄 新しいシャッフルセットを開始", use_container_width=True):
        if "第1〜40課" in shuffle_filter:
            sub_df = cards_df.iloc[:40]
        elif "第41〜80課" in shuffle_filter:
            sub_df = cards_df.iloc[40:80]
        elif "第81〜113課" in shuffle_filter:
            sub_df = cards_df.iloc[80:]
        else:
            sub_df = cards_df
            
        n_sample = len(sub_df) if shuffle_count == "全問エンドレス" else min(int(shuffle_count), len(sub_df))
        st.session_state.interleave_deck = sub_df.sample(n=n_sample).to_dict("records")
        st.session_state.interleave_idx = 0
        st.session_state.interleave_answered = False
        st.session_state.interleave_score = 0
        st.session_state.interleave_start_time = time.time()
        st.rerun()

    deck = st.session_state.interleave_deck
    idx = st.session_state.interleave_idx
    
    if idx >= len(deck):
        st.success(f"🎉 シャッフル特訓完了！ スコア: {st.session_state.interleave_score} / {len(deck)} 問正解！")
        st.balloons()
        if st.button("もう一度挑戦する 🔄", type="primary", use_container_width=True):
            del st.session_state.interleave_deck
            st.rerun()
    else:
        q_card = deck[idx]
        st.caption(f"問題 {idx + 1} / {len(deck)} ｜ 現在の正解数: {st.session_state.interleave_score}")
        st.progress((idx + 1) / len(deck))
        
        card_content_box = (
            '<div style="background-color:#f8fafc; border:1px solid #e2e8f0; border-left:6px solid #8b5cf6; padding:18px; border-radius:10px; margin-bottom:16px;">'
            f'<div style="font-size:0.9rem; color:#6b21a8; font-weight:bold; margin-bottom:4px;">【{q_card["category"]}】 {q_card["lesson_title"]}</div>'
            f'<div style="font-size:1.15rem; font-weight:bold; color:#1e293b; margin-bottom:12px;">{q_card["title"]}</div>'
            '<div style="background-color:#ffffff; border:1px solid #cbd5e1; padding:14px; border-radius:8px; font-size:1.35rem; font-weight:bold; color:#0f172a;">'
            f'{q_card["sentence"].replace("[___]", "＿＿＿＿")}'
            '</div>'
            '</div>'
        )
        st.markdown(card_content_box, unsafe_allow_html=True)
        
        if "interleave_start_time" not in st.session_state:
            st.session_state.interleave_start_time = time.time()
            
        options = [opt.strip() for opt in q_card["options"].split(",")]
        
        if not st.session_state.interleave_answered:
            cols = st.columns(len(options))
            for i, opt in enumerate(options):
                if cols[i].button(f"{i+1}. {opt}", key=f"int_opt_{idx}_{i}", use_container_width=True):
                    st.session_state.interleave_elapsed = max(0.1, round(time.time() - st.session_state.interleave_start_time, 1))
                    st.session_state.interleave_answered = True
                    st.session_state.interleave_selected = opt
                    is_cor = (opt.strip().lower() == q_card["correct_answer"].strip().lower())
                    if is_cor:
                        st.session_state.interleave_score += 1
                    st.session_state.interleave_is_correct = is_cor
                    record_study_time(st.session_state.interleave_elapsed, "interleave", 1)
                    conn = sqlite3.connect(DB_PATH)
                    c = conn.cursor()
                    c.execute('''
                    INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                    VALUES (?, ?, ?, ?, 'interleave')
                    ''', (int(q_card["id"]), 4 if is_cor else 1, 1 if is_cor else 0, datetime.datetime.now().isoformat()))
                    conn.commit()
                    conn.close()
                    st.rerun()
        else:
            if st.session_state.interleave_is_correct:
                st.success(f"🎉 正解！ (正解: {q_card['correct_answer']}) ⏱️ 回答時間: {st.session_state.interleave_elapsed:.1f}秒")
            else:
                st.error(f"❌ 不正解！ (選択: {st.session_state.interleave_selected} ／ 正解: {q_card['correct_answer']})")
                
            exp_box = f'<div style="background-color:#fff7ed; border-left:4px solid #f97316; padding:14px; border-radius:6px; margin-bottom:16px;"><strong>💡 解説:</strong><br>{q_card["explanation"]}</div>'
            st.markdown(exp_box, unsafe_allow_html=True)
            
            if st.button("次の問題へ進む ➡️", type="primary", use_container_width=True):
                st.session_state.interleave_idx += 1
                st.session_state.interleave_answered = False
                st.session_state.interleave_start_time = time.time()
                st.rerun()

# 3. ⚡ 瞬間パターンプラクティス (瞬間西作文)
elif menu == "⚡ 瞬間パターンプラクティス (瞬間西作文)":
    st.title("⚡ 瞬間パターンプラクティス (瞬間西作文 10本ノック)")
    st.caption("脳内の文法知識を「口の筋肉の反射（手続き記憶）」へ転換！日本語を見て3秒以内に声に出してスペイン語を言う瞬発力トレーニングです。")
    
    drill_names = [d["pattern_name"] for d in PATTERN_PRACTICE_DATA]
    sel_drill_name = st.selectbox("🎯 特訓する文型パターンを選択", drill_names, key="pattern_drill_select")
    selected_drill = next(d for d in PATTERN_PRACTICE_DATA if d["pattern_name"] == sel_drill_name)
    
    st.info(f"💡 <b>基本ルール:</b> {selected_drill['base_rule']}", icon="📐")
    
    if "drill_idx" not in st.session_state or st.session_state.get("current_drill_name") != sel_drill_name:
        st.session_state.drill_idx = 0
        st.session_state.current_drill_name = sel_drill_name
        st.session_state.drill_revealed = False
        st.session_state.drill_start_time = time.time()
        
    drills = selected_drill["drills"]
    idx = st.session_state.drill_idx
    
    if idx >= len(drills):
        st.success(f"🎉 お見事！「{sel_drill_name}」の10本ノックを完走しました！")
        st.balloons()
        if st.button("もう一度最初から特訓する 🔄", type="primary", use_container_width=True):
            st.session_state.drill_idx = 0
            st.session_state.drill_revealed = False
            st.session_state.drill_start_time = time.time()
            st.rerun()
    else:
        drill_item = drills[idx]
        if len(drill_item) == 4:
            q_jp, ans_es, reading, breakdown = drill_item
        else:
            q_jp, ans_es, breakdown = drill_item
            reading = ""
        
        st.caption(f"第 {idx + 1} / {len(drills)} 問")
        st.progress((idx + 1) / len(drills))
        
        drill_front_html = (
            '<div style="background-color:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #e11d48; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">'
            '<div style="font-size:0.95rem; color:#e11d48; font-weight:bold; margin-bottom:8px;">⏱️ 3秒以内に声に出してスペイン語で言ってください：</div>'
            f'<div style="font-size:1.8rem; font-weight:bold; color:#1e293b; padding:12px 0;">{q_jp}</div>'
            '</div>'
        )
        st.markdown(drill_front_html, unsafe_allow_html=True)
        
        if not st.session_state.drill_revealed:
            if st.button("💡 スペイン語の正解を見る (めくる)", type="primary", use_container_width=True):
                st.session_state.drill_elapsed = max(0.1, round(time.time() - st.session_state.drill_start_time, 1))
                st.session_state.drill_revealed = True
                st.rerun()
        else:
            speed_badge = "⚡ 即答！" if st.session_state.drill_elapsed < 3.0 else "🟢 Good"
            reading_html = f'<div style="font-size:1.15rem; color:#be123c; margin:4px 0 10px 0; font-weight:bold;">【 {reading} 】</div>' if reading else ""
            drill_reveal_html = (
                '<div style="background-color:#fff1f2; border:1px solid #fecdd3; border-left:6px solid #e11d48; padding:20px; border-radius:10px; margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">'
                '<span style="font-size:0.95rem; color:#9f1239; font-weight:bold;">🇪🇸 正解のスペイン語:</span>'
                f'<span style="background-color:#ffe4e6; color:#be123c; padding:2px 10px; border-radius:10px; font-size:0.85rem; font-weight:bold;">⏱️ {st.session_state.drill_elapsed:.1f}秒 ({speed_badge})</span>'
                '</div>'
                f'<h1 style="font-size:2.4rem; color:#881337; margin:6px 0 2px 0; font-weight:800;">{ans_es}</h1>'
                f'{reading_html}'
                '<hr style="border:none; border-top:1px solid #fecdd3; margin:10px 0;">'
                f'<div style="font-size:1.0rem; color:#334155; line-height:1.7;"><b>🔍 単語分解:</b> {breakdown}</div>'
                '</div>'
            )
            st.markdown(drill_reveal_html, unsafe_allow_html=True)
            
            b_col1, b_col2 = st.columns([1.5, 1])
            with b_col1:
                if st.button("⭕️ 言えた！（次の問題へ ➡️）", type="primary", use_container_width=True):
                    record_study_time(st.session_state.drill_elapsed, "pattern_practice", 1)
                    conn = sqlite3.connect(DB_PATH)
                    c = conn.cursor()
                    c.execute('''
                    INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                    VALUES (0, 4, 1, ?, 'pattern_practice')
                    ''', (datetime.datetime.now().isoformat(),))
                    conn.commit()
                    conn.close()
                    st.session_state.drill_idx += 1
                    st.session_state.drill_revealed = False
                    st.session_state.drill_start_time = time.time()
                    st.rerun()
            with b_col2:
                if st.button("❌ 詰まった（もう一度復習）", use_container_width=True):
                    record_study_time(st.session_state.drill_elapsed, "pattern_practice", 1)
                    conn = sqlite3.connect(DB_PATH)
                    c = conn.cursor()
                    c.execute('''
                    INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                    VALUES (0, 1, 0, ?, 'pattern_practice')
                    ''', (datetime.datetime.now().isoformat(),))
                    conn.commit()
                    conn.close()
                    st.session_state.drill_revealed = False
                    st.session_state.drill_start_time = time.time()
                    st.rerun()

# 4. 🧩 最重要チャンクマスター (50選 / Smart SRS)
elif menu == "🧩 最重要チャンクマスター (50選 / Smart SRS)":
    st.title("🧩 最重要チャンク（定型フレーズ）マスター 50選")
    st.caption("単語ではなく「2〜4語の定型ブロック（チャンク）」で覚えることで、文法を考えずにスラスラ話せるようになります！")
    
    chunks_df = get_chunks_df()
    today_str = date.today().isoformat()
    
    c_cat1, c_cat2 = st.columns(2)
    with c_cat1:
        chunk_categories = ["すべて"] + list(chunks_df["category"].unique())
        sel_chunk_cat = st.selectbox("🏷️ チャンクカテゴリー", chunk_categories, key="chunk_cat_select")
    with c_cat2:
        chunk_direction = st.selectbox("🔄 出題方向", ["🇪🇸 西 ➔ 🇯🇵 日 (インプット)", "🇯🇵 日 ➔ 🇪🇸 西 (アウトプット特訓)"], key="chunk_direction_select")
        
    filtered_chunks = chunks_df if sel_chunk_cat == "すべて" else chunks_df[chunks_df["category"] == sel_chunk_cat]
    
    if len(filtered_chunks) == 0:
        st.info("チャンクが見つかりませんでした。")
    else:
        if "chunk_idx" not in st.session_state or st.session_state.chunk_idx >= len(filtered_chunks):
            st.session_state.chunk_idx = 0
            st.session_state.chunk_revealed = False
            
        c_card = filtered_chunks.iloc[st.session_state.chunk_idx]
        
        st.caption(f"残り {len(filtered_chunks) - st.session_state.chunk_idx} / {len(filtered_chunks)} チャンク")
        st.progress((st.session_state.chunk_idx + 1) / len(filtered_chunks))
        
        if "chunk_start_time" not in st.session_state or st.session_state.get("chunk_card_id") != c_card["id"]:
            st.session_state.chunk_start_time = time.time()
            st.session_state.chunk_card_id = int(c_card["id"])
            st.session_state.chunk_elapsed_sec = 0.0
            
        is_j_to_s = ("日 ➔ 🇪🇸 西" in chunk_direction)
        
        if not is_j_to_s:
            # 西 ➔ 日
            front_chunk_html = (
                '<div style="background-color:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #0891b2; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">'
                f'<span style="background-color:#cffafe; color:#0e7490; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{c_card["category"]}</span>'
                f'<span style="font-size:0.9rem; color:#64748b;">Lv.{c_card["repetitions"]} / 間隔:{c_card["interval_days"]}日</span>'
                '</div>'
                '<div style="text-align:center; padding:16px 0;">'
                f'<h1 style="font-size:2.8rem; color:#0f172a; margin:0; font-weight:800;">{c_card["chunk"]}</h1>'
                f'<div style="font-size:1.2rem; color:#64748b; margin-top:8px;">【 {c_card["reading"]} 】</div>'
                '</div>'
                '</div>'
            )
        else:
            # 日 ➔ 西
            front_chunk_html = (
                '<div style="background-color:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #0891b2; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">'
                f'<span style="background-color:#cffafe; color:#0e7490; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{c_card["category"]} (日➔西 特訓)</span>'
                f'<span style="font-size:0.9rem; color:#64748b;">Lv.{c_card["repetitions"]}</span>'
                '</div>'
                '<div style="padding:14px 0;">'
                '<div style="font-size:0.95rem; color:#0891b2; font-weight:bold; margin-bottom:8px;">🤔 この意味のスペイン語チャンク（定型フレーズ）を思い出してください：</div>'
                f'<div style="font-size:1.5rem; font-weight:bold; color:#1e293b; background-color:#ecfeff; padding:16px; border-radius:8px; border-left:5px solid #0891b2;">{c_card["meaning"]}</div>'
                '</div>'
                '</div>'
            )
        st.markdown(front_chunk_html, unsafe_allow_html=True)
        
        if not st.session_state.chunk_revealed:
            if st.button("💡 答えと例文をめくる", type="primary", use_container_width=True):
                st.session_state.chunk_elapsed_sec = max(0.1, round(time.time() - st.session_state.chunk_start_time, 1))
                st.session_state.chunk_revealed = True
                st.rerun()
        else:
            ans_box = ""
            if is_j_to_s:
                ans_box = (
                    '<div style="background-color:#ffffff; border:2px solid #0891b2; padding:18px; border-radius:10px; text-align:center; margin-bottom:16px;">'
                    '<div style="font-size:0.9rem; color:#0891b2; font-weight:bold;">🇪🇸 正解のチャンク</div>'
                    f'<h1 style="font-size:2.8rem; color:#0f172a; margin:4px 0; font-weight:800;">{c_card["chunk"]}</h1>'
                    f'<div style="font-size:1.2rem; color:#64748b;">【 {c_card["reading"]} 】</div>'
                    '</div>'
                )
            reveal_chunk_html = (
                f'{ans_box}'
                '<div style="background-color:#ecfeff; border:1px solid #cffafe; border-left:6px solid #06b6d4; padding:18px; border-radius:10px; margin-bottom:16px;">'
                '<h4 style="color:#0e7490; margin-top:0;">📖 日本語の意味:</h4>'
                f'<div style="font-size:1.2rem; color:#1e293b; font-weight:bold; margin-bottom:12px;">{c_card["meaning"]}</div>'
                '<hr style="border:none; border-top:1px solid #cffafe; margin:12px 0;">'
                '<h4 style="color:#0284c7; margin-top:0;">💬 実際の会話例文 (単語分解つき):</h4>'
                f'<div style="font-size:1.05rem; line-height:1.8; color:#1e293b;">{c_card["example"]}</div>'
                '<hr style="border:none; border-top:1px solid #cffafe; margin:12px 0;">'
                f'<div style="font-size:0.95rem; color:#334155; line-height:1.6;">{c_card["grammar_point"]}</div>'
                '</div>'
            )
            st.markdown(reveal_chunk_html, unsafe_allow_html=True)
            
            # Smart SRS
            s_reps, s_inv, s_ef, s_date, s_rat, s_lbl, s_det = calculate_smart_srs(
                int(c_card["repetitions"]), int(c_card["interval_days"]), float(c_card["ease_factor"]),
                int(c_card["mistake_count"]), float(st.session_state.chunk_elapsed_sec), int(c_card["interval_days"]), is_correct=True
            )
            f_reps, f_inv, f_ef, f_date, f_rat, f_lbl, f_det = calculate_smart_srs(
                int(c_card["repetitions"]), int(c_card["interval_days"]), float(c_card["ease_factor"]),
                int(c_card["mistake_count"]), float(st.session_state.chunk_elapsed_sec), int(c_card["interval_days"]), is_correct=False
            )
            
            chunk_smart_fb = (
                '<div style="background-color:#f0fdf4; border:1px solid #bbf7d0; border-left:6px solid #16a34a; padding:14px 18px; border-radius:8px; margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center;">'
                '<span style="font-weight:bold; color:#15803d;">🧠 AI忘却曲線判定:</span>'
                f'<span style="background-color:#dcfce7; color:#166534; padding:2px 10px; border-radius:10px; font-weight:bold; font-size:0.85rem;">{s_lbl}</span>'
                '</div>'
                f'<div style="font-size:0.9rem; color:#334155; margin-top:4px;">{s_det}</div>'
                '</div>'
            )
            st.markdown(chunk_smart_fb, unsafe_allow_html=True)
            
            def submit_chunk_record(reps, interval, ef, next_date, mistakes_delta, rating, is_correct):
                record_study_time(st.session_state.chunk_elapsed_sec, "chunk", 1)
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                new_m = max(0, int(c_card["mistake_count"]) + mistakes_delta)
                c.execute('''
                UPDATE chunks 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE id = ?
                ''', (reps, interval, ef, next_date, new_m, int(c_card["id"])))
                c.execute('''
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                VALUES (?, ?, ?, ?, 'chunk')
                ''', (int(c_card["id"]), rating, is_correct, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()
                st.session_state.chunk_idx += 1
                st.session_state.chunk_revealed = False
                st.session_state.chunk_start_time = time.time()
                st.rerun()
                
            c_col1, c_col2 = st.columns([1.5, 1])
            with c_col1:
                if st.button(f"⭕️ 分かった！正解（{s_inv}日後に再出題 ➡️）", key="chk_btn_ok", type="primary", use_container_width=True):
                    submit_chunk_record(s_reps, s_inv, s_ef, s_date, 0, s_rat, 1)
            with c_col2:
                if st.button("❌ 分からなかった（明日復習）", key="chk_btn_ng", use_container_width=True):
                    submit_chunk_record(f_reps, f_inv, f_ef, f_date, 1, f_rat, 0)

# 5. 🎬 映画・ドラマ・アニメ名セリフ (Sentence Mining)
elif menu == "🎬 映画・ドラマ・アニメ名セリフ (Sentence Mining)":
    st.title("🎬 映画・ドラマ・アニメ名セリフで学ぶスペイン語")
    st.caption("感情やストーリー（文脈）と結びつけることで、脳に強烈に記憶が焼き付く「センテンス・マイニング」学習です！")
    
    pop_df = get_pop_culture_df()
    
    pop_categories = ["すべて"] + list(pop_df["category"].unique())
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        sel_pop_cat = st.selectbox("🏷️ ジャンルを選択", pop_categories, key="pop_cat_filter")
    with col_p2:
        hide_spanish = st.checkbox("🙈 セリフを隠して思い出す（暗記特訓モード）", value=False)
        
    filtered_pop = pop_df if sel_pop_cat == "すべて" else pop_df[pop_df["category"] == sel_pop_cat]
    
    st.caption(f"全 {len(filtered_pop)} 件の名セリフ")
    st.divider()
    
    for _, quote in filtered_pop.iterrows():
        badge_bg = "#f3e8ff" if "アニメ" in quote["category"] or "ジブリ" in quote["category"] else "#fee2e2"
        badge_color = "#6b21a8" if "アニメ" in quote["category"] or "ジブリ" in quote["category"] else "#991b1b"
        disp_quote_spanish = "🔒 [クリックしてセリフを表示]" if hide_spanish else quote["spanish"]
        
        quote_card_html = (
            '<div style="background-color:#ffffff; border:1px solid #e2e8f0; border-left:6px solid #8b5cf6; padding:20px; border-radius:12px; margin-bottom:20px; box-shadow:0 2px 4px rgba(0,0,0,0.04);">'
            '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">'
            '<div>'
            f'<span style="font-size:1.15rem; font-weight:bold; color:#1e293b;">🎬 {quote["work"]}</span>'
            f'<span style="font-size:0.95rem; color:#64748b; margin-left:8px;">キャラ: <b>{quote["character"]}</b></span>'
            '</div>'
            f'<span style="background-color:{badge_bg}; color:{badge_color}; padding:4px 12px; border-radius:14px; font-size:0.85rem; font-weight:bold;">{quote["category"]}</span>'
            '</div>'
            '<div style="margin-top:10px; padding:16px; background-color:#faf5ff; border-radius:8px;">'
            '<div style="font-size:0.9rem; color:#7c3aed; font-weight:bold; margin-bottom:4px;">🇪🇸 スペイン語セリフ:</div>'
            f'<div style="font-size:1.45rem; font-weight:bold; color:#581c87; line-height:1.6;">{disp_quote_spanish}</div>'
            f'<div style="font-size:1.0rem; color:#6b7280; margin-top:6px;">【 {quote["reading"]} 】</div>'
            '</div>'
            '<div style="margin-top:12px; padding:14px; background-color:#f8fafc; border-radius:8px;">'
            '<div style="font-size:0.9rem; color:#0284c7; font-weight:bold; margin-bottom:4px;">🇯🇵 日本語の意味:</div>'
            f'<div style="font-size:1.15rem; color:#0f172a; font-weight:bold;">{quote["japanese"]}</div>'
            '</div>'
            '<div style="margin-top:12px; padding:12px; background-color:#f1f5f9; border-radius:6px; font-size:0.95rem; color:#334155; line-height:1.7;">'
            f'<b>🔍 単語分解:</b><br>{quote["breakdown"]}'
            '</div>'
            '<div style="margin-top:12px; padding:12px; background-color:#fffbeb; border-radius:6px; font-size:0.95rem; color:#92400e; line-height:1.7;">'
            f'{quote["grammar_point"]}'
            '</div>'
            '</div>'
        )
        st.markdown(quote_card_html, unsafe_allow_html=True)

# 6. 🗂️ 単語フラッシュカード (Smart Timer SRS)
elif menu == "🗂️ 単語フラッシュカード (Smart Timer SRS)":
    st.title("🗂️ 単語フラッシュカード (SRS忘却曲線 暗記特訓)")
    st.caption("エビングハウスの忘却曲線アルゴリズム (SM-2) に基づき、最適な復習タイミングで単語を自動出題します。")

    dict_df = get_dict_df()
    today_str = date.today().isoformat()

    # カテゴリ・出題方向・出題範囲フィルター
    vocab_categories = ["すべて"] + list(dict_df["category"].unique())
    col_filter1, col_filter2, col_filter3 = st.columns([1, 1, 1])
    with col_filter1:
        sel_vocab_cat = st.selectbox("🏷️ 学習カテゴリー", vocab_categories, key="vocab_srs_cat")
    with col_filter2:
        study_direction = st.selectbox("🔄 出題の向き", ["🇪🇸 西 ➔ 🇯🇵 日 (インプット)", "🇯🇵 日 ➔ 🇪🇸 西 (アウトプット特訓)"], key="vocab_direction")
    with col_filter3:
        study_mode = st.selectbox("🎯 出題範囲", ["本日の復習待ち ＋ 未学習（推奨）", "全単語からランダム特訓", "苦手単語（ミス多数）集中特訓"], key="vocab_study_mode")

    filtered_df = dict_df if sel_vocab_cat == "すべて" else dict_df[dict_df["category"] == sel_vocab_cat]

    if study_mode == "本日の復習待ち ＋ 未学習（推奨）":
        due_vocab = filtered_df[(filtered_df["next_review_date"] <= today_str) | (filtered_df["repetitions"] == 0)].sort_values(
            ["mistake_count", "next_review_date"], ascending=[False, True]
        )
    elif study_mode == "苦手単語（ミス多数）集中特訓":
        due_vocab = filtered_df[filtered_df["mistake_count"] > 0].sort_values("mistake_count", ascending=False)
    else:
        due_vocab = filtered_df.sample(frac=1, random_state=42) if len(filtered_df) > 0 else filtered_df

    if len(due_vocab) == 0:
        st.success(f"🎉 素晴らしい！「{sel_vocab_cat}」の本日の単語復習はすべて完了しています！")
        st.balloons()
    else:
        if "vocab_idx" not in st.session_state or st.session_state.vocab_idx >= len(due_vocab):
            st.session_state.vocab_idx = 0
            st.session_state.vocab_revealed = False

        v_card = due_vocab.iloc[st.session_state.vocab_idx]
        
        # 進捗バー
        st.caption(f"復習待ち単語：残り {len(due_vocab) - st.session_state.vocab_idx} / {len(due_vocab)} 語（カテゴリ内全 {len(filtered_df)} 語）")
        st.progress((st.session_state.vocab_idx + 1) / len(due_vocab))

        # 単語カードUI
        status_label = "🌱 未学習" if v_card["repetitions"] == 0 else f"🔄 復習中 (Lv{v_card['repetitions']} / 間隔:{v_card['interval_days']}日)"
        if v_card["repetitions"] >= 4:
            status_label = f"🏆 定着済み (Lv{v_card['repetitions']} / 間隔:{v_card['interval_days']}日)"

        is_j_to_s = ("日 ➔ 🇪🇸 西" in study_direction)

        if not is_j_to_s:
            # 🇪🇸 西 ➔ 🇯🇵 日
            card_front_html = (
                '<div style="background-color:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #0284c7; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">'
                f'<span style="background-color:#e0f2fe; color:#0369a1; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{v_card["category"]}</span>'
                f'<span style="font-size:0.9rem; color:#64748b;">{status_label}</span>'
                '</div>'
                '<div style="text-align:center; padding:20px 0;">'
                f'<h1 style="font-size:3.2rem; color:#0f172a; margin:0; font-weight:800; letter-spacing:0.02em;">{v_card["word"]}</h1>'
                f'<div style="font-size:1.25rem; color:#64748b; margin-top:8px;">【 {v_card["reading"]} 】</div>'
                f'<div style="font-size:1.0rem; color:#0284c7; font-weight:bold; margin-top:4px;">{v_card["pos"]}</div>'
                '</div>'
                '</div>'
            )
        else:
            # 🇯🇵 日 ➔ 🇪🇸 西
            card_front_html = (
                '<div style="background-color:#ffffff; border:2px solid #e2e8f0; border-top:6px solid #ea580c; padding:24px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">'
                f'<span style="background-color:#ffedd5; color:#c2410c; padding:4px 12px; border-radius:16px; font-size:0.9rem; font-weight:bold;">{v_card["category"]} (日➔西 アウトプット特訓)</span>'
                f'<span style="font-size:0.9rem; color:#64748b;">{status_label}</span>'
                '</div>'
                '<div style="padding:12px 0;">'
                '<div style="font-size:0.95rem; color:#ea580c; font-weight:bold; margin-bottom:10px;">🤔 この日本語の意味に対応するスペイン語を思い出してください：</div>'
                f'<div style="font-size:1.35rem; font-weight:bold; color:#1e293b; line-height:1.7; background-color:#fff7ed; padding:18px; border-radius:8px; border-left:5px solid #ea580c;">{v_card["meanings"]}</div>'
                f'<div style="font-size:1.0rem; color:#64748b; margin-top:12px;">品詞ヒント: <b style="color:#0284c7;">{v_card["pos"]}</b></div>'
                '</div>'
                '</div>'
            )
        st.markdown(card_front_html, unsafe_allow_html=True)

        if "vocab_card_start_time" not in st.session_state or st.session_state.get("vocab_current_card_id") != v_card["id"]:
            st.session_state.vocab_card_start_time = time.time()
            st.session_state.vocab_current_card_id = int(v_card["id"])
            st.session_state.vocab_elapsed_sec = 0.0

        if not st.session_state.vocab_revealed:
            btn_label = "💡 スペイン語の正解を見る" if is_j_to_s else "💡 意味と例文をめくる (答えを見る)"
            if st.button(btn_label, use_container_width=True, type="primary"):
                elapsed = max(0.1, round(time.time() - st.session_state.vocab_card_start_time, 1))
                st.session_state.vocab_elapsed_sec = elapsed
                st.session_state.vocab_revealed = True
                st.rerun()
        else:
            header_answer = ""
            if is_j_to_s:
                header_answer = (
                    '<div style="background-color:#ffffff; border:2px solid #0284c7; padding:20px; border-radius:10px; text-align:center; margin-bottom:16px; box-shadow:0 2px 4px rgba(0,0,0,0.05);">'
                    '<div style="font-size:0.95rem; color:#0284c7; font-weight:bold;">🇪🇸 正解のスペイン語単語</div>'
                    f'<h1 style="font-size:3.2rem; color:#0f172a; margin:6px 0; font-weight:800;">{v_card["word"]}</h1>'
                    f'<div style="font-size:1.25rem; color:#64748b;">【 {v_card["reading"]} 】 <span style="color:#0284c7; font-weight:bold; margin-left:8px;">{v_card["pos"]}</span></div>'
                    '</div>'
                )

            conj_section = ""
            if pd.notna(v_card.get("conjugation")) and str(v_card.get("conjugation")).strip():
                conj_section = (
                    '<hr style="border:none; border-top:1px solid #bfdbfe; margin:14px 0;">'
                    '<div style="background-color:#eff6ff; border:1px solid #bfdbfe; border-left:6px solid #2563eb; padding:14px 18px; border-radius:8px;">'
                    '<h4 style="color:#1d4ed8; margin-top:0; margin-bottom:8px;">🔄 人称変化（全6人称）/ 性数変化:</h4>'
                    f'<div style="font-size:1.05rem; line-height:1.9; color:#1e293b;">{v_card["conjugation"]}</div>'
                    '</div>'
                )

            reveal_html = (
                f'{header_answer}'
                '<div style="background-color:#fffbeb; border:1px solid #fef3c7; border-left:6px solid #f59e0b; padding:20px; border-radius:10px; margin-bottom:16px;">'
                '<h4 style="color:#b45309; margin-top:0;">📖 日本語の意味・語義:</h4>'
                f'<div style="font-size:1.15rem; line-height:1.8; color:#1e293b;">{v_card["meanings"]}</div>'
                f'{conj_section}'
                '<hr style="border:none; border-top:1px solid #fde68a; margin:14px 0;">'
                '<h4 style="color:#0284c7; margin-top:0;">💬 実際の会話例文 (単語分解つき):</h4>'
                f'<div style="font-size:1.05rem; line-height:1.8; color:#1e293b;">{v_card["examples"]}</div>'
                '</div>'
            )
            st.markdown(reveal_html, unsafe_allow_html=True)

            # 経過日数の計算
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("SELECT reviewed_at FROM study_logs WHERE card_id = ? AND item_type = 'word' ORDER BY id DESC LIMIT 1", (int(v_card["id"]),))
            last_rev_row = c.fetchone()
            conn.close()
            
            days_since = int(v_card["interval_days"])
            if last_rev_row and last_rev_row[0]:
                try:
                    last_rev_dt = datetime.datetime.fromisoformat(last_rev_row[0]).date()
                    days_since = (date.today() - last_rev_dt).days
                except Exception:
                    pass

            elapsed_sec = float(st.session_state.get("vocab_elapsed_sec", 3.0))

            # 正解時＆不正解時の自動忘却曲線計算
            s_reps, s_interval, s_ef, s_next_date, s_rating, s_label, s_detail = calculate_smart_srs(
                int(v_card["repetitions"]), int(v_card["interval_days"]), float(v_card["ease_factor"]),
                int(v_card["mistake_count"]), elapsed_sec, days_since, is_correct=True, pos=v_card["pos"]
            )
            f_reps, f_interval, f_ef, f_next_date, f_rating, f_label, f_detail = calculate_smart_srs(
                int(v_card["repetitions"]), int(v_card["interval_days"]), float(v_card["ease_factor"]),
                int(v_card["mistake_count"]), elapsed_sec, days_since, is_correct=False, pos=v_card["pos"]
            )

            # AI忘却曲線・自動判定フィードバックUI
            smart_feedback_html = (
                '<div style="background-color:#f0fdf4; border:1px solid #bbf7d0; border-left:6px solid #16a34a; padding:16px 20px; border-radius:10px; margin-bottom:18px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">'
                '<span style="font-weight:bold; color:#15803d; font-size:1.1rem;">🧠 AI忘却曲線・自動定着度判定</span>'
                f'<span style="background-color:#dcfce7; color:#166534; padding:3px 12px; border-radius:14px; font-weight:bold; font-size:0.9rem;">{s_label}</span>'
                '</div>'
                f'<div style="font-size:0.95rem; color:#334155; line-height:1.7;">{s_detail}</div>'
                '</div>'
            )
            st.markdown(smart_feedback_html, unsafe_allow_html=True)

            def submit_vocab_record(reps, interval, ef, next_date, mistakes_delta, rating, is_correct):
                init_logs_db()
                record_study_time(elapsed_sec, "word", 1)
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                new_mistakes = max(0, int(v_card["mistake_count"]) + mistakes_delta)
                cursor.execute('''
                UPDATE dictionary 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE id = ?
                ''', (reps, interval, ef, next_date, new_mistakes, int(v_card["id"])))
                
                cursor.execute('''
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                VALUES (?, ?, ?, ?, 'word')
                ''', (int(v_card["id"]), rating, is_correct, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()

                st.session_state.vocab_idx += 1
                st.session_state.vocab_revealed = False
                st.session_state.vocab_card_start_time = time.time()
                st.rerun()

            # ワンタップ操作ボタン (スマート自動判定)
            ans_col1, ans_col2 = st.columns([1.5, 1])
            with ans_col1:
                if st.button(f"⭕️ 分かった！正解（{s_interval}日後に再出題 ➡️）", type="primary", use_container_width=True):
                    submit_vocab_record(s_reps, s_interval, s_ef, s_next_date, 0, s_rating, 1)
            with ans_col2:
                if st.button("❌ 分からなかった（明日復習）", use_container_width=True):
                    submit_vocab_record(f_reps, f_interval, f_ef, f_next_date, 1, f_rating, 0)

            # 手動上書き用エキスパンダー
            with st.expander("⚙️ 手動で評価を直接上書きする場合 (従来の4段階評価)"):
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                if m_col1.button("🔴 もう一度 (1)", key="m_rate_1", use_container_width=True):
                    m_reps, m_inv, m_ef, m_date = calculate_sm2(int(v_card["repetitions"]), int(v_card["interval_days"]), float(v_card["ease_factor"]), 1)
                    submit_vocab_record(m_reps, m_inv, m_ef, m_date, 1, 1, 0)
                if m_col2.button("🟡 難しかった (2)", key="m_rate_2", use_container_width=True):
                    m_reps, m_inv, m_ef, m_date = calculate_sm2(int(v_card["repetitions"]), int(v_card["interval_days"]), float(v_card["ease_factor"]), 2)
                    submit_vocab_record(m_reps, m_inv, m_ef, m_date, 0, 2, 1)
                if m_col3.button("🟢 覚えた (3)", key="m_rate_3", use_container_width=True):
                    m_reps, m_inv, m_ef, m_date = calculate_sm2(int(v_card["repetitions"]), int(v_card["interval_days"]), float(v_card["ease_factor"]), 3)
                    submit_vocab_record(m_reps, m_inv, m_ef, m_date, 0, 3, 1)
                if m_col4.button("🔵 簡単！ (4)", key="m_rate_4", use_container_width=True):
                    m_reps, m_inv, m_ef, m_date = calculate_sm2(int(v_card["repetitions"]), int(v_card["interval_days"]), float(v_card["ease_factor"]), 4)
                    submit_vocab_record(m_reps, m_inv, m_ef, m_date, 0, 4, 1)

# 3. 🔍 単語帳＆実用辞書 (220語+)
elif menu == "🔍 単語帳＆実用辞書 (220語+)":
    st.title("🔍 単語帳＆実用辞書 (全221語マスター)")
    st.caption("初級〜中級で最頻出の220語以上の単語・熟語を、カタカナ発音・複数の意味・会話例文付きで網羅しています。")
    
    init_dict_db()
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        search_query = st.text_input("🔍 単語・意味・例文を検索", placeholder="例：tener, 家, 食べる, para, 旅行, ありがとう...", key="dict_search_input")
    with d_col2:
        sel_cat = st.selectbox("🏷️ カテゴリ・品詞フィルター", ["すべて", "基本動詞", "日常・生活", "人物・家族", "街・旅行", "形容詞", "副詞・前置詞", "挨拶・基本表現", "身体・健康", "暦・曜日", "疑問詞"], key="dict_cat_filter")
        
    dict_results = get_dict_df(search_query, sel_cat)
    
    st.caption(f"検索結果: {len(dict_results)} 件の単語が見つかりました")
    st.divider()
    
    if len(dict_results) == 0:
        st.info(f"「{search_query}」に一致する単語が見つかりませんでした。別のキーワード（スペイン語または日本語）でお試しください。")
    else:
        for _, entry in dict_results.iterrows():
            with st.container():
                # 習熟バッジ
                reps = entry.get("repetitions", 0)
                badge_bg = "#f1f5f9"
                badge_color = "#475569"
                badge_text = "未学習"
                if reps >= 4:
                    badge_bg = "#dcfce7"
                    badge_color = "#166534"
                    badge_text = f"🏆 定着 Lv{reps}"
                elif reps > 0:
                    badge_bg = "#e0f2fe"
                    badge_color = "#0369a1"
                    badge_text = f"🔄 復習中 Lv{reps}"

                conj_entry_section = ""
                if pd.notna(entry.get("conjugation")) and str(entry.get("conjugation")).strip():
                    conj_entry_section = (
                        '<div style="margin-top:10px; padding:12px; background-color:#eff6ff; border-radius:6px; font-size:0.95rem; line-height:1.8; color:#1e293b;">'
                        f'<strong style="color:#1d4ed8;">🔄 人称変化（全6人称）/ 性数変化:</strong><br>{entry["conjugation"]}'
                        '</div>'
                    )

                card_entry_html = (
                    '<div style="background-color:#ffffff; border:1px solid #e2e8f0; border-left:6px solid #f59e0b; padding:18px; border-radius:10px; margin-bottom:18px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">'
                    '<div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">'
                    f'<span style="font-size:1.6rem; font-weight:bold; color:#1e293b;">{entry["word"]}</span>'
                    f'<span style="font-size:1.05rem; color:#64748b; margin-left:12px;">【{entry["reading"]}】</span>'
                    f'<span style="background-color:#fef3c7; color:#92400e; padding:3px 10px; border-radius:12px; font-size:0.85rem; font-weight:bold; margin-left:10px;">{entry["pos"]}</span>'
                    f'<span style="background-color:{badge_bg}; color:{badge_color}; padding:3px 10px; border-radius:12px; font-size:0.85rem; font-weight:bold; margin-left:auto;">{badge_text}</span>'
                    '</div>'
                    '<div style="margin-top:10px; padding:12px; background-color:#fffbeb; border-radius:6px; font-size:1.05rem; line-height:1.7; color:#334155;">'
                    f'<strong style="color:#b45309;">📖 意味・語義:</strong><br>{entry["meanings"]}'
                    '</div>'
                    f'{conj_entry_section}'
                    '<div style="margin-top:12px; padding:12px; background-color:#f8fafc; border-radius:6px; font-size:1.0rem; line-height:1.8; color:#1e293b;">'
                    f'<strong style="color:#0284c7;">💬 実用例文:</strong><br>{entry["examples"]}'
                    '</div>'
                    '</div>'
                )
                st.markdown(card_entry_html, unsafe_allow_html=True)

# 4. 📐 文法公式＆活用マスター
elif menu == "📐 文法公式＆活用マスター":
    st.title("📐 スペイン語 文法公式＆活用マスター")
    st.caption("文法ルール、例文の単語分解、活用形の意味と読み方をスッキリ整理した完全リファレンスです。")
    
    g_tab1, g_tab2, g_tab3 = st.tabs(["📐 5大文法公式（例文・単語解説付き）", "🔄 動詞活用早見表（読み・意味付き）", "📋 冠詞・代名詞・前置詞一覧"])
    
    with g_tab1:
        st.subheader("💡 覚えるべきスペイン語の 5大文法公式")
        
        with st.expander("① 代名詞と動詞の語順公式（人に + 物を + 動詞）", expanded=True):
            st.markdown('''
            <b>【公式】</b><br>
            `主語` + <b>(no)</b> + <b>【人に (me / te / se / le / nos / les)】</b> + <b>【物を (lo / la / los / las)】</b> + <b>【動詞】</b><br><br>
            ・<b>重要ポイント:</b><br>
            - 「〜に」と「〜を」の代名詞は、必ず<b>動詞の前</b>に置きます。<br>
            - 3人称同士（`le lo` や `le la`）が連続する場合は、発音の都合で `le` が必ず <b>`se`</b> に変化します（例: `se lo doy`）。<br>
            - 不定詞（動詞の原形）の後ろには直接くっつけられます（例: `Quiero comprártelo`）。<br>
            <hr>
            <b>📖 例文と単語の分解解説:</b><br>
            1. <b>Él me lo da.</b>（彼は私にそれをくれます）<br>
               - 単語分解: <b>Él</b>（彼は）＋ <b>me</b>（私に）＋ <b>lo</b>（それを）＋ <b>da</b>（くれる [dar]）<br>
            2. <b>No te lo digo.</b>（君にそれを言わないよ）<br>
               - 単語分解: <b>No</b>（〜ない）＋ <b>te</b>（君に）＋ <b>lo</b>（それを）＋ <b>digo</b>（言う [decir]）<br>
            3. <b>Yo se lo explico a María.</b>（私はマリアにそれを説明します）<br>
               - 単語分解: <b>Yo</b>（私は）＋ <b>se</b>（彼女に [leの変化]）＋ <b>lo</b>（それを）＋ <b>explico</b>（説明する）＋ <b>a María</b>（マリアに）
            ''', unsafe_allow_html=True)
            
        with st.expander("② por と para の使い分け公式", expanded=False):
            st.markdown('''
            <b>【公式】</b><br>
            - <b>para</b> ＝ <b>【矢印の先 ➔ 目的・用途・期限・目的地】</b>（〜のために、〜に向けて、〜までに）<br>
            - <b>por</b> ＝ <b>【原因・理由・手段・通過・交換・期間】</b>（〜のせいで/おかげで、〜を通って、〜によって）<br>
            <hr>
            <b>📖 例文と単語の分解解説:</b><br>
            1. <b>Estudio para trabajar en España.</b>（スペインで働くために勉強しています [目的]）<br>
            2. <b>El tren sale para Madrid.</b>（電車はマドリードに向けて出発します [目的地]）<br>
            3. <b>Es para mañana.</b>（それは明日までの期限です [期限]）<br>
            4. <b>Gracias por tu ayuda.</b>（手伝ってくれてありがとう [原因・理由]）<br>
            5. <b>Viajo por tren.</b>（電車で旅行します [手段]）<br>
            6. <b>Camino por el parque.</b>（公園を通って散歩します [通過]）
            ''', unsafe_allow_html=True)

        with st.expander("③ gustar 型動詞の文型公式（主語が後ろに来る受動構造）", expanded=False):
            st.markdown('''
            <b>【公式】</b><br>
            (A + 人) + <b>【間接代名詞 (me / te / le / nos / les)】</b> + <b>【動詞 (gusta / gustan)】</b> + <b>【好きな物・事】</b><br><br>
            - 英語の like と違い、<b>「好きな対象」が文の主語</b>になります。<br>
            - 好きな物が単数または動詞原形なら ➔ <b>gusta</b><br>
            - 好きな物が複数なら ➔ <b>gustan</b><br>
            <hr>
            <b>📖 例文と単語の分解解説:</b><br>
            1. <b>Me gusta el café.</b>（私はコーヒーが好きです）<br>
            2. <b>Me gustan los perros.</b>（私は犬が好きです）<br>
            3. <b>¿Te gusta viajar?</b>（君は旅行するのが好き？）
            ''', unsafe_allow_html=True)

        with st.expander("④ 2大過去形（点過去 vs 線過去）の使い分け公式", expanded=False):
            st.markdown('''
            <b>【公式】</b><br>
            - <b>点過去</b> ＝ <b>【完了した行為・一回限りの出来事・期間が区切られた過去】</b><br>
            - <b>線過去</b> ＝ <b>【過去の習慣・進行中の状態・背景描写】</b><br>
            <hr>
            <b>📖 例文と単語の分解解説:</b><br>
            1. <b>Ayer fui al cine.</b>（昨日、映画館に行きました [点過去]）<br>
            2. <b>Cuando era niño, jugaba al fútbol.</b>（子どもの頃、よくサッカーをしていました [線過去]）<br>
            3. <b>Cuando veía la tele, sonó el teléfono.</b>（テレビを見ていた時、電話が鳴った [線過去＋点過去]）
            ''', unsafe_allow_html=True)

        with st.expander("⑤ 接続法（Subjuntivo）のトリガー公式", expanded=False):
            st.markdown('''
            <b>【公式】</b><br>
            <b>【主節の動詞（願望・感情・疑惑・要求）】</b> + <b>que</b> + <b>【接続法動詞】</b><br>
            <hr>
            <b>📖 例文と単語の分解解説:</b><br>
            1. <b>Quiero que vengas a mi casa.</b>（私はあなたに私の家に来てほしい [願望]）<br>
            2. <b>Me alegro de que estés bien.</b>（あなたが元気でいてくれて嬉しいです [感情]）<br>
            3. <b>No creo que sea verdad.</b>（それが本当だとは思いません [疑惑・否定]）
            ''', unsafe_allow_html=True)

    with g_tab2:
        st.subheader("🔄 主要動詞の時制・活用早見表（カタカナ読み・意味付き）")
        sel_verb = st.selectbox("動詞を選択してください", ["hablar (話す)", "comer (食べる)", "vivir (住む)", "ser (〜である/本質)", "estar (〜にいる/状態)", "tener (持つ/年齢)", "ir (行く)"])
        conjugation_tables = {
            "hablar (話す)": pd.DataFrame({"直説法現在 (〜する)": ["hablo (アブロ: 私は話す)", "hablas (アブラス: 君は話す)", "habla (アブラ: 彼は話す)", "hablamos (アブラモス: 私たちは話す)", "hablan (アブラン: 彼らは話す)"], "点過去 (〜した)": ["hablé (アブレ: 私は話した)", "hablaste (アブラステ: 君は話した)", "habló (アブロ: 彼は話した)", "hablamos (アブラモス: 私たちは話した)", "hablaron (アブラロン: 彼らは話した)"], "線過去 (〜していた)": ["hablaba (アブラバ: 私は話していた)", "hablabas (アブラバス: 君は話していた)", "hablaba (アブラバ: 彼は話していた)", "hablábamos (アブラバモス: 私たちは〜)", "hablaban (アブラバン: 彼らは〜)"], "未来形 (〜するだろう)": ["hablaré (アブラレ: 私は話すだろう)", "hablarás (アブララス: 君は〜)", "hablará (アブララ: 彼は〜)", "hablaremos (アブラレモス: 私たちは〜)", "hablarán (アブララン: 彼らは〜)"], "接続法現在 (願望など)": ["hable (アブレ: 私が話すように)", "hables (アブレス: 君が〜)", "hable (アブレ: 彼が〜)", "hablemos (アブレモス: 私たちが〜)", "hablen (アブレン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"]),
            "comer (食べる)": pd.DataFrame({"直説法現在 (〜する)": ["como (コモ: 私は食べる)", "comes (コメス: 君は食べる)", "come (コメ: 彼は食べる)", "comemos (コメモス: 私たちは食べる)", "comen (コメン: 彼らは食べる)"], "点過去 (〜した)": ["comí (コミ: 私は食べた)", "comiste (コミステ: 君は食べた)", "comió (コミオ: 彼は食べた)", "comimos (コミモス: 私たちは食べた)", "comieron (コミエロン: 彼らは食べた)"], "線過去 (〜していた)": ["comía (コミア: 私は食べていた)", "comías (コミアス: 君は食べていた)", "comía (コミア: 彼は食べていた)", "comíamos (コミアモス: 私たちは〜)", "comían (コミアン: 彼らは〜)"], "未来形 (〜するだろう)": ["comeré (コメレ: 私は食べるだろう)", "comerás (コメラス: 君は〜)", "comerá (コメラ: 彼は〜)", "comeremos (コメレモス: 私たちは〜)", "comerán (コメラン: 彼らは〜)"], "接続法現在 (願望など)": ["coma (コマ: 私が食べるように)", "comas (コマス: 君が〜)", "coma (コマ: 彼が〜)", "comamos (コマモス: 私たちが〜)", "coman (コマン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"]),
            "vivir (住む)": pd.DataFrame({"直説法現在 (〜する)": ["vivo (ビボ: 私は住む)", "vives (ビベス: 君は住む)", "vive (ビベ: 彼は住む)", "vivimos (ビビモス: 私たちは住む)", "viven (ビベン: 彼らは住む)"], "点過去 (〜した)": ["viví (ビビ: 私は住んだ)", "viviste (ビビステ: 君は住んだ)", "vivió (ビビオ: 彼は住んだ)", "vivimos (ビビモス: 私たちは住んだ)", "vivieron (ビビエロン: 彼らは住んだ)"], "線過去 (〜していた)": ["vivía (ビビア: 私は住んでいた)", "vivías (ビビアス: 君は住んでいた)", "vivía (ビビア: 彼は住んでいた)", "vivíamos (ビビアモス: 私たちは〜)", "vivían (ビビアン: 彼らは〜)"], "未来形 (〜するだろう)": ["viviré (ビビレ: 私は住むだろう)", "vivirás (ビビラス: 君は〜)", "vivirá (ビビラ: 彼は〜)", "viviremos (ビビレモス: 私たちは〜)", "vivirán (ビビラン: 彼らは〜)"], "接続法現在 (願望など)": ["viva (ビバ: 私が住むように)", "vivas (ビバス: 君が〜)", "viva (ビバ: 彼が〜)", "vivamos (ビバモス: 私たちが〜)", "vivan (ビバン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"]),
            "ser (〜である/本質)": pd.DataFrame({"直説法現在 (〜である)": ["soy (ソイ: 私は〜です)", "eres (エレス: 君は〜です)", "es (エス: 彼は〜です)", "somos (ソモス: 私たちは〜です)", "son (ソン: 彼らは〜です)"], "点過去 (〜だった)": ["fui (フイ: 私は〜だった)", "fuiste (フイステ: 君は〜だった)", "fue (フエ: 彼は〜だった)", "fuimos (フイモス: 私たちは〜だった)", "fueron (フエロン: 彼らは〜だった)"], "線過去 (昔〜だった)": ["era (エラ: 昔私は〜だった)", "eras (エラス: 昔君は〜だった)", "era (エラ: 昔彼は〜だった)", "éramos (エラモス: 私たちは〜だった)", "eran (エラン: 彼らは〜だった)"], "未来形 (〜だろう)": ["seré (セレ: 私は〜だろう)", "serás (セラス: 君は〜だろう)", "será (セラ: 彼は〜だろう)", "seremos (セレモス: 私たちは〜だろう)", "serán (セラン: 彼らは〜だろう)"], "接続法現在 (願望など)": ["sea (セア: 私が〜であるように)", "seas (セアス: 君が〜であるように)", "sea (セア: 彼が〜であるように)", "seamos (セアモス: 私たちが〜)", "sean (セアン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"]),
            "estar (〜にいる/状態)": pd.DataFrame({"直説法現在 (〜にいる)": ["estoy (エストイ: 私はいる)", "estás (エスタス: 君はいる)", "está (エスタ: 彼はいる)", "estamos (エスタモス: 私たちはいる)", "están (エスタン: 彼らはいる)"], "点過去 (〜にいた)": ["estuve (エストゥベ: 私はいた)", "estuviste (エストゥビステ: 君はいた)", "estuvo (エストゥボ: 彼はいた)", "estuvimos (エストゥビモス: 私たちは〜)", "estuvieron (エストゥビエロン: 彼らは〜)"], "線過去 (〜にいた)": ["estaba (エスタバ: 私はいた)", "estabas (エスタバス: 君はいた)", "estaba (エスタバ: 彼はいた)", "estábamos (エスタバモス: 私たちは〜)", "estaban (エスタバン: 彼らは〜)"], "未来形 (〜にいるだろう)": ["estaré (エスタレ: 私はいるだろう)", "estarás (エスタラス: 君は〜)", "estará (エスタラ: 彼は〜)", "estaremos (エスタレモス: 私たちは〜)", "estarán (エスタラン: 彼らは〜)"], "接続法現在 (願望など)": ["esté (エステ: 私がいるように)", "estés (エステス: 君が〜)", "esté (エステ: 彼が〜)", "estemos (エステモス: 私たちが〜)", "estén (エステン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"]),
            "tener (持つ/年齢)": pd.DataFrame({"直説法現在 (持つ)": ["tengo (テンゴ: 私は持つ/〜歳)", "tienes (ティエネス: 君は持つ)", "tiene (ティエネ: 彼は持つ)", "tenemos (テメモス: 私たちは持つ)", "tienen (ティエネン: 彼らは持つ)"], "点過去 (持った/得た)": ["tuve (トゥベ: 私は持った)", "tuviste (トゥビステ: 君は持った)", "tuvo (トゥボ: 彼は持った)", "tuvimos (トゥビモス: 私たちは持った)", "tuvieron (トゥビエロン: 彼らは持った)"], "線過去 (持っていた)": ["tenía (テニア: 私は持っていた)", "tenías (テニアス: 君は持っていた)", "tenía (テニア: 彼は持っていた)", "teníamos (テニアモス: 私たちは〜)", "tenían (テニアン: 彼らは〜)"], "未来形 (持つだろう)": ["tendré (テンドレ: 私は持つだろう)", "tendrás (テンドラス: 君は〜)", "tendrá (テンドラ: 彼は〜)", "tendremos (テンドレモス: 私たちは〜)", "tendrán (テンドラン: 彼らは〜)"], "接続法現在 (願望など)": ["tenga (テンガ: 私が持つように)", "tengas (テンガス: 君が〜)", "tenga (テンガ: 彼が〜)", "tengamos (テンガモス: 私たちが〜)", "tengan (テンガン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"]),
            "ir (行く)": pd.DataFrame({"直説法現在 (行く)": ["voy (ボイ: 私は行く)", "vas (バス: 君は行く)", "va (バ: 彼は行く)", "vamos (バモス: 私たちは行く)", "van (バン: 彼らは行く)"], "点過去 (行った)": ["fui (フイ: 私は行った)", "fuiste (フイステ: 君は行った)", "fue (フエ: 彼は行った)", "fuimos (フイモス: 私たちは行った)", "fueron (フエロン: 彼らは行った)"], "線過去 (行っていた)": ["iba (イバ: 私は行っていた)", "ibas (イバス: 君は行っていた)", "iba (イバ: 彼は行っていた)", "íbamos (イバモス: 私たちは〜)", "iban (イバン: 彼らは〜)"], "未来形 (行くだろう)": ["iré (イレ: 私は行くだろう)", "irás (イラス: 君は〜)", "irá (イラ: 彼は〜)", "iremos (イレモス: 私たちは〜)", "irán (イラン: 彼らは〜)"], "接続法現在 (願望など)": ["vaya (バヤ: 私が行くように)", "vayas (バヤス: 君が〜)", "vaya (バヤ: 彼が〜)", "vayamos (バヤモス: 私たちが〜)", "vayan (バヤン: 彼らが〜)"]}, index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女/あなた)", "Nosotros (私たち)", "Ellos/Uds (彼ら/あなた方)"])
        }
        st.dataframe(conjugation_tables[sel_verb], use_container_width=True)

    with g_tab3:
        st.subheader("📋 冠詞・代名詞・前置詞の早見表")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### 📌 冠詞（定冠詞・不定冠詞）")
            art_df = pd.DataFrame({"男性単数": ["el (エル: その)", "un (ウン: 1つの)"], "女性単数": ["la (ラ: その)", "una (ウナ: 1つの)"], "男性複数": ["los (ロス: その)", "unos (ウノス: いくつかの)"], "女性複数": ["las (ラス: その)", "unas (ウナス: いくつかの)"]}, index=["定冠詞 (the)", "不定冠詞 (a / some)"])
            st.dataframe(art_df, use_container_width=True)
            st.markdown("##### 📌 所有形容詞")
            pos_df = pd.DataFrame({"単数名詞の前": ["mi (ミ: 私の)", "tu (トゥ: 君の)", "su (ス: 彼の/あなたの)", "nuestro/a (ヌエストロ: 私たちの)"], "複数名詞の前": ["mis (ミス: 私の〜たち)", "tus (トゥス: 君の〜たち)", "sus (スス: 彼の〜たち)", "nuestros/as (私たちの〜たち)"]}, index=["1人称単数 (私)", "2人称単数 (君)", "3人称 (彼/彼女/あなた)", "1人称複数 (私たち)"])
            st.dataframe(pos_df, use_container_width=True)
        with c2:
            st.markdown("##### 📌 人称代名詞・目的格代名詞")
            pron_df = pd.DataFrame({"主語 (〜は)": ["yo (ヨ: 私は)", "tú (トゥ: 君は)", "él / ella / usted (彼/彼女/あなた)", "nosotros (ノソトロス: 私たちは)", "ellos / ustedes (彼ら/あなた方)"], "直接目的語 (〜を)": ["me (メ: 私を)", "te (テ: 君を)", "lo / la (ロ/ラ: 彼を/彼女を/それを)", "nos (ノス: 私たちを)", "los / las (ロス/ラス: 彼らを/それらを)"], "間接目的語 (〜に)": ["me (メ: 私に)", "te (テ: 君に)", "le / se (レ/セ: 彼に/彼女に/あなたに)", "nos (ノス: 私たちに)", "les / se (レス/セ: 彼らに/あなた方に)"], "再帰代名詞 (自分を)": ["me (メ: 自分を)", "te (テ: 自分を)", "se (セ: 自分を)", "nos (ノス: 自分たちを)", "se (セ: 自分たちを)"]}, index=["1人称 (私)", "2人称 (君)", "3人称 (彼/彼女/あなた)", "1人称複数 (私たち)", "3人称複数 (彼ら/あなた方)"])
            st.dataframe(pron_df, use_container_width=True)

# 9. 📝 文法復習セッション (SRS)
elif menu == "📝 文法復習セッション (SRS)":
    st.title("📝 文法復習セッション (忘却曲線 SRS)")
    cards_df = get_cards_df()
    today_str = date.today().isoformat()
    
    due_cards = cards_df[(cards_df["next_review_date"] <= today_str) | (cards_df["repetitions"] == 0)].sort_values(
        ["mistake_count", "next_review_date"], ascending=[False, True]
    ).head(20)
    
    if len(due_cards) == 0:
        st.success("🎉 おめでとうございます！本日の文法復習はすべて完了しました！")
        st.balloons()
    else:
        st.caption(f"本日の復習待ちカード：残り {len(due_cards)} 問（全 {len(cards_df)} 課中）")
        if "card_index" not in st.session_state or st.session_state.card_index >= len(due_cards):
            st.session_state.card_index = 0
            st.session_state.answered = False
            st.session_state.show_hint = False
            
        card = due_cards.iloc[st.session_state.card_index]
        options = [opt.strip() for opt in card["options"].split(",")]
        
        st.progress((st.session_state.card_index + 1) / len(due_cards))
        st.markdown(f"#### 【{card['category']}】 {card['lesson_title']} (ミス: {card['mistake_count']}回 / 復習間隔: {card['interval_days']}日)")
        st.subheader(card["title"])
        
        display_sentence = card["sentence"].replace("[___]", "＿＿＿＿")
        st.markdown(f'<div style="background-color:#f0f2f6; padding:16px; border-radius:8px; font-size:1.4rem; font-weight:bold; color:#1e293b;">{display_sentence}</div>', unsafe_allow_html=True)
        
        if not st.session_state.show_hint:
            if st.button("💡 ヒントを見る"):
                st.session_state.show_hint = True
                st.rerun()
        else:
            st.info(f"💡 ヒント: {card['hint']}")
            
        if "quiz_start_time" not in st.session_state or st.session_state.get("quiz_current_card_id") != card["id"]:
            st.session_state.quiz_start_time = time.time()
            st.session_state.quiz_current_card_id = int(card["id"])
            st.session_state.quiz_elapsed_sec = 0.0

        st.write("")
        if not st.session_state.answered:
            cols = st.columns(len(options))
            for i, opt in enumerate(options):
                if cols[i].button(f"{i+1}. {opt}", key=f"quiz_opt_{i}", use_container_width=True):
                    st.session_state.quiz_elapsed_sec = max(0.1, round(time.time() - st.session_state.quiz_start_time, 1))
                    st.session_state.answered = True
                    st.session_state.selected_opt = opt
                    st.session_state.is_correct = (opt.strip().lower() == card["correct_answer"].strip().lower())
                    st.rerun()
        else:
            if st.session_state.is_correct:
                st.success(f"🎉 正解！ (正解: {card['correct_answer']})")
            else:
                st.error(f"❌ 不正解！ (あなたの選択: {st.session_state.selected_opt} ／ 正解: {card['correct_answer']})")
                
            exp_html = f'<div style="background-color:#fff7ed; border-left:4px solid #f97316; padding:12px; border-radius:6px; margin-bottom:14px;"><strong>💡 解説:</strong><br>{card["explanation"]}</div>'
            st.markdown(exp_html, unsafe_allow_html=True)
            
            # 経過日数の計算
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("SELECT reviewed_at FROM study_logs WHERE card_id = ? AND item_type = 'grammar' ORDER BY id DESC LIMIT 1", (int(card["id"]),))
            last_rev_row = c.fetchone()
            conn.close()
            
            days_since = int(card["interval_days"])
            if last_rev_row and last_rev_row[0]:
                try:
                    last_rev_dt = datetime.datetime.fromisoformat(last_rev_row[0]).date()
                    days_since = (date.today() - last_rev_dt).days
                except Exception:
                    pass

            elapsed_quiz_sec = float(st.session_state.get("quiz_elapsed_sec", 3.0))

            # スマートSRS計算
            g_reps, g_interval, g_ef, g_next_date, g_rating, g_label, g_detail = calculate_smart_srs(
                int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]),
                int(card["mistake_count"]), elapsed_quiz_sec, days_since, is_correct=st.session_state.is_correct
            )

            # AI解析フィードバックUI
            q_border_color = "#16a34a" if st.session_state.is_correct else "#dc2626"
            q_bg_color = "#f0fdf4" if st.session_state.is_correct else "#fef2f2"
            q_text_color = "#15803d" if st.session_state.is_correct else "#b91c1c"
            
            g_feedback_html = (
                f'<div style="background-color:{q_bg_color}; border:1px solid #e2e8f0; border-left:6px solid {q_border_color}; padding:14px 18px; border-radius:8px; margin-bottom:16px;">'
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">'
                f'<span style="font-weight:bold; color:{q_text_color}; font-size:1.05rem;">🧠 AI忘却曲線判定:</span>'
                f'<span style="font-weight:bold; font-size:0.9rem; color:{q_text_color};">{g_label}</span>'
                '</div>'
                f'<div style="font-size:0.95rem; color:#334155; line-height:1.6;">{g_detail}</div>'
                '</div>'
            )
            st.markdown(g_feedback_html, unsafe_allow_html=True)
            
            def submit_grammar_record(reps, interval, ef, next_date, mistakes_delta, rating, is_correct):
                init_logs_db()
                record_study_time(elapsed_quiz_sec, "grammar_srs", 1)
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                new_mistakes = max(0, int(card["mistake_count"]) + mistakes_delta)
                cursor.execute('''
                UPDATE cards 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE id = ?
                ''', (reps, interval, ef, next_date, new_mistakes, int(card["id"])))
                cursor.execute('''
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at, item_type)
                VALUES (?, ?, ?, ?, 'grammar')
                ''', (int(card["id"]), rating, is_correct, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()
                st.session_state.card_index += 1
                st.session_state.answered = False
                st.session_state.show_hint = False
                st.session_state.quiz_start_time = time.time()
                st.rerun()

            if st.button(f"次の問題に進む（{g_interval}日後に再出題 ➡️）", type="primary", use_container_width=True):
                submit_grammar_record(g_reps, g_interval, g_ef, g_next_date, 0 if st.session_state.is_correct else 1, g_rating, 1 if st.session_state.is_correct else 0)

            with st.expander("⚙️ 手動で評価を直接上書きする場合 (4段階評価)"):
                r_col1, r_col2, r_col3, r_col4 = st.columns(4)
                if r_col1.button("🔴 もう一度 (1)", key="g_m_1", use_container_width=True):
                    m_r, m_i, m_ef, m_d = calculate_sm2(int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]), 1)
                    submit_grammar_record(m_r, m_i, m_ef, m_d, 1, 1, 0)
                if r_col2.button("🟡 難しかった (2)", key="g_m_2", use_container_width=True):
                    m_r, m_i, m_ef, m_d = calculate_sm2(int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]), 2)
                    submit_grammar_record(m_r, m_i, m_ef, m_d, 0, 2, 1)
                if r_col3.button("🟢 ちょうど良い (3)", key="g_m_3", use_container_width=True):
                    m_r, m_i, m_ef, m_d = calculate_sm2(int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]), 3)
                    submit_grammar_record(m_r, m_i, m_ef, m_d, 0, 3, 1)
                if r_col4.button("🔵 簡単！ (4)", key="g_m_4", use_container_width=True):
                    m_r, m_i, m_ef, m_d = calculate_sm2(int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]), 4)
                    submit_grammar_record(m_r, m_i, m_ef, m_d, 0, 4, 1)

# 10. 📊 学習ダッシュボード
elif menu == "📊 学習ダッシュボード":
    st.title("📊 学習ダッシュボード (文法・単語・学習時間 総合)")
    cards_df = get_cards_df()
    dict_df = get_dict_df()
    chunks_df = get_chunks_df()
    
    today_str = date.today().isoformat()
    
    # 学習時間・ストリーク情報
    stats = get_user_study_stats()
    streak_days = stats["streak_days"]
    t_min = int(stats["today_seconds"] // 60)
    t_sec = int(stats["today_seconds"] % 60)
    tot_hrs = round(stats["total_seconds"] / 3600.0, 1)

    # 文法指標
    total_cards = len(cards_df)
    due_cards = len(cards_df[cards_df["next_review_date"] <= today_str])
    mastered_cards = len(cards_df[cards_df["repetitions"] >= 4])
    
    # 単語指標
    total_words = len(dict_df)
    due_words = len(dict_df[dict_df["next_review_date"] <= today_str])
    mastered_words = len(dict_df[dict_df["repetitions"] >= 4])
    learning_words = len(dict_df[(dict_df["repetitions"] > 0) & (dict_df["repetitions"] < 4)])
    unseen_words = len(dict_df[dict_df["repetitions"] == 0])

    # チャンク指標
    total_chunks = len(chunks_df)
    mastered_chunks = len(chunks_df[chunks_df["repetitions"] >= 4])

    st.subheader("🔥 モチベーション ＆ 学習時間")
    st_col1, st_col2, st_col3, st_col4 = st.columns(4)
    st_col1.metric("🔥 連続学習ストリーク", f"{streak_days} 日間", delta="毎日継続中！" if streak_days > 0 else "今日からスタート")
    st_col2.metric("⏱️ 今日の学習時間", f"{t_min}分 {t_sec}秒", delta=f"{stats['today_items']} 問完了")
    st_col3.metric("⏳ 累計総学習時間", f"{tot_hrs} 時間", delta=f"総計 {stats['total_items']} 回想起")
    st_col4.metric("📌 本日の総復習待ち", f"{due_cards + due_words} 件")

    st.divider()

    st.subheader("⏱️ 過去7日間の学習時間推移 (分)")
    daily_time_df = get_daily_study_time_df(7)
    st.bar_chart(daily_time_df.set_index("日付")["学習時間 (分)"])

    st.divider()

    st.subheader("📚 総合マスター進捗")
    col1, col2, col3 = st.columns(3)
    col1.metric("📖 文法カリキュラム", f"{total_cards} 課", delta=f"{mastered_cards} 課 定着" if mastered_cards > 0 else "学習中")
    col2.metric("🗂️ 単語マスター", f"{total_words} 語", delta=f"{mastered_words} 語 定着" if mastered_words > 0 else "学習中")
    col3.metric("🧩 定型チャンク", f"{total_chunks} 個", delta=f"{mastered_chunks} 個 定着" if mastered_chunks > 0 else "学習中")
    
    st.write("")
    st.subheader("🎯 単語・チャンクの暗記定着度 (Smart SRS ステータス)")
    v_stat_col1, v_stat_col2, v_stat_col3 = st.columns(3)
    v_stat_col1.metric("🌱 未学習の単語", f"{unseen_words} 語")
    v_stat_col2.metric("🔄 復習中 (Lv1〜3)", f"{learning_words} 語")
    v_stat_col3.metric("🏆 完全定着 (Lv4以上)", f"{mastered_words} 語")

    # カテゴリ別進捗グラフ
    st.write("")
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("⚠️ 苦手な単語 (ミス回数順)")
        mistake_words = dict_df[dict_df["mistake_count"] > 0].sort_values("mistake_count", ascending=False)
        if len(mistake_words) > 0:
            st.dataframe(
                mistake_words[["word", "reading", "category", "mistake_count", "interval_days"]].rename(
                    columns={"word": "単語", "reading": "読み", "category": "カテゴリ", "mistake_count": "ミス数", "interval_days": "間隔(日)"}
                ),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("🎉 素晴らしい！まだミスのついた単語はありません。")

    with col_right:
        st.subheader("📈 カテゴリ別 単語の習熟レベル")
        cat_word_progress = dict_df.groupby("category")["repetitions"].mean().round(1).reset_index()
        cat_word_progress.columns = ["カテゴリ", "平均習熟レベル"]
        st.bar_chart(cat_word_progress.set_index("カテゴリ"))

# 7. 📚 カリキュラム・単語一覧
elif menu == "📚 カリキュラム・単語一覧":
    st.title("📚 カリキュラム・単語データ一覧")
    cards_df = get_cards_df()
    dict_df = get_dict_df()
    
    tab1, tab2, tab3, tab4 = st.tabs(["📖 文法113課 一覧", "🗂️ 単語220語+ 一覧", "➕ 新規登録", "⚙️ データ管理 (CSV)"])
    with tab1:
        st.subheader(f"登録済み文法カリキュラム (全 {len(cards_df)} 課)")
        st.dataframe(
            cards_df[["id", "category", "lesson_title", "title", "correct_answer", "repetitions", "interval_days", "mistake_count"]].rename(
                columns={"id": "ID", "category": "章", "lesson_title": "レッスン名", "title": "問題", "correct_answer": "正解", "repetitions": "学習回数", "interval_days": "復習間隔(日)", "mistake_count": "ミス数"}
            ),
            use_container_width=True,
            hide_index=True
        )
    with tab2:
        st.subheader(f"登録済み単語マスター (全 {len(dict_df)} 語)")
        st.dataframe(
            dict_df[["id", "word", "reading", "pos", "category", "repetitions", "interval_days", "mistake_count"]].rename(
                columns={"id": "ID", "word": "単語", "reading": "読み", "pos": "品詞", "category": "カテゴリ", "repetitions": "学習回数", "interval_days": "間隔(日)", "mistake_count": "ミス数"}
            ),
            use_container_width=True,
            hide_index=True
        )
    with tab3:
        st.subheader("新しいカードを追加")
        add_type = st.radio("追加する種類", ["文法クイズカード", "単語カード"], horizontal=True)
        if add_type == "文法クイズカード":
            with st.form("add_card_form"):
                new_cat = st.selectbox("カテゴリ", list(cards_df["category"].unique()) + ["自作カスタム"])
                new_lesson = st.text_input("レッスン名", placeholder="例：カフェでの注文フレーズ")
                new_cont = st.text_area("解説コンテンツ", placeholder="例：カフェで注文する時は...")
                new_title = st.text_input("問題（日本語の意味）", placeholder="例：私はコーヒーが好きです。")
                new_sentence = st.text_input("スペイン語文（穴埋め部分は [___] と記述）", placeholder="例：Me [___] el café.")
                new_options = st.text_input("選択肢（カンマ区切りで4つ）", placeholder="例：gusta, gusto, gustas, gustan")
                new_correct = st.text_input("正解の単語", placeholder="例：gusta")
                new_hint = st.text_input("ヒント", placeholder="例：主語が単数なので...")
                new_exp = st.text_area("解説", placeholder="例：gustar動詞は〜")
                
                if st.form_submit_button("文法カードを登録する"):
                    if new_title and new_sentence and new_options and new_correct:
                        conn = sqlite3.connect(DB_PATH)
                        cursor = conn.cursor()
                        today_str = date.today().isoformat()
                        cursor.execute('''
                        INSERT INTO cards (category, lesson_title, content, title, sentence, options, correct_answer, hint, explanation, repetitions, interval_days, ease_factor, next_review_date, mistake_count, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, 2.5, ?, 0, ?)
                        ''', (new_cat, new_lesson, new_cont, new_title, new_sentence, new_options, new_correct, new_hint, new_exp, today_str, today_str))
                        conn.commit()
                        conn.close()
                        st.success(f"カード「{new_title}」を追加しました！")
                        st.rerun()
                    else:
                        st.error("必須項目を入力してください。")
        else:
            with st.form("add_word_form"):
                w_word = st.text_input("スペイン語単語", placeholder="例：viajar")
                w_reading = st.text_input("カタカナ読み", placeholder="例：ビアハール")
                w_pos = st.text_input("品詞", placeholder="例：規則動詞 [動]")
                w_cat = st.selectbox("カテゴリ", list(dict_df["category"].unique()) + ["カスタム"])
                w_meanings = st.text_area("意味・語義", placeholder="例：① 旅行する、旅をする")
                w_conj = st.text_area("人称変化・活用（全6人称）/ 性数変化（任意）", placeholder="例：<b>【現在形】</b> Yo: viajo, Tú: viajas, Él: viaja, Nosotros: viajamos, Vosotros: viajáis, Ellos: viajan")
                w_examples = st.text_area("例文", placeholder="例：・<b>Me gusta viajar.</b>（旅行するのが好きです）")

                if st.form_submit_button("単語を登録する"):
                    if w_word and w_reading and w_meanings:
                        conn = sqlite3.connect(DB_PATH)
                        cursor = conn.cursor()
                        today_str = date.today().isoformat()
                        now_str = datetime.datetime.now().isoformat()
                        cursor.execute('''
                        INSERT INTO dictionary (word, reading, pos, meanings, examples, category, conjugation, repetitions, interval_days, ease_factor, next_review_date, mistake_count, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, 2.5, ?, 0, ?)
                        ''', (w_word, w_reading, w_pos, w_meanings, w_examples, w_cat, w_conj, today_str, now_str))
                        conn.commit()
                        conn.close()
                        st.success(f"単語「{w_word}」を追加しました！")
                        st.rerun()
                    else:
                        st.error("単語・読み・意味は必須です。")

    with tab4:
        st.subheader("💾 学習進捗の完全バックアップ ＆ 復元 (JSON)")
        st.caption("Rebootや端末移行時でも安心！あなたの単語・文法・チャンクの定着レベル、復習間隔、学習時間ログを1つのファイルとして保存・復元できます。")
        
        bk_col1, bk_col2 = st.columns(2)
        with bk_col1:
            progress_json_str = export_progress_json()
            st.download_button(
                label="💾 学習進捗データをダウンロード (JSON)",
                data=progress_json_str,
                file_name=f"spanish_learning_progress_{date.today().isoformat()}.json",
                mime="application/json",
                type="primary",
                use_container_width=True
            )
        with bk_col2:
            uploaded_file = st.file_uploader("📥 バックアップJSONから進捗を復元", type=["json"], key="uploader_restore_json")
            if uploaded_file is not None:
                if st.button("🔄 復元を実行する", use_container_width=True):
                    content = uploaded_file.getvalue().decode("utf-8")
                    ok, msg = import_progress_json(content)
                    if ok:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
                        
        st.divider()
        st.subheader("📊 CSV エクスポート")
        csv_cards = cards_df.to_csv(index=False).encode('utf-8_sig')
        csv_dict = dict_df.to_csv(index=False).encode('utf-8_sig')
        
        c_dl1, c_dl2 = st.columns(2)
        with c_dl1:
            st.download_button(label="📥 全113課の文法カリキュラムをCSVダウンロード", data=csv_cards, file_name="spanish_grammar_113.csv", mime="text/csv", use_container_width=True)
        with c_dl2:
            st.download_button(label="📥 全221語の単語帳をCSVダウンロード", data=csv_dict, file_name="spanish_vocabulary_221.csv", mime="text/csv", use_container_width=True)

# 12. 📈 学習ログ・履歴分析
elif menu == "📈 学習ログ・履歴分析":
    st.title("📈 学習ログ・履歴分析")
    st.caption("日々の学習時間推移、正答率、学習カテゴリーの内訳を分析します。")

    stats = get_user_study_stats()
    streak_days = stats["streak_days"]
    t_min = int(stats["today_seconds"] // 60)
    t_sec = int(stats["today_seconds"] % 60)
    tot_hrs = round(stats["total_seconds"] / 3600.0, 1)

    s1, s2, s3, s4 = st.columns(4)
    s1.metric("🔥 連続学習ストリーク", f"{streak_days} 日間")
    s2.metric("⏱️ 今日の学習時間", f"{t_min}分 {t_sec}秒", delta=f"{stats['today_items']} 問完了")
    s3.metric("⏳ 累計総学習時間", f"{tot_hrs} 時間", delta=f"総計 {stats['total_items']} 回想起")
    
    logs_df = get_logs_df()
    if len(logs_df) > 0:
        total_ans = len(logs_df)
        total_cor = int(logs_df["is_correct"].sum())
        acc = round(total_cor / total_ans * 100, 1)
        s4.metric("🎯 累計正答率", f"{acc}%", delta=f"{total_cor}/{total_ans} 問正解")
    else:
        s4.metric("🎯 累計正答率", "-- %")

    st.divider()
    
    st.subheader("⏱️ 過去7日間の日別学習時間推移")
    daily_time_df = get_daily_study_time_df(7)
    st.bar_chart(daily_time_df.set_index("日付")["学習時間 (分)"])
    st.dataframe(daily_time_df, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("📊 正誤ログ・回答数推移")
    if len(logs_df) == 0:
        st.info("まだ学習ログがありません。「単語フラッシュカード」や「インターリービング」「パターンプラクティス」で学習を開始すると、ここにグラフが表示されます。")
    else:
        logs_df["date"] = pd.to_datetime(logs_df["reviewed_at"]).dt.date
        daily_stats = logs_df.groupby("date").agg(total_reviews=("id", "count"), correct_count=("is_correct", "sum")).reset_index()
        daily_stats["accuracy"] = (daily_stats["correct_count"] / daily_stats["total_reviews"] * 100).round(1)
        st.line_chart(daily_stats.set_index("date")[["total_reviews", "accuracy"]])
        st.dataframe(daily_stats.rename(columns={"date": "日付", "total_reviews": "総想起数", "correct_count": "正解数", "accuracy": "正答率 (%)"}), use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("💾 学習進捗のバックアップ＆復元")
    bk_c1, bk_c2 = st.columns(2)
    with bk_c1:
        st.download_button(
            label="💾 現在の学習進捗を保存 (JSON)",
            data=export_progress_json(),
            file_name=f"spanish_progress_backup_{date.today().isoformat()}.json",
            mime="application/json",
            type="primary",
            use_container_width=True
        )
    with bk_c2:
        up_file = st.file_uploader("📥 バックアップから復元", type=["json"], key="logs_restore_json")
        if up_file is not None and st.button("復元を実行 🔄", key="btn_logs_restore"):
            ok, msg = import_progress_json(up_file.getvalue().decode("utf-8"))
            if ok:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)