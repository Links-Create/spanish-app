# -*- coding: utf-8 -*-
"""
スペイン語 瞬間パターンプラクティス (瞬間西作文ドリル)
日本語を見て3秒以内に口からスペイン語を出す反射神経トレーニング用データ
(日本語, スペイン語, カタカナ発音, 単語分解)
"""

PATTERN_PRACTICE_DATA = [
    # ==========================================
    # ドリル 1: 【tener】現在形・人称置換マスター
    # ==========================================
    {
        "category": "基本動詞 活用",
        "pattern_name": "① 【tener】 人称置換ドリル（持っている・ある）",
        "base_rule": "主語に合わせて tener を瞬時に変形する：tengo, tienes, tiene, tenemos, tenéis, tienen",
        "drills": [
            ("私は時間があります。", "Tengo tiempo.", "テンゴ ティエンポ", "Tengo(持つ) + tiempo(時間)"),
            ("君は時間がある？", "¿Tienes tiempo?", "ティエネス ティエンポ？", "Tienes(持つ/疑問) + tiempo(時間)"),
            ("彼は時間があります。", "Él tiene tiempo.", "エル ティエネ ティエンポ", "Él(彼) + tiene(持つ) + tiempo(時間)"),
            ("私たちは時間があります。", "Tenemos tiempo.", "テネモス ティエンポ", "Tenemos(私たち持つ) + tiempo(時間)"),
            ("君たちは時間がある？", "¿Tenéis tiempo?", "テネイス ティエンポ？", "Tenéis(君たち持つ) + tiempo(時間)"),
            ("彼らは時間がありません。", "Ellos no tienen tiempo.", "エジョス ノ ティエネン ティエンポ", "Ellos(彼ら) + no(ない) + tienen(持つ) + tiempo(時間)"),
            ("私は車を持っています。", "Tengo un coche.", "テンゴ ウン コチェ", "Tengo(持つ) + un coche(車)"),
            ("君は兄弟がいる？", "¿Tienes hermanos?", "ティエネス エルマノス？", "Tienes(持つ) + hermanos(兄弟)"),
            ("私たちは予約があります。", "Tenemos una reserva.", "テネモス ウナ レセルバ", "Tenemos(持つ) + una reserva(予約)"),
            ("あなた（敬称）はパスポートを持っていますか？", "¿Tiene usted el pasaporte?", "ティエネ ウステッ エル パサポルテ？", "Tiene(持つ) + usted(あなた) + el pasaporte(パスポート)")
        ]
    },

    # ==========================================
    # ドリル 2: 【tener que + 原形】 義務・予定置換
    # ==========================================
    {
        "category": "重要構文",
        "pattern_name": "② 【tener que + 動詞】 瞬間義務ドリル（〜しなきゃいけない）",
        "base_rule": "「主語の人称変化 + que + 動詞の原形」で瞬時に作る",
        "drills": [
            ("私は勉強しなければなりません。", "Tengo que estudiar.", "テンゴ ケ エストゥディアール", "Tengo que(せねばならない) + estudiar(勉強する)"),
            ("君は働かなければならないの？", "¿Tienes que trabajar?", "ティエネス ケ トラバハール？", "Tienes que(せねばならないか) + trabajar(働く)"),
            ("彼女は早く起きなければなりません。", "Ella tiene que levantarse temprano.", "エジャ ティエネ ケ レバンタールセ テンプラノ", "tiene que(せねばならない) + levantarse(起きる) + temprano(早く)"),
            ("私たちは今出発しなければなりません。", "Tenemos que salir ahora.", "テネモス ケ サリール アオラ", "Tenemos que(せねばならない) + salir(出る/出発) + ahora(今)"),
            ("彼らは部屋を掃除しなければなりません。", "Ellos tienen que limpiar la habitación.", "エジョス ティエネン ケ リンピアール ラ アビタシオン", "tienen que(せねばならない) + limpiar(掃除する) + la habitación(部屋)"),
            ("私は薬を飲まなければなりません。", "Tengo que tomar la medicina.", "テンゴ ケ トマール ラ メディシナ", "Tengo que(せねばならない) + tomar(飲む/取る) + la medicina(薬)"),
            ("君は待たなきゃいけないよ。", "Tienes que esperar.", "ティエネス ケ エスペラール", "Tienes que(せねばならない) + esperar(待つ)"),
            ("私たちはチケットを買わなければなりません。", "Tenemos que comprar los billetes.", "テネモス ケ コンプラール ロス ビジェテス", "Tenemos que(せねばならない) + comprar(買う) + los billetes(切符)"),
            ("私は家に帰らなきゃ。", "Tengo que ir a casa.", "テンゴ ケ イール ア カサ", "Tengo que(せねばならない) + ir(行く) + a casa(家へ)"),
            ("君は先生と話さなければなりません。", "Tienes que hablar con el profesor.", "ティエネス ケ アブラール コン エル プロフェソール", "Tienes que(せねばならない) + hablar(話す) + con el profesor(先生と)")
        ]
    },

    # ==========================================
    # ドリル 3: 【ir a + 原形】 近接未来置換
    # ==========================================
    {
        "category": "時制・未来",
        "pattern_name": "③ 【ir a + 動詞】 瞬間未来ドリル（〜する予定だ）",
        "base_rule": "voy a, vas a, va a, vamos a, vais a, van a + 動詞原形",
        "drills": [
            ("私は明日旅行する予定です。", "Voy a viajar mañana.", "ボイ ア ビアハール マニャーナ", "Voy a(〜する予定) + viajar(旅行する) + mañana(明日)"),
            ("君は何を食べるつもり？", "¿Qué vas a comer?", "ケ バス ア コメール？", "Qué(何を) + vas a(〜する予定) + comer(食べる)"),
            ("彼は車を買う予定です。", "Él va a comprar un coche.", "エル バ ア コンプラール ウン コチェ", "va a(〜する予定) + comprar(買う) + un coche(車)"),
            ("私たちは今夜映画を見ます。", "Vamos a ver una película esta noche.", "バモス ア ベール ウナ ペリクラ エスタ ノチェ", "Vamos a(〜する予定) + ver(見る) + una película(映画) + esta noche(今夜)"),
            ("彼らは来週到着する予定です。", "Van a llegar la semana que viene.", "バン ア ジェガール ラ セマナ ケ ビエネ", "Van a(〜する予定) + llegar(到着する) + la semana que viene(来週)"),
            ("私はコーヒーを飲むつもりです。", "Voy a tomar un café.", "ボイ ア トマール ウン カフェ", "Voy a(〜する予定) + tomar(飲む) + un café(コーヒー)"),
            ("君はパーティーに行く？", "¿Vas a ir a la fiesta?", "バス ア イール ア ラ フィエスタ？", "Vas a ir(行く予定か) + a la fiesta(パーティーへ)"),
            ("私たちはスペイン料理を料理する予定です。", "Vamos a cocinar comida española.", "バモス ア コシナール コミダ エスパニョーラ", "Vamos a(〜する予定) + cocinar(料理する) + comida española(スペイン料理)"),
            ("彼女は新しい言語を学ぶつもりです。", "Ella va a aprender un nuevo idioma.", "エジャ バ ア アプレンデール ウン ヌエボ イディオマ", "va a(〜する予定) + aprender(学ぶ) + un nuevo idioma(新しい言語)"),
            ("君たちはいつ出発する予定？", "¿Cuándo vais a salir?", "クアンド バイス ア サリール？", "Cuándo(いつ) + vais a(君たち〜する予定) + salir(出発する)")
        ]
    },

    # ==========================================
    # ドリル 4: 【gustar 型動詞】 好き・お気に入り置換
    # ==========================================
    {
        "category": "重要文型",
        "pattern_name": "④ 【gustar型】 好き・好み瞬時置換ドリル",
        "base_rule": "me / te / le / nos / os / les + gusta (単数・動詞) / gustan (複数)",
        "drills": [
            ("私はスペインが好きです。", "Me gusta España.", "メ グスタ エスパーニャ", "Me gusta(私に好まれる) + España(スペイン)"),
            ("君は音楽が好き？", "¿Te gusta la música?", "テ グスタ ラ ムシカ？", "Te gusta(君に好まれる) + la música(音楽)"),
            ("彼は本を読むのが好きです。", "A él le gusta leer libros.", "ア エル レ グスタ レエール リブロス", "A él le gusta(彼にとって好き) + leer libros(本を読むこと)"),
            ("私たちはタパスが大好きです。", "Nos encantan las tapas.", "ノス エンカンタン ラス タパス", "Nos encantan(大好物だ [複数]) + las tapas(タパス)"),
            ("君たちは旅行が好き？", "¿Os gusta viajar?", "オス グスタ ビアハール？", "Os gusta(君たちにとって好き) + viajar(旅すること)"),
            ("彼らはサッカーが好きです。", "A ellos les gusta el fútbol.", "ア エジョス レス グスタ エル フットボル", "les gusta(彼らにとって好き) + el fútbol(サッカー)"),
            ("私は犬が好きです（複数）。", "Me gustan los perros.", "メ グスタン ロス ペロス", "Me gustan(好まれる [複数]) + los perros(犬たち)"),
            ("君はこの料理が好き？", "¿Te gusta este plato?", "テ グスタ エステ プラト？", "Te gusta(好きか) + este plato(この料理)"),
            ("私は踊るのが好きではありません。", "No me gusta bailar.", "ノ メ グスタ バイラール", "No me gusta(好きではない) + bailar(踊ること)"),
            ("彼女は花が好きです（複数）。", "A ella le gustan las flores.", "ア エジャ レ グスタン ラス フローレス", "le gustan(好まれる [複数]) + las flores(花たち)")
        ]
    },

    # ==========================================
    # ドリル 5: 【点過去 (Pretérito Indefinido)】 完了過去置換
    # ==========================================
    {
        "category": "過去時制",
        "pattern_name": "⑤ 【点過去】 完了した過去の出来事ドリル（〜した）",
        "base_rule": "昨日や過去の一点で行われた動作を瞬時に点過去で答える",
        "drills": [
            ("私は昨日パエリアを食べました。", "Ayer comí paella.", "アジェール コミ パエリア", "Ayer(昨日) + comí(食べた [comer点過去1単]) + paella(パエリア)"),
            ("君は昨日何をしたの？", "¿Qué hiciste ayer?", "ケ イシステ アジェール？", "Qué(何を) + hiciste(した [hacer点過去2単]) + ayer(昨日)"),
            ("私たちは先週マドリードへ行きました。", "La semana pasada fuimos a Madrid.", "ラ セマナ パサダ フイモス ア マドリード", "fuimos(行った [ir点過去1複]) + a Madrid(マドリードへ)"),
            ("彼は昨日来ませんでした。", "Él no vino ayer.", "エル ノ ビノ アジェール", "Él(彼) + no(〜ない) + vino(来た [venir点過去3単]) + ayer(昨日)"),
            ("私は新しい靴を買いました。", "Compré unos zapatos nuevos.", "コンプレ ウノス サパトス ヌエボス", "Compré(買った [comprar点過去1単]) + unos zapatos nuevos(新しい靴)"),
            ("君は鍵を見つけた？", "¿Encontraste las llaves?", "エンコントラステ ラス ジャベス？", "Encontraste(見つけたか [encontrar点過去2単]) + las llaves(鍵)"),
            ("彼女は手紙を書きました。", "Ella escribió una carta.", "エジャ エスクリビオ ウナ カルタ", "Ella(彼女) + escribió(書いた [escribir点過去3単]) + una carta(手紙)"),
            ("私たちは夜の10時に到着しました。", "Llegamos a las diez de la noche.", "ジェガモス ア ラス ディエス デ ラ ノチェ", "Llegamos(到着した) + a las diez(10時に) + de la noche(夜の)"),
            ("彼らは一日中勉強しました。", "Ellos estudiaron todo el día.", "エジョス エストゥディアロン トド エル ディア", "estudiaron(勉強した [estudiar点過去3複]) + todo el día(一日中)"),
            ("私はそのニュースを聞きました。", "Oí la noticia.", "オイ ラ ノティシア", "Oí(聞いた [oír点過去1単]) + la noticia(ニュース)")
        ]
    }
]
