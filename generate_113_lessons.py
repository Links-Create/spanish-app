import sqlite3
import datetime
import os

DB_PATH = "spanish_learning.db"

LESSONS_DATA = [
    # --- 0. 発音・文字と基本ルール (第1課〜第8課) ---
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第1課: 無音の「h」ルール (Hは発音しない)",
        "content": "<b>【発音の基本ルール】</b><br>スペイン語の <b>h</b> (アチェ) は原則として全く発音しません（無音）。<br>・<i>hola</i>（オラ）: こんにちは<br>・<i>hotel</i>（オテル）: ホテル<br>・<i>hijo</i>（イホ）: 息子<br><br>※<i>ch</i> は「チ」と発音します（例: <i>chico</i> チコ）。",
        "title": "「h」の発音ルール",
        "sentence": "「こんにちは」を意味する \"hola\" の正しい発音はどれでしょう？ [___]",
        "options": "オラ, ホラ, ジョラ, コラ",
        "correct_answer": "オラ",
        "hint": "スペイン語の h は発音しません。",
        "explanation": "スペイン語では h を発音しないため、hola は「オラ」と読みます。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第2課: 「b」と「v」は同じ音 (バ行の音)",
        "content": "<b>【b と v の発音】</b><br>スペイン語では <b>b</b> と <b>v</b> の発音上の区別がなく、どちらも「バ行」の音になります。<br>・<i>vino</i>（ビノ）: ワイン<br>・<i>bueno</i>（ブエノ）: 良い<br>・<i>vaca</i>（バカ）: 牛",
        "title": "b と v の同音ルール",
        "sentence": "「ワイン」を意味する \"vino\" の発音として正しいものはどれでしょう？ [___]",
        "options": "ビノ, ヴィノ, フィノ, ピノ",
        "correct_answer": "ビノ",
        "hint": "v も b と同じくバ行音になります。",
        "explanation": "スペイン語では v と b の区別がなく、どちらもバ行音（ビノ）となります。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第3課: 巻き舌の「rr」と通常の「r」",
        "content": "<b>【r と rr の発音】</b><br>語頭の <b>r</b> や、単語の途中の <b>rr</b> は舌を震わせる「巻き舌」で発音します。<br>・<i>pero</i>（ペロ）: しかし（単一のr）<br>・<i>perro</i>（ペロ/巻き舌）: 犬（double rr）",
        "title": "巻き舌のルール",
        "sentence": "「犬」を意味する \"perro\" の r の発音はどうするべきでしょう？ [___]",
        "options": "舌を震わせる巻き舌で発音する, 英語のRのように奥に引く, サイレントで発音しない, Lの音に置き換える",
        "correct_answer": "舌を震わせる巻き舌で発音する",
        "hint": "rr は強く巻き舌で発音します。",
        "explanation": "rr は舌を強く震わせる巻き舌音です。pero (しかし) と perro (犬) の区別に重要です。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第4課: 「ll」と「y」の発音 (ジェ・イェ)",
        "content": "<b>【ll と y の発音】</b><br><b>ll</b> や <b>y</b> は地域によって「ヤ・ユ・ヨ」または「ジャ・ジュ・ジョ」に近い音で発音されます。<br>・<i>llamar</i>（ヤマール/ジャマール）: 呼ぶ<br>・<i>yo</i>（ヨ/ジョ）: わたし",
        "title": "ll と y の発音",
        "sentence": "「私」を意味する \"yo\" の発音として適切なものはどれでしょう？ [___]",
        "options": "ヨ（またはジョ）, ヴォ, ロ, ゾ",
        "correct_answer": "ヨ（またはジョ）",
        "hint": "y はヤ行またはジャ行に近い音になります。",
        "explanation": "yo は地域により「ヨ」または「ジョ」と発音されます。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第5課: 「ñ」の発音 (ニャ・ニュ・ニョ)",
        "content": "<b>【ñ (エニェ) の発音】</b><br><b>ñ</b> は日本語の「ニャ・二・ニュ・ニェ・ニョ」の音です。<br>・<i>España</i>（エスパーニャ）: スペイン<br>・<i>niño</i>（ニーニョ）: 男の子",
        "title": "ñ の発音",
        "sentence": "「スペイン」を意味する \"España\" の正しい読み方はどれでしょう？ [___]",
        "options": "エスパーニャ, エスパナ, エスパーナ, エスパニア",
        "correct_answer": "エスパーニャ",
        "hint": "ñ は「ニャ行」の音になります。",
        "explanation": "ñ はエニェと呼ばれ、Español（エスパニョール）、España（エスパーニャ）のようにニャ行で発音します。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第6課: 「j」と「g(+e,i)」の喉鳴らしハ行音",
        "content": "<b>【j と g の発音】</b><br><b>j</b> 全般および <b>g</b> に e, i が続く場合、喉の奥を鳴らす強い「ハ行」音になります。<br>・<i>Japón</i>（ハポン）: 日本<br>・<i>gente</i>（ヘンテ）: 人々",
        "title": "j と g の発音",
        "sentence": "「日本」を意味する \"Japón\" の読み方はどれでしょう？ [___]",
        "options": "ハポン, ジャポン, ヤポン, ガポン",
        "correct_answer": "ハポン",
        "hint": "j は強いハ行音です。",
        "explanation": "スペイン語の j は強いハ行音のため、Japón は「ハポン」と発音します。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第7課: 「c」と「z」の発音ルール",
        "content": "<b>【c と z の発音】</b><br><b>z</b> および <b>c (+ e, i)</b> は英語の th のような音（またはサ行）になります。<br>・<i>zapato</i>（サパト）: 靴<br>・<i>cero</i>（セロ）: ゼロ<br>※<i>c (+ a, o, u)</i> はカ行音（<i>casa</i> カサ）。",
        "title": "c と z の発音",
        "sentence": "「家」を意味する \"casa\" の読み方はどれでしょう？ [___]",
        "options": "カサ, ササ, チャサ, ガサ",
        "correct_answer": "カサ",
        "hint": "c の後に a が続く場合は「カ行」になります。",
        "explanation": "c + a/o/u はカ行（カ・コ・ク）、c + e/i はサ行（セ・シ）になります。"
    },
    {
        "category": "0. 発音・文字と基本ルール",
        "lesson_title": "第8課: アクセント（強勢）の 3大ルール",
        "content": "<b>【アクセントの規則】</b><br>1. 母音または n, s で終わる単語 ➔ <b>後ろから2番目の母音</b>を強く読む。<br>2. それ以外の子音で終わる単語 ➔ <b>最後の母音</b>を強く読む。<br>3. アクセント記号 (á, é, í, ó, ú) がある単語 ➔ <b>記号の位置</b>を強く読む。",
        "title": "アクセントルール",
        "sentence": "アクセント記号がついている単語 (例: teléfono) はどこを強く読みますか？ [___]",
        "options": "アクセント記号のある音節, 常に最後の音節, 常に最初の音節, どこでもよい",
        "correct_answer": "アクセント記号のある音節",
        "hint": "アクセント記号がある場合はルール例外としてその位置を強く読みます。",
        "explanation": "アクセント記号(á, é, í, ó, ú)が付いている箇所を最優先で強く発音します。"
    },

    # --- 1. 名詞・冠詞・形容詞の基礎 (第9課〜第16課) ---
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第9課: 母音の発音 (a, e, i, o, u)",
        "content": "<b>【母音の発音】</b><br>スペイン語の母音は <b>a, e, i, o, u</b> の5つで、日本語の「ア・エ・イ・オ・ウ」とほぼ同じ明確な発音です。",
        "title": "母音の発音",
        "sentence": "スペイン語の基本母音は何種類ありますか？ [___]",
        "options": "5種類, 7種類, 12種類, 26種類",
        "correct_answer": "5種類",
        "hint": "日本語のアイウエオと同じ5つです。",
        "explanation": "スペイン語の母音は a, e, i, o, u の5つで、日本語と同じように発音するため日本人にとって非常に聞き取りやすいです。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第10課: 名詞の性と語尾 (-o と -a)",
        "content": "<b>【名詞の性】</b><br>スペイン語の名詞はすべて男性名詞か女性名詞に分かれます。<br>・<b>-o</b> で終わる名詞の多くは<b>男性名詞</b> (例: <i>libro</i> 本)<br>・<b>-a</b> で終わる名詞の多くは<b>女性名詞</b> (例: <i>casa</i> 家)",
        "title": "名詞の性別",
        "sentence": "語尾が -o で終わる \"libro\"（本）の性別はどちらでしょう？ [___]",
        "options": "男性名詞, 女性名詞, 中性名詞, 両性名詞",
        "correct_answer": "男性名詞",
        "hint": "-o で終わる名詞は基本的に男性名詞です。",
        "explanation": "-o で終わる名詞の多くは男性名詞、-a で終わる名詞の多くは女性名詞です。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第11課: 定冠詞単数形 (el, la)",
        "content": "<b>【定冠詞 (単数)】</b><br>特定のものを示す「その〜」に当たる定冠詞です。<br>・男性単数 ➔ <b>el</b> (例: <i>el libro</i>)<br>・女性単数 ➔ <b>la</b> (例: <i>la casa</i>)",
        "title": "定冠詞 (単数)",
        "sentence": "女性名詞 \"casa\"（家）につく定冠詞（単数）はどれでしょう？ [___]",
        "options": "la, el, los, las",
        "correct_answer": "la",
        "hint": "女性単数名詞には la を使います。",
        "explanation": "男性単数は el、女性単数は la です。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第12課: 定冠詞複数形 (los, las) と名詞の複数形",
        "content": "<b>【定冠詞 (複数) と複数形】</b><br>・母音終わり ➔ <b>-s</b> をつける<br>・子音終わり ➔ <b>-es</b> をつける<br>・男性複数定冠詞 ➔ <b>los</b> (<i>los libros</i>)<br>・女性複数定冠詞 ➔ <b>las</b> (<i>las casas</i>)",
        "title": "定冠詞 (複数)",
        "sentence": "男性複数名詞 \"libros\" につく定冠詞はどれでしょう？ [___]",
        "options": "los, el, las, la",
        "correct_answer": "los",
        "hint": "男性複数の定冠詞は los です。",
        "explanation": "男性複数は los、女性複数は las をつけます。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第13課: 不定冠詞 (un, una, unos, unas)",
        "content": "<b>【不定冠詞 (〜のひとつの)】</b><br>・男性単数 ➔ <b>un</b> (<i>un libro</i>)<br>・女性単数 ➔ <b>una</b> (<i>una casa</i>)<br>・男性複数 ➔ <b>unos</b> (いくつかの / 約)<br>・女性複数 ➔ <b>unas</b> (いくつかの / 約)",
        "title": "不定冠詞",
        "sentence": "「一軒の家」を表す \"[___] casa\" に入る不定冠詞はどれでしょう？",
        "options": "una, un, unos, unas",
        "correct_answer": "una",
        "hint": "casa は女性単数名詞です。",
        "explanation": "女性単数名詞 casa の前の不定冠詞は una になります。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第14課: 形容詞の性数一致ルール",
        "content": "<b>【形容詞の位置と性数一致】</b><br>形容詞は原則として<b>名詞の後ろ</b>に置き、名詞の性・数に合わせて語尾変化させます。<br>・<i>el libro rojo</i> (赤い本・男単)<br>・<i>la casa roja</i> (赤い家・女単)<br>・<i>los libros rojos</i> (赤い本・男複)",
        "title": "形容詞の一致",
        "sentence": "「赤い家（単数）」を表す正しい組み合わせはどれでしょう？ [___]",
        "options": "la casa roja, el casa rojo, la casa rojo, las casas rojas",
        "correct_answer": "la casa roja",
        "hint": "casa は女性単数なので形容詞も roja になります。",
        "explanation": "名詞 casa (女性単数) に合わせて形容詞も roja に性数一致させます。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第15課: 主格人称代名詞 (yo, tú, él, ella, nosotros...)",
        "content": "<b>【人称代名詞】</b><br>・<b>yo</b>（私）<br>・<b>tú</b>（君）<br>・<b>él / ella / usted</b>（彼 / 彼女 / あなた）<br>・<b>nosotros/as</b>（私たち）<br>・<b>vosotros/as</b>（君たち）<br>・<b>ellos / ellas / ustedes</b>（彼ら / 彼女ら / あなたがた）",
        "title": "人称代名詞",
        "sentence": "「私」を意味するスペイン語の人称代名詞はどれでしょう？ [___]",
        "options": "yo, tú, él, nosotros",
        "correct_answer": "yo",
        "hint": "1人称単数は yo です。",
        "explanation": "1人称単数（私）は yo です。"
    },
    {
        "category": "1. 名詞・冠詞・形容詞の基礎",
        "lesson_title": "第16課: 主語の省略ルール",
        "content": "<b>【主語の省略】</b><br>スペイン語では動詞の活用形で主語が特定できるため、強調や明確化が必要な場合を除き<b>主語代名詞を省略するのが普通</b>です。<br>例: <i>(Yo) Hablo español.</i> ➔ <b>Hablo español.</b>",
        "title": "主語の省略",
        "sentence": "スペイン語で「私はスペイン語を話します」と言う時、通常どう言いますか？ [___]",
        "options": "Hablo español. (主語yoを省略するのが普通), 必ず Yo hablo español. と言わなければならない, Hablo yo español., Yo español hablo.",
        "correct_answer": "Hablo español. (主語yoを省略するのが普通)",
        "hint": "動詞の語尾で主語がわかるため、主語は省略するのが自然です。",
        "explanation": "活用形で主語が判明するため、通常は主語代名詞を省略します。"
    },

    # --- 2. 主語代名詞と 2大be動詞 (ser / estar) (第17課〜第24課) ---
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第17課: ser動詞の概念 (本質・属性)",
        "content": "<b>【ser動詞の用途】</b><br>永久的・本質的な性質（国籍・職業・性格・アイデンティティ等）を表します。<br>・<i>Yo soy japonés.</i> (私は日本人です)<br>・<i>Ella es profesora.</i> (彼女は教師です)",
        "title": "ser動詞",
        "sentence": "「私は日本人です」と言う時の動詞 ser の活用形はどれでしょう？ Yo [___] japonés.",
        "options": "soy, eres, es, somos",
        "correct_answer": "soy",
        "hint": "Yo (私) に対する ser の活用形です。",
        "explanation": "Yo に対する ser の活用は soy です。(Yo soy japonés.)"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第18課: ser動詞の現在形活用パターン",
        "content": "<b>【ser の活用】</b><br>・yo ➔ <b>soy</b><br>・tú ➔ <b>eres</b><br>・él/ella/ud. ➔ <b>es</b><br>・nosotros ➔ <b>somos</b><br>・vosotros ➔ <b>sois</b><br>・ellos/ellas/uds. ➔ <b>son</b>",
        "title": "ser の活用一覧",
        "sentence": "「君は学生です」の空欄に入る語は？ Tú [___] estudiante.",
        "options": "eres, soy, es, son",
        "correct_answer": "eres",
        "hint": "tú に対する ser の活用です。",
        "explanation": "Tú に対する ser の活用は eres です。"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第19課: estar動詞の概念 (状態・所在)",
        "content": "<b>【estar動詞の用途】</b><br>一時的な状態・体調、および人や物の「場所・位置（所在）」を表します。<br>・<i>Estoy cansado.</i> (私は疲れている [一時的な状態])<br>・<i>El libro está en la mesa.</i> (本はテーブルの上にある [所在])",
        "title": "estar動詞の概念",
        "sentence": "一時的な体調や物の所在を表す動詞はどちらでしょう？ [___]",
        "options": "estar, ser, tener, haber",
        "correct_answer": "estar",
        "hint": "一時的な状態・位置には estar を用います。",
        "explanation": "一時的な状態や場所の所在には estar を使用します。"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第20課: estar動詞の現在形活用パターン",
        "content": "<b>【estar の活用】</b><br>・yo ➔ <b>estoy</b><br>・tú ➔ <b>estás</b><br>・él/ella/ud. ➔ <b>está</b><br>・nosotros ➔ <b>estamos</b><br>・vosotros ➔ <b>estáis</b><br>・ellos/ellas/uds. ➔ <b>están</b>",
        "title": "estar の活用一覧",
        "sentence": "「お元気ですか？ (君)」と尋ねる文に入る語は？ ¿Cómo [___]? ",
        "options": "estás, estoy, está, están",
        "correct_answer": "estás",
        "hint": "Tú に対する estar の活用形です。",
        "explanation": "Tú に対する estar は estás です。(¿Cómo estás?)"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第21課: ser と estar の使い分け徹底比較",
        "content": "<b>【ser vs estar 比較】</b><br>・<i>Es listo.</i> (彼は頭が良い [本質])<br>・<i>Está listo.</i> (彼は準備ができている [状態])<br>・<i>Es rico.</i> (彼はお金持ちだ)<br>・<i>Está rico.</i> (料理が美味しい)",
        "title": "ser と estar の比較",
        "sentence": "料理を食べて「美味しい！」と言う時の適切な表現はどちらでしょう？ [___]",
        "options": "¡Está rico!, ¡Es rico!, ¡Soy rico!, ¡Están rico!",
        "correct_answer": "¡Está rico!",
        "hint": "食べ物の今の一時的な状態・美味しさには estar を使います。",
        "explanation": "一時的な味覚の状態を表すため estar を使い ¡Está rico! と言います。"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第22課: 場所の表現 en と estar",
        "content": "<b>【所在の表現】</b><br>「〜は[場所]にいる/ある」は <b>[主語] + estar + en + [場所]</b> で表します。<br>・<i>Estoy en Tokio.</i> (私は東京にいます)<br>・<i>Mis amigos están en Madrid.</i> (私の友人たちはマドリードにいます)",
        "title": "場所の表現",
        "sentence": "「私は家にいます」の正しいスペイン語は？ [___]",
        "options": "Estoy en casa., Soy en casa., Tengo en casa., Hago en casa.",
        "correct_answer": "Estoy en casa.",
        "hint": "所在を示すには estar を使います。",
        "explanation": "所在を表すので estar を使い Estoy en casa. となります。"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第23課: hay (存在を表す haber 動詞)",
        "content": "<b>【hay の使い方】</b><br>特定されていない人や物の「存在（〜がある/いる）」を表す不変形です。単数・複数に関わらず常に <b>hay</b> を使います。<br>・<i>Hay un libro.</i> (本が1冊あります)<br>・<i>Hay muchas personas.</i> (たくさんの人がいます)",
        "title": "hay の使い方",
        "sentence": "「公園にたくさんの子供たちがいます」の文頭に入る語は？ [___] muchos niños en el parque.",
        "options": "Hay, Está, Están, Son",
        "correct_answer": "Hay",
        "hint": "不特定の人や物の存在には単複共通の Hay を用きます。",
        "explanation": "不特定多数の存在を表す場合は Hay を使います。"
    },
    {
        "category": "2. 主語代名詞と 2大be動詞 (ser / estar)",
        "lesson_title": "第24課: estar + 現在分詞 (進行形)",
        "content": "<b>【現在進行形】</b><br><b>estar + 現在分詞 (-ando / -iendo)</b> で「今〜している最中だ」を表します。<br>・<i>hablar</i> ➔ <i>hablando</i><br>・<i>comer</i> ➔ <i>comiendo</i><br>・<i>Estoy estudiando.</i> (私は勉強しています)",
        "title": "現在進行形",
        "sentence": "「私は今勉強しています」の空欄に入る分詞は？ Estoy [___] (estudiar).",
        "options": "estudiando, estudiado, estudiar, estudias",
        "correct_answer": "estudiando",
        "hint": "-ar 動詞の現在分詞語尾は -ando です。",
        "explanation": "estudiar の現在分詞は estudiando です。"
    },

    # --- 3. 現在形：規則動詞 (-ar, -er, -ir) (第25課〜第32課) ---
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第25課: -ar 動詞の現在形活用ルール",
        "content": "<b>【-ar 動詞の活用】</b><br>例: <i>hablar</i>（話す）<br>・yo ➔ <b>hablo</b><br>・tú ➔ <b>hablas</b><br>・él/ella ➔ <b>habla</b><br>・nosotros ➔ <b>hablamos</b><br>・vosotros ➔ <b>habláis</b><br>・ellos ➔ <b>hablan</b>",
        "title": "-ar 動詞の活用",
        "sentence": "-ar 動詞 hablar の yo (私) に対する現在形活用は？ Yo [___].",
        "options": "hablo, hablas, habla, hablamos",
        "correct_answer": "hablo",
        "hint": "yo の活用語尾は -o です。",
        "explanation": "yo hablar ➔ hablo となります。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第26課: -er 動詞の現在形活用ルール",
        "content": "<b>【-er 動詞の活用】</b><br>例: <i>comer</i>（食べる）<br>・yo ➔ <b>como</b><br>・tú ➔ <b>comes</b><br>・él/ella ➔ <b>come</b><br>・nosotros ➔ <b>comemos</b><br>・vosotros ➔ <b>coméis</b><br>・ellos ➔ <b>comen</b>",
        "title": "-er 動詞の活用",
        "sentence": "-er 動詞 comer の tú (君) に対する現在形活用は？ Tú [___].",
        "options": "comes, como, come, comemos",
        "correct_answer": "comes",
        "hint": "tú の -er 動詞語尾は -es です。",
        "explanation": "tú comer ➔ comes です。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第27課: -ir 動詞の現在形活用ルール",
        "content": "<b>【-ir 動詞の活用】</b><br>例: <i>vivir</i>（住む/生きる）<br>・yo ➔ <b>vivo</b><br>・tú ➔ <b>vives</b><br>・él/ella ➔ <b>vive</b><br>・nosotros ➔ <b>vivimos</b><br>・vosotros ➔ <b>vivís</b><br>・ellos ➔ <b>viven</b>",
        "title": "-ir 動詞の活用",
        "sentence": "「私たちは東京に住んでいます」の空欄に入る活用形は？ Nosotros [___] en Tokio.",
        "options": "vivimos, vivo, vives, viven",
        "correct_answer": "vivimos",
        "hint": "nosotros の -ir 動詞語尾は -imos です。",
        "explanation": "nosotros vivir ➔ vivimos です。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第28課: よく使う -ar 規則動詞 (trabajar, estudiar, comprar)",
        "content": "<b>【日常の -ar 動詞】</b><br>・<i>trabajar</i>（働く）<br>・<i>estudiar</i>（勉強する）<br>・<i>comprar</i>（買う）<br>・<i>escuchar</i>（聴く）<br>例: <i>Estudio español todos los días.</i> (毎日スペイン語を勉強します)",
        "title": "日常の -ar 動詞",
        "sentence": "「彼女は病院で働いています」の空欄に入る語は？ Ella [___] en el hospital.",
        "options": "trabaja, trabajo, trabajas, trabajan",
        "correct_answer": "trabaja",
        "hint": "Ella (3人称単数) に対する trabajar の活用です。",
        "explanation": "Ella trabajar ➔ trabaja となります。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第29課: よく使う -er 規則動詞 (aprender, beber, leer)",
        "content": "<b>【日常の -er 動詞】</b><br>・<i>aprender</i>（学ぶ）<br>・<i>beber</i>（飲む）<br>・<i>leer</i>（読む [tú lees, él lee]）<br>例: <i>Bebo agua.</i> (私は水を飲みます)",
        "title": "日常の -er 動詞",
        "sentence": "「彼らはワインを飲みます」の空欄に入る語は？ Ellos [___] vino.",
        "options": "beben, bebo, bebes, bebemos",
        "correct_answer": "beben",
        "hint": "Ellos (3人称複数) に対する beber の活用形です。",
        "explanation": "Ellos beber ➔ beben です。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第30課: よく使う -ir 規則動詞 (escribir, abrir)",
        "content": "<b>【日常の -ir 動詞】</b><br>・<i>escribir</i>（書く）<br>・<i>abrir</i>（開ける）<br>例: <i>Escribo una carta.</i> (手紙を書きます)",
        "title": "日常の -ir 動詞",
        "sentence": "「私は手紙を書きます」の空欄に入る語は？ Yo [___] una carta.",
        "options": "escribo, escribes, escribe, escribimos",
        "correct_answer": "escribo",
        "hint": "Yo に対する escribir の活用形です。",
        "explanation": "Yo escribir ➔ escribo となります。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第31課: 動詞の原形 (不定詞) を従える表現",
        "content": "<b>【助動詞的表現 + 不定詞】</b><br>・<b>querer + 原形</b> (〜したい)<br>・<b>poder + 原形</b> (〜できる)<br>・<b>necesitar + 原形</b> (〜する必要がある)<br>例: <i>Quiero hablar español.</i> (スペイン語を話したい)",
        "title": "不定詞を従える表現",
        "sentence": "「私はスペイン語を話したい」の空欄に入る語は？ Quiero [___] español.",
        "options": "hablar, hablo, hablas, habla",
        "correct_answer": "hablar",
        "hint": "querer の後ろには動詞の原形（不定詞）が来ます。",
        "explanation": "Quiero の直後には動詞の原形 hablar を置きます。"
    },
    {
        "category": "3. 現在形：規則動詞 (-ar, -er, -ir)",
        "lesson_title": "第32課: 習慣を表す現在形の副詞 (siempre, a veces, nunca)",
        "content": "<b>【頻度を表す副詞】</b><br>・<b>siempre</b>（いつも）<br>・<b>a veces</b>（時々）<br>・<b>nunca</b>（決して〜ない）<br>例: <i>Siempre estudio por la mañana.</i> (私はいつも朝勉強します)",
        "title": "頻度の副詞",
        "sentence": "「いつも」を意味するスペイン語の副詞はどれでしょう？ [___]",
        "options": "siempre, a veces, nunca, mañana",
        "correct_answer": "siempre",
        "hint": "英語の always に相当します。",
        "explanation": "「いつも」は siempre です。"
    },

    # --- 4. 現在形：重要不規則動詞 (第33課〜第42課) ---
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第33課: tener動詞 (持つ・年齢・空腹)",
        "content": "<b>【tener の用途と活用】</b><br>「持っている」「年齢」「生理的状態」を表します。<br>・yo <b>tengo</b> / tú <b>tienes</b> / él <b>tiene</b> / nosotros <b>tenemos</b> / ellos <b>tienen</b><br>・<i>Tengo 20 años.</i> (20歳です)<br>・<i>Tengo hambre.</i> (お腹が空いています)",
        "title": "tener動詞",
        "sentence": "「私は20歳です」を表す正しい文は？ [___]",
        "options": "Tengo 20 años., Soy 20 años., Estoy 20 años., Hago 20 años.",
        "correct_answer": "Tengo 20 años.",
        "hint": "年齢を表す時は tener を用います。",
        "explanation": "スペイン語で年齢を言う時は tener + [数字] + años を使います。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第34課: ir動詞 (行く) と ir a + 原形 (近接未来)",
        "content": "<b>【ir の活用と近接未来】</b><br>・yo <b>voy</b> / tú <b>vas</b> / él <b>va</b> / nosotros <b>vamos</b> / ellos <b>van</b><br>・<b>ir a + 原形</b> ➔ 「〜する予定だ / 〜しに行く」<br>・<i>Voy a estudiar.</i> (勉強するつもりです)",
        "title": "ir動詞と近接未来",
        "sentence": "「私は行くつもりです」を表す文に入る語は？ [___] a ir.",
        "options": "Voy, Vas, Va, Vamos",
        "correct_answer": "Voy",
        "hint": "Yo に対する ir の活用です。",
        "explanation": "Yo の ir 活用は voy です。Voy a + 原形 で近接未来を表します。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第35課: hacer動詞 (する・作る・天気)",
        "content": "<b>【hacer の活用と天気表現】</b><br>・yo <b>hago</b> / tú <b>haces</b> / él <b>hace</b>...<br>・<i>Hago los deberes.</i> (宿題をします)<br>・<i>Hace buen tiempo.</i> (良い天気です [3人称単数使用])",
        "title": "hacer動詞",
        "sentence": "「私は宿題をします」の空欄に入る語は？ Yo [___] los deberes.",
        "options": "hago, haces, hace, hacemos",
        "correct_answer": "hago",
        "hint": "Yo に対する hacer の 1人称単数不規則活用です。",
        "explanation": "Yo に対する hacer は hago になります。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第36課: poder動詞 (〜できる / o➔ue 語幹変化)",
        "content": "<b>【語幹変化動詞 o ➔ ue】</b><br><i>poder</i> (〜できる)<br>・yo <b>puedo</b> / tú <b>puedes</b> / él <b>puede</b> / nosotros <b>podemos</b> / ellos <b>pueden</b><br>・<i>¿Puedo entrar?</i> (入ってもいいですか？)",
        "title": "poder動詞",
        "sentence": "「私にできます」を表す poder の活用形は？ Yo [___].",
        "options": "puedo, puedes, puede, podemos",
        "correct_answer": "puedo",
        "hint": "o が ue に変化して yo 語尾 -o が付きます。",
        "explanation": "poder の yo 形は puedo です。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第37課: querer動詞 (〜したい / e➔ie 語幹変化)",
        "content": "<b>【語幹変化動詞 e ➔ ie】</b><br><i>querer</i> (〜したい/愛する)<br>・yo <b>quiero</b> / tú <b>quieres</b> / él <b>quiere</b> / nosotros <b>queremos</b> / ellos <b>quieren</b><br>・<i>Te quiero.</i> (君を愛している)",
        "title": "querer動詞",
        "sentence": "「コーヒーが欲しい/飲みたい」を表す文の空欄は？ [___] un café.",
        "options": "Quiero, Quieres, Quiere, Queremos",
        "correct_answer": "Quiero",
        "hint": "1人称単数「私」の querer 活用形です。",
        "explanation": "Yo に対する querer は quiero です。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第38課: saber と conocer (知っている の違い)",
        "content": "<b>【2つの 知っている】</b><br>・<b>saber</b> (知識・事実・やり方を知っている / yo <i>sé</i>)<br>・<b>conocer</b> (人・場所を体験として知っている・面識がある / yo <i>conozco</i>)<br>例: <i>Sé hablar español.</i> / <i>Conozco a Juan.</i>",
        "title": "saber と conocer",
        "sentence": "「私はフアンを知っている(面識がある)」と言う時の動詞は？ Yo [___] a Juan.",
        "options": "conozco, sé, sabe, conoce",
        "correct_answer": "conozco",
        "hint": "人を知っている（面識がある）場合は conocer を使います。",
        "explanation": "人物との知り合い・面識を表す場合は conocer (yo conozco) を使います。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第39課: venir動詞 (来る) と salir動詞 (出る)",
        "content": "<b>【yo形不規則 (go動詞)】</b><br>・<i>venir</i> (来る): yo <b>vengo</b> / tú vienes<br>・<i>salir</i> (出る/外出する): yo <b>salgo</b> / tú sales<br>例: <i>Vengo de Japón.</i> (日本から来ました)",
        "title": "venir と salir",
        "sentence": "「私は日本出身です/日本から来ました」の空欄に入る語は？ [___] de Japón.",
        "options": "Vengo, Vienes, Viene, Venimos",
        "correct_answer": "Vengo",
        "hint": "venir の yo 活用形は vengo です。",
        "explanation": "Yo の venir 活用は vengo です。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第40課: dar動詞 (与える) と ver動詞 (見る)",
        "content": "<b>【dar と ver】</b><br>・<i>dar</i> (与える): yo <b>doy</b>, tú das, él da...<br>・<i>ver</i> (見る): yo <b>veo</b>, tú ves, él ve...<br>例: <i>Veo la televisión.</i> (テレビを見ます)",
        "title": "dar と ver",
        "sentence": "「テレビを見る」の yo に対する文は？ [___] la televisión.",
        "options": "Veo, Ves, Ve, Vemos",
        "correct_answer": "Veo",
        "hint": "ver の yo 活用形は veo です。",
        "explanation": "Yo の ver 活用は veo です。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第41課: poner動詞 (置く) と traer動詞 (持ってくる)",
        "content": "<b>【poner と traer】</b><br>・<i>poner</i>: yo <b>pongo</b><br>・<i>traer</i>: yo <b>traigo</b><br>例: <i>Pongo el libro en la mesa.</i> (テーブルに本を置きます)",
        "title": "poner と traer",
        "sentence": "poner (置く) の yo 活用形はどれでしょう？ Yo [___].",
        "options": "pongo, pones, pone, ponemos",
        "correct_answer": "pongo",
        "hint": "yo 形が -go となる不規則動詞です。",
        "explanation": "poner の yo 形は pongo です。"
    },
    {
        "category": "4. 現在形：重要不規則動詞",
        "lesson_title": "第42課: decir動詞 (言う) と pedir動詞 (頼む/e➔i 変化)",
        "content": "<b>【e ➔ i 語幹変化動詞】</b><br>・<i>decir</i> (言う): yo <b>digo</b>, tú dices, él dice...<br>・<i>pedir</i> (頼む/注文する): yo <b>pido</b>, tú pides...<br>例: <i>Digo la verdad.</i> (本当のことを言います)",
        "title": "decir と pedir",
        "sentence": "「私は本当のことを言います」の空欄に入る語は？ Yo [___] la verdad.",
        "options": "digo, dices, dice, decimos",
        "correct_answer": "digo",
        "hint": "decir の yo 活用形は digo です。",
        "explanation": "decir の 1人称単数形は digo です。"
    },

    # --- 5. 指示詞・所有表現・数詞 (第43課〜第50課) ---
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第43課: 指示形容詞 (este, ese, aquel)",
        "content": "<b>【指示形容詞 (この・その・あの)】</b><br>・<b>este / esta</b>（この）➔ 手元<br>・<b>ese / esa</b>（その）➔ 相手の近く<br>・<b>aquel / aquella</b>（あの）➔ 遠く<br>例: <i>este libro</i> (この本), <i>esa casa</i> (その家)",
        "title": "指示形容詞",
        "sentence": "「この本（男性単数）」を表す表現はどれでしょう？ [___] libro.",
        "options": "este, ese, aquel, esta",
        "correct_answer": "este",
        "hint": "手元にある男性単数名詞を指す指示形容詞は este です。",
        "explanation": "男性単数の「この」は este です。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第44課: 指示代名詞 (esto, eso, aquello - 中性)",
        "content": "<b>【中性指示代名詞】</b><br>名前がわからない物体や概念「これ・それ・あれ」を指す時は中性形を使います。<br>・<b>esto</b>（これ）<br>・<b>eso</b>（それ）<br>・<b>aquello</b>（あれ）<br>例: <i>¿Qué es esto?</i> (これ何？)",
        "title": "中性指示代名詞",
        "sentence": "「これ何？」と尋ねる定番フレーズは？ ¿Qué es [___]?",
        "options": "esto, este, esta, estos",
        "correct_answer": "esto",
        "hint": "未知の物「これ」を指す中性代名詞は esto です。",
        "explanation": "「これ」と抽象的に指す中性代名詞は esto を用います。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第45課: 所有形容詞前置形 (mi, tu, su, nuestro...)",
        "content": "<b>【所有形容詞 (〜の)】</b><br>・<b>mi / mis</b> (私の)<br>・<b>tu / tus</b> (君の)<br>・<b>su / sus</b> (彼・彼女・あなたの/彼らの)<br>・<b>nuestro/a/os/as</b> (私たちの)<br>例: <i>mi amigo</i>, <i>mis amigos</i>",
        "title": "所有形容詞",
        "sentence": "「私の友人たち（複数）」を表す表現は？ [___] amigos.",
        "options": "mis, mi, tu, su",
        "correct_answer": "mis",
        "hint": "修飾する名詞 amigos が複数なので所有形も複数になります。",
        "explanation": "名詞が複数なので mi も複数形の mis になります。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第46課: 所有代名詞 (mío, tuyo, suyo...)",
        "content": "<b>【所有代名詞 (〜のもの)】</b><br>・<i>el mío / la mía</i> (私のもの)<br>・<i>el tuyo / la tuya</i> (君のもの)<br>・<i>el suyo / la suya</i> (彼・彼女のもの)<br>例: <i>Este libro es mío.</i> (この本は私のものです)",
        "title": "所有代名詞",
        "sentence": "「この本は私のものです」の空欄に入る語は？ Este libro es [___].",
        "options": "mío, mi, mis, me",
        "correct_answer": "mío",
        "hint": "「私のもの」を表す補語は mío です。",
        "explanation": "補語として「私のもの」と言う場合は mío を用います。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第47課: 基数 1〜10 のマスター",
        "content": "<b>【数字 1〜10】</b><br>1: <i>uno</i> (名詞の前で <i>un</i>)<br>2: <i>dos</i><br>3: <i>tres</i><br>4: <i>cuatro</i><br>5: <i>cinco</i><br>6: <i>seis</i><br>7: <i>siete</i><br>8: <i>ocho</i><br>9: <i>nueve</i><br>10: <i>diez</i>",
        "title": "数字 1〜10",
        "sentence": "数字の「5」を表すスペイン語はどれでしょう？ [___]",
        "options": "cinco, cuatro, seis, tres",
        "correct_answer": "cinco",
        "hint": "1:uno, 2:dos, 3:tres, 4:cuatro, 5:cinco",
        "explanation": "数字の 5 は cinco です。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第48課: 基数 11〜30 と規則性",
        "content": "<b>【数字 11〜30】</b><br>11: <i>once</i>, 12: <i>doce</i>, 13: <i>trece</i>, 14: <i>catorce</i>, 15: <i>quince</i><br>16: <i>dieciséis</i>, 20: <i>veinte</i>, 21: <i>veintiuno</i>, 30: <i>treinta</i>",
        "title": "数字 11〜30",
        "sentence": "数字の「15」を表すスペイン語はどれでしょう？ [___]",
        "options": "quince, catorce, trece, diez y cinco",
        "correct_answer": "quince",
        "hint": "15 は quince と言います。",
        "explanation": "数字の 15 は quince です。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第49課: 基数 40〜1000 と金額表現",
        "content": "<b>【大きな数字】</b><br>40: <i>cuarenta</i>, 50: <i>cincuenta</i>, 100: <i>cien / ciento</i>, 1000: <i>mil</i><br>例: <i>cien euros</i> (100ユーロ), <i>dos mil yenes</i> (2000円)",
        "title": "大きな数字",
        "sentence": "数字の「1000」を表すスペイン語はどれでしょう？ [___]",
        "options": "mil, cien, ciento, un millón",
        "correct_answer": "mil",
        "hint": "1000 は mil です。",
        "explanation": "1000 は mil です。"
    },
    {
        "category": "5. 指示詞・所有表現・数詞",
        "lesson_title": "第50課: 序数 (1st〜5th: primero, segundo...)",
        "content": "<b>【序数 (〜番目)】</b><br>・1番目: <b>primero</b> (男単の前で <i>primer</i>)<br>・2番目: <b>segundo</b><br>・3番目: <b>tercero</b> (男単の前で <i>tercer</i>)<br>・4番目: <b>cuarto</b><br>・5番目: <b>quinto</b><br>例: <i>el primer piso</i> (1階/2階)",
        "title": "序数",
        "sentence": "「最初の(1番目の)」を表す男性単数名詞直前の形は？ el [___] día",
        "options": "primer, primero, primera, unos",
        "correct_answer": "primer",
        "hint": "primero は男性単数名詞の直前で primer に語尾短縮します。",
        "explanation": "primero は男性単数名詞の前で primer になります。"
    },

    # --- 6. 目的語代名詞 (直接・間接・再帰) (第51課〜第58課) ---
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第51課: 直接目的語代名詞 (me, te, lo, la, nos, los, las)",
        "content": "<b>【直接目的代名詞 (〜を)】</b><br>名詞の代わりに「〜を」と動詞の前に置きます。<br>・私を: <b>me</b> / 君を: <b>te</b><br>・彼/それを: <b>lo</b> / 彼女/それを: <b>la</b><br>・私たちを: <b>nos</b> / 彼ら/それらを: <b>los / las</b><br>例: <i>Lo veo.</i> (それを見ます)",
        "title": "直接目的語代名詞",
        "sentence": "「私はそれ(男性名詞libro)を見ます」の「それ」に入る代名詞は？ [___] veo.",
        "options": "Lo, La, Le, Me",
        "correct_answer": "Lo",
        "hint": "男性単数を指す「それを」は lo です。",
        "explanation": "男性単数直接目的語は lo です。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第52課: 間接目的語代名詞 (me, te, le, nos, les)",
        "content": "<b>【間接目的代名詞 (〜に)】</b><br>・私に: <b>me</b> / 君に: <b>te</b><br>・彼/彼女/あなたに: <b>le</b><br>・私達に: <b>nos</b> / 彼ら/あなたがたに: <b>les</b><br>例: <i>Juan me da un libro.</i> (フアンは私に本をくれる)",
        "title": "間接目的語代名詞",
        "sentence": "「彼(Juan)に電話します」の「彼に」に入る代名詞は？ [___] llamo a Juan.",
        "options": "Le, Lo, La, Me",
        "correct_answer": "Le",
        "hint": "3人称単数「彼に」は le です。",
        "explanation": "「彼に」という間接目的語は le です。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第53課: 二重目的語の語順と le➔se 変化",
        "content": "<b>【「人に」+「物を」の二重目的語】</b><br>語順: <b>[人に] + [物を] + 動詞</b><br>※3人称同士 (le lo など) が連続する場合、発音上の都合で <b>le/les は se に変化</b>します。<br>例: <i>Se lo doy.</i> (彼にそれをあげます)",
        "title": "二重目的語と se 変化",
        "sentence": "「私は彼にそれをあげます」の正しい文はどれでしょう？ [___]",
        "options": "Se lo doy., Le lo doy., Lo le doy., Doy se lo.",
        "correct_answer": "Se lo doy.",
        "hint": "le lo の連続は se lo に変化します。",
        "explanation": "le + lo ➔ se lo と変化するため Se lo doy. が正解です。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第54課: 再帰動詞の基礎 (llamarse, levantarse)",
        "content": "<b>【再帰動詞】</b><br>主語と目的語が同じ動作（自分自身に〜する）を表す動詞です。<br>再帰代名詞: <b>me, te, se, nos, os, se</b><br>・<i>Me llamo Taro.</i> (私はタロウと申します)<br>・<i>Me levanto a las 7.</i> (7時に起きます)",
        "title": "再帰動詞の基礎",
        "sentence": "「私の名前は〜です」と言う時のフレーズは？ [___] llamo...",
        "options": "Me, Te, Se, Nos",
        "correct_answer": "Me",
        "hint": "1人称単数 yo に対する再帰代名詞は me です。",
        "explanation": "Yo に対する再帰代名詞は me なので Me llamo... となります。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第55課: 日常の再帰動詞 (ducharse, acostarse, vestirse)",
        "content": "<b>【日課を表す再帰動詞】</b><br>・<i>ducharse</i> (シャワーを浴びる)<br>・<i>acostarse</i> (寝る / o➔ue)<br>・<i>vestirse</i> (服を着る / e➔i)<br>例: <i>Me ducho por la mañana.</i> (朝シャワーを浴びます)",
        "title": "日課の再帰動詞",
        "sentence": "「私は夜11時に寝ます」の空欄に入る活用形は？ Me [___] (acostarse) a las 11.",
        "options": "acuesto, acostamos, acuesta, acuestas",
        "correct_answer": "acuesto",
        "hint": "acostarse は o➔ue 変化し、yo 形は acuesto になります。",
        "explanation": "Yo に対する acostarse は me acuesto になります。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第56課: gustar型動詞 (Me gusta... の文型構造)",
        "content": "<b>【gustar 型動詞の構造】</b><br><b>(A人) + [間接代名詞 me/te/le...] + gusta/gustan + [主語]</b><br>・好きな物が単数/動詞原形 ➔ <b>gusta</b><br>・好きな物が複数 ➔ <b>gustan</b><br>例: <i>Me gusta el café.</i> / <i>Me gustan los perros.</i>",
        "title": "gustar型動詞",
        "sentence": "「私は犬たち(los perros)が好きです」の空欄に入る動詞は？ Me [___] los perros.",
        "options": "gustan, gusta, gusto, gustas",
        "correct_answer": "gustan",
        "hint": "主語 los perros が複数形なので動詞も 3人称複数形になります。",
        "explanation": "主語 los perros が複数なので gustan を用います。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第57課: その他の gustar 型動詞 (encantar, interesar, doler)",
        "content": "<b>【同型の感情・状態動詞】</b><br>・<b>encantar</b> (大〜好きだ)<br>・<b>interesar</b> (興味がある)<br>・<b>doler</b> (痛む / o➔ue)<br>例: <i>Me duele la cabeza.</i> (頭が痛いです)",
        "title": "その他の gustar 型動詞",
        "sentence": "「私は頭が痛い(la cabeza)」の空欄に入る動詞は？ Me [___] la cabeza.",
        "options": "duele, duelen, dolió, dolor",
        "correct_answer": "duele",
        "hint": "la cabeza は単数名詞なので duele になります。",
        "explanation": "単数主語 la cabeza に対して duele を使います。"
    },
    {
        "category": "6. 目的語代名詞 (直接・間接・再帰)",
        "lesson_title": "第58課: 目的語代名詞の位置 (動詞の前 vs 不定詞/現在分詞の後ろ結合)",
        "content": "<b>【代名詞を置く位置】</b><br>1. 活用動詞の前 ➔ <i>Me lo quieres dar.</i><br>2. 不定詞・現在分詞の後ろに直結 ➔ <i>Quieres dármelo.</i> / <i>Estoy diciéndotelo.</i>",
        "title": "代名詞の位置",
        "sentence": "「私はそれを買いたい」で代名詞を不定詞の後ろにつける正しい表記は？ Quiero comprar[___]. (lo)",
        "options": "comprarlo, lo comprar, comprar lo, comprarlos",
        "correct_answer": "comprarlo",
        "hint": "不定詞の末尾に直接結合させます。",
        "explanation": "不定詞 comprar の後ろに結合して comprarlo となります。"
    },

    # --- 7. 疑問文・否定文・比較表現 (第59課〜第66課) ---
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第59課: 疑問文の作り方と倒置・感嘆符 (¿? ¡!)",
        "content": "<b>【疑問文・感嘆文のルール】</b><br>スペイン語では文頭に倒置感嘆符・倒置疑問符 <b>¿ ? ¡ !</b> を置きます。<br>語順は [動詞] + [主語] に倒置されることが多いです。<br>例: <i>¿Hablas español?</i> (スペイン語話しますか？)",
        "title": "疑問文のルール",
        "sentence": "スペイン語の疑問文の文頭につける記号はどれでしょう？ [___]",
        "options": "¿, ?, ¡, !",
        "correct_answer": "¿",
        "hint": "逆さの疑問符を使います。",
        "explanation": "スペイン語の疑問文の文頭には ¿ を置きます。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第60課: 主要な疑問詞 (qué, quién, dónde, cuándo, cómo, por qué)",
        "content": "<b>【疑問詞一覧】</b><br>・<b>qué</b> (何)<br>・<b>quién</b> (誰)<br>・<b>dónde</b> (どこ)<br>・<b>cuándo</b> (いつ)<br>・<b>cómo</b> (どのように)<br>・<b>por qué</b> (なぜ)",
        "title": "主要な疑問詞",
        "sentence": "「お名前は何ですか？」と尋ねる \"¿[___] te llamas?\" に入る疑問詞は？",
        "options": "Cómo, Qué, Dónde, Cuándo",
        "correct_answer": "Cómo",
        "hint": "直訳「どのように呼ばれていますか」で Cómo を使います。",
        "explanation": "¿Cómo te llamas? でお名前は何ですかという意味になります。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第61課: 量や数を尋ねる cuánto / cuántos",
        "content": "<b>【cuánto の性数変化】</b><br>修飾する名詞の性・数に合わせて変化します。<br>・<i>¿Cuánto dinero?</i> (いくらのお金)<br>・<i>¿Cuántos años tienes?</i> (何歳ですか？)",
        "title": "cuánto の変化",
        "sentence": "「何歳ですか？」と尋ねる文の空欄に入る疑問詞は？ ¿[___] años tienes?",
        "options": "Cuántos, Cuántas, Cuánto, Cuánta",
        "correct_answer": "Cuántos",
        "hint": "años は男性複数名詞です。",
        "explanation": "男性複数名詞 años に合わせて Cuántos を使います。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第62課: 否定文の基本 (no + 動詞) と二重否定 (nada, nadie, nunca)",
        "content": "<b>【否定文と二重否定】</b><br>・<b>no + 動詞</b> (〜ない)<br>・<b>no + 動詞 + nada</b> (何も〜ない)<br>・<b>no + 動詞 + nadie</b> (誰も〜ない)<br>例: <i>No sé nada.</i> (私は何も知りません)",
        "title": "否定文と二重否定",
        "sentence": "「私は何も知りません」を表す正解は？ [___]",
        "options": "No sé nada., Sé nada., No sé algo., Yo no sé algo.",
        "correct_answer": "No sé nada.",
        "hint": "no + 動詞 + nada で「何も〜ない」になります。",
        "explanation": "スペイン語では二重否定構造 No sé nada. を用います。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第63課: 優劣比較級 (más... que / menos... que)",
        "content": "<b>【比較級 (〜より〜だ)】</b><br>・<b>más + 形容詞 + que</b> (〜より〜だ)<br>・<b>menos + 形容詞 + que</b> (〜より〜でない)<br>例: <i>Juan es más alto que Taro.</i> (フアンはタロウより背が高い)",
        "title": "優劣比較級",
        "sentence": "「フアンはタロウより背が高い」の空欄に入る語は？ Juan es [___] alto que Taro.",
        "options": "más, tan, menos, mucho",
        "correct_answer": "más",
        "hint": "「より〜だ」を表す比較記号は más です。",
        "explanation": "「〜より…だ」は más ... que を使います。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第64課: 同等比較級 (tan... como / tanto... como)",
        "content": "<b>【同等比較 (〜と同じくらい〜だ)】</b><br>・<b>tan + 形容詞 + como</b> (同じくらい〜だ)<br>・<b>tanto/a/os/as + 名詞 + como</b> (同じくらいの量の〜)<br>例: <i>María es tan alta como Ana.</i>",
        "title": "同等比較級",
        "sentence": "「マリアはアナと同じくらい背が高い」の空欄に入る語は？ María es [___] alta como Ana.",
        "options": "tan, más, menos, tanto",
        "correct_answer": "tan",
        "hint": "形容詞の同等比較には tan ... como を使います。",
        "explanation": "形容詞 alta の前の同等比較語は tan です。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第65課: 不規則比較級 (mejor, peor, mayor, menor)",
        "content": "<b>【不規則比較級】</b><br>・<i>bueno</i> ➔ <b>mejor</b> (より良い)<br>・<i>malo</i> ➔ <b>peor</b> (より悪い)<br>・<i>grande</i> (年齢) ➔ <b>mayor</b> (年上)<br>・<i>pequeño</i> (年齢) ➔ <b>menor</b> (年下)<br>例: <i>Este vino es mejor que aquel.</i>",
        "title": "不規則比較級",
        "sentence": "「このワインはあのワインより良い」の空欄に入る不規則比較級は？ Este vino es [___] que aquel.",
        "options": "mejor, más bueno, peor, mayor",
        "correct_answer": "mejor",
        "hint": "bueno の比較級は más bueno ではなく mejor です。",
        "explanation": "bueno の比較級形は mejor です。"
    },
    {
        "category": "7. 疑問文・否定文・比較表現",
        "lesson_title": "第66課: 最上級表現 (el más... de)",
        "content": "<b>【最上級 (〜の中で最も〜)】</b><br><b>定冠詞 + 名詞 + más + 形容詞 + de [範囲]</b><br>例: <i>Juan es el chico más alto de la clase.</i> (フアンはクラスで一番背が高い)",
        "title": "最上級表現",
        "sentence": "「世界で最も美しい街」を表す最上級は？ la ciudad [___] bonita del mundo.",
        "options": "más, tan, mejor, mucho",
        "correct_answer": "más",
        "hint": "「最も〜」を表すには定冠詞+名詞+más+形容詞 を使います。",
        "explanation": "最上級をつくる語は más です。"
    },

    # --- 8. 過去形①：点過去 (完了過去) (第67課〜第74課) ---
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第67課: 点過去の概念 (完了した1回限りの過去)",
        "content": "<b>【点過去の用途】</b><br>「〜した」という<b>完了した動作・過去の一時点の出来事</b>を表します。<br>時間語句: <i>ayer</i> (昨日), <i>anoche</i> (昨夜), <i>el año pasado</i> (去年)",
        "title": "点過去の概念",
        "sentence": "昨日完了した一回限りの行為を表すのに適した過去形はどちらでしょう？ [___]",
        "options": "点過去 (完了過去), 線過去 (不完了過去), 現在完了, 未来形",
        "correct_answer": "点過去 (完了過去)",
        "hint": "完了した動作・出来事には点過去を使います。",
        "explanation": "区切られた過去の一瞬の動作や完了した事実には点過去を使います。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第68課: -ar 動詞の点過去活用パターン",
        "content": "<b>【-ar 動詞の点過去】</b><br>例: <i>hablar</i><br>・yo <b>hablé</b><br>・tú <b>hablaste</b><br>・él/ella <b>habló</b><br>・nosotros <b>hablamos</b><br>・ellos <b>hablaron</b>",
        "title": "-ar 点過去活用",
        "sentence": "「私は昨日話しました」の空欄に入る点過去形は？ Ayer yo [___] (hablar).",
        "options": "hablé, habló, hablaste, hablaron",
        "correct_answer": "hablé",
        "hint": "-ar 動詞の yo 点過去語尾は -é です。",
        "explanation": "Yo に対する hablar の点過去形は hablé です。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第69課: -er / -ir 動詞の点過去活用パターン",
        "content": "<b>【-er / -ir 動詞の点過去】</b><br>例: <i>comer</i> / <i>vivir</i><br>・yo <b>comí</b> / <b>viví</b><br>・tú <b>comiste</b> / <b>viviste</b><br>・él/ella <b>comió</b> / <b>vivió</b><br>・nosotros <b>comimos</b> / <b>vivimos</b><br>・ellos <b>comieron</b> / <b>vivieron</b>",
        "title": "-er/-ir 点過去活用",
        "sentence": "「彼はピザを食べました」の空欄に入る点過去形は？ Él [___] (comer) pizza.",
        "options": "comió, comí, comiste, comieron",
        "correct_answer": "comió",
        "hint": "3人称単数 -er/-ir の点過去語尾は -ió です。",
        "explanation": "Él の comer 点過去形は comió です。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第70課: ser と ir の共通点過去活用 (fui, fuiste, fue...)",
        "content": "<b>【ser と ir の完全同型点過去】</b><br>ser (〜だった) と ir (行った) の点過去は<b>全く同じ形</b>です！<br>・yo <b>fui</b> / tú <b>fuiste</b> / él <b>fue</b> / nosotros <b>fuimos</b> / ellos <b>fueron</b><br>例: <i>Ayer fui al cine.</i> (昨日映画館に行きました)",
        "title": "ser と ir の点過去",
        "sentence": "「昨日、私は映画館へ行きました」の点過去形は？ Ayer [___] al cine.",
        "options": "fui, fue, iba, vaya",
        "correct_answer": "fui",
        "hint": "ir の 1人称単数点過去は fui です。",
        "explanation": "ir (行く) の yo 点過去活用形は fui です。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第71課: hacer, tener, estar の不規則点過去",
        "content": "<b>【強不規則点過去】</b><br>・<i>hacer</i> ➔ <b>hice, hiciste, hizo...</b><br>・<i>tener</i> ➔ <b>tuve, tuviste, tuvo...</b><br>・<i>estar</i> ➔ <b>estuve, estuviste, estuvo...</b>",
        "title": "hacer/tener/estar 点過去",
        "sentence": "「私は時間がありました」の空欄に入る tener の点過去形は？ Yo [___] tiempo.",
        "options": "tuve, tenia, tení, tuvo",
        "correct_answer": "tuve",
        "hint": "tener の yo 点過去形は tuve です。",
        "explanation": "tener の yo 点過去形は tuve です。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第72課: dar と ver の点過去活用",
        "content": "<b>【dar と ver の点過去】</b><br>・<i>dar</i>: <b>di, diste, dio, dimos, dieron</b><br>・<i>ver</i>: <b>vi, viste, vio, vimos, vieron</b><br>※アクセント記号がつかない点に注意！",
        "title": "dar と ver の点過去",
        "sentence": "「私は映画を見ました」の ver の点過去形は？ Yo [___] una película.",
        "options": "vi, vio, veía, viste",
        "correct_answer": "vi",
        "hint": "ver の yo 点過去形は vi (アクセント記号なし) です。",
        "explanation": "ver の yo 点過去活用は vi です。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第73課: 語尾変化動詞 (-car, -gar, -zar ➔ qué, gué, cé)",
        "content": "<b>【1人称単数での綴り変化】</b><br>発音を維持するため yo 形のみ変化します。<br>・<i>buscar</i> ➔ yo <b>busqué</b><br>・<i>llegar</i> ➔ yo <b>llegué</b><br>・<i>empezar</i> ➔ yo <b>empecé</b>",
        "title": "-car, -gar, -zar 点過去",
        "sentence": "「私は9時に到着しました」の llegar の yo 点過去形は？ Yo [___] a las 9.",
        "options": "llegué, llegó, llegaste, llegaba",
        "correct_answer": "llegué",
        "hint": "llegar の yo 点過去形は -gué と綴ります。",
        "explanation": "llegar の yo 点過去は llegué になります。"
    },
    {
        "category": "8. 過去形①：点過去 (完了過去)",
        "lesson_title": "第74課: 点過去で使われる時間の副詞 (ayer, anoche, la semana pasada)",
        "content": "<b>【点過去のキーフレーズ】</b><br>・<b>ayer</b> (昨日)<br>・<b>anoche</b> (昨夜)<br>・<b>la semana pasada</b> (先週)<br>・<b>el año pasado</b> (去年)",
        "title": "点過去のキーフレーズ",
        "sentence": "「昨夜」を意味するスペイン語はどれでしょう？ [___]",
        "options": "anoche, ayer, mañana, esta noche",
        "correct_answer": "anoche",
        "hint": "昨夜は anoche です。",
        "explanation": "昨夜は anoche と言います。"
    },

    # --- 9. 過去形②：線過去 (不完了過去) (第75課〜第82課) ---
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第75課: 線過去の概念 (継続・習慣・背景描写)",
        "content": "<b>【線過去の用途】</b><br>「〜していた」「昔よく〜したものだ」という<b>過去の継続的状態・習慣・背景・時刻・年齢描写</b>を表します。",
        "title": "線過去の概念",
        "sentence": "「子どもの頃よくサッカーをしていた」のような過去の習慣を表す時使う過去形は？ [___]",
        "options": "線過去 (不完了過去), 点過去 (完了過去), 現在完了, 将来形",
        "correct_answer": "線過去 (不完了過去)",
        "hint": "過去の継続的な状態や繰り返していた習慣には線過去を使います。",
        "explanation": "過去の習慣・進行中の状態・背景には線過去を用います。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第76課: -ar 動詞の線過去活用 (-aba, -abas, -aba...)",
        "content": "<b>【-ar 動詞の線過去】</b><br>例: <i>hablar</i><br>・yo <b>hablaba</b><br>・tú <b>hablabas</b><br>・él/ella <b>hablaba</b><br>・nosotros <b>hablábamos</b><br>・ellos <b>hablaban</b>",
        "title": "-ar 線過去活用",
        "sentence": "「子どもの頃、よく遊んでいた」の jugar の yo 線過去形は？ Yo [___] mucho.",
        "options": "jugaba, jugué, jugara, jugaste",
        "correct_answer": "jugaba",
        "hint": "-ar 動詞の yo 線過去語尾は -aba です。",
        "explanation": "jugar の yo 線過去形は jugaba です。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第77課: -er / -ir 動詞の線過去活用 (-ía, -ías, -ía...)",
        "content": "<b>【-er / -ir 動詞の線過去】</b><br>例: <i>comer</i> / <i>vivir</i><br>・yo <b>comía</b> / <b>vivía</b><br>・tú <b>comías</b> / <b>vivías</b><br>・él/ella <b>comía</b> / <b>vivía</b><br>・nosotros <b>comíamos</b> / <b>vivíamos</b><br>・ellos <b>comían</b> / <b>vivían</b>",
        "title": "-er/-ir 線過去活用",
        "sentence": "「私はスペインに住んでいた」の vivir の yo 線過去形は？ Yo [___] en España.",
        "options": "vivía, viví, vivías, vivieron",
        "correct_answer": "vivía",
        "hint": "-er/-ir 動詞の yo 線過去語尾は -ía です。",
        "explanation": "vivir の yo 線過去形は vivía です。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第78課: たった3つしかない線過去の不規則動詞 (ser, ir, ver)",
        "content": "<b>【線過去の不規則動詞は3つだけ！】</b><br>1. <i>ser</i> ➔ <b>era, eras, era, éramos, eran</b><br>2. <i>ir</i> ➔ <b>iba, ibas, iba, íbamos, iban</b><br>3. <i>ver</i> ➔ <b>veía, veías, veía, veíamos, veían</b>",
        "title": "線過去の不規則動詞",
        "sentence": "「子どもの頃(cuando era niño)」の era はどの動詞の線過去形でしょう？ [___]",
        "options": "ser, estar, ir, ver",
        "correct_answer": "ser",
        "hint": "ser の線過去形が era です。",
        "explanation": "ser の線過去形は era, eras, era... と活用します。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第79課: 過去の時刻・年齢の表現 (Eran las 3 / Tenía 10 años)",
        "content": "<b>【過去の時刻と年齢】</b><br>時刻や年齢の背景描写には必ず<b>線過去</b>を使います。<br>・<i>Eran las tres.</i> (3時だった)<br>・<i>Tenía diez años.</i> (10歳だった)",
        "title": "過去の時刻と年齢",
        "sentence": "「3時でした」を表す過去表現はどちらでしょう？ [___]",
        "options": "Eran las tres., Fueron las tres., Son las tres., Hay las tres.",
        "correct_answer": "Eran las tres.",
        "hint": "過去の時刻描写には ser の線過去複数形 Eran を使います。",
        "explanation": "時間の背景描写には Eran las + [数字] を使います。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第80課: 点過去 vs 線過去のコンビネーション (〜していた時、〜した)",
        "content": "<b>【割り込みの表現】</b><br>進行中・背景 (<b>線過去</b>) の時に一瞬の出来事 (<b>点過去</b>) が起こる文型です。<br>例: <i>Cuando veía la tele, sonó el teléfono.</i> (テレビを見ている時、電話が鳴った)",
        "title": "点過去 vs 線過去",
        "sentence": "「テレビを見ている(背景)時、電話が鳴った(割り込み)」の「見ていた」に入る動詞形は？ Cuando [___] (ver) la tele, sonó el teléfono.",
        "options": "veía, vi, vio, vería",
        "correct_answer": "veía",
        "hint": "背景・進行中の動作には線過去 veía を用います。",
        "explanation": "進行中の背景動作には線過去 veía を用います。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第81課: 過去の進行形 (estaba + 現在分詞)",
        "content": "<b>【過去進行形】</b><br><b>estarの線過去 (estaba) + 現在分詞</b> で「ちょうど〜している最中だった」を強調します。<br>例: <i>Estaba estudiando cuando llegaste.</i> (君が着いた時、私は勉強中だった)",
        "title": "過去進行形",
        "sentence": "「ちょうど勉強している最中だった」を表す文の空欄は？ [___] estudiando.",
        "options": "Estaba, Estuve, Estoy, Estaría",
        "correct_answer": "Estaba",
        "hint": "estar の線過去形 estaba を使います。",
        "explanation": "過去進行形は estaba + 現在分詞 です。"
    },
    {
        "category": "9. 過去形②：線過去 (不完了過去)",
        "lesson_title": "第82課: 昔の習慣を表す soler + 原形 の過去形 (solía...)",
        "content": "<b>【solía + 動詞の原形】</b><br>「昔よく〜したものだ」という過去の習慣を明確に表します。<br>例: <i>Solía ir al parque.</i> (昔よく公園に行ったものだ)",
        "title": "solía + 原形",
        "sentence": "「昔よく散歩したものだ」の空欄に入る語は？ [___] pasear.",
        "options": "Solía, Solí, Suelo, Soler",
        "correct_answer": "Solía",
        "hint": "soler の線過去形 solía を使います。",
        "explanation": "昔の習慣を表す solía + 原形 です。"
    },

    # --- 10. 過去形③：現在完了と 3大過去の使い分け (第83課〜第90課) ---
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第83課: 現在完了の概念と構造 (haber + 過去分詞)",
        "content": "<b>【現在完了形】</b><br>「(今までに)〜したことがある」「(今日/今週)〜してしまった」など、現在と関連のある過去を表します。<br>構造: <b>haberの現在形 + 過去分詞</b>",
        "title": "現在完了の構造",
        "sentence": "現在完了形を作る際の助動詞はどれでしょう？ [___]",
        "options": "haber, tener, ser, estar",
        "correct_answer": "haber",
        "hint": "現在完了には haber + 過去分詞 を用います。",
        "explanation": "現在完了の助動詞は haber です。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第84課: haber動詞の現在形活用 (he, has, ha, hemos, habéis, han)",
        "content": "<b>【haber の活用】</b><br>・yo <b>he</b><br>・tú <b>has</b><br>・él/ella <b>ha</b><br>・nosotros <b>hemos</b><br>・vosotros <b>habéis</b><br>・ellos <b>han</b>",
        "title": "haber の活用",
        "sentence": "「私は〜した」の yo に対する haber の活用形は？ Yo [___] comido.",
        "options": "he, has, ha, hemos",
        "correct_answer": "he",
        "hint": "Yo に対する haber の活用は he です。",
        "explanation": "Yo の haber 活用は he です。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第85課: 過去分詞の作り方 (規則: -ado, -ido)",
        "content": "<b>【過去分詞の作り方】</b><br>・-ar 動詞 ➔ <b>-ado</b> (<i>hablado</i>)<br>・-er / -ir 動詞 ➔ <b>-ido</b> (<i>comido</i>, <i>vivido</i>)<br>例: <i>He hablado con Juan.</i> (フアンと話しました)",
        "title": "過去分詞の規則変化",
        "sentence": "hablar の過去分詞形はどれでしょう？ [___]",
        "options": "hablado, comido, hablada, hablando",
        "correct_answer": "hablado",
        "hint": "-ar 動詞の過去分詞語尾は -ado です。",
        "explanation": "hablar の過去分詞は hablado です。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第86課: 重要な不規則過去分詞 (hecho, escrito, visto, dicho...)",
        "content": "<b>【主要な不規則過去分詞】</b><br>・<i>hacer</i> ➔ <b>hecho</b><br>・<i>escribir</i> ➔ <b>escrito</b><br>・<i>ver</i> ➔ <b>visto</b><br>・<i>decir</i> ➔ <b>dicho</b><br>・<i>abrir</i> ➔ <b>abierto</b><br>・<i>volver</i> ➔ <b>vuelto</b>",
        "title": "不規則過去分詞",
        "sentence": "hacer (する/作る) の過去分詞形はどれでしょう？ [___]",
        "options": "hecho, hacido, haciado, haciendo",
        "correct_answer": "hecho",
        "hint": "hacer の過去分詞は hecho です。",
        "explanation": "hacer の過去分詞は hecho になります。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第87課: 現在完了で使われる時間語句 (hoy, esta semana, ya, todavía no)",
        "content": "<b>【現在完了のキーワード】</b><br>・<b>hoy</b> (今日)<br>・<b>esta semana</b> (今週)<br>・<b>ya</b> (もう/すでに)<br>・<b>todavía no</b> (まだ〜ない)<br>例: <i>Ya he comido.</i> (もう食べました)",
        "title": "現在完了キーワード",
        "sentence": "「まだ〜していない」を表すフレーズはどれでしょう？ [___]",
        "options": "todavía no, ya, hoy, nunca",
        "correct_answer": "todavía no",
        "hint": "todavía no は「まだ〜ない」を意味します。",
        "explanation": "「まだ〜ない」は todavía no です。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第88課: 経験を表す Alguna vez (今までに〜したことがあるか)",
        "content": "<b>【経験の表現】</b><br><b>¿Alguna vez has + 過去分詞?</b> で「今までに〜したことある？」と経験を尋ねます。<br>例: <i>¿Alguna vez has estado en España?</i> (スペインに行ったことありますか？)",
        "title": "経験の表現",
        "sentence": "「今までに〜したことありますか？」の「今までに」は？ ¿[___] vez...?",
        "options": "Alguna, Ninguna, Una, Muchas",
        "correct_answer": "Alguna",
        "hint": "¿Alguna vez...? で「今までに」を意味します。",
        "explanation": "経験を尋ねる疑問詞表現は ¿Alguna vez...? です。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第89課: スペイン（本国）と中南米での現在完了・点過去の地域差",
        "content": "<b>【地域による使い分けの差異】</b><br>・スペイン本国 ➔ 「今日・最近の出来事」に<b>現在完了</b>を多用。<br>・中南米 ➔ 今日完了したことであっても<b>点過去</b>を好む傾向が強い。",
        "title": "過去形の地域差",
        "sentence": "スペイン本国で「今日〜した」という最近の出来事に頻用される過去形は？ [___]",
        "options": "現在完了形, 点過去形, 過去完了形, 未来形",
        "correct_answer": "現在完了形",
        "hint": "スペイン本国では hoy や esta mañana に現在完了を好みます。",
        "explanation": "スペイン本国では身近な過去・今日の出来事に現在完了形を多用します。"
    },
    {
        "category": "10. 過去形③：現在完了と 3大過去の使い分け",
        "lesson_title": "第90課: 過去完了形 (había + 過去分詞: 大過去)",
        "content": "<b>【過去完了 (大過去)】</b><br>「過去のある時点より前にすでに完了していた」ことを表します。<br>構造: <b>había / habías / había / habíamos / habían + 過去分詞</b>",
        "title": "過去完了形",
        "sentence": "「私が着いた時、彼はすでに出発していた」の空欄に入る過去完了助動詞は？ Cuando llegué, él ya [___] salido.",
        "options": "había, ha, fue, estuvo",
        "correct_answer": "había",
        "hint": "haber の線過去形 había を用いて過去完了を作ります。",
        "explanation": "大過去（過去完了）には había + 過去分詞 を使います。"
    },

    # --- 11. 未来形・可能形・命令形 (第91課〜第98課) ---
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第91課: 直説法未来形の規則活用 (語尾: -é, -ás, -á, -emos, -éis, -án)",
        "content": "<b>【直説法未来形の活用】</b><br><b>動詞の原形 (不定詞) + 共通語尾</b> をつけます！<br>-ar, -er, -ir 全て共通:<br>・<b>-é, -ás, -á, -emos, -éis, -án</b><br>例: <i>hablaré</i>, <i>comeré</i>, <i>viviré</i>",
        "title": "直説法未来形",
        "sentence": "「私は明日勉強するでしょう」の estudiar の未来形は？ Mañana [___] (estudiar).",
        "options": "estudiaré, estudié, estudiaba, estudiarás",
        "correct_answer": "estudiaré",
        "hint": "原形 estudiar に -é をつけます。",
        "explanation": "estudiar + é ➔ estudiaré となります。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第92課: 未来形の不規則語幹 (tendr-, habr-, podr-, har-, dir-...)",
        "content": "<b>【未来形の不規則語幹】</b><br>・<i>tener</i> ➔ <b>tendr-</b> (tendré)<br>・<i>hacer</i> ➔ <b>har-</b> (haré)<br>・<i>decir</i> ➔ <b>dir-</b> (diré)<br>・<i>poder</i> ➔ <b>podr-</b> (podré)<br>・<i>haber</i> ➔ <b>habr-</b> (habrá)",
        "title": "未来形の不規則語幹",
        "sentence": "hacer (する) の 1人称単数未来形はどれでしょう？ [___]",
        "options": "haré, haceré, hago, hiciera",
        "correct_answer": "haré",
        "hint": "hacer の語幹は har- になります。",
        "explanation": "hacer の未来形は haré です。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第93課: 推測を表す未来形 (〜だろう、〜かな)",
        "content": "<b>【現在についての推測】</b><br>未来形は「未来の出来事」だけでなく「現在の推測（〜だろう）」を表すのによく使われます。<br>例: <i>¿Qué hora es? - Serán las cuatro.</i> (4時くらいだろう)",
        "title": "推測の未来形",
        "sentence": "「今4時くらいだろう(推測)」の空欄に入る未来形は？ [___] las cuatro.",
        "options": "Serán, Son, Eran, Serían",
        "correct_answer": "Serán",
        "hint": "現在の推測には ser の未来形 Serán を使います。",
        "explanation": "現在の推測には直説法未来形 Serán を使います。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第94課: 可能法 (条件法) の基礎 (-aría, -arías, -aría...)",
        "content": "<b>【可能法 (条件法)】</b><br><b>動詞原形 + -ía, -ías, -ía, -íamos, -íais, -ían</b><br>丁寧な依頼や「〜だろうに(過去から見た未来/仮定)」を表します。<br>例: <i>Me gustaría un café.</i> (コーヒーを頂きたいのですが)",
        "title": "可能法 (条件法)",
        "sentence": "「〜したいのですが(丁寧な表現)」の Me [___] (gustar) un café.",
        "options": "gustaría, gustaba, gustará, guste",
        "correct_answer": "gustaría",
        "hint": "gustar の可能法形は gustaría です。",
        "explanation": "丁寧な表現 Me gustaría... には可能法を使います。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第95課: 肯定命令形 (tú に対する命令: 3人称単数現在と同じ)",
        "content": "<b>【親しい人(tú)への肯定命令】</b><br>原則として<b>直説法現在の3人称単数形（él/ellaの形）と同じ</b>です！<br>・<i>hablar</i> ➔ <b>¡Habla!</b> (話して！)<br>・<i>comer</i> ➔ <b>¡Come!</b> (食べて！)",
        "title": "tú 肯定命令",
        "sentence": "親しい友人(tú)に「話して！」と命令する形は？ ¡[___]! (hablar)",
        "options": "Habla, Hablas, Hablo, Hable",
        "correct_answer": "Habla",
        "hint": "tú に対する肯定命令は 3人称単数現在形 Habla と同型です。",
        "explanation": "tú に対する肯定命令形は Habla です。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第96課: tú 命令の不規則 8大動詞 (haz, ve, ten, pon, sal, ven, di, sé)",
        "content": "<b>【8大不規則 tú 命令】</b><br>・<i>hacer</i> ➔ <b>haz</b><br>・<i>ir</i> ➔ <b>ve</b><br>・<i>tener</i> ➔ <b>ten</b><br>・<i>poner</i> ➔ <b>pon</b><br>・<i>salir</i> ➔ <b>sal</b><br>・<i>venir</i> ➔ <b>ven</b><br>・<i>decir</i> ➔ <b>di</b><br>・<i>ser</i> ➔ <b>sé</b>",
        "title": "不規則 tú 命令",
        "sentence": "hacer (する/作る) の tú 肯定命令形はどれでしょう？ ¡[___]lo! (それをしなさい)",
        "options": "Haz, Hace, Hago, Hice",
        "correct_answer": "Haz",
        "hint": "hacer の tú 命令は 短い Haz です。",
        "explanation": "hacer の tú 命令形は Haz です。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第97課: usted / ustedes に対する丁寧な命令",
        "content": "<b>【丁寧な命令 (usted/es)】</b><br>接続法現在の形（あべこべ活用: -ar ➔ -e, -er/-ir ➔ -a）を使います。<br>・<i>hablar</i> ➔ <b>¡Hable usted!</b> / <b>¡Hablen ustedes!</b><br>・<i>comer</i> ➔ <b>¡Coma usted!</b>",
        "title": "usted 丁寧命令",
        "sentence": "usted (あなた) に対する hablar の丁寧な命令形は？ ¡[___] usted!",
        "options": "Hable, Habla, Hablo, Hablan",
        "correct_answer": "Hable",
        "hint": "usted 命令はあべこべ活用の Hable になります。",
        "explanation": "usted に対する命令は接続法と同型の Hable です。"
    },
    {
        "category": "11. 未来形・可能形・命令形",
        "lesson_title": "第98課: 否定命令 (No + 接続法)",
        "content": "<b>【否定命令 (〜するな)】</b><br>人称に関わらず <b>No + 接続法現在</b> を使います。<br>・<i>tú</i> ➔ <b>No hables.</b> (話すな)<br>・<i>usted</i> ➔ <b>No hable.</b>",
        "title": "否定命令",
        "sentence": "tú に対する「心配しないで！」の正しい否定命令文は？ ¡No [___]! (preocuparse)",
        "options": "te preocupes, te preocupas, preocúpate, preocupes",
        "correct_answer": "te preocupes",
        "hint": "No + 再帰代名詞 + 接続法 で No te preocupes となります。",
        "explanation": "否定命令は No te preocupes (心配しないで) となります。"
    },

    # --- 12. 前置詞 (por/para) と関係詞 (第99課〜第106課) ---
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第99課: por と para の基本概念比較 (方向 vs 原因)",
        "content": "<b>【por vs para 徹底比較】</b><br>・<b>para</b> ➔ 矢印の先 (目的・目的地・期限・受取人)<br>・<b>por</b> ➔ 原因・理由・手段・通過・交換・期間",
        "title": "por と para 比較",
        "sentence": "「働くために勉強する(目的)」の空欄に入る前置詞は？ Estudio [___] trabajar.",
        "options": "para, por, de, a",
        "correct_answer": "para",
        "hint": "目的「〜のために」は para を使います。",
        "explanation": "目的を表す「〜のために」は para です。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第100課: para の用法 (目的・期限・目的地・受取人)",
        "content": "<b>【para の具体例】</b><br>・<i>para mañana</i> (明日までの期限)<br>・<i>para Madrid</i> (マドリード行き)<br>・<i>para ti</i> (君へのおくりもの)",
        "title": "para の用法",
        "sentence": "「これは君へのプレゼントです」の空欄に入る前置詞は？ Es un regalo [___] ti.",
        "options": "para, por, de, con",
        "correct_answer": "para",
        "hint": "受取人を示す「〜宛ての」は para です。",
        "explanation": "受取人を示す「〜へ/向け」は para です。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第101課: por の用法 (原因理由・手段・通過・感謝・交換)",
        "content": "<b>【por の具体例】</b><br>・<i>Gracias por tu ayuda.</i> (手助けに感謝 [原因])<br>・<i>por avión</i> (飛行機で [手段])<br>・<i>por el parque</i> (公園を通って [通過])",
        "title": "por の用法",
        "sentence": "「助けてくれてありがとう」の Gracias [___] tu ayuda に入る語は？",
        "options": "por, para, de, en",
        "correct_answer": "por",
        "hint": "感謝の理由・原因には por を使います。",
        "explanation": "感謝の理由を表すには por を用います。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第102課: 主要前置詞 a, de, en, con, sin のマスター",
        "content": "<b>【基礎前置詞】</b><br>・<b>a</b> (〜へ/〜に)<br>・<b>de</b> (〜の/〜から)<br>・<b>en</b> (〜の中に/〜で)<br>・<b>con</b> (〜と一緒に) / <b>sin</b> (〜なしで)<br>例: <i>Café con leche</i> (ミルク入りコーヒー)",
        "title": "基礎前置詞",
        "sentence": "「砂糖なしのコーヒー」の「〜なしで」に入る前置詞は？ café [___] azúcar",
        "options": "sin, con, de, para",
        "correct_answer": "sin",
        "hint": "「〜なしで」は sin です。",
        "explanation": "「〜なしで」を表す前置詞は sin です。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第103課: 前置詞と人称代名詞 (para mí, con él, conmigo, contigo)",
        "content": "<b>【前置詞の後の代名詞】</b><br>前置詞の後ろは原則 <b>mí, ti, él, ella, nosotros...</b> となります。<br>※<b>con + mí ➔ conmigo</b> (私と一緒に)<br>※<b>con + ti ➔ contigo</b> (君と一緒に)",
        "title": "前置詞と代名詞",
        "sentence": "「私と一緒に来たいですか？」の「私と一緒に」を表す単語は？ ¿Quieres venir [___]?",
        "options": "conmigo, con mí, contigo, con yo",
        "correct_answer": "conmigo",
        "hint": "con + mí は conmigo という1語になります。",
        "explanation": "con + mí は特殊形 conmigo になります。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第104課: 関係代名詞 que (最も普遍的な関係詞)",
        "content": "<b>【関係代名詞 que】</b><br>先行詞が「人」でも「物」でも使える万能な関係代名詞です。<br>例: <i>El libro que compré es interesante.</i> (私が買った本は面白い)",
        "title": "関係代名詞 que",
        "sentence": "「私が買った本」をつなぐ関係代名詞は？ El libro [___] compré...",
        "options": "que, quien, donde, cual",
        "correct_answer": "que",
        "hint": "最も一般的な関係代名詞は que です。",
        "explanation": "先行詞をつなぐ最も普遍的な関係代名詞は que です。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第105課: 人を先行詞とする関係詞 quien / quienes",
        "content": "<b>【関係代名詞 quien】</b><br>先行詞が「人」で、前置詞と一緒に使われる際によく用いられます。<br>例: <i>La chica con quien hablé es María.</i> (私が話した女の子はマリアです)",
        "title": "関係代名詞 quien",
        "sentence": "「私が一緒に話した女の子」の La chica con [___] hablé...",
        "options": "quien, que, donde, cual",
        "correct_answer": "quien",
        "hint": "前置詞 con の後ろで人を指す関係代名詞は quien です。",
        "explanation": "前置詞 + 人を先行詞とする関係代名詞には quien を用います。"
    },
    {
        "category": "12. 前置詞 (por/para) と関係詞",
        "lesson_title": "第106課: 場所を表す関係副詞 donde",
        "content": "<b>【関係副詞 donde】</b><br>場所を表す先行詞を修飾します。<br>例: <i>La casa donde vivo es grande.</i> (私が住んでいる家は大きい)",
        "title": "関係副詞 donde",
        "sentence": "「私が住んでいる家」の La casa [___] vivo...",
        "options": "donde, que, quien, cuando",
        "correct_answer": "donde",
        "hint": "場所を受ける関係詞は donde です。",
        "explanation": "場所の先行詞を受ける関係副詞は donde です。"
    },

    # --- 13. 接続法入門と実践マスター (第107課〜第113課) ---
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第107課: 接続法現在の概念 (主観・願望・感情・不確定の世界)",
        "content": "<b>【接続法の世界】</b><br>直説法が「客観的・確定した事実」を表すのに対し、接続法は<b>主観・願望・感情・疑念・不確定な事象</b>を表します。<br>トリガー: <b>Quiero que...</b> (〜してほしい), <b>Espero que...</b> (〜を願う)",
        "title": "接続法の概念",
        "sentence": "話者の願望・感情・不確定な気持ちを表す法はどちらでしょう？ [___]",
        "options": "接続法, 直説法, 命令法, 受動態",
        "correct_answer": "接続法",
        "hint": "主観・願望・感情には接続法を用います。",
        "explanation": "願望・感情・不確定な内容には接続法を使います。"
    },
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第108課: 接続法現在の作り方 (あべこべ活用ルール)",
        "content": "<b>【あべこべ活用ルール】</b><br>現在形の yo から -o を取り、母音を反対にします！<br>・<b>-ar 動詞 ➔ -e, -es, -e, -emos, -éis, -en</b><br>・<b>-er / -ir 動詞 ➔ -a, -as, -a, -amos, -áis, -an</b><br>例: <i>hablar</i> ➔ <b>hable</b> / <i>comer</i> ➔ <b>coma</b>",
        "title": "接続法現在の作り方",
        "sentence": "-ar 動詞 hablar の接続法現在 3人称単数形 (él/ella) はどれでしょう？ [___]",
        "options": "hable, habla, hablo, hablará",
        "correct_answer": "hable",
        "hint": "-ar 動詞はあべこべの -e 語尾になります。",
        "explanation": "hablar の接続法現在形は hable です。"
    },
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第109課: 願望を表すトリガー (Quiero que / Espero que + 接続法)",
        "content": "<b>【願望の表現】</b><br><b>Quiero que + [接続法]</b> ➔ 「〜してほしい」<br>例: <i>Quiero que vengas.</i> (あなたに来てほしい)<br>※主語が異なる場合に que + 接続法 になります。",
        "title": "願望の接続法",
        "sentence": "「あなたに来てほしい(venir)」の空欄に入る接続法形は？ Quiero que [___] (tú).",
        "options": "vengas, vienes, ven, vendrás",
        "correct_answer": "vengas",
        "hint": "venir の yo 形 vengo から -o を取ってあべこべ語尾 -as をつけます。",
        "explanation": "venir の 2人称単数接続法現在形は vengas です。"
    },
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第110課: 感情を表すトリガー (Me alegro de que / Siento que + 接続法)",
        "content": "<b>【感情の表現】</b><br>嬉しい、残念だなどの感情を表す主節に続く que 節内は<b>接続法</b>になります。<br>例: <i>Me alegro de que estés bien.</i> (あなたが元気でいてくれて嬉しいです)",
        "title": "感情の接続法",
        "sentence": "「あなたが元気でいてくれて嬉しい」の Me alegro de que [___] (estar) bien.",
        "options": "estés, estás, estar, estuviste",
        "correct_answer": "estés",
        "hint": "estar の 2人称接続法現在形は estés です。",
        "explanation": "estar の 2人称単数接続法形は estés です。"
    },
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第111課: 疑惑・否定を表すトリガー (No creo que + 接続法)",
        "content": "<b>【否定・疑惑の接続法】</b><br>・<i>Creo que es verdad.</i> (本当だと思う ➔ 直説法)<br>・<b>No creo que sea verdad.</b> (本当だとは思わない ➔ 接続法 sea)",
        "title": "否定・疑惑の接続法",
        "sentence": "「それが本当だとは思わない」の No creo que [___] (ser) verdad.",
        "options": "sea, es, era, será",
        "correct_answer": "sea",
        "hint": "ser の接続法現在形は sea です。",
        "explanation": "No creo que の後は接続法 sea を用います。"
    },
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第112課: 非人称表現のトリガー (Es necesario que / Es posible que + 接続法)",
        "content": "<b>【非人称構文 + 接続法】</b><br>・<b>Es necesario que...</b> (〜することが必要だ)<br>・<b>Es posible que...</b> (〜する可能性がある)<br>例: <i>Es necesario que estudies.</i> (君は勉強する必要がある)",
        "title": "非人称の接続法",
        "sentence": "「君が勉強することが必要だ」の Es necesario que [___] (estudiar).",
        "options": "estudies, estudias, estudiar, estudiaras",
        "correct_answer": "estudies",
        "hint": "tú に対する estudiar の接続法形は estudies です。",
        "explanation": "estudiar の 2人称単数接続法形は estudies です。"
    },
    {
        "category": "13. 接続法入門と実践マスター",
        "lesson_title": "第113課: 全113課完了！ 1年マスター達成と継続学習のアドバイス",
        "content": "<b>【🎉 全113課 修了おめでとうございます！】</b><br>発音、文法基礎、2大過去形、未来形、命令形、前置詞、そして接続法まで、スペイン語の全主要文法体系をマスターしました！<br>今後は SRS 復習クイズや辞書機能を活用し、語彙力と会話力を磨いていきましょう。¡Enhorabuena!",
        "title": "修了テスト＆全113課達成",
        "sentence": "全113課を達成したあなたへのお祝いの言葉「おめでとう！」はどれでしょう？ [___]",
        "options": "¡Enhorabuena!, ¡Hola!, ¡Adiós!, ¡Gracias!",
        "correct_answer": "¡Enhorabuena!",
        "hint": "「おめでとう！」を意味するスペイン語です。",
        "explanation": "スペイン語で「おめでとう！」は ¡Enhorabuena! または ¡Felicidades! です。"
    }
]

def seed_database():
    print(f"Total defined lessons: {len(LESSONS_DATA)}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS cards")
    cursor.execute('''
    CREATE TABLE cards (
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

    today_str = datetime.date.today().isoformat()
    now_str = datetime.datetime.now().isoformat()

    for item in LESSONS_DATA:
        cursor.execute('''
        INSERT INTO cards (category, lesson_title, content, title, sentence, options, correct_answer, hint, explanation, repetitions, interval_days, ease_factor, next_review_date, mistake_count, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, 2.5, ?, 0, ?)
        ''', (
            item["category"],
            item["lesson_title"],
            item["content"],
            item["title"],
            item["sentence"],
            item["options"],
            item["correct_answer"],
            item["hint"],
            item["explanation"],
            today_str,
            now_str
        ))

    conn.commit()

def seed_dictionary_database():
    from dictionary_data import DICTIONARY_DATA
    print(f"Total defined words: {len(DICTIONARY_DATA)}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS dictionary")
    cursor.execute('''
    CREATE TABLE dictionary (
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

    today_str = datetime.date.today().isoformat()
    now_str = datetime.datetime.now().isoformat()

    for item in DICTIONARY_DATA:
        conj_text = item[6] if len(item) > 6 else ""
        cursor.execute('''
        INSERT INTO dictionary (word, reading, pos, meanings, examples, category, conjugation, repetitions, interval_days, ease_factor, next_review_date, mistake_count, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, 2.5, ?, 0, ?)
        ''', (
            item[0],
            item[1],
            item[2],
            item[3],
            item[4],
            item[5],
            conj_text,
            today_str,
            now_str
        ))

    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM dictionary")
    count = cursor.fetchone()[0]
    print(f"Successfully seeded {count} words with conjugations into {DB_PATH}")
    conn.close()

def seed_chunks_database():
    from chunks_data import CHUNKS_DATA
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS chunks")
    cursor.execute('''
    CREATE TABLE chunks (
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

    today_str = datetime.date.today().isoformat()
    for item in CHUNKS_DATA:
        cursor.execute('''
        INSERT INTO chunks (chunk, reading, category, meaning, example, grammar_point, repetitions, interval_days, ease_factor, next_review_date, mistake_count)
        VALUES (?, ?, ?, ?, ?, ?, 0, 0, 2.5, ?, 0)
        ''', (item[0], item[1], item[2], item[3], item[4], item[5], today_str))

    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM chunks")
    count = cursor.fetchone()[0]
    print(f"Successfully seeded {count} chunks into {DB_PATH}")
    conn.close()

def seed_pop_culture_database():
    from pop_culture_data import POP_CULTURE_DATA
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS pop_culture")
    cursor.execute('''
    CREATE TABLE pop_culture (
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

    for item in POP_CULTURE_DATA:
        cursor.execute('''
        INSERT INTO pop_culture (work, character, category, spanish, reading, japanese, breakdown, grammar_point)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (item["work"], item["character"], item["category"], item["spanish"], item["reading"], item["japanese"], item["breakdown"], item["grammar_point"]))

    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM pop_culture")
    count = cursor.fetchone()[0]
    print(f"Successfully seeded {count} pop culture quotes into {DB_PATH}")
    conn.close()

if __name__ == "__main__":
    seed_database()
    seed_dictionary_database()
    seed_chunks_database()
    seed_pop_culture_database()
