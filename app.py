import streamlit as st
import sqlite3
import pandas as pd
import datetime
from datetime import date, timedelta
import os
import re

# --- ページ設定 ---
st.set_page_config(
    page_title="🇪🇸 スペイン語 1年マスター学習システム",
    page_icon="🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

DB_PATH = "spanish_learning.db"

def get_cards_df():
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM cards", conn)
    conn.close()
    if not df.empty:
        for col in ["id", "repetitions", "interval_days", "mistake_count"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        if "ease_factor" in df.columns:
            df["ease_factor"] = pd.to_numeric(df["ease_factor"], errors="coerce").fillna(2.5).astype(float)
    return df

def get_logs_df():
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

st.sidebar.title("🇪🇸 Español SRS")
st.sidebar.caption("全113課・発音＆文法マスター搭載")

menu = st.sidebar.radio(
    "メニューを選択",
    [
        "📖 学習レッスン (教科書・解説)",
        "📐 文法公式＆活用マスター",
        "📝 今日の復習・クイズ (SRS)",
        "📊 学習ダッシュボード",
        "📚 単語・文法カード一覧",
        "📈 学習ログ・履歴分析"
    ]
)

# 1. 📖 学習レッスン (教科書・解説)
if menu == "📖 学習レッスン (教科書・解説)":
    st.title("📖 スペイン語 体系的学習レッスン")
    cards_df = get_cards_df()
    
    if len(cards_df) == 0:
        st.warning("⚠️ データベースを構築中です。ステップ2のコマンドを実行してください。")
    else:
        if "current_lesson_idx" not in st.session_state:
            st.session_state.current_lesson_idx = 0
            
        st.session_state.current_lesson_idx = max(0, min(st.session_state.current_lesson_idx, len(cards_df) - 1))
        card = cards_df.iloc[st.session_state.current_lesson_idx]
        
        c_cat, c_les = st.columns(2)
        with c_cat:
            categories = list(cards_df["category"].unique())
            cat_idx = categories.index(card["category"]) if card["category"] in categories else 0
            sel_cat = st.selectbox("📚 章を選択してジャンプ", categories, index=cat_idx)
            if sel_cat != card["category"]:
                first_idx = cards_df[cards_df["category"] == sel_cat].index[0]
                st.session_state.current_lesson_idx = int(first_idx)
                st.rerun()
                
        with c_les:
            cat_cards = cards_df[cards_df["category"] == sel_cat]
            les_list = list(cat_cards["lesson_title"])
            cur_les_idx_in_cat = les_list.index(card["lesson_title"]) if card["lesson_title"] in les_list else 0
            sel_lesson = st.selectbox("📑 レッスンを選択", les_list, index=cur_les_idx_in_cat)
            if sel_lesson != card["lesson_title"]:
                target_idx = cards_df[cards_df["lesson_title"] == sel_lesson].index[0]
                st.session_state.current_lesson_idx = int(target_idx)
                st.rerun()

        nav_prev, nav_info, nav_next = st.columns(3)
        with nav_prev:
            if st.button("⬅️ 前のレッスン", disabled=(st.session_state.current_lesson_idx == 0), use_container_width=True, key="btn_nav_prev_top"):
                st.session_state.current_lesson_idx -= 1
                st.rerun()
        with nav_info:
            progress_val = (st.session_state.current_lesson_idx + 1) / len(cards_df)
            st.progress(progress_val, text=f"進捗: {st.session_state.current_lesson_idx + 1} / {len(cards_df)} 課")
        with nav_next:
            if st.button("次のレッスン ➡️", disabled=(st.session_state.current_lesson_idx >= len(cards_df) - 1), use_container_width=True, key="btn_nav_next_top"):
                st.session_state.current_lesson_idx += 1
                st.rerun()

        st.divider()
        st.subheader(f"💡 第 {st.session_state.current_lesson_idx + 1} 課: {card['lesson_title']}")
        st.caption(f"カテゴリー: **{card['category']}")
        
        st.markdown(f'''
        <div style="background-color:#f8fafc; border-left:5px solid #0284c7; padding:18px; border-radius:8px; font-size:1.1rem; line-height:1.8; color:#1e293b;">
            {card['content']}
        </div>
        ''', unsafe_allow_html=True)
        
        st.write("")
        st.markdown("### ✍️ 理解度チェック問題")
        st.write(f"**")
        
        disp_sent = card["sentence"].replace("[___]", "＿＿＿＿")
        st.markdown(f'<div style="background-color:#f1f5f9; padding:14px; border-radius:6px; font-size:1.25rem; font-weight:bold;">{disp_sent}</div>', unsafe_allow_html=True)
        
        options = [opt.strip() for opt in card["options"].split(",")]
        cols = st.columns(len(options))
        for i, opt in enumerate(options):
            if cols[i].button(f"{i+1}. {opt}", key=f"less_opt_{i}_{card['id']}", use_container_width=True):
                if opt.strip().lower() == card["correct_answer"].strip().lower():
                    st.success(f"🎉 **正解です！ （正解: **）")
                else:
                    st.error(f"❌ **不正解です。 （正解は: **）")
                st.info(f"💡 **解説**: {card['explanation']}")

        st.divider()
        b_prev, b_spacer, b_next = st.columns(3)
        with b_prev:
            if st.button("⬅️ 前のレッスンに戻る", disabled=(st.session_state.current_lesson_idx == 0), use_container_width=True, key="btn_nav_prev_bottom"):
                st.session_state.current_lesson_idx -= 1
                st.rerun()
        with b_next:
            if st.button("次のレッスンに進む ➡️", disabled=(st.session_state.current_lesson_idx >= len(cards_df) - 1), use_container_width=True, key="btn_nav_next_bottom"):
                st.session_state.current_lesson_idx += 1
                st.rerun()

# 2. 📐 文法公式＆活用マスター
elif menu == "📐 文法公式＆活用マスター":
    st.title("📐 スペイン語 文法公式＆活用マスター")
    st.caption("初学者が迷いやすい文法ルール、語順、動詞の活用をスッキリ整理したリファレンスです。")
    
    g_tab1, g_tab2, g_tab3 = st.tabs(["📐 5大文法公式", "🔄 動詞活用早見表", "📋 冠詞・代名詞・前置詞一覧"])
    
    with g_tab1:
        st.subheader("💡 覚えるべきスペイン語の 5大文法公式")
        with st.expander("① 代名詞と動詞の語順公式（人に + 物を + 動詞）", expanded=True):
            st.markdown('''
            **【公式】**  
            `<主語>` + **(no)** + **【人に (me / te / se / le / nos / les)】** + **【物を (lo / la / los / las)】** + **【動詞】**
            
            - **重要ポイント**:
              - 「〜に」と「〜を」の代名詞は、必ず**動詞の前**に置きます。
              - 3人称同士（`le lo` や `le la`）が連続する場合は、発音の都合で `le` が必ず **`se`** に変化します（例: `se lo doy`）。
              - 不定詞（動詞の原形）の後ろには直接くっつけることができます（例: `Quiero comprártelo`）。
            
            > **例文**:  
            > ・Él **me lo** da.（彼は私にそれをくれます）  
            > ・**No te lo** digo.（君にそれを言わないよ）  
            > ・Yo **se lo** explico a María.（私はマリアにそれを説明します）
            ''')
            
        with st.expander("② por と para の使い分け公式", expanded=False):
            st.markdown('''
            **【公式】**  
            - **para** ＝ **【矢印の先 ➔ 目的・用途・期限・目的地】**
            - **por** ＝ **【原因・理由・手段・通過・交換・期間】**
            
            | 前置詞 | 表す意味のイメージ | 例文 |
            | :--- | :--- | :--- |
            | **para** | 目的（〜のために） | Estudio **para** trabajar en España.（働くために勉強する） |
            | **para** | 目的地・期限 | El tren sale **para** Madrid. / Es **para** mañana.（明日まで） |
            | **por** | 原因・理由（〜のせいで/おかげで） | Gracias **por** tu幫助.（手伝ってくれてありがとう） |
            | **por** | 手段・経路 | Viajo **por** tren. / Camino **por** el parque.（公園を通る） |
            ''')

        with st.expander("③ gustar 型動詞の文型公式（主語が後ろに来る受動構造）", expanded=False):
            st.markdown('''
            **【公式】**  
            (A + 人) + **【間接代名詞 (me / te / le / nos / les)】** + **【動詞 (gusta / gustan)】** + **【好きな物・事】**
            
            - 英語の *like* と違い、「好きな対象」が主語になります。
            - 好きな物が**単数**または**動詞の原形**なら ➔ **gusta**
            - 好きな物が**複数**なら ➔ **gustan**
            
            > **例文**:  
            > ・**Me gusta** el café.（私はコーヒーが好きです：単数）  
            > ・**Me gustan** los perros.（私は犬が好きです：複数）  
            > ・¿**Te gusta** viajar?（君は旅行が好き？：動詞原形）
            ''')

        with st.expander("④ 2大過去形（点過去 vs 線過去）の使い分け公式", expanded=False):
            st.markdown('''
            **【公式】**  
            - **点過去** ＝ **【完了した行為・一回限りの出来事・期間が区切られた過去】**
            - **線過去** ＝ **【過去の習慣・進行中の状態・背景描写（〜していた、〜だった）】**
            
            > **黄金の組み合わせパターン**:  
            > **「〜していた時（線過去）、…が起きた（点過去）」**  
            > ・Cuando **veía** la tele (線過去), **sonó** el teléfono (点過去).  
            > （テレビを見ていた時、電話が鳴った）
            ''')

        with st.expander("⑤ 接続法（Subjuntivo）のトリガー公式", expanded=False):
            st.markdown('''
            **【公式】**  
            **【主節の動詞（願望・感情・疑惑・要求）】** + **que** + **【接続法動詞】**
            
            > **定番トリガー**:  
            > ・願望：**Quiero que** vengas.（あなたに来てほしい）  
            > ・感情：**Me alegro de que** estés bien.（元気で嬉しい）  
            > ・否定・疑い：**No creo que** sea verdad.（本当だとは思わない）
            ''')

    with g_tab2:
        st.subheader("🔄 主要動詞の時制・活用早見表")
        sel_verb = st.selectbox("動詞を選択してください", ["hablar (話す)", "comer (食べる)", "vivir (住む)", "ser (〜である)", "estar (〜にいる)", "tener (持つ)", "ir (行く)"])
        conjugations = {
            "hablar (話す)": {"現在形": ["hablo", "hablas", "habla", "hablamos", "hablan"], "点過去": ["hablé", "hablaste", "habló", "hablamos", "hablaron"], "線過去": ["hablaba", "hablabas", "hablaba", "hablábamos", "hablaban"], "未来形": ["hablaré", "hablarás", "hablará", "hablaremos", "hablarán"], "接続法現在": ["hable", "hables", "hable", "hablemos", "hablen"]},
            "comer (食べる)": {"現在形": ["como", "comes", "come", "comemos", "comen"], "点過去": ["comí", "comiste", "comió", "comimos", "comieron"], "線過去": ["comía", "comías", "comía", "comíamos", "comían"], "未来形": ["comeré", "comerás", "comerá", "comeremos", "comerán"], "接続法現在": ["coma", "comas", "coma", "comamos", "coman"]},
            "vivir (住む)": {"現在形": ["vivo", "vives", "vive", "vivimos", "viven"], "点過去": ["viví", "viviste", "vivió", "vivimos", "vivieron"], "線過去": ["vivía", "vivías", "vivía", "vivíamos", "vivían"], "未来形": ["viviré", "vivirás", "vivirá", "viviremos", "vivirán"], "接続法現在": ["viva", "vivas", "viva", "vivamos", "vivan"]},
            "ser (〜である)": {"現在形": ["soy", "eres", "es", "somos", "son"], "点過去": ["fui", "fuiste", "fue", "fuimos", "fueron"], "線過去": ["era", "eras", "era", "éramos", "eran"], "未来形": ["seré", "serás", "será", "seremos", "serán"], "接続法現在": ["sea", "seas", "sea", "seamos", "sean"]},
            "estar (〜にいる)": {"現在形": ["estoy", "estás", "está", "estamos", "están"], "点過去": ["estuve", "estuviste", "estuvo", "estuvimos", "estuvieron"], "線過去": ["estaba", "estabas", "estaba", "estábamos", "estaban"], "未来形": ["estaré", "estarás", "estará", "estaremos", "estarán"], "接続法現在": ["esté", "estés", "esté", "estemos", "estén"]},
            "tener (持つ)": {"現在形": ["tengo", "tienes", "tiene", "tenemos", "tienen"], "点過去": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvieron"], "線過去": ["tenía", "tenías", "tenía", "teníamos", "tenían"], "未来形": ["tendré", "tendrás", "tendrá", "tendremos", "tendrán"], "接続法現在": ["tenga", "tengas", "tenga", "tengamos", "tengan"]},
            "ir (行く)": {"現在形": ["voy", "vas", "va", "vamos", "van"], "点過去": ["fui", "fuiste", "fue", "fuimos", "fueron"], "線過去": ["iba", "ibas", "iba", "íbamos", "iban"], "未来形": ["iré", "irás", "irá", "iremos", "irán"], "接続法現在": ["vaya", "vayas", "vaya", "vayamos", "vayan"]}
        }
        v_df = pd.DataFrame(conjugations[sel_verb], index=["Yo (私)", "Tú (君)", "Él/Ella/Ud (彼/彼女)", "Nosotros (私たち)", "Ellos/Uds (彼ら)"])
        st.dataframe(v_df, use_container_width=True)

    with g_tab3:
        st.subheader("📋 冠詞・代名詞・前置詞の早見表")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### 📌 冠詞（定冠詞・不定冠詞）")
            art_df = pd.DataFrame({"男性単数": ["el", "un"], "女性単数": ["la", "una"], "男性複数": ["los", "unos"], "女性複数": ["las", "unas"]}, index=["定冠詞 (the)", "不定冠詞 (a / some)"])
            st.dataframe(art_df, use_container_width=True)
            st.markdown("##### 📌 所有形容詞")
            pos_df = pd.DataFrame({"単数名詞の前": ["mi (私の)", "tu (君の)", "su (彼の/あなたの)", "nuestro/a (私たちの)"], "複数名詞の前": ["mis", "tus", "sus", "nuestros/as"]}, index=["1人称単数", "2人称単数", "3人称", "1人称複数"])
            st.dataframe(pos_df, use_container_width=True)
        with c2:
            st.markdown("##### 📌 人称代名詞・目的格代名詞")
            pron_df = pd.DataFrame({"主語 (私は)": ["yo", "tú", "él / ella / usted", "nosotros", "ellos / ustedes"], "直接 (〜を)": ["me", "te", "lo / la", "nos", "los / las"], "間接 (〜に)": ["me", "te", "le (se)", "nos", "les (se)"], "再帰 (自分を)": ["me", "te", "se", "nos", "se"]}, index=["私", "君", "彼/彼女/あなた", "私たち", "彼ら/あなた方"])
            st.dataframe(pron_df, use_container_width=True)

# 3. 📝 今日の復習・クイズ (SRS)
elif menu == "📝 今日の復習・クイズ (SRS)":
    st.title("📝 スペイン語 復習セッション (忘却曲線)")
    cards_df = get_cards_df()
    today_str = date.today().isoformat()
    
    due_cards = cards_df[(cards_df["next_review_date"] <= today_str) | (cards_df["repetitions"] == 0)].sort_values(
        ["mistake_count", "next_review_date"], ascending=[False, True]
    ).head(20)
    
    if len(due_cards) == 0:
        st.success("🎉 おめでとうございます！本日の復習はすべて完了しました！")
        st.balloons()
    else:
        st.caption(f"本日の復習待ちカード：残り **{len(due_cards)}** 問（全 {len(cards_df)} 課中）")
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
            st.info(f"💡 **ヒント**: {card['hint']}")
            
        st.write("")
        if not st.session_state.answered:
            cols = st.columns(len(options))
            for i, opt in enumerate(options):
                if cols[i].button(f"{i+1}. {opt}", key=f"quiz_opt_{i}", use_container_width=True):
                    st.session_state.answered = True
                    st.session_state.selected_opt = opt
                    st.session_state.is_correct = (opt.strip().lower() == card["correct_answer"].strip().lower())
                    st.rerun()
        else:
            if st.session_state.is_correct:
                st.success(f"🎉 **正解！ （正解: **）")
            else:
                st.error(f"❌ **不正解！ （あなたの選択: {st.session_state.selected_opt} ／ 正解: **）")
                
            st.markdown(f'''
            <div style="background-color:#fff7ed; border-left:4px solid #f97316; padding:12px; border-radius:6px;">
                <strong>💡 解説:</strong><br>{card['explanation']}
            </div>
            ''', unsafe_allow_html=True)
            
            st.write("")
            st.markdown("##### 🧠 記憶の定着度（自己評価）を選択してください:")
            r_col1, r_col2, r_col3, r_col4 = st.columns(4)
            
            def submit_rating(rating):
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                reps, interval, ef, next_date = calculate_sm2(
                    int(card["repetitions"]), int(card["interval_days"]), float(card["ease_factor"]), rating
                )
                mistakes = int(card["mistake_count"]) + (1 if rating == 1 else 0)
                cursor.execute('''
                UPDATE cards 
                SET repetitions = ?, interval_days = ?, ease_factor = ?, next_review_date = ?, mistake_count = ?
                WHERE id = ?
                ''', (reps, interval, ef, next_date, mistakes, int(card["id"])))
                cursor.execute('''
                INSERT INTO study_logs (card_id, rating, is_correct, reviewed_at)
                VALUES (?, ?, ?, ?)
                ''', (int(card["id"]), rating, 1 if rating >= 3 else 0, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()
                st.session_state.card_index += 1
                st.session_state.answered = False
                st.session_state.show_hint = False
                st.rerun()

            if r_col1.button("🔴 もう一度 (Again)<br><small>明日復習</small>", use_container_width=True):
                submit_rating(1)
            if r_col2.button("🟡 難しかった (Hard)<br><small>短い間隔</small>", use_container_width=True):
                submit_rating(2)
            if r_col3.button("🟢 ちょうど良い (Good)<br><small>標準間隔</small>", use_container_width=True):
                submit_rating(3)
            if r_col4.button("🔵 簡単！ (Easy)<br><small>長い間隔</small>", use_container_width=True):
                submit_rating(4)

# 4. 📊 学習ダッシュボード
elif menu == "📊 学習ダッシュボード":
    st.title("📊 学習ダッシュボード")
    cards_df = get_cards_df()
    
    today_str = date.today().isoformat()
    total_cards = len(cards_df)
    due_cards = len(cards_df[cards_df["next_review_date"] <= today_str])
    mastered_cards = len(cards_df[cards_df["repetitions"] >= 4])
    unseen_cards = len(cards_df[cards_df["repetitions"] == 0])
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📌 本日の復習待ち", f"{due_cards} 問", delta=f"{due_cards} 件" if due_cards > 0 else "完了！", delta_color="inverse")
    col2.metric("🌱 未学習カード", f"{unseen_cards} 問")
    col3.metric("🏆 定着済み (Lv4以上)", f"{mastered_cards} 問")
    col4.metric("📚 カリキュラム総数", f"{total_cards} 課")
    
    st.divider()
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("⚠️ 苦手な項目ランキング (ミス回数順)")
        mistake_df = cards_df[cards_df["mistake_count"] > 0].sort_values("mistake_count", ascending=False)
        if len(mistake_df) > 0:
            st.dataframe(
                mistake_df[["category", "lesson_title", "correct_answer", "mistake_count", "interval_days"]].rename(
                    columns={"category": "カテゴリ", "lesson_title": "レッスン", "correct_answer": "正解", "mistake_count": "ミス回数", "interval_days": "復習間隔(日)"}
                ),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("🎉 素晴らしい！まだミスしたカードはありません。")
    with col_right:
        st.subheader("🎯 カテゴリ別の学習進捗")
        cat_progress = cards_df.groupby("category")["repetitions"].mean().round(1).reset_index()
        cat_progress.columns = ["カテゴリ", "平均習熟レベル"]
        st.bar_chart(cat_progress.set_index("カテゴリ"))

# 5. 📚 単語・文法カード一覧
elif menu == "📚 単語・文法カード一覧":
    st.title("📚 カリキュラム・カード一覧")
    cards_df = get_cards_df()
    
    tab1, tab2, tab3 = st.tabs(["📋 全113課の一覧", "➕ 新規カード追加", "⚙️ データ管理 (CSV)"])
    with tab1:
        st.subheader(f"登録済みカリキュラム (全 {len(cards_df)} 課)")
        st.dataframe(
            cards_df[["id", "category", "lesson_title", "title", "correct_answer", "repetitions", "interval_days", "mistake_count"]].rename(
                columns={"id": "ID", "category": "章", "lesson_title": "レッスン名", "title": "問題", "correct_answer": "正解", "repetitions": "学習回数", "interval_days": "復習間隔(日)", "mistake_count": "ミス数"}
            ),
            use_container_width=True,
            hide_index=True
        )
    with tab2:
        st.subheader("新しいカードを追加")
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
            
            if st.form_submit_button("カードを登録する"):
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

    with tab3:
        st.subheader("CSV エクスポート / 初期化")
        csv_data = cards_df.to_csv(index=False).encode('utf-8_sig')
        st.download_button(label="📥 全113課のカリキュラムをCSVでダウンロード", data=csv_data, file_name="spanish_curriculum_113.csv", mime="text/csv")

# 6. 📈 学習ログ・履歴分析
elif menu == "📈 学習ログ・履歴分析":
    st.title("📈 学習ログ・履歴分析")
    logs_df = get_logs_df()
    
    if len(logs_df) == 0:
        st.info("まだ学習履歴がありません。「今日の復習・クイズ」で学習を開始すると、ここにグラフが表示されます。")
    else:
        logs_df["date"] = pd.to_datetime(logs_df["reviewed_at"]).dt.date
        daily_stats = logs_df.groupby("date").agg(total_reviews=("id", "count"), correct_count=("is_correct", "sum")).reset_index()
        daily_stats["accuracy"] = (daily_stats["correct_count"] / daily_stats["total_reviews"] * 100).round(1)
        st.subheader("📅 日別の学習量と正答率")
        st.line_chart(daily_stats.set_index("date")[["total_reviews", "accuracy"]])
        st.dataframe(daily_stats.rename(columns={"date": "日付", "total_reviews": "総復習数", "correct_count": "正解数", "accuracy": "正答率 (%)"}), use_container_width=True, hide_index=True)
