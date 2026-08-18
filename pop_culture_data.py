# -*- coding: utf-8 -*-
"""
映画・海外ドラマ・アニメ名セリフで学ぶスペイン語 (Sentence Mining)
作品名、キャラクター、スペイン語セリフ、日本語訳、単語分解、文法ポイント
"""

POP_CULTURE_DATA = [
    # ==========================================
    # 1. 🇪🇸 海外ドラマ: 『ペーパー・ハウス (La Casa de Papel)』
    # ==========================================
    {
        "work": "ペーパー・ハウス (La Casa de Papel)",
        "character": "El Profesor (教授)",
        "category": "海外ドラマ",
        "spanish": "En este mundo, todo se rige por un simple equilibrio: lo que estás dispuesto a perder y lo que quieres ganar.",
        "reading": "エン エステ ムンド, トド セ リヘ ポル ウン シンプレ エキリブリオ...",
        "japanese": "この世界では、すべてはシンプルな均衡で支配されている。失う覚悟があるものと、手に入れたいものだ。",
        "breakdown": "<b>En este mundo</b>(この世界で) + <b>todo se rige</b>(すべてが支配される [再帰受動]) + <b>por un simple equilibrio</b>(単純な均衡によって) + <b>lo que</b>(〜のもの) + <b>estás dispuesto a perder</b>(失う覚悟がある) + <b>y lo que quieres ganar</b>(そして勝ち取りたいもの)",
        "grammar_point": "<b>【再帰受動態 & estar dispuesto a】</b><br>・<b>se rige</b>: 動詞 regir（統治する）の再帰受動態（se + 3人称動詞）。<br>・<b>estar dispuesto/a a + 原形</b>: 「〜する覚悟・準備ができている」という強い意志を表す上級表現。<br>・<b>lo que</b>: 「〜すること、〜するもの」を表す関係代名詞。"
    },
    {
        "work": "ペーパー・ハウス (La Casa de Papel)",
        "character": "Berlín (ベルリン)",
        "category": "海外ドラマ",
        "spanish": "La muerte puede ser la mejor oportunidad de tu vida.",
        "reading": "ラ ムエルテ プエデ セール ラ メホール オポルチュニダッ デ トゥ ビダ",
        "japanese": "死というのは、人生で最高の好機になり得るんだよ。",
        "breakdown": "<b>La muerte</b>(死) + <b>puede ser</b>(〜になり得る/できる) + <b>la mejor oportunidad</b>(最高の好機) + <b>de tu vida</b>(君の人生の)",
        "grammar_point": "<b>【最上級 & 助動詞 poder】</b><br>・<b>puede + 原形</b>: 「〜する可能性がある、〜になり得る」。<br>・<b>la mejor + 名詞</b>: 「最高の〜」（bueno の最上級）。"
    },
    {
        "work": "ペーパー・ハウス (La Casa de Papel)",
        "character": "Tokio (トーキョー)",
        "category": "海外ドラマ",
        "spanish": "Al final, el amor es una buena razón para que todas las cosas salgan mal.",
        "reading": "アル フィナル, エル アモール エス ウナ ブエナ ラソン パラ ケ...",
        "japanese": "結局のところ、愛ってやつはすべての物事が狂ってしまう十分な理由になるのよ。",
        "breakdown": "<b>Al final</b>(結局/最後に) + <b>el amor es</b>(愛は〜だ) + <b>una buena razón</b>(十分な理由) + <b>para que todas las cosas salgan mal</b>(すべてがうまくいかなくなるための)",
        "grammar_point": "<b>【接続法現在 (para que + 接続法)】</b><br>・<b>para que + 接続法 (salgan)</b>: 「〜するために、〜となるように」。主節と従属節で主語が異なるため、動詞 salir が接続法現在形の <b>salgan</b> に活用しています。"
    },

    # ==========================================
    # 2. 🇲🇽 ディズニー/ピクサー映画: 『リメンバー・ミー (Coco)』
    # ==========================================
    {
        "work": "リメンバー・ミー (Coco)",
        "character": "Héctor (ヘクター)",
        "category": "名作映画",
        "spanish": "Recuérdame, hoy me tengo que ir mi amor. Recuérdame, no llores por favor.",
        "reading": "レクエルダメ, オイ メ テンゴ ケ イール ミ アモール...",
        "japanese": "僕を思い出しておくれ、愛する人よ、僕は今日行かなきゃいけない。僕を思い出しておくれ、お願いだから泣かないで。",
        "breakdown": "<b>Recuérdame</b>(私を思い出して [命令+代名詞]) + <b>hoy</b>(今日) + <b>me tengo que ir</b>(行かねばならない [irse]) + <b>mi amor</b>(私の愛しい人) + <b>no llores</b>(泣かないで [否定命令]) + <b>por favor</b>(どうか)",
        "grammar_point": "<b>【肯定命令・否定命令・代名詞後置】</b><br>・<b>Recuérdame</b>: 動詞 recordar（e➔ue不規則）のtúに対する肯定命令形 recuerda に直接目的語 me を後置結合。<br>・<b>No llores</b>: 動詞 llorar の否定命令形（No + 接続法現在）。肯定命令と否定命令の違いが1曲で学べる最高のフレーズです。"
    },
    {
        "work": "リメンバー・ミー (Coco)",
        "character": "Mamá Coco (ママ・ココ)",
        "category": "名作映画",
        "spanish": "Cuando alguien te ama, nunca te olvida de verdad.",
        "reading": "クアンド アルギエン テ アマ, ヌンカ テ オルビダ デ ベルダッ",
        "japanese": "誰かがあなたを愛しているなら、その人は本当にあなたを忘れたりはしないわ。",
        "breakdown": "<b>Cuando</b>(〜の時) + <b>alguien</b>(誰かが) + <b>te ama</b>(君を愛する) + <b>nunca</b>(決して〜ない) + <b>te olvida</b>(君を忘れる) + <b>de verdad</b>(本当に/真実に)",
        "grammar_point": "<b>【直接目的語代名詞 & 否定副詞】</b><br>・<b>te ama / te olvida</b>: 動詞の直前に「君を (te)」を配置。<br>・<b>nunca</b>: 動詞の前に置いて完全な否定「決して〜ない」を作ります。"
    },

    # ==========================================
    # 3. 🇯🇵 日本のアニメ名セリフ（スペイン語吹き替え版）
    # ==========================================
    {
        "work": "鬼滅の刃 (Demon Slayer)",
        "character": "竈門炭治郎 (Tanjiro Kamado)",
        "category": "大人気アニメ",
        "spanish": "¡Pase lo que pase, nunca te rindas! ¡Sigue adelante!",
        "reading": "パセ ロ ケ パセ, ヌンカ テ リンダス! シゲ アデランテ!",
        "japanese": "何があっても決して諦めるな！前へ進み続けろ！（頑張れ炭治郎頑張れ！）",
        "breakdown": "<b>Pase lo que pase</b>(何が起ころうとも) + <b>nunca te rindas</b>(決して諦めるな [否定命令]) + <b>Sigue adelante</b>(前へ進み続けろ [命令])",
        "grammar_point": "<b>【接続法構文 & 再帰動詞命令】</b><br>・<b>Pase lo que pase</b>: 「何が起きようと（たとえ何があっても）」という接続法を用いたスペイン語の決まり文句！<br>・<b>No te rindas</b>: 再帰動詞 rendirse（諦める・屈する）の否定命令（No + 接続法）。<br>・<b>Sigue adelante</b>: 動詞 seguir（進む/続ける）の肯定命令。"
    },
    {
        "work": "ONE PIECE (ワンピース)",
        "character": "モンキー・D・ルフィ (Luffy)",
        "category": "大人気アニメ",
        "spanish": "¡Voy a ser el Rey de los Piratas!",
        "reading": "ボイ ア セール エル レイ デ ロス ピラタス!",
        "japanese": "海賊王に、おれはなる！！！",
        "breakdown": "<b>Voy a ser</b>(私は〜になるつもりだ [ir a + 原形]) + <b>el Rey</b>(王) + <b>de los Piratas</b>(海賊たちの)",
        "grammar_point": "<b>【近接未来 ir a + ser】</b><br>・<b>Voy a + 原形</b>: 「〜するぞ、〜になる予定だ」という固い決意を表す最も基本的かつ力強い表現。<br>・<b>el Rey de ...</b>: 「〜の王」。英語の King of Pirates と同構造。"
    },
    {
        "work": "千と千尋の神隠し (El Viaje de Chihiro)",
        "character": "ハク (Haku)",
        "category": "スタジオジブリ",
        "spanish": "Una vez que conoces a alguien, nunca lo olvidas realmente.",
        "reading": "ウナ ベス ケ コノセス ア アルギエン, ヌンカ ロ オルビダス レアルメンテ",
        "japanese": "一度出会った者は、決して本当には忘れないものだよ（思い出せないだけで）。",
        "breakdown": "<b>Una vez que</b>(一度〜したら) + <b>conoces a alguien</b>(誰かと知り合う) + <b>nunca</b>(決して〜ない) + <b>lo olvidas</b>(彼を忘れる) + <b>realmente</b>(本当に)",
        "grammar_point": "<b>【接続詞 Una vez que & 人の目的語 a】</b><br>・<b>conocer a alguien</b>: 「人」を目的語に取る場合、前置詞 <b>a</b> が必須（Personal 'a'）。<br>・<b>lo olvidas</b>: 「彼を忘れる」の直接目的語代名詞 lo。"
    },
    {
        "work": "ドラゴンボールZ (Dragon Ball Z)",
        "character": "孫悟空 (Goku)",
        "category": "大人気アニメ",
        "spanish": "¡Hola, soy Goku! ¡Vamos a luchar con todas nuestras fuerzas!",
        "reading": "オラ, ソイ ゴク! バモス ア ルチャール コン トダス ヌエストラス フエルサス!",
        "japanese": "オッス、オラ悟空！オラたちの全力を尽くして戦おうぜ！",
        "breakdown": "<b>Hola, soy Goku</b>(やあ、悟空だ) + <b>Vamos a luchar</b>(戦おう [勧誘]) + <b>con todas nuestras fuerzas</b>(私たちのすべての力で)",
        "grammar_point": "<b>【vamos a + 原形 (勧誘) & 所有形容詞】</b><br>・<b>Vamos a + 原形</b>: 「〜しよう！（Let's）」の定番表現。<br>・<b>nuestras fuerzas</b>: 「私たちの力」（所有形容詞 nuestro は修飾する名詞 fuerza [女性複数] に一致して <b>nuestras</b> になる）。"
    },
    {
        "work": "進撃の巨人 (Attack on Titan)",
        "character": "エレン・イェーガー (Eren Jaeger)",
        "category": "大人気アニメ",
        "spanish": "Si no luchas, no puedes ganar. ¡Lucha!",
        "reading": "シ ノ ルチャス, ノ プエデス ガナール. ルチャ!",
        "japanese": "戦わなければ勝てない。戦え！",
        "breakdown": "<b>Si no luchas</b>(もし戦わないなら) + <b>no puedes ganar</b>(勝つことはできない) + <b>¡Lucha!</b>(戦え！ [命令])",
        "grammar_point": "<b>【条件節 Si + 直説法現在 & 肯定命令】</b><br>・<b>Si + 直説法現在</b>: 「もし〜ならば（現実的な条件）」。<br>・<b>¡Lucha!</b>: 動詞 luchar の tú に対する肯定命令形（-ar動詞の命令は語尾 -a）。"
    },
    {
        "work": "NARUTO (ナルト)",
        "character": "うずまきナルト (Naruto)",
        "category": "大人気アニメ",
        "spanish": "¡Nunca me retracto de mis palabras! ¡Ese es mi camino ninja!",
        "reading": "ヌンカ メ レトラクト デ ミス パラブラス! エセ エス ミ カミノ ニンジャ!",
        "japanese": "まっすぐ自分の言葉は曲げねぇ！それがオレの忍道だ！",
        "breakdown": "<b>Nunca</b>(決して〜ない) + <b>me retracto de</b>(前言を撤回する/曲げる [再帰]) + <b>mis palabras</b>(私の言葉) + <b>Ese es</b>(それが〜だ) + <b>mi camino ninja</b>(私の忍道/道)",
        "grammar_point": "<b>【再帰動詞 retractarse de & 指示代名詞 ese】</b><br>・<b>retractarse de</b>: 「前言を撤回する、取り消す」という再帰動詞（Yo me retracto）。<br>・<b>Ese es</b>: 「それが〜だ」（中距離の指示代名詞 ese）。"
    }
]
