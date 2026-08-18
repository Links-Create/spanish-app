import streamlit as st
import sqlite3
import pandas as pd
import datetime
from datetime import date, timedelta
import os
import re
from dictionary_data import DICTIONARY_DATA

# --- ページ設定 ---
st.set_page_config(
    page_title="🇪🇸 スペイン語 1年マスター学習システム",
    page_icon="🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        category TEXT NOT NULL
    )
    ''')
    cursor.execute("SELECT COUNT(*) FROM dictionary")
    if cursor.fetchone()[0] == 0:
        for item in DICTIONARY_DATA:
            cursor.execute('''
            INSERT INTO dictionary (word, reading, pos, meanings, examples, category)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', item)
    conn.commit()
    conn.close()

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
            df = pd.read_sql_query("SELECT * FROM dictionary ORDER BY word ASC", conn)
        else:
            df = pd.read_sql_query("SELECT * FROM dictionary WHERE category = ? ORDER BY word ASC", conn, params=(category,))
    conn.close()
    return df

def init_cards_db():
    if not os.path.exists(DB_PATH):
        import generate_113_lessons
        generate_113_lessons.seed_database()
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
st.sidebar.caption("全113課・辞書＆文法マスター搭載")

menu = st.sidebar.radio(
    "メニューを選択",
    [
        "📖 学習レッスン (教科書・解説)",
        "📐 文法公式＆活用マスター",
        "🔍 スペイン語辞書 (単語・例文検索)",
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
        st.warning("⚠️ データベースを読み込み中...")
    else:
        if "current_lesson_idx" not in st.session_state:
            st.session_state.current_lesson_idx = get_last_lesson_idx()
            
        st.session_state.current_lesson_idx = max(0, min(st.session_state.current_lesson_idx, len(cards_df) - 1))
        card = cards_df.iloc[st.session_state.current_lesson_idx]
        
        last_saved = get_last_lesson_idx()
        if last_saved > 0 and st.session_state.current_lesson_idx == last_saved:
            st.info(f"📍 **前回の続き（第 {last_saved + 1} 課）から再開しています")
        
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
        st.caption(f"カテゴリー: ")
        
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
                save_last_lesson_idx(st.session_state.current_lesson_idx)
                st.rerun()
        with b_next:
            if st.button("次のレッスンに進む ➡️", disabled=(st.session_state.current_lesson_idx >= len(cards_df) - 1), use_container_width=True, key="btn_nav_next_bottom"):
                st.session_state.current_lesson_idx += 1
                save_last_lesson_idx(st.session_state.current_lesson_idx)
                st.rerun()

# 2. 📐 文法公式＆活用マスター
elif menu == "📐 文法公式＆活用マスター":
    st.title("📐 スペイン語 文法公式＆活用マスター")
    st.caption("文法ルール、例文の単語分解、活用形の意味と読み方をスッキリ整理した完全リファレンスです。")
    
    g_tab1, g_tab2, g_tab3 = st.tabs(["📐 5大文法公式（例文・単語解説付き）", "🔄 動詞活用早見表（読み・意味付き）", "📋 冠詞・代名詞・前置詞一覧"])
    
    with g_tab1:
        st.subheader("💡 覚えるべきスペイン語の 5大文法公式")
        
        with st.expander("① 代名詞と動詞の語順公式（人に + 物を + 動詞）", expanded=True):
            st.markdown('''
            **【公式】**  
            `<主語>` + **(no)** + **【人に (me / te / se / le / nos / les)】** + **【物を (lo / la / los / las)】** + **【動詞】**
            
            - **重要ポイント**:
              - 「〜に」と「〜を」の代名詞は、必ず**動詞の前**に置きます。
              - 3人称同士（`le lo` や `le la`）が連続する場合は、発音の都合で `le` が必ず **`se`** に変化します（例: `se lo doy`）。
              - 不定詞（動詞の原形）の後ろには直接くっつけられます（例: `Quiero comprártelo`）。
            
            ---
            ##### 📖 例文と単語の分解解説:
            1. **Él me lo da.**  
               - **意味**: 彼は私にそれをくれます。  
               - **単語分解**: **Él**（エル：[代] 彼は）＋ **me**（メ：[代] 私に）＋ **lo**（ロ：[代] それを）＋ **da**（ダ：[動] 与える/くれる [dar]）
            
            2. **No te lo digo.**  
               - **意味**: 君にそれを言わないよ。  
               - **単語分解**: **No**（ノ：[副] 〜ない）＋ **te**（テ：[代] 君に）＋ **lo**（ロ：[代] それを）＋ **digo**（ディゴ：[動] 言う [decir]）
            
            3. **Yo se lo explico a María.**  
               - **意味**: 私はマリアにそれを説明します。  
               - **単語分解**: **Yo**（ヨ：[代] 私は）＋ **se**（セ：[代] 彼女に [leの変化形]）＋ **lo**（ロ：[代] それを）＋ **explico**（エクスプリコ：[動] 説明する）＋ **a María**（ア マリア：マリアに）
            
            4. **Quiero comprártelo.**  
               - **意味**: 私は君にそれを買ってあげたい。  
               - **単語分解**: **Quiero**（キエロ：[動] 〜したい [querer]）＋ **comprar**（コンプラール：[動] 買う）＋ **te**（君に）＋ **lo**（それを）
            ''')
            
        with st.expander("② por と para の使い分け公式", expanded=False):
            st.markdown('''
            **【公式】**  
            - **para** ＝ **【矢印の先 ➔ 目的・用途・期限・目的地】**（〜のために、〜に向けて、〜までに）
            - **por** ＝ **【原因・理由・手段・通過・交換・期間】**（〜のせいで/おかげで、〜を通って、〜によって）
            
            ---
            ##### 📖 例文と単語の分解解説:
            1. **Estudio para trabajar en España.**  
               - **意味**: 私はスペインで働くために勉強しています。（**目的**）  
               - **単語分解**: **Estudio**（エストゥディオ：勉強する [estudiar]）＋ **para**（パラ：〜のために）＋ **trabajar**（トラバハール：働く）＋ **en España**（エン エスパーニャ：スペインで）
            
            2. **El tren sale para Madrid.**  
               - **意味**: 電車はマドリードに向けて出発します。（**目的地**）  
               - **単語分解**: **El tren**（エル トレン：[男] 電車）＋ **sale**（サレ：出発する [salir]）＋ **para Madrid**（パラ マドリード：マドリードへ向けて）
            
            3. **Es para mañana.**  
               - **意味**: それは明日まで（の期限）です。（**期限**）  
               - **単語分解**: **Es**（エス：〜である [ser]）＋ **para mañana**（パラ マニャーナ：明日までに）
            
            4. **Gracias por tu ayuda.**  
               - **意味**: 手伝ってくれてありがとう。（**原因・理由**）  
               - **単語分解**: **Gracias**（グラシアス：ありがとう）＋ **por**（ポル：〜に対して）＋ **tu ayuda**（トゥ アユダ：[女] 君の手助け）
            
            5. **Viajo por tren.**  
               - **意味**: 私は電車で旅行します。（**手段**）  
               - **単語分解**: **Viajo**（ビアホ：旅行する [viajar]）＋ **por tren**（ポル トレン：電車によって）
            
            6. **Camino por el parque.**  
               - **意味**: 私は公園を通って散歩します。（**通過**）  
               - **単語分解**: **Camino**（カミーノ：歩く [caminar]）＋ **por el parque**（ポル エル パルケ：[男] 公園を通って）
            ''')

        with st.expander("③ gustar 型動詞の文型公式（主語が後ろに来る受動構造）", expanded=False):
            st.markdown('''
            **【公式】**  
            (A + 人) + **【間接代名詞 (me / te / le / nos / les)】** + **【動詞 (gusta / gustan)】** + **【好きな物・事】**
            
            - 英語の *like* と違い、**「好きな対象」が文の主語**になります。
            - 好きな物が**単数**または**動詞の原形**なら ➔ **gusta**
            - 好きな物が**複数**なら ➔ **gustan**
            
            ---
            ##### 📖 例文と単語の分解解説:
            1. **Me gusta el café.**  
               - **直訳**: コーヒーが私に好まれる。 ➔ **意味**: 私はコーヒーが好きです。  
               - **単語分解**: **Me**（メ：私に）＋ **gusta**（グスタ：好かれている [単数]）＋ **el café**（エル カフェ：[男] コーヒー [単数主語]）
            
            2. **Me gustan los perros.**  
               - **直訳**: 犬たちが私に好まれる。 ➔ **意味**: 私は犬が好きです。  
               - **単語分解**: **Me**（メ：私に）＋ **gustan**（グスタン：好かれている [複数]）＋ **los perros**（ロス ペロス：[男] 犬たち [複数主語]）
            
            3. **¿Te gusta viajar?**  
               - **意味**: 君は旅行するのが好き？  
               - **単語分解**: **Te**（テ：君に）＋ **gusta**（グスタ：好かれている）＋ **viajar**（ビアハール：[動] 旅行すること [動詞原形は単数扱い]）
            ''')

        with st.expander("④ 2大過去形（点過去 vs 線過去）の使い分け公式", expanded=False):
            st.markdown('''
            **【公式】**  
            - **点過去** ＝ **【完了した行為・一回限りの出来事・期間が区切られた過去】**
            - **線過去** ＝ **【過去の習慣・進行中の状態・背景描写】**
            
            ---
            ##### 📖 例文と単語の分解解説:
            1. **Ayer fui al cine.**  
               - **意味**: 昨日、映画館に行きました。（**点過去**：昨日の1回限りの行為）  
               - **単語分解**: **Ayer**（アジェール：昨日）＋ **fui**（フイ：行った [irの点過去1人称]）＋ **al cine**（アル シネ：映画館へ）
            
            2. **Cuando era niño, jugaba al fútbol.**  
               - **意味**: 子どもの頃、私はよくサッカーをしていました。（**線過去**：昔の習慣）  
               - **単語分解**: **Cuando**（クアンド：〜の時）＋ **era niño**（エラ ニニョ：子どもだった [ser]）＋ **jugaba**（フガバ：遊んでいた [jugar]）＋ **al fútbol**（アル フトボル：サッカーを）
            
            3. **Cuando veía la tele, sonó el teléfono.**  
               - **意味**: 私がテレビを見ていた（背景）時、電話が鳴った（一瞬の割り込み）。  
               - **単語分解**: **veía**（ベイア：見ていた [ver]）＋ **la tele**（テレビを）＋ **sonó**（ソノ：鳴った [sonar]）＋ **el teléfono**（電話が）
            ''')

        with st.expander("⑤ 接続法（Subjuntivo）のトリガー公式", expanded=False):
            st.markdown('''
            **【公式】**  
            **【主節の動詞（願望・感情・疑惑・要求）】** + **que** + **【接続法動詞】**
            
            ---
            ##### 📖 例文と単語の分解解説:
            1. **Quiero que vengas a mi casa.**  
               - **意味**: 私はあなたに私の家に来てほしい。（**願望**）  
               - **単語分解**: **Quiero**（キエロ：私は望む）＋ **que**（〜ということを）＋ **vengas**（ベンガス：あなたが来る [venir接続法]）＋ **a mi casa**（私の家へ）
            
            2. **Me alegro de que estés bien.**  
               - **意味**: あなたが元気でいてくれて嬉しいです。（**感情**）  
               - **単語分解**: **Me alegro de**（メ アレグロ デ：嬉しく思う）＋ **que**（〜であることを）＋ **estés**（エステス：あなたが〜である [estar接続法]）＋ **bien**（元気で）
            
            3. **No creo que sea verdad.**  
               - **意味**: それが本当だとは思いません。（**疑惑・否定**）  
               - **単語分解**: **No creo**（ノ クレオ：信じない）＋ **que**（〜だとは）＋ **sea**（セア：〜である [ser接続法]）＋ **verdad**（ベルダッ(ド)：本当のこと）
            ''')

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

# 3. 🔍 スペイン語辞書 (単語・例文検索)
elif menu == "🔍 スペイン語辞書 (単語・例文検索)":
    st.title("🔍 スペイン語 実用例文つき辞書")
    st.caption("単語の複数の意味、カタカナ発音、品詞（性別）、実際の日常会話で使える例文を確認できます。")
    
    init_dict_db()
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        search_query = st.text_input("🔍 単語・意味・例文を検索", placeholder="例：tener, 家, 食べる, para, 旅行, ありがとう...", key="dict_search_input")
    with d_col2:
        sel_cat = st.selectbox("🏷️ 品詞フィルター", ["すべて", "動詞", "名詞", "形容詞", "前置詞", "副詞"], key="dict_cat_filter")
        
    dict_results = get_dict_df(search_query, sel_cat)
    
    st.caption(f"検索結果: **{len(dict_results)}** 件の単語が見つかりました")
    st.divider()
    
    if len(dict_results) == 0:
        st.info(f"「**{search_query}**」に一致する単語が見つかりませんでした。別のキーワード（スペイン語または日本語）でお試しください。")
    else:
        for _, entry in dict_results.iterrows():
            with st.container():
                st.markdown(f'''
                <div style="background-color:#ffffff; border:1px solid #e2e8f0; border-left:6px solid #f59e0b; padding:18px; border-radius:10px; margin-bottom:18px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
                    <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
                        <span style="font-size:1.6rem; font-weight:bold; color:#1e293b;">{entry['word']}</span>
                        <span style="font-size:1.05rem; color:#64748b; margin-left:12px;">【{entry['reading']}】</span>
                        <span style="background-color:#fef3c7; color:#92400e; padding:3px 10px; border-radius:12px; font-size:0.85rem; font-weight:bold; margin-left:auto;">{entry['pos']}</span>
                    </div>
                    <div style="margin-top:10px; padding:12px; background-color:#fffbeb; border-radius:6px; font-size:1.05rem; line-height:1.7; color:#334155;">
                        <strong style="color:#b45309;">📖 意味・語義:</strong><br>
                        {entry['meanings']}
                    </div>
                    <div style="margin-top:12px; padding:12px; background-color:#f8fafc; border-radius:6px; font-size:1.0rem; line-height:1.8; color:#1e293b;">
                        <strong style="color:#0284c7;">💬 実用例文:</strong><br>
                        {entry['examples']}
                    </div>
                </div>
                ''', unsafe_allow_html=True)

# 4. 📝 今日の復習・クイズ (SRS)
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

# 5. 📊 学習ダッシュボード
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

# 6. 📚 単語・文法カード一覧
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
        
        st.write("")
        st.divider()
        st.subheader("🔄 初期カリキュラムのリセット")
        st.caption("全113課の公式カリキュラムデータを初期状態に再ロードします。")
        if st.button("⚠️ 全113課の公式データを再初期化する", key="btn_reset_curriculum"):
            import generate_113_lessons
            generate_113_lessons.seed_database()
            st.success("✅ 全113課のカリキュラムデータを再初期化しました！")
            st.rerun()

# 7. 📈 学習ログ・履歴分析
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