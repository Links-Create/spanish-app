# -*- coding: utf-8 -*-
"""
スペイン語 重要単語マスター データベース (221語)
全6人称活用 (Yo, Tú, Él/Ud, Nosotros, Vosotros, Ellos/Uds) ＆ 性数変化データ付き
"""

DICTIONARY_DATA = [
    # ==========================================
    # 1. 最重要基本動詞 (46語) - 全6人称活用付き
    # ==========================================
    ("tener", "テネール", "不規則動詞 [動]", 
     "① （物・人を）持っている、所有している<br>② （年齢が）〜歳である<br>③ （空腹・眠気などの感覚を）感じる<br>④ 【tener que + 原形】〜しなければならない<br>⑤ 【tener ganas de + 原形】〜したい", 
     "・<b>Tengo un coche nuevo.</b>（新しい車を持っています）<br>・<b>¿Cuántos años tienes? - Tengo 20 años.</b>（何歳ですか？ - 20歳です）<br>・<b>Tengo que estudiar hoy.</b>（今日は勉強しなければなりません）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo (私): <b>tengo</b> (テンゴ)<br>・Tú (君): <b>tienes</b> (ティエネス)<br>・Él/Ella/Ud (彼/彼女/あなた): <b>tiene</b> (ティエネ)<br>・Nosotros (私たち): <b>tenemos</b> (テネモス)<br>・Vosotros (君たち): <b>tenéis</b> (テネイス)<br>・Ellos/Uds (彼ら/あなた方): <b>tienen</b> (ティエネン)"),

    ("ser", "セール", "不規則動詞 [動]", 
     "① （本質・国籍・職業が）〜である<br>② （時刻・日付が）〜である<br>③ （素材・所属が）〜のものである<br>④ （イベントが）開催される", 
     "・<b>Yo soy japonés y soy estudiante.</b>（私は日本人で学生です）<br>・<b>Son las tres de la tarde.</b>（午後3時です）<br>・<b>Este reloj es de oro.</b>（この時計は金製です）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>soy</b> (ソイ)<br>・Tú: <b>eres</b> (エレス)<br>・Él/Ella/Ud: <b>es</b> (エス)<br>・Nosotros: <b>somos</b> (ソモス)<br>・Vosotros: <b>sois</b> (ソイス)<br>・Ellos/Uds: <b>son</b> (ソン)"),

    ("estar", "エスタール", "不規則動詞 [動]", 
     "① （一時的な状態・体調が）〜である<br>② （人・物が）〜にいる、ある（所在）<br>③ 【estar + 現在分詞】〜している最中だ<br>④ 【estar de acuerdo】賛成である", 
     "・<b>¿Cómo estás? - Estoy muy bien.</b>（元気？ - とても元気です）<br>・<b>¿Dónde está la estación?</b>（駅はどこですか？）<br>・<b>Estoy estudiando español.</b>（スペイン語を勉強しています）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>estoy</b> (エストイ)<br>・Tú: <b>estás</b> (エスタス)<br>・Él/Ella/Ud: <b>está</b> (エスタ)<br>・Nosotros: <b>estamos</b> (エスタモス)<br>・Vosotros: <b>estáis</b> (エスタイス)<br>・Ellos/Uds: <b>están</b> (エスタン)"),

    ("hacer", "アセール", "不規則動詞 [動]", 
     "① （物を）作る、製作する<br>② （行動・仕事を）する、行う<br>③ （天気が）〜である<br>④ 【hace + 時間】〜前", 
     "・<b>Hago la cena todos los días.</b>（毎日夕食を作ります）<br>・<b>Hoy hace muy buen tiempo.</b>（今日はとてもいい天気です）<br>・<b>Llegué hace dos días.</b>（2日前に到着しました）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>hago</b> (アゴ)<br>・Tú: <b>haces</b> (アセス)<br>・Él/Ella/Ud: <b>hace</b> (アセ)<br>・Nosotros: <b>hacemos</b> (アセモス)<br>・Vosotros: <b>hacéis</b> (アセイス)<br>・Ellos/Uds: <b>hacen</b> (アセン)"),

    ("ir", "イール", "不規則動詞 [動]", 
     "① （場所へ）行く、向かう（a 〜）<br>② 【ir a + 原形】〜する予定だ（近接未来）<br>③ （物事が）進む、うまくいく<br>④ 【irse】立ち去る、帰る", 
     "・<b>Voy al supermercado en metro.</b>（地下鉄でスーパーに行きます）<br>・<b>Mañana voy a viajar.</b>（明日旅行する予定です）<br>・<b>¡Ya me voy! ¡Hasta luego!</b>（もう行くね！またね！）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>voy</b> (ボイ)<br>・Tú: <b>vas</b> (バス)<br>・Él/Ella/Ud: <b>va</b> (バ)<br>・Nosotros: <b>vamos</b> (バモス)<br>・Vosotros: <b>vais</b> (バイス)<br>・Ellos/Uds: <b>van</b> (バン)"),

    ("poder", "ポデール", "不規則動詞 [動]", 
     "① （能力・状況的に）〜できる<br>② （許可）〜してもよい<br>③ （依頼）〜してくれますか？", 
     "・<b>Puedo hablar un poco de español.</b>（スペイン語が少し話せます）<br>・<b>¿Puedo pagar con tarjeta?</b>（カードで払えますか？）<br>・<b>¿Puedes ayudarme?</b>（手伝ってくれますか？）", "基本動詞",
     "<b>【現在形 6人称変化 (o➔ue)】</b><br>・Yo: <b>puedo</b> (プエド)<br>・Tú: <b>puedes</b> (プエデス)<br>・Él/Ella/Ud: <b>puede</b> (プエデ)<br>・Nosotros: <b>podemos</b> (ポデモス)<br>・Vosotros: <b>podéis</b> (ポデイス)<br>・Ellos/Uds: <b>pueden</b> (プエデン)"),

    ("querer", "ケレール", "不規則動詞 [動]", 
     "① （物が）欲しい<br>② （〜することを）欲する、〜したい<br>③ （人を）愛している、好いている", 
     "・<b>Quiero un café con leche, por favor.</b>（カフェラテを1つください）<br>・<b>Quiero aprender más.</b>（もっと学びたいです）<br>・<b>Te quiero mucho.</b>（君のことが大好きです）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>quiero</b> (キエロ)<br>・Tú: <b>quieres</b> (キエレス)<br>・Él/Ella/Ud: <b>quiere</b> (キエレ)<br>・Nosotros: <b>queremos</b> (ケレモス)<br>・Vosotros: <b>queréis</b> (ケレイス)<br>・Ellos/Uds: <b>quieren</b> (キエレン)"),

    ("saber", "サベール", "不規則動詞 [動]", 
     "① （情報・知識・事実を）知っている<br>② 【saber + 原形】（技術として）〜できる<br>③ （味が）〜の味がする", 
     "・<b>No sé la respuesta.</b>（答えを知りません）<br>・<b>¿Sabes nadar?</b>（泳げますか？）<br>・<b>Este plato sabe muy rico.</b>（この料理はとても美味しいです）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>sé</b> (セ)<br>・Tú: <b>sabes</b> (サベス)<br>・Él/Ella/Ud: <b>sabe</b> (サベ)<br>・Nosotros: <b>sabemos</b> (サベモス)<br>・Vosotros: <b>sabéis</b> (サベイス)<br>・Ellos/Uds: <b>saben</b> (サベン)"),

    ("conocer", "コノセール", "不規則動詞 [動]", 
     "① （人・場所・街を）知っている、経験として知る<br>② （人と）知り合う、面識ができる", 
     "・<b>¿Conoces a María? - Sí, la conozco.</b>（マリアさんを知ってる？ - ええ、知っています）<br>・<b>No conozco Madrid todavía.</b>（まだマドリードに行ったことがありません）", "基本動詞",
     "<b>【現在形 6人称変化 (yo不規則)】</b><br>・Yo: <b>conozco</b> (コノスコ)<br>・Tú: <b>conoces</b> (コノセス)<br>・Él/Ella/Ud: <b>conoce</b> (コノセ)<br>・Nosotros: <b>conocemos</b> (コノセモス)<br>・Vosotros: <b>conocéis</b> (コノセイス)<br>・Ellos/Uds: <b>conocen</b> (コノセン)"),

    ("dar", "ダール", "不規則動詞 [動]", 
     "① （人に物を）与える、あげる、渡す<br>② 【dar un paseo】散歩する<br>③ 【dar las gracias】お礼を言う", 
     "・<b>Te doy mi número de teléfono.</b>（私の電話番号を教えるよ）<br>・<b>Vamos a dar un paseo.</b>（散歩に行きましょう）<br>・<b>Le di las gracias por su ayuda.</b>（助けてくれたことに感謝しました）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>doy</b> (ドイ)<br>・Tú: <b>das</b> (ダス)<br>・Él/Ella/Ud: <b>da</b> (ダ)<br>・Nosotros: <b>damos</b> (ダモス)<br>・Vosotros: <b>dais</b> (ダイス)<br>・Ellos/Uds: <b>dan</b> (ダン)"),

    ("decir", "デシール", "不規則動詞 [動]", 
     "① （言葉・意見を）言う、話す<br>② 【es decir】つまり、すなわち<br>③ 【¿Cómo se dice...?】〜は何と言いますか？", 
     "・<b>Dime la verdad.</b>（私に本当のことを言って）<br>・<b>¿Cómo se dice esto en español?</b>（これはスペイン語で何と言いますか？）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔i / yo:digo)】</b><br>・Yo: <b>digo</b> (ディゴ)<br>・Tú: <b>dices</b> (ディセス)<br>・Él/Ella/Ud: <b>dice</b> (ディセ)<br>・Nosotros: <b>decimos</b> (デシモス)<br>・Vosotros: <b>decís</b> (デシス)<br>・Ellos/Uds: <b>dicen</b> (ディセン)"),

    ("ver", "ベエール", "不規則動詞 [動]", 
     "① （目で）見る、眺める、見学する<br>② （人に）会う<br>③ 【¡Nos vemos!】また会おう！", 
     "・<b>Veo la televisión por la noche.</b>（夜にテレビを見ます）<br>・<b>Mañana veo a mi amigo.</b>（明日友達に会います）<br>・<b>¡Nos vemos pronto!</b>（また近いうちに会おうね！）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>veo</b> (ベオ)<br>・Tú: <b>ves</b> (ベス)<br>・Él/Ella/Ud: <b>ve</b> (ベ)<br>・Nosotros: <b>vemos</b> (ベモス)<br>・Vosotros: <b>veis</b> (ベイス)<br>・Ellos/Uds: <b>ven</b> (ベン)"),

    ("venir", "ベニール", "不規則動詞 [動]", 
     "① （こちらへ）来る<br>② （出身が）〜から来ている（de 〜）", 
     "・<b>¿Vienes a la fiesta hoy?</b>（今日のパーティーに来る？）<br>・<b>Vengo de Japón.</b>（私は日本から来ました）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie / yo:vengo)】</b><br>・Yo: <b>vengo</b> (ベンゴ)<br>・Tú: <b>vienes</b> (ビエネス)<br>・Él/Ella/Ud: <b>viene</b> (ビエネ)<br>・Nosotros: <b>venimos</b> (ベニモス)<br>・Vosotros: <b>venís</b> (ベニス)<br>・Ellos/Uds: <b>vienen</b> (ビエネン)"),

    ("poner", "ポネール", "不規則動詞 [動]", 
     "① （物を場所に）置く、設置する<br>② （スイッチを）つける<br>③ 【ponerse】（服を）着る、（感情に）なる", 
     "・<b>Pongo el libro en la mesa.</b>（本を机の上に置きます）<br>・<b>Me pongo el abrigo.</b>（コートを着ます）<br>・<b>Se puso muy contento.</b>（彼はとても嬉しくなりました）", "基本動詞",
     "<b>【現在形 6人称変化 (yo:pongo)】</b><br>・Yo: <b>pongo</b> (ポンゴ)<br>・Tú: <b>pones</b> (ポネス)<br>・Él/Ella/Ud: <b>pone</b> (ポネ)<br>・Nosotros: <b>ponemos</b> (ポネモス)<br>・Vosotros: <b>ponéis</b> (ポネイス)<br>・Ellos/Uds: <b>ponen</b> (ポネン)"),

    ("salir", "サリール", "不規則動詞 [動]", 
     "① （場所から）出る、出発する<br>② （友人と）出かける、遊びに行く<br>③ （太陽・月が）出る", 
     "・<b>El tren sale a las ocho.</b>（電車は8時に出発します）<br>・<b>Salgo con mis amigos los fines de semana.</b>（週末は友達と出かけます）", "基本動詞",
     "<b>【現在形 6人称変化 (yo:salgo)】</b><br>・Yo: <b>salgo</b> (サルゴ)<br>・Tú: <b>sales</b> (サレス)<br>・Él/Ella/Ud: <b>sale</b> (サレ)<br>・Nosotros: <b>salimos</b> (サリモス)<br>・Vosotros: <b>salís</b> (サリス)<br>・Ellos/Uds: <b>salen</b> (サレン)"),

    ("traer", "トラエール", "不規則動詞 [動]", 
     "① （物をこちらに）持ってくる<br>② （人を連れて）連れてくる", 
     "・<b>¿Puedes traerme la cuenta, por favor?</b>（お会計を持ってきてくれますか？）<br>・<b>Traigo un regalo para ti.</b>（君にプレゼントを持ってきたよ）", "基本動詞",
     "<b>【現在形 6人称変化 (yo:traigo)】</b><br>・Yo: <b>traigo</b> (トライゴ)<br>・Tú: <b>traes</b> (トラエス)<br>・Él/Ella/Ud: <b>trae</b> (トラエ)<br>・Nosotros: <b>traemos</b> (トラエモス)<br>・Vosotros: <b>traéis</b> (トラエイス)<br>・Ellos/Uds: <b>traen</b> (トラエン)"),

    ("llevar", "ジェバール", "規則動詞 [動]", 
     "① （物をあちらへ）持っていく、運ぶ<br>② （服・靴・メガネを）身につけている<br>③ （時間を）〜過ごしている", 
     "・<b>Llevo una camisa blanca.</b>（白いシャツを着ています）<br>・<b>Llevo tres años viviendo en España.</b>（スペインに住んで3年になります）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>llevo</b> (ジェボ)<br>・Tú: <b>llevas</b> (ジェバス)<br>・Él/Ella/Ud: <b>lleva</b> (ジェバ)<br>・Nosotros: <b>llevamos</b> (ジェバモス)<br>・Vosotros: <b>lleváis</b> (ジェバイス)<br>・Ellos/Uds: <b>llevan</b> (ジェバン)"),

    ("hablar", "アブラール", "規則動詞 [動]", 
     "① （言語を）話す<br>② （人と）会話する（con 〜）", 
     "・<b>Hablo español e inglés.</b>（スペイン語と英語を話します）<br>・<b>Quiero hablar contigo.</b>（君と話がしたいです）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>hablo</b> (アブロ)<br>・Tú: <b>hablas</b> (アブラス)<br>・Él/Ella/Ud: <b>habla</b> (アブラ)<br>・Nosotros: <b>hablamos</b> (アブラモス)<br>・Vosotros: <b>habláis</b> (アブライス)<br>・Ellos/Uds: <b>hablan</b> (アブラン)"),

    ("comer", "コメール", "規則動詞 [動]", 
     "① （食事を）食べる<br>② （昼食を）とる", 
     "・<b>Como paella todos los domingos.</b>（毎週日曜日にパエリアを食べます）<br>・<b>¿A qué hora comemos?</b>（何時に昼食にする？）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>como</b> (コモ)<br>・Tú: <b>comes</b> (コメス)<br>・Él/Ella/Ud: <b>come</b> (コメ)<br>・Nosotros: <b>comemos</b> (コメモス)<br>・Vosotros: <b>coméis</b> (コメイス)<br>・Ellos/Uds: <b>comen</b> (コメン)"),

    ("vivir", "ビビール", "規則動詞 [動]", 
     "① （場所に）住む、暮らす<br>② 生きる、生活する", 
     "・<b>Vivo en Tokio con mi familia.</b>（家族と東京に住んでいます）<br>・<b>Hay que vivir el momento.</b>（今を生きなければならない）", "基本動詞",
     "<b>【現在形 6人称変化 (-ir規則)】</b><br>・Yo: <b>vivo</b> (ビボ)<br>・Tú: <b>vives</b> (ビベス)<br>・Él/Ella/Ud: <b>vive</b> (ビベ)<br>・Nosotros: <b>vivimos</b> (ビビモス)<br>・Vosotros: <b>vivís</b> (ビビス)<br>・Ellos/Uds: <b>viven</b> (ビベン)"),

    ("beber", "ベベール", "規則動詞 [動]", 
     "① （飲み物を）飲む<br>② （お酒を）飲む", 
     "・<b>Bebo mucha agua todos los días.</b>（毎日たくさん水を飲みます）<br>・<b>¿Qué quieres beber?</b>（何を飲みたいですか？）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>bebo</b> (ベボ)<br>・Tú: <b>bebes</b> (ベベス)<br>・Él/Ella/Ud: <b>bebe</b> (ベベ)<br>・Nosotros: <b>bebemos</b> (ベベモス)<br>・Vosotros: <b>bebéis</b> (ベベイス)<br>・Ellos/Uds: <b>beben</b> (ベベン)"),

    ("escribir", "エスクリビール", "規則動詞 [動]", 
     "① （文字・文章を）書く<br>② （手紙・メッセージを）送る", 
     "・<b>Escribo un correo a mi profesor.</b>（先生にメールを書きます）<br>・<b>Escribe tu nombre aquí, por favor.</b>（ここに名前を書いてください）", "基本動詞",
     "<b>【現在形 6人称変化 (-ir規則)】</b><br>・Yo: <b>escribo</b> (エスクリボ)<br>・Tú: <b>escribes</b> (エスクリベス)<br>・Él/Ella/Ud: <b>escribe</b> (エスクリベ)<br>・Nosotros: <b>escribimos</b> (エスクリビモス)<br>・Vosotros: <b>escribís</b> (エスクリビス)<br>・Ellos/Uds: <b>escriben</b> (エスクリベン)"),

    ("leer", "レエール", "規則動詞 [動]", 
     "① （本・新聞などを）読む", 
     "・<b>Leo el periódico todas las mañanas.</b>（毎朝新聞を読みます）<br>・<b>Me gusta leer novelas.</b>（小説を読むのが好きです）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>leo</b> (レオ)<br>・Tú: <b>lees</b> (レエス)<br>・Él/Ella/Ud: <b>lee</b> (レエ)<br>・Nosotros: <b>leemos</b> (レエモス)<br>・Vosotros: <b>leéis</b> (レエイス)<br>・Ellos/Uds: <b>leen</b> (レエン)"),

    ("escuchar", "エスクチャール", "規則動詞 [動]", 
     "① （音・音楽を意識して）聴く、耳を傾ける", 
     "・<b>Escucho música latina mientras cocino.</b>（料理をしながらラテン音楽を聴きます）<br>・<b>¡Escúchame, por favor!</b>（私の話を聞いてください！）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>escucho</b> (エスクチョ)<br>・Tú: <b>escuchas</b> (エスクチャス)<br>・Él/Ella/Ud: <b>escucha</b> (エスクチャ)<br>・Nosotros: <b>escuchamos</b> (エスクチャモス)<br>・Vosotros: <b>escucháis</b> (エスクチャイス)<br>・Ellos/Uds: <b>escuchan</b> (エスクチャン)"),

    ("oír", "オイール", "不規則動詞 [動]", 
     "① （自然に音が耳に）聞こえる", 
     "・<b>No te oigo bien, ¿puedes repetir?</b>（よく聞こえません、もう一度言ってくれますか？）", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>oigo</b> (オイゴ)<br>・Tú: <b>oyes</b> (オジェス)<br>・Él/Ella/Ud: <b>oye</b> (オジェ)<br>・Nosotros: <b>oímos</b> (オイモス)<br>・Vosotros: <b>oís</b> (オイス)<br>・Ellos/Uds: <b>oyen</b> (オジェン)"),

    ("abrir", "アブリール", "規則動詞 [動]", 
     "① （ドア・窓・本などを）開ける、開く<br>② （店が）開店する", 
     "・<b>¿Puedes abrir la ventana?</b>（窓を開けてくれますか？）<br>・<b>La tienda abre a las diez.</b>（店は10時に開きます）", "基本動詞",
     "<b>【現在形 6人称変化 (-ir規則)】</b><br>・Yo: <b>abro</b> (アブロ)<br>・Tú: <b>abres</b> (アブレス)<br>・Él/Ella/Ud: <b>abre</b> (アブレ)<br>・Nosotros: <b>abrimos</b> (アブリモス)<br>・Vosotros: <b>abrís</b> (アブリス)<br>・Ellos/Uds: <b>abren</b> (アブレン)"),

    ("cerrar", "セラール", "不規則動詞 [動]", 
     "① （ドア・店などを）閉める、閉じる", 
     "・<b>Cierra la puerta, por favor.</b>（ドアを閉めてください）<br>・<b>El banco cierra a las dos.</b>（銀行は2時に閉まります）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>cierro</b> (シエロ)<br>・Tú: <b>cierras</b> (シエラス)<br>・Él/Ella/Ud: <b>cierra</b> (シエラ)<br>・Nosotros: <b>cerramos</b> (セラモス)<br>・Vosotros: <b>cerráis</b> (セライス)<br>・Ellos/Uds: <b>cierran</b> (シエラン)"),

    ("comprar", "コンプラール", "規則動詞 [動]", 
     "① （物を）買う、購入する", 
     "・<b>Compré un regalo para ti.</b>（君にプレゼントを買いました）<br>・<b>Voy a comprar comida.</b>（買い出しに行きます）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>compro</b> (コンプロ)<br>・Tú: <b>compras</b> (コンプラス)<br>・Él/Ella/Ud: <b>compra</b> (コンプラ)<br>・Nosotros: <b>compramos</b> (コンプラモス)<br>・Vosotros: <b>compráis</b> (コンプライス)<br>・Ellos/Uds: <b>compran</b> (コンプラン)"),

    ("vender", "ベンデール", "規則動詞 [動]", 
     "① （物を）売る、販売する", 
     "・<b>Ellos venden frutas frescas en el mercado.</b>（彼らは市場で新鮮な果物を売っています）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>vendo</b> (ベンド)<br>・Tú: <b>vendes</b> (ベンデス)<br>・Él/Ella/Ud: <b>vende</b> (ベンデ)<br>・Nosotros: <b>vendemos</b> (ベンデモス)<br>・Vosotros: <b>vendéis</b> (ベンデイス)<br>・Ellos/Uds: <b>venden</b> (ベンデン)"),

    ("pagar", "パガール", "規則動詞 [動]", 
     "① （代金を）支払う、払う", 
     "・<b>¿Cómo quieres pagar? - En efectivo.</b>（お支払い方法は？ - 現金で）<br>・<b>Yo pago la cuenta hoy.</b>（今日は私がおごります）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>pago</b> (パゴ)<br>・Tú: <b>pagas</b> (パガス)<br>・Él/Ella/Ud: <b>paga</b> (パガ)<br>・Nosotros: <b>pagamos</b> (パガモス)<br>・Vosotros: <b>pagáis</b> (パガイス)<br>・Ellos/Uds: <b>pagan</b> (パガン)"),

    ("pedir", "ペディール", "不規則動詞 [動]", 
     "① （料理などを）注文する、頼む<br>② （手助け・許可を）求める、お願いする", 
     "・<b>Voy a pedir una pizza.</b>（ピザを注文します）<br>・<b>Quiero pedirte un favor.</b>（君にお願いがあるんだ）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔i)】</b><br>・Yo: <b>pido</b> (ピド)<br>・Tú: <b>pides</b> (ピデス)<br>・Él/Ella/Ud: <b>pide</b> (ピデ)<br>・Nosotros: <b>pedimos</b> (ペディモス)<br>・Vosotros: <b>pedís</b> (ペディス)<br>・Ellos/Uds: <b>piden</b> (ピデン)"),

    ("preguntar", "プレグンタール", "規則動詞 [動]", 
     "① （人に質問を）尋ねる、質問する", 
     "・<b>Le pregunté la hora a un policía.</b>（警察官に時間を尋ねました）<br>・<b>¿Puedo preguntarte algo?</b>（ちょっと聞いてもいい？）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>pregunto</b> (プレグント)<br>・Tú: <b>preguntas</b> (プレグンタス)<br>・Él/Ella/Ud: <b>pregunta</b> (プレグンタ)<br>・Nosotros: <b>preguntamos</b> (プレグンタモス)<br>・Vosotros: <b>preguntáis</b> (プレグンタイス)<br>・Ellos/Uds: <b>preguntan</b> (プレグンタン)"),

    ("responder", "レスポンデール", "規則動詞 [動]", 
     "① （質問・手紙に）答える、返事をする", 
     "・<b>Él no me respondió el mensaje.</b>（彼はメッセージに返信してくれませんでした）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>respondo</b> (レスポンド)<br>・Tú: <b>respondes</b> (レスポンデス)<br>・Él/Ella/Ud: <b>responde</b> (レスポンデ)<br>・Nosotros: <b>respondemos</b> (レスポンデモス)<br>・Vosotros: <b>respondéis</b> (レスポンデイス)<br>・Ellos/Uds: <b>responden</b> (レスポンデン)"),

    ("buscar", "ブスカール", "規則動詞 [動]", 
     "① （人・物を）探す、検索する", 
     "・<b>Estoy buscando mis gafas.</b>（メガネを探しています）<br>・<b>Busco un hotel barato cerca del centro.</b>（中心部近くの安いホテルを探しています）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>busco</b> (ブスコ)<br>・Tú: <b>buscas</b> (ブスカス)<br>・Él/Ella/Ud: <b>busca</b> (ブスカ)<br>・Nosotros: <b>buscamos</b> (ブスカモス)<br>・Vosotros: <b>buscáis</b> (ブスカイス)<br>・Ellos/Uds: <b>buscan</b> (ブスカン)"),

    ("encontrar", "エンコントラール", "不規則動詞 [動]", 
     "① （探していた物を）見つける、発見する<br>② （人と偶然）出会う<br>③ 【encontrarse】〜な気分である", 
     "・<b>¡Por fin encontré mis llaves!</b>（やっと鍵を見つけた！）<br>・<b>Me encuentro muy bien hoy.</b>（今日はとても気分が良いです）", "基本動詞",
     "<b>【現在形 6人称変化 (o➔ue)】</b><br>・Yo: <b>encuentro</b> (エンクエントロ)<br>・Tú: <b>encuentras</b> (エンクエントラス)<br>・Él/Ella/Ud: <b>encuentra</b> (エンクエントラ)<br>・Nosotros: <b>encontramos</b> (エンコントラモス)<br>・Vosotros: <b>encontráis</b> (エンコントライス)<br>・Ellos/Uds: <b>encuentran</b> (エンクエントラン)"),

    ("pensar", "ペンサール", "不規則動詞 [動]", 
     "① （頭で）考える、思う<br>② 【pensar + 原形】〜するつもりである", 
     "・<b>¿Qué piensas de este plan?</b>（この計画についてどう思う？）<br>・<b>Pienso viajar a España este verano.</b>（今年の夏スペインに旅行するつもりです）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>pienso</b> (ピエンソ)<br>・Tú: <b>piensas</b> (ピエンサス)<br>・Él/Ella/Ud: <b>piensa</b> (ピエンサ)<br>・Nosotros: <b>pensamos</b> (ペンサモス)<br>・Vosotros: <b>pensáis</b> (ペンサイス)<br>・Ellos/Uds: <b>piensan</b> (ピエンサン)"),

    ("creer", "クレエール", "規則動詞 [動]", 
     "① （〜だと）信じる、思う<br>② （宗教などを）信じる", 
     "・<b>Creo que sí. / Creo que no.</b>（そう思います / そうは思いません）<br>・<b>No creo que sea verdad.</b>（本当だとは思いません）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>creo</b> (クレオ)<br>・Tú: <b>crees</b> (クレエス)<br>・Él/Ella/Ud: <b>cree</b> (クレエ)<br>・Nosotros: <b>creemos</b> (クレエモス)<br>・Vosotros: <b>creéis</b> (クレエイス)<br>・Ellos/Uds: <b>creen</b> (クレエン)"),

    ("entender", "エンテンデール", "不規則動詞 [動]", 
     "① （言葉・意味・理由を）理解する、わかる", 
     "・<b>¿Entiendes lo que digo? - Sí, entiendo.</b>（私の言うことがわかる？ - ええ、わかります）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>entiendo</b> (エンティエンド)<br>・Tú: <b>entiendes</b> (エンティエンデス)<br>・Él/Ella/Ud: <b>entiende</b> (エンティエンデ)<br>・Nosotros: <b>entendemos</b> (エンテンデモス)<br>・Vosotros: <b>entendéis</b> (エンテンデイス)<br>・Ellos/Uds: <b>entienden</b> (エンティエンデン)"),

    ("comprender", "コンプレンデール", "規則動詞 [動]", 
     "① （深く本質を）理解する、把握する", 
     "・<b>Comprendo tu situación perfectamente.</b>（君の状況は痛いほどよく分かります）", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>comprendo</b> (コンプレンド)<br>・Tú: <b>comprendes</b> (コンプレンデス)<br>・Él/Ella/Ud: <b>comprende</b> (コンプレンデ)<br>・Nosotros: <b>comprendemos</b> (コンプレンデモス)<br>・Vosotros: <b>comprendéis</b> (コンプレンデイス)<br>・Ellos/Uds: <b>comprenden</b> (コンプレンデン)"),

    ("ayudar", "アユダール", "規則動詞 [動]", 
     "① （人を）手伝う、助ける、援助する", 
     "・<b>¿Puedes ayudarme con esta maleta?</b>（このスーツケースを運ぶのを手伝ってくれますか？）<br>・<b>¡Ayuda, por favor!</b>（助けてください！）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>ayudo</b> (アユド)<br>・Tú: <b>ayudas</b> (アユダス)<br>・Él/Ella/Ud: <b>ayuda</b> (アユダ)<br>・Nosotros: <b>ayudamos</b> (アユダモス)<br>・Vosotros: <b>ayudáis</b> (アユダイス)<br>・Ellos/Uds: <b>ayudan</b> (アユダン)"),

    ("necesitar", "ネセシタール", "規則動詞 [動]", 
     "① （物・人を）必要とする<br>② 【necesitar + 原形】〜する必要がある", 
     "・<b>Necesito descansar un poco.</b>（少し休む必要があります）<br>・<b>Necesito tu ayuda.</b>（君の助けが必要です）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>necesito</b> (ネセシト)<br>・Tú: <b>necesitas</b> (ネセシタス)<br>・Él/Ella/Ud: <b>necesita</b> (ネセシタ)<br>・Nosotros: <b>necesitamos</b> (ネセシタモス)<br>・Vosotros: <b>necesitáis</b> (ネセシタイス)<br>・Ellos/Uds: <b>necesitan</b> (ネセシタン)"),

    ("esperar", "エスペラール", "規則動詞 [動]", 
     "① （人を）待つ<br>② （希望して）期待する、願う", 
     "・<b>Espérame un momento, por favor.</b>（ちょっと待ってください）<br>・<b>Espero que tengas un buen día.</b>（良い一日になりますように）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>espero</b> (エスペロ)<br>・Tú: <b>esperas</b> (エスペラス)<br>・Él/Ella/Ud: <b>espera</b> (エスペラ)<br>・Nosotros: <b>esperamos</b> (エスペラモス)<br>・Vosotros: <b>esperáis</b> (エスペライス)<br>・Ellos/Uds: <b>esperan</b> (エスペラン)"),

    ("empezar", "エンペサール", "不規則動詞 [動]", 
     "① （活動・仕事が）始まる、始める（a + 原形）", 
     "・<b>La película empieza a las siete.</b>（映画は7時に始まります）<br>・<b>Empiezo a estudiar ahora.</b>（今から勉強を始めます）", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>empiezo</b> (エンピエソ)<br>・Tú: <b>empiezas</b> (エンピエサス)<br>・Él/Ella/Ud: <b>empieza</b> (エンピエサ)<br>・Nosotros: <b>empezamos</b> (エンペサモス)<br>・Vosotros: <b>empezáis</b> (エンペサイス)<br>・Ellos/Uds: <b>empiezan</b> (エンピエサン)"),

    ("terminar", "テルミナール", "規則動詞 [動]", 
     "① （仕事・授業を）終える、終わる（de + 原形）", 
     "・<b>Terminé mi trabajo a las seis.</b>（6時に仕事を終えました）<br>・<b>La clase termina pronto.</b>（授業はもうすぐ終わります）", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>termino</b> (テルミノ)<br>・Tú: <b>terminas</b> (テルミナス)<br>・Él/Ella/Ud: <b>termina</b> (テルミナ)<br>・Nosotros: <b>terminamos</b> (テルミナモス)<br>・Vosotros: <b>termináis</b> (テルミナイス)<br>・Ellos/Uds: <b>terminan</b> (テルミナン)"),

    ("gustar", "グスタール", "規則動詞 [動]", 
     "① （物・事が人に）好まれる、好きだ", 
     "・<b>Me gusta mucho la comida española.</b>（スペイン料理が大好きです）<br>・<b>¿Te gusta la música clásica?</b>（クラシック音楽は好き？）", "基本動詞",
     "<b>【gustar型 活用】</b><br>・単数/動詞原形が主語: <b>gusta</b> (グスタ)<br>・複数が主語: <b>gustan</b> (グスタン)<br>※(A mí) me gusta, (A ti) te gusta, (A él) le gusta..."),

    ("encantar", "エンカンタール", "規則動詞 [動]", 
     "① （物・事が人に）大〜好きだ、たまらなく好きだ", 
     "・<b>¡Me encanta viajar por el mundo!</b>（世界中を旅するのが大好きです！）", "基本動詞",
     "<b>【gustar型 活用】</b><br>・単数/動詞原形が主語: <b>encanta</b> (エンカンタ)<br>・複数が主語: <b>encantan</b> (エンカンタン)"),

    # ==========================================
    # 2. 日常・生活・家庭名詞 (42語)
    # ==========================================
    ("casa", "カサ", "女性名詞 [女]", "① 家、我が家、住まい<br>② 【en casa】家で<br>③ 【a casa】家へ（帰宅）", "・<b>Estoy en casa descansando.</b>（家で休んでいます）<br>・<b>Vamos a casa.</b>（家に帰ろう）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la casa</b> / 複数: <b>las casas</b>"),
    ("tiempo", "ティエンポ", "男性名詞 [男]", "① 時間、暇<br>② 天気、気候<br>③ 【a tiempo】時間通りに", "・<b>No tengo mucho tiempo.</b>（あまり時間がありません）<br>・<b>Hace buen tiempo.</b>（いい天気です）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el tiempo</b> / 複数: <b>los tiempos</b>"),
    ("día", "ディア", "男性名詞 [男 ※語尾-aだが男性]", "① 日、1日、昼間<br>② 【buenos días】おはよう<br>③ 【todos los días】毎日", "・<b>¡Buenos días!</b>（おはようございます！）<br>・<b>Estudio todos los días.</b>（毎日勉強します）", "日常・生活", "<b>【性数変化】</b> 男性名詞: <b>el día</b> / 複数: <b>los días</b>"),
    ("noche", "ノチェ", "女性名詞 [女]", "① 夜<br>② 【buenas noches】こんばんは、おやすみ<br>③ 【esta noche】今夜", "・<b>¡Buenas noches!</b>（おやすみなさい！）<br>・<b>Salgo esta noche.</b>（今夜出かけます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la noche</b> / 複数: <b>las noches</b>"),
    ("tarde", "タルデ", "女性名詞 [女]", "① 午後、夕方<br>② 【buenas tardes】こんにちは<br>③ 【por la tarde】午後に", "・<b>¡Buenas tardes!</b>（こんにちは！）<br>・<b>Nos vemos por la tarde.</b>（午後に会いましょう）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la tarde</b> / 複数: <b>las tardes</b>"),
    ("mañana", "マニャーナ", "女性名詞 [女]", "① 朝、午前中（la mañana）<br>② 明日（副詞: mañana）", "・<b>Por la mañana tomo café.</b>（朝はコーヒーを飲みます）<br>・<b>Hasta mañana.</b>（また明日）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la mañana</b> / 複数: <b>las mañanas</b>"),
    ("semana", "セマナ", "女性名詞 [女]", "① 週、1週間<br>② 【fin de semana】週末<br>③ 【la semana que viene】来週", "・<b>Buen fin de semana.</b>（良い週末を！）<br>・<b>La semana pasada estuve ocupado.</b>（先週は忙しかったです）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la semana</b> / 複数: <b>las semanas</b>"),
    ("mes", "メス", "男性名詞 [男]", "① 月、1ヶ月", "・<b>El mes que viene voy a España.</b>（来月スペインに行きます）<br>・<b>¿En qué mes naciste?</b>（何月生まれですか？）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el mes</b> / 複数: <b>los meses</b> (-es付加)"),
    ("año", "アニョ", "男性名詞 [男]", "① 年、1年<br>② 年齢（歳）<br>③ 【¡Feliz Año Nuevo!】あけましておめでとう！", "・<b>Tengo veinte años.</b>（20歳です）<br>・<b>El año pasado viajé mucho.</b>（去年はたくさん旅をしました）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el año</b> / 複数: <b>los años</b>"),
    ("hora", "オラ", "女性名詞 [女]", "① 時間、時刻、1時間<br>② 【¿Qué hora es?】何時ですか？", "・<b>¿Qué hora es? - Son las dos.</b>（何時ですか？ - 2時です）<br>・<b>Llegué una hora antes.</b>（1時間早く着きました）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la hora</b> / 複数: <b>las horas</b>"),
    ("minuto", "ミヌート", "男性名詞 [男]", "① 分（60秒）<br>② 【un minuto】少々（待って）", "・<b>Espera un minuto, por favor.</b>（1分待ってください）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el minuto</b> / 複数: <b>los minutos</b>"),
    ("dinero", "ディネロ", "男性名詞 [男]", "① お金、通貨、資金", "・<b>No tengo suficiente dinero para comprarlo.</b>（それを買うのに十分なお金がありません）", "日常・生活", "<b>【性数変化】</b> 不可算名詞: <b>el dinero</b>"),
    ("precio", "プレシオ", "男性名詞 [男]", "① 値段、価格、料金", "・<b>¿Cuál es el precio de este abrigo?</b>（このコートの値段はいくらですか？）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el precio</b> / 複数: <b>los precios</b>"),
    ("tarjeta", "タルヘタ", "女性名詞 [女]", "① カード、クレジットカード（tarjeta de crédito）", "・<b>¿Aceptan tarjeta de crédito?</b>（クレジットカードは使えますか？）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la tarjeta</b> / 複数: <b>las tarjetas</b>"),
    ("efectivo", "エフェクティボ", "男性名詞 [男]", "① 現金、キャッシュ", "・<b>Prefiero pagar en efectivo.</b>（現金で払いたいです）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el efectivo</b>"),
    ("comida", "コミダ", "女性名詞 [女]", "① 食べ物、食事<br>② 昼食（スペインのメイン食）", "・<b>La comida española es deliciosa.</b>（スペイン料理はとても美味しいです）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la comida</b> / 複数: <b>las comidas</b>"),
    ("agua", "アグア", "女性名詞 [女 ※単数形はel agua]", "① 水、飲料水（el agua）", "・<b>Un vaso de agua, por favor.</b>（お水をコップ1杯ください）", "日常・生活", "<b>【特殊性数】</b> 単数: <b>el agua</b> (女性名詞だが発音上el) / 複数: <b>las aguas</b>"),
    ("pan", "パン", "男性名詞 [男]", "① パン", "・<b>Compro pan fresco en la panadería.</b>（パン屋さんで焼きたてのパンを買います）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el pan</b> / 複数: <b>los panes</b>"),
    ("café", "カフェ", "男性名詞 [男]", "① コーヒー<br>② 喫茶店、カフェ", "・<b>Tomo una taza de café todas las mañanas.</b>（毎朝コーヒーを1杯飲みます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el café</b> / 複数: <b>los cafés</b>"),
    ("leche", "レチェ", "女性名詞 [女]", "① 牛乳、ミルク<br>② 【café con leche】カフェラテ", "・<b>¿Tomas café con leche o solo?</b>（コーヒーはミルク入り？それともブラック？）", "日常・生活", "<b>【性数変化】</b> 女性名詞: <b>la leche</b>"),
    ("té", "テ", "男性名詞 [男]", "① お茶、紅茶", "・<b>Prefiero el té verde.</b>（私は緑茶のほうが好きです）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el té</b> / 複数: <b>los tés</b>"),
    ("vino", "ビノ", "男性名詞 [男]", "① ワイン、ぶどう酒（vino tinto 赤ワイン / blanco 白）", "・<b>Una copa de vino tinto, por favor.</b>（赤ワインをグラスで1杯ください）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el vino</b> / 複数: <b>los vinos</b>"),
    ("cerveza", "セルベサ", "女性名詞 [女]", "① ビール<br>② 【una caña】生ビール1杯", "・<b>¡Una cerveza bien fría, por favor!</b>（よく冷えたビールを1本ください！）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la cerveza</b> / 複数: <b>las cervezas</b>"),
    ("carne", "カルネ", "女性名詞 [女]", "① 肉、肉料理", "・<b>Me gusta la carne asada.</b>（焼肉・ローストビーフが好きです）", "日常・生活", "<b>【性数変化】</b> 女性名詞: <b>la carne</b>"),
    ("pescado", "ペスカド", "男性名詞 [男]", "① 魚、魚料理（※生きた魚は pez）", "・<b>En España comen mucho pescado fresco.</b>（スペインでは新鮮な魚をたくさん食べます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el pescado</b> / 複数: <b>los pescados</b>"),
    ("arroz", "アロス", "男性名詞 [男]", "① 米、ご飯、米料理", "・<b>La paella se hace con arroz.</b>（パエリアはお米で作られます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el arroz</b> / 複数: <b>los arroces</b> (z➔c)"),
    ("fruta", "フルタ", "女性名詞 [女]", "① 果物、フルーツ", "・<b>Como fruta para el desayuno.</b>（朝食に果物を食べます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la fruta</b> / 複数: <b>las frutas</b>"),
    ("manzana", "マンサナ", "女性名詞 [女]", "① りんご<br>② 街の1ブロック", "・<b>Una manzana al día es buena para la salud.</b>（1日1個のりんごは健康に良い）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la manzana</b> / 複数: <b>las manzanas</b>"),
    ("mesa", "メサ", "女性名詞 [女]", "① テーブル、机、食卓", "・<b>Una mesa para dos personas, por favor.</b>（2人用の席をお願いします）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la mesa</b> / 複数: <b>las mesas</b>"),
    ("silla", "シージャ", "女性名詞 [女]", "① 椅子、腰掛け", "・<b>Toma una silla y siéntate.</b>（椅子を持ってきて座って）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la silla</b> / 複数: <b>las sillas</b>"),
    ("puerta", "プエルタ", "女性名詞 [女]", "① ドア、扉、門、搭乗口（空港のゲート）", "・<b>Cierra la puerta al salir.</b>（出る時にドアを閉めてね）<br>・<b>El vuelo sale por la puerta 4.</b>（フライトは4番ゲートから出発します）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la puerta</b> / 複数: <b>las puertas</b>"),
    ("ventana", "ベンタナ", "女性名詞 [女]", "① 窓", "・<b>Abre la ventana para ventilar.</b>（換気のために窓を開けて）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la ventana</b> / 複数: <b>las ventanas</b>"),
    ("cama", "カマ", "女性名詞 [女]", "① ベッド、寝床", "・<b>Voy a la cama, tengo mucho sueño.</b>（とても眠いのでベッドに行きます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la cama</b> / 複数: <b>las camas</b>"),
    ("ropa", "ロパ", "女性名詞 [女]", "① 衣服、服、洋服", "・<b>Compré ropa nueva para el viaje.</b>（旅行のために新しい服を買いました）", "日常・生活", "<b>【性数変化】</b> 集合名詞: <b>la ropa</b>"),
    ("zapato", "サパト", "男性名詞 [男]", "① 靴、シューズ（通常複数は zapatos）", "・<b>Estos zapatos son muy cómodos para caminar.</b>（この靴は歩くのにとても快適です）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el zapato</b> / 複数: <b>los zapatos</b>"),
    ("libro", "リブロ", "男性名詞 [男]", "① 本、書籍、教科書", "・<b>Estoy leyendo un libro muy interesante.</b>（とても面白い本を読んでいます）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el libro</b> / 複数: <b>los libros</b>"),
    ("carta", "カルタ", "女性名詞 [女]", "① 手紙<br>② レストランのメニュー表", "・<b>¿Nos trae la carta, por favor?</b>（メニューを持ってきてくれますか？）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la carta</b> / 複数: <b>las cartas</b>"),
    ("teléfono", "テレフォノ", "男性名詞 [男]", "① 電話、スマートフォン（teléfono móvil）", "・<b>¿Cuál es tu número de teléfono?</b>（君の電話番号は何番？）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el teléfono</b> / 複数: <b>los teléfonos</b>"),
    ("móvil", "モビル", "男性名詞 [男]", "① 携帯電話、スマホ（スペインで頻用）", "・<b>Olvidé mi móvil en casa.</b>（家にスマホを忘れてきました）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el móvil</b> / 複数: <b>los móviles</b>"),
    ("llave", "ジャベ", "女性名詞 [女]", "① 鍵、キー", "・<b>No encuentro las llaves de mi casa.</b>（家の鍵が見つかりません）", "日常・生活", "<b>【性数変化】</b> 単数: <b>la llave</b> / 複数: <b>las llaves</b>"),
    ("bolso", "ボルソ", "男性名詞 [男]", "① ハンドバッグ、鞄、バッグ", "・<b>Llevo la cartera en el bolso.</b>（バッグの中に財布を入れています）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el bolso</b> / 複数: <b>los bolsos</b>"),
    ("baño", "バニョ", "男性名詞 [男]", "① トイレ、浴室、お手洗い<br>② 【¿Dónde está el baño?】トイレはどこ？", "・<b>Perdón, ¿dónde está el baño?</b>（すみません、トイレはどこですか？）", "日常・生活", "<b>【性数変化】</b> 単数: <b>el baño</b> / 複数: <b>los baños</b>"),

    # ==========================================
    # 3. 人物・家族・職業名詞 (18語)
    # ==========================================
    ("persona", "ペルソナ", "女性名詞 [女]", "① 人、人物、人間（常に女性名詞）", "・<b>Ella es una persona muy amable.</b>（彼女はとても親切な人です）", "人物・家族", "<b>【性数変化】</b> 単数: <b>la persona</b> / 複数: <b>las personas</b>"),
    ("amigo", "アミゴ", "男性名詞 [男]", "① 友人、友達（女性の友達は amiga）", "・<b>Juan es mi mejor amigo.</b>（フアンは私の親友です）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>amigo</b> / 女単: <b>amiga</b> / 男複: <b>amigos</b> / 女複: <b>amigas</b>"),
    ("familia", "ファミリア", "女性名詞 [女]", "① 家族、親族", "・<b>Mi familia vive en Japón.</b>（私の家族は日本に住んでいます）", "人物・家族", "<b>【性数変化】</b> 単数: <b>la familia</b> / 複数: <b>las familias</b>"),
    ("padre", "パドレ", "男性名詞 [男]", "① 父親、お父さん（複数は padres 両親）", "・<b>Mis padres están bien de salud.</b>（私の両親は元気です）", "人物・家族", "<b>【性数変化】</b> 単数: <b>el padre</b> / 複数: <b>los padres</b> (両親/父親たち)"),
    ("madre", "マドレ", "女性名詞 [女]", "① 母親、お母さん", "・<b>Mi madre cocina muy rico.</b>（母は料理がとても上手です）", "人物・家族", "<b>【性数変化】</b> 単数: <b>la madre</b> / 複数: <b>las madres</b>"),
    ("hijo", "イホ", "男性名詞 [男]", "① 息子（娘は hija、子どもたちは hijos）", "・<b>Tengo dos hijos: un niño y una niña.</b>（私には息子と娘の2人の子どもがいます）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>hijo</b> / 女単: <b>hija</b> / 複数: <b>hijos</b> (子どもたち)"),
    ("hermano", "エルマノ", "男性名詞 [男]", "① 兄弟、兄、弟（姉妹は hermana）", "・<b>Mi hermano mayor vive en Madrid.</b>（私の兄はマドリードに住んでいます）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>hermano</b> / 女単: <b>hermana</b> / 複数: <b>hermanos</b> (兄弟たち)"),
    ("abuelo", "アブエロ", "男性名詞 [男]", "① 祖父、おじいちゃん（祖母は abuela）", "・<b>Visito a mis abuelos en verano.</b>（夏に祖父母を訪ねます）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>abuelo</b> / 女単: <b>abuela</b> / 複数: <b>abuelos</b> (祖父母)"),
    ("hombre", "オンブレ", "男性名詞 [男]", "① 男性、男の人、大人", "・<b>Aquel hombre es mi profesor.</b>（あの男性は私の先生です）", "人物・家族", "<b>【性数変化】</b> 単数: <b>el hombre</b> / 複数: <b>los hombres</b>"),
    ("mujer", "ムヘール", "女性名詞 [女]", "① 女性、女の人<br>② 妻、奥さん", "・<b>Es una mujer muy trabajadora.</b>（彼女はとても働き者の女性です）", "人物・家族", "<b>【性数変化】</b> 単数: <b>la mujer</b> / 複数: <b>las mujeres</b>"),
    ("niño", "ニーニョ", "男性名詞 [男]", "① 男の子、子ども（女の子は niña）", "・<b>Los niños juegan en el parque.</b>（子どもたちが公園で遊んでいます）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>niño</b> / 女単: <b>niña</b> / 複数: <b>niños</b> (子どもたち)"),
    ("chico", "チコ", "男性名詞 [男]", "① 少年、若い男の子（女の子は chica）", "・<b>Ese chico es muy simpático.</b>（その男の子はとても感じが良いです）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>chico</b> / 女単: <b>chica</b> / 男複: <b>chicos</b> / 女複: <b>chicas</b>"),
    ("profesor", "プロフェソール", "男性名詞 [男]", "① 教師、先生、教授（女性は profesora）", "・<b>El profesor explica muy bien la gramática.</b>（先生は文法をとても分かりやすく説明してくれます）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>profesor</b> / 女単: <b>profesora</b> / 男複: <b>profesores</b> / 女複: <b>profesoras</b>"),
    ("estudiante", "エストゥディアンテ", "名詞 [男女同形]", "① 学生、生徒", "・<b>Soy estudiante de español.</b>（私はスペイン語の学生です）", "人物・家族", "<b>【男女同形】</b> 男性: <b>el estudiante</b> / 女性: <b>la estudiante</b> / 複数: <b>estudiantes</b>"),
    ("médico", "メディコ", "男性名詞 [男]", "① 医者、医師（女性医師は médica）", "・<b>Tengo que ir al médico hoy.</b>（今日お医者さんに行かなければなりません）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>médico</b> / 女単: <b>médica</b> / 複数: <b>médicos</b>"),
    ("camarero", "カマレロ", "男性名詞 [男]", "① ウェイター、給仕（女性は camarera）", "・<b>¡Camarero, la cuenta por favor!</b>（店員さん、お会計をお願いします！）", "人物・家族", "<b>【男女・性数】</b> 男単: <b>camarero</b> / 女単: <b>camarera</b> / 複数: <b>camareros</b>"),
    ("nombre", "ノンブレ", "男性名詞 [男]", "① 名前、氏名<br>② 【¿Cómo es tu nombre?】名前は何？", "・<b>Mi nombre es Taro Yamada.</b>（私の名前は山田太郎です）", "人物・家族", "<b>【性数変化】</b> 単数: <b>el nombre</b> / 複数: <b>los nombres</b>"),
    ("apellido", "アペジード", "男性名詞 [男]", "① 苗字、姓", "・<b>¿Cómo se escribe tu apellido?</b>（苗字はどう書きますか？）", "人物・家族", "<b>【性数変化】</b> 単数: <b>el apellido</b> / 複数: <b>los apellidos</b>"),

    # ==========================================
    # 4. 街・旅行・交通・場所名詞 (22語)
    # ==========================================
    ("ciudad", "シウダッ(ド)", "女性名詞 [女]", "① 都市、街、都会", "・<b>Madrid es una ciudad muy hermosa.</b>（マドリードはとても美しい街です）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la ciudad</b> / 複数: <b>las ciudades</b>"),
    ("país", "パイス", "男性名詞 [男]", "① 国、国家", "・<b>España es un país fascinante.</b>（スペインは魅力的な国です）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el país</b> / 複数: <b>los países</b>"),
    ("calle", "カジェ", "女性名詞 [女]", "① 通り、道、街路", "・<b>¿En qué calle está el restaurante?</b>（レストランは何通りにありますか？）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la calle</b> / 複数: <b>las calles</b>"),
    ("plaza", "プラサ", "女性名詞 [女]", "① 広場（例: Plaza Mayor マヨール広場）", "・<b>Nos encontramos en la plaza a las cinco.</b>（5時に広場で待ち合わせしよう）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la plaza</b> / 複数: <b>las plazas</b>"),
    ("estación", "エスタシオン", "女性名詞 [女]", "① 駅（estación de tren 電車駅）<br>② 季節（estaciones del año 四季）", "・<b>El hotel está cerca de la estación.</b>（ホテルは駅の近くにあります）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la estación</b> / 複数: <b>las estaciones</b>"),
    ("aeropuerto", "アエロプエルト", "男性名詞 [男]", "① 空港", "・<b>Tengo que estar en el aeropuerto dos horas antes.</b>（2時間前に空港にいなければなりません）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el aeropuerto</b> / 複数: <b>los aeropuertos</b>"),
    ("hotel", "オテル", "男性名詞 [男]", "① ホテル、宿", "・<b>Tengo una reserva en este hotel.</b>（このホテルに予約があります）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el hotel</b> / 複数: <b>los hoteles</b>"),
    ("restaurante", "レスタウランテ", "男性名詞 [男]", "① レストラン、飲食店", "・<b>Vamos a cenar a un restaurante español.</b>（スペイン料理レストランへ夕食に行きましょう）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el restaurante</b> / 複数: <b>los restaurantes</b>"),
    ("tienda", "ティエンダ", "女性名詞 [女]", "① 店、売店、ショップ", "・<b>Esta tienda vende ropa muy bonita.</b>（この店はとても可愛い服を売っています）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la tienda</b> / 複数: <b>las tiendas</b>"),
    ("supermercado", "スペルメルカード", "男性名詞 [男]", "① スーパーマーケット", "・<b>Voy al supermercado a comprar fruta.</b>（果物を買いにスーパーへ行きます）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el supermercado</b> / 複数: <b>los supermercados</b>"),
    ("museo", "ムセオ", "男性名詞 [男]", "① 博物館、美術館（Museo del Prado プラド美術館）", "・<b>Ayer visité el Museo del Prado.</b>（昨日プラド美術館を訪れました）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el museo</b> / 複数: <b>los museos</b>"),
    ("playa", "プラジャ", "女性名詞 [女]", "① 砂浜、ビーチ、海岸", "・<b>Me encanta nadar en la playa en verano.</b>（夏にビーチで泳ぐのが大好きです）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la playa</b> / 複数: <b>las playas</b>"),
    ("parque", "パルケ", "男性名詞 [男]", "① 公園", "・<b>Paseo por el parque todos los días.</b>（毎日公園を散歩します）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el parque</b> / 複数: <b>los parques</b>"),
    ("tren", "トレン", "男性名詞 [男]", "① 電車、列車、鉄道", "・<b>Viajo en tren de Madrid a Barcelona.</b>（マドリードからバルセロナまで電車で旅します）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el tren</b> / 複数: <b>los trenes</b>"),
    ("autobús", "アウトブス", "男性名詞 [男]", "① バス、路線バス", "・<b>El autobús número 5 va al centro.</b>（5番のバスは中心部へ行きます）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el autobús</b> / 複数: <b>los autobuses</b>"),
    ("metro", "メトロ", "男性名詞 [男]", "① 地下鉄", "・<b>Es más rápido ir en metro.</b>（地下鉄で行くほうが早いです）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el metro</b>"),
    ("taxi", "タクシ", "男性名詞 [男]", "① タクシー", "・<b>Vamos a tomar un taxi.</b>（タクシーに乗りましょう）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el taxi</b> / 複数: <b>los taxis</b>"),
    ("coche", "コチェ", "男性名詞 [男]", "① 自動車、車（中南米では auto / carro）", "・<b>Voy al trabajo en coche.</b>（車で通勤します）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el coche</b> / 複数: <b>los coches</b>"),
    ("avión", "アビオン", "男性名詞 [男]", "① 飛行機", "・<b>El avión sale a las tres.</b>（飛行機は3時に出発します）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el avión</b> / 複数: <b>los aviones</b>"),
    ("billete", "ビジェテ", "男性名詞 [男]", "① 切符、チケット、紙幣（中南米では boleto）", "・<b>Un billete de ida y vuelta, por favor.</b>（往復切符を1枚ください）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el billete</b> / 複数: <b>los billetes</b>"),
    ("viaje", "ビアヘ", "男性名詞 [男]", "① 旅行、旅<br>② 【¡Buen viaje!】良い旅を！", "・<b>¡Buen viaje a España!</b>（スペインへの良い旅を！）", "街・旅行", "<b>【性数変化】</b> 単数: <b>el viaje</b> / 複数: <b>los viajes</b>"),
    ("maleta", "マレタ", "女性名詞 [女]", "① スーツケース、旅行カバン", "・<b>Tengo que preparar mi maleta para mañana.</b>（明日のためにスーツケースを準備しなきゃ）", "街・旅行", "<b>【性数変化】</b> 単数: <b>la maleta</b> / 複数: <b>las maletas</b>"),

    # ==========================================
    # 5. 性格・感情・評価・状態形容詞 (30語)
    # ==========================================
    ("bueno", "ブエノ", "形容詞 [形]", "① 良い、優れた（ser bueno）<br>② 優しい、親切な<br>③ 美味しい（estar bueno）", "・<b>Es un buen libro.</b>（良い本です）<br>・<b>La sopa está muy buena.</b>（スープがとても美味しいです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>bueno (buen)</b> / 女単: <b>buena</b> / 男複: <b>buenos</b> / 女複: <b>buenas</b>"),
    ("malo", "マロ", "形容詞 [形]", "① 悪い、有害な<br>② 体調が悪い（estar malo）<br>③ 不味い（estar malo）", "・<b>Fumar es malo para la salud.</b>（喫煙は健康に悪いです）<br>・<b>Hoy estoy malo con fiebre.</b>（今日は熱があって体調が悪いです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>malo (mal)</b> / 女単: <b>mala</b> / 男複: <b>malos</b> / 女複: <b>malas</b>"),
    ("grande", "グランデ", "形容詞 [形]", "① 大きい、広い<br>② 偉大な（名詞の前で gran）", "・<b>Mi casa tiene una cocina grande.</b>（私の家には広いキッチンがあります）<br>・<b>Un gran hombre.</b>（偉大な男性）", "形容詞", "<b>【男女同形】</b> 単数: <b>grande (gran)</b> / 複数: <b>grandes</b>"),
    ("pequeño", "ペケーニョ", "形容詞 [形]", "① 小さい、狭い<br>② 幼い、年下の", "・<b>Vivo en un apartamento pequeño.</b>（小さなアパートに住んでいます）", "形容詞", "<b>【男女・性数】</b> 男単: <b>pequeño</b> / 女単: <b>pequeña</b> / 男複: <b>pequeños</b> / 女複: <b>pequeñas</b>"),
    ("nuevo", "ヌエボ", "形容詞 [形]", "① 新しい、新品の", "・<b>Compré un coche nuevo.</b>（新しい車を買いました）", "形容詞", "<b>【男女・性数】</b> 男単: <b>nuevo</b> / 女単: <b>nueva</b> / 男複: <b>nuevos</b> / 女複: <b>nuevas</b>"),
    ("viejo", "ビエホ", "形容詞 [形]", "① 古い、年をとった<br>② 【un viejo amigo】旧友", "・<b>Es un edificio muy viejo.</b>（とても古い建物です）", "形容詞", "<b>【男女・性数】</b> 男単: <b>viejo</b> / 女単: <b>vieja</b> / 男複: <b>viejos</b> / 女複: <b>viejas</b>"),
    ("bonito", "ボニート", "形容詞 [形]", "① きれいな、美しい、可愛い", "・<b>¡Qué flores tan bonitas!</b>（なんて綺麗なお花！）", "形容詞", "<b>【男女・性数】</b> 男単: <b>bonito</b> / 女単: <b>bonita</b> / 男複: <b>bonitos</b> / 女複: <b>bonitas</b>"),
    ("hermoso", "エルモソ", "形容詞 [形]", "① 美しい、見事な、素晴らしい", "・<b>Es una vista hermosa.</b>（見事な景色です）", "形容詞", "<b>【男女・性数】</b> 男単: <b>hermoso</b> / 女単: <b>hermosa</b> / 男複: <b>hermosos</b> / 女複: <b>hermosas</b>"),
    ("feo", "フェオ", "形容詞 [形]", "① 醜い、見苦しい、不格好な", "・<b>Hoy hace un día feo con lluvia.</b>（今日は雨で嫌な天気です）", "形容詞", "<b>【男女・性数】</b> 男単: <b>feo</b> / 女単: <b>fea</b> / 男複: <b>feos</b> / 女複: <b>feas</b>"),
    ("fácil", "ファシル", "形容詞 [形]", "① 簡単な、易しい", "・<b>El examen fue muy fácil.</b>（試験はとても簡単でした）", "形容詞", "<b>【男女同形】</b> 単数: <b>fácil</b> / 複数: <b>fáciles</b>"),
    ("difícil", "ディフィシル", "形容詞 [形]", "① 難しい、困難な", "・<b>La pronunciación no es difícil.</b>（発音は難しくありません）", "形容詞", "<b>【男女同形】</b> 単数: <b>difícil</b> / 複数: <b>difíciles</b>"),
    ("importante", "インポルタンテ", "形容詞 [形]", "① 重要な、大切な", "・<b>Es una reunión muy importante.</b>（とても重要な会議です）", "形容詞", "<b>【男女同形】</b> 単数: <b>importante</b> / 複数: <b>importantes</b>"),
    ("necesario", "ネセサリオ", "形容詞 [形]", "① 必要な、不可欠な", "・<b>Es necesario practicar todos los días.</b>（毎日練習することが必要です）", "形容詞", "<b>【男女・性数】</b> 男単: <b>necesario</b> / 女単: <b>necesaria</b> / 男複: <b>necesarios</b> / 女複: <b>necesarias</b>"),
    ("posible", "ポシブレ", "形容詞 [形]", "① 可能な、あり得る<br>② 【lo antes posible】できるだけ早く", "・<b>Llámame lo antes posible.</b>（できるだけ早く電話して）", "形容詞", "<b>【男女同形】</b> 単数: <b>posible</b> / 複数: <b>posibles</b>"),
    ("imposible", "インポシブレ", "形容詞 [形]", "① 不可能な、あり得ない", "・<b>Nada es imposible si te esfuerzas.</b>（努力すれば不可能なことは何もない）", "形容詞", "<b>【男女同形】</b> 単数: <b>imposible</b> / 複数: <b>imposibles</b>"),
    ("caro", "カロ", "形容詞 [形]", "① （値段が）高い、高価な", "・<b>Este restaurante es un poco caro pero delicioso.</b>（このレストランは少し高いですが美味しいです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>caro</b> / 女単: <b>cara</b> / 男複: <b>caros</b> / 女複: <b>caras</b>"),
    ("barato", "バラト", "形容詞 [形]", "① （値段が）安い、お手頃な", "・<b>Encontré un hotel muy barato.</b>（とても安いホテルを見つけました）", "形容詞", "<b>【男女・性数】</b> 男単: <b>barato</b> / 女単: <b>barata</b> / 男複: <b>baratos</b> / 女複: <b>baratas</b>"),
    ("rápido", "ラピド", "形容詞・副詞 [形/副]", "① 速い、素早い、迅速な", "・<b>El AVE es un tren muy rápido.</b>（AVEはとても速い新幹線列車です）", "形容詞", "<b>【男女・性数】</b> 男単: <b>rápido</b> / 女単: <b>rápida</b> / 男複: <b>rápidos</b> / 女複: <b>rápidas</b>"),
    ("lento", "レント", "形容詞 [形]", "① 遅い、ゆっくりした", "・<b>El autobús va muy lento por el tráfico.</b>（渋滞でバスがとても遅いです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>lento</b> / 女単: <b>lenta</b> / 男複: <b>lentos</b> / 女複: <b>lentas</b>"),
    ("contento", "コンテント", "形容詞 [形]", "① 満足した、喜んでいる、嬉しい（estar）", "・<b>Estoy muy contento con mis resultados.</b>（結果にとても満足しています）", "形容詞", "<b>【男女・性数】</b> 男単: <b>contento</b> / 女単: <b>contenta</b> / 男複: <b>contentos</b> / 女複: <b>contentas</b>"),
    ("feliz", "フェリス", "形容詞 [形]", "① 幸せな、幸福な<br>② 【¡Feliz cumpleaños!】お誕生日おめでとう！", "・<b>¡Feliz cumpleaños, amigo!</b>（誕生日おめでとう！）", "形容詞", "<b>【男女同形】</b> 単数: <b>feliz</b> / 複数: <b>felices</b> (z➔c)"),
    ("triste", "トリステ", "形容詞 [形]", "① 悲しい、憂鬱な", "・<b>¿Por qué estás triste hoy?</b>（どうして今日悲しそうなの？）", "形容詞", "<b>【男女同形】</b> 単数: <b>triste</b> / 複数: <b>tristes</b>"),
    ("cansado", "カンサード", "形容詞 [形]", "① 疲れている、くたくたな（estar）", "・<b>Estoy muy cansado de tanto trabajar.</b>（働きすぎてとても疲れています）", "形容詞", "<b>【男女・性数】</b> 男単: <b>cansado</b> / 女単: <b>cansada</b> / 男複: <b>cansados</b> / 女複: <b>cansadas</b>"),
    ("ocupado", "オクパード", "形容詞 [形]", "① 忙しい、ふさがっている（estar）", "・<b>Esta semana estoy muy ocupado.</b>（今週はとても忙しいです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>ocupado</b> / 女単: <b>ocupada</b> / 男複: <b>ocupados</b> / 女複: <b>ocupadas</b>"),
    ("libre", "リブレ", "形容詞 [形]", "① 自由な、暇な、空いている", "・<b>¿Estás libre esta tarde?</b>（今日の午後空いてる？）", "形容詞", "<b>【男女同形】</b> 単数: <b>libre</b> / 複数: <b>libres</b>"),
    ("limpio", "リンピオ", "形容詞 [形]", "① 清潔な、綺麗な、汚れていない", "・<b>La habitación está muy limpia.</b>（部屋はとても綺麗です）", "形容詞", "<b>【男女・性数】</b> 男単: <b>limpio</b> / 女単: <b>limpia</b> / 男複: <b>limpios</b> / 女複: <b>limpias</b>"),
    ("sucio", "スシオ", "形容詞 [形]", "① 汚れた、不潔な", "・<b>Mis zapatos están sucios de barro.</b>（靴が泥で汚れています）", "形容詞", "<b>【男女・性数】</b> 男単: <b>sucio</b> / 女単: <b>sucia</b> / 男複: <b>sucios</b> / 女複: <b>sucias</b>"),
    ("caliente", "カリエンテ", "形容詞 [形]", "① 熱い、温かい", "・<b>Cuidado, el café está muy caliente.</b>（気をつけて、コーヒーがとても熱いです）", "形容詞", "<b>【男女同形】</b> 単数: <b>caliente</b> / 複数: <b>calientes</b>"),
    ("frío", "フリオ", "形容詞・名詞 [形/男]", "① 冷たい、寒い<br>② 寒さ（Tengo frío 寒い）", "・<b>Tengo mucho frío hoy.</b>（今日はとても寒いです）<br>・<b>Quiero agua fría.</b>（冷たい水が欲しいです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>frío</b> / 女単: <b>fría</b> / 男複: <b>fríos</b> / 女複: <b>frías</b>"),
    ("simpático", "シンパティコ", "形容詞 [形]", "① 感じの良い、親しみやすい、優しい", "・<b>Los españoles son muy simpáticos.</b>（スペイン人はとても親切で親しみやすいです）", "形容詞", "<b>【男女・性数】</b> 男単: <b>simpático</b> / 女単: <b>simpática</b> / 男複: <b>simpáticos</b> / 女複: <b>simpáticas</b>"),

    # ==========================================
    # 6. 副詞・前置詞・接続詞・重要表現 (34語)
    # ==========================================
    ("aquí", "アキ", "副詞 [副]", "① ここ、こちら（話し手の近く）", "・<b>Ven aquí, por favor.</b>（ここに来てください）<br>・<b>Estoy aquí.</b>（ここにいます）", "副詞・前置詞", "<b>【位置対応】</b> aquí (ここ) ➔ ahí (そこ) ➔ allí (あそこ)"),
    ("ahí", "アイ", "副詞 [副]", "① そこ（聞き手の近く）", "・<b>Déjalo ahí.</b>（そこに置いておいて）", "副詞・前置詞", "<b>【位置対応】</b> aquí (ここ) ➔ ahí (そこ) ➔ allí (あそこ)"),
    ("allí", "アジー", "副詞 [副]", "① あそこ、向こう（双方から離れた場所）", "・<b>Mi casa está allí.</b>（私の家はあそこにあります）", "副詞・前置詞", "<b>【位置対応】</b> aquí (ここ) ➔ ahí (そこ) ➔ allí (あそこ)"),
    ("ahora", "アオラ", "副詞 [副]", "① 今、現在<br>② 【ahora mismo】今すぐ", "・<b>Ahora estoy estudiando.</b>（今勉強しているところです）<br>・<b>¡Hazlo ahora mismo!</b>（今すぐやりなさい！）", "副詞・前置詞", "<b>【派生表現】</b> ahora mismo (たった今/今すぐ)"),
    ("hoy", "オイ", "副詞 [副]", "① 今日、本日", "・<b>Hoy es un día muy especial.</b>（今日はとても特別な日です）", "副詞・前置詞", "<b>【時間対比】</b> ayer (昨日) ➔ hoy (今日) ➔ mañana (明日)"),
    ("ayer", "アジェール", "副詞 [副]", "① 昨日", "・<b>Ayer fui al cine con María.</b>（昨日マリアと映画に行きました）", "副詞・前置詞", "<b>【時間対比】</b> anteayer (一昨日) ➔ ayer (昨日) ➔ hoy (今日)"),
    ("mañana", "マニャーナ", "副詞 [副]", "① 明日", "・<b>Mañana tengo un examen importante.</b>（明日重要なテストがあります）", "副詞・前置詞", "<b>【時間対比】</b> hoy (今日) ➔ mañana (明日) ➔ pasado mañana (明後日)"),
    ("siempre", "シエンプレ", "副詞 [副]", "① いつも、常に、いつでも", "・<b>Siempre desayuno a las siete.</b>（いつも7時に朝食をとります）", "副詞・前置詞", "<b>【頻度対比】</b> siempre (100%) ➔ a veces (50%) ➔ nunca (0%)"),
    ("nunca", "ヌンカ", "副詞 [副]", "① 決して〜ない、一度も〜ない", "・<b>Nunca he estado en México.</b>（一度もメキシコに行ったことがありません）", "副詞・前置詞", "<b>【頻度対比】</b> nunca / jamás (決して〜ない)"),
    ("a veces", "ア ベセス", "副詞句 [副]", "① 時々、たまに", "・<b>A veces voy al gimnasio después del trabajo.</b>（時々仕事帰りにジムへ行きます）", "副詞・前置詞", "<b>【頻度対比】</b> siempre (いつも) ➔ a veces (時々)"),
    ("también", "タンビエン", "副詞 [副]", "① 〜もまた、同様に（肯定の同調）", "・<b>Yo también quiero ir a España.</b>（私もスペインに行きたいです）", "副詞・前置詞", "<b>【対比】</b> 肯定: también (〜も) / 否定: tampoco (〜も…ない)"),
    ("tampoco", "タンポコ", "副詞 [副]", "① 〜もまた…ない（否定の同調）", "・<b>Yo tampoco lo sé.</b>（私もそれを知りません）", "副詞・前置詞", "<b>【対比】</b> 肯定: también (〜も) / 否定: tampoco (〜も…ない)"),
    ("mucho", "ムチョ", "副詞・形容詞 [副/形]", "① たくさん、大いに、非常に", "・<b>Muchas gracias por todo.</b>（いろいろ本当にありがとう）<br>・<b>Te quiero mucho.</b>（大好きです）", "副詞・前置詞", "<b>【性数変化(形容詞時)】</b> mucho / mucha / muchos / muchas"),
    ("poco", "ポコ", "副詞・形容詞 [副/形]", "① 少し、わずか<br>② 【un poco de】少しの〜", "・<b>Hablo un poco de español.</b>（スペイン語が少し話せます）", "副詞・前置詞", "<b>【性数変化(形容詞時)】</b> poco / poca / pocos / pocas"),
    ("muy", "ムイ", "副詞 [副]", "① とても、大変（形容詞・副詞を修飾）", "・<b>Estoy muy contento hoy.</b>（今日はとても嬉しいです）", "副詞・前置詞", "<b>【使い分け】</b> muy + 形容詞/副詞 (例: muy bien, muy bonito)"),
    ("más", "マス", "副詞 [副]", "① もっと、より多く（比較級を作る）", "・<b>Quiero aprender más español.</b>（もっとスペイン語を学びたいです）", "副詞・前置詞", "<b>【比較級】</b> más + 形容詞 + que (〜より…だ)"),
    ("menos", "メノス", "副詞 [副]", "① より少なく、〜を除いて", "・<b>Cuesta menos de diez euros.</b>（10ユーロ未満です）", "副詞・前置詞", "<b>【劣等比較】</b> menos + 形容詞 + que (〜より…でない)"),
    ("ya", "ジャ", "副詞 [副]", "① もう、すでに<br>② 今すぐ<br>③ 【ya no】もう〜ない", "・<b>¿Ya has comido? - Sí, ya comí.</b>（もうご飯食べた？ - うん、もう食べたよ）", "副詞・前置詞", "<b>【重要成句】</b> ya no (もう〜ない) / ya veo (なるほど)"),
    ("todavía", "トダビア", "副詞 [副]", "① まだ、依然として<br>② 【todavía no】まだ〜ない", "・<b>Todavía no he terminado.</b>（まだ終わっていません）", "副詞・前置詞", "<b>【重要成句】</b> todavía no (まだ〜ない)"),
    ("casi", "カシ", "副詞 [副]", "① ほとんど、もう少しで、ほぼ", "・<b>Ya son casi las diez.</b>（もうほぼ10時です）", "副詞・前置詞", "<b>【用法】</b> casi todos (ほぼ全員) / casi nunca (めったに〜ない)"),
    ("bien", "ビエン", "副詞 [副]", "① よく、上手に、元気に", "・<b>¡Muy bien hecho!</b>（よくできました！）<br>・<b>Estoy bien.</b>（元気です）", "副詞・前置詞", "<b>【対比】</b> bien (良く) ⇄ mal (悪く)"),
    ("mal", "マル", "副詞 [副]", "① 悪く、下手に、具合悪く", "・<b>Me siento mal hoy.</b>（今日は気分が悪いです）", "副詞・前置詞", "<b>【対比】</b> bien (良く) ⇄ mal (悪く)"),
    ("con", "コン", "前置詞 [前]", "① 〜と一緒に、〜を使って（手段）<br>② 【conmigo】私と / 【contigo】君と", "・<b>Voy con mi familia.</b>（家族と一緒に行きます）<br>・<b>Café con leche.</b>（ミルク入りコーヒー）", "副詞・前置詞", "<b>【特殊形】</b> conmigo (私と) / contigo (君と) / consigo (彼自身と)"),
    ("sin", "シン", "前置詞 [前]", "① 〜なしで、〜を持たずに", "・<b>Un café sin azúcar, por favor.</b>（砂糖なしのコーヒーをお願いします）", "副詞・前置詞", "<b>【対比】</b> con (〜と一緒に) ⇄ sin (〜なしで)"),
    ("en", "エン", "前置詞 [前]", "① 〜の中で、〜で（場所・時・手段）", "・<b>Estoy en casa.</b>（家にいます）<br>・<b>Viajo en tren.</b>（電車で旅行します）", "副詞・前置詞", "<b>【用法】</b> 所在(en Tokio) / 交通手段(en autobús)"),
    ("a", "ア", "前置詞 [前]", "① 〜へ（方向・目的地）<br>② 〜に（時刻・対象）", "・<b>Voy a la estación a las ocho.</b>（8時に駅へ行きます）<br>・<b>Veo a Juan.</b>（フアンに会います）", "副詞・前置詞", "<b>【結合則】</b> a + el ➔ <b>al</b> (例: al cine)"),
    ("de", "デ", "前置詞 [前]", "① 〜の（所有・素材）<br>② 〜から（出身・起点）", "・<b>Soy de Japón.</b>（日本出身です）<br>・<b>El libro de María.</b>（マリアの本）", "副詞・前置詞", "<b>【結合則】</b> de + el ➔ <b>del</b> (例: del profesor)"),
    ("para", "パラ", "前置詞 [前]", "① 〜のために（目的・受取人）<br>② 〜に向けて（目的地）<br>③ 〜までに（期限）", "・<b>Estudio para trabajar en España.</b>（スペインで働くために勉強しています）<br>・<b>Es para ti.</b>（君へのプレゼントです）", "副詞・前置詞", "<b>【porとの違い】</b> para: 矢印の先（目的・期限・宛先）"),
    ("por", "ポル", "前置詞 [前]", "① 〜によって（原因・手段）<br>② 〜を通って（通過）<br>③ 〜に対して（感謝・交換）", "・<b>Muchas gracias por tu ayuda.</b>（手伝ってくれて本当にありがとう）<br>・<b>Paseo por el parque.</b>（公園を通って散歩します）", "副詞・前置詞", "<b>【paraとの違い】</b> por: 原因・理由・手段・通過・交換"),
    ("porque", "ポルケ", "接続詞 [接]", "① なぜなら〜だから（理由を答える）", "・<b>No voy porque estoy cansado.</b>（疲れているので行きません）", "副詞・前置詞", "<b>【対比】</b> 問い: ¿Por qué? (なぜ?) ➔ 答え: Porque... (〜だから)"),
    ("pero", "ペロ", "接続詞 [接]", "① しかし、だが（逆接）", "・<b>Es caro, pero muy bueno.</b>（高いですが、とても良いです）", "副詞・前置詞", "<b>【用法】</b> 文と文をつなぐ逆接接続詞"),
    ("y", "イ", "接続詞 [接]", "① そして、〜と（並列）", "・<b>Hablo japonés y español.</b>（日本語とスペイン語を話します）", "副詞・前置詞", "<b>【発音規則】</b> i / hi で始まる語の前では <b>e</b> に変化 (例: español e inglés)"),
    ("o", "オ", "接続詞 [接]", "① または、あるいは（選択）", "・<b>¿Prefieres té o café?</b>（お茶とコーヒー、どちらがいい？）", "副詞・前置詞", "<b>【発音規則】</b> o / ho で始まる語の前では <b>u</b> に変化 (例: siete u ocho)"),
    ("si", "シ", "接続詞 [接]", "① もし〜ならば（条件）", "・<b>Si tienes tiempo, vamos a comer.</b>（もし時間があれば、ご飯食べに行こう）", "副詞・前置詞", "<b>【注意】</b> アクセント記号なし: si (もし) / あり: sí (はい/Yes)")
]

# 挨拶・身体・曜日・疑問詞
DICTIONARY_DATA += [
    # 7. 挨拶・基本コミュニケーション表現 (8語)
    ("hola", "オラ", "間投詞 [間]", "① こんにちは、やあ（親しい挨拶）", "・<b>¡Hola! ¿Cómo estás?</b>（やあ！元気？）", "挨拶・基本表現", "<b>【発音】</b> h は無音。いつでも使える最も一般的な挨拶"),
    ("adiós", "アディオス", "間投詞 [間]", "① さようなら、バイバイ", "・<b>¡Adiós! ¡Que tengas un buen día!</b>（さようなら！良い1日を！）", "挨拶・基本表現", "<b>【別表現】</b> ¡Hasta luego! (また後で) / ¡Hasta pronto! (また近いうちに)"),
    ("por favor", "ポル ファボール", "副詞句 [副]", "① お願いします、どうぞ（please）", "・<b>La cuenta, por favor.</b>（お会計をお願いします）", "挨拶・基本表現", "<b>【用法】</b> 依頼の末尾や先頭につけて丁寧にする表現"),
    ("de nada", "デ ナダ", "慣用句 [間]", "① どういたしまして、お気になさらず", "・<b>- ¡Muchas gracias! - De nada.</b>（- ありがとう！ - どういたしまして）", "挨拶・基本表現", "<b>【別表現】</b> No hay de qué. (どういたしまして)"),
    ("perdón", "ペルドン", "間投詞 [間]", "① ごめんなさい、すみません（軽い謝罪・呼びかけ）", "・<b>¡Perdón! No fue mi intención.</b>（ごめんなさい！そんなつもりじゃなかったんです）", "挨拶・基本表現", "<b>【用法】</b> 軽くぶつかった時や呼びかけに使う"),
    ("disculpe", "ディスクルペ", "動詞活用 [間]", "① すみません、失礼します（丁寧な呼びかけ）", "・<b>Disculpe, ¿dónde está la parada de autobús?</b>（すみません、バス停はどこですか？）", "挨拶・基本表現", "<b>【用法】</b> usted に対する丁寧な呼びかけ"),
    ("mucho gusto", "ムチョ グスト", "慣用句 [間]", "① はじめまして、お会いできて嬉しいです", "・<b>- Soy Taro. - Mucho gusto.</b>（- タロウです。 - はじめまして）", "挨拶・基本表現", "<b>【同義】</b> Encantado (男性) / Encantada (女性)"),
    ("bienvenido", "ビエンベニード", "形容詞・間投詞 [形/間]", "① ようこそ、歓迎します（女性には bienvenida）", "・<b>¡Bienvenidos a España!</b>（スペインへようこそ！）", "挨拶・基本表現", "<b>【男女・性数】</b> 男単: bienvenido / 女単: bienvenida / 複: bienvenidos"),

    # 8. 身体・健康名詞 (6語)
    ("cabeza", "カベサ", "女性名詞 [女]", "① 頭、頭部<br>② 【me duele la cabeza】頭が痛い", "・<b>Me duele mucho la cabeza.</b>（頭がとても痛いです）", "身体・健康", "<b>【性数変化】</b> 単数: <b>la cabeza</b> / 複数: <b>las cabezas</b>"),
    ("mano", "マノ", "女性名詞 [女 ※語尾-oだが女性]", "① 手（※女性名詞: la mano）", "・<b>Lávate las manos antes de comer.</b>（食べる前に手を洗ってね）", "身体・健康", "<b>【性数変化】</b> 女性名詞: <b>la mano</b> / 複数: <b>las manos</b>"),
    ("ojo", "オホ", "男性名詞 [男]", "① 目、瞳（複数は ojos）<br>② 【¡Ojo!】気をつけて！注意！", "・<b>Tiene los ojos azules.</b>（彼女は青い目をしています）", "身体・健康", "<b>【性数変化】</b> 単数: <b>el ojo</b> / 複数: <b>los ojos</b>"),
    ("boca", "ボカ", "女性名詞 [女]", "① 口、口元、地下鉄の入り口", "・<b>Abre la boca, por favor.</b>（口を開けてください）", "身体・健康", "<b>【性数変化】</b> 単数: <b>la boca</b> / 複数: <b>las bocas</b>"),
    ("corazón", "コラソン", "男性名詞 [男]", "① 心臓、心、ハート、愛情表現（愛しい人）", "・<b>Te quiero con todo mi corazón.</b>（心から君を愛しています）", "身体・健康", "<b>【性数変化】</b> 単数: <b>el corazón</b> / 複数: <b>los corazones</b>"),
    ("cuerpo", "クエルポ", "男性名詞 [男]", "① 身体、体、胴体", "・<b>El ejercicio es bueno para el cuerpo.</b>（運動は体に良いです）", "身体・健康", "<b>【性数変化】</b> 単数: <b>el cuerpo</b> / 複数: <b>los cuerpos</b>"),

    # 9. 曜日・暦名詞 (7語)
    ("lunes", "ルネス", "男性名詞 [男]", "① 月曜日（el lunes）", "・<b>Nos vemos el lunes.</b>（月曜日に会いましょう）", "暦・曜日", "<b>【冠詞】</b> 曜日には定冠詞をつける: <b>el lunes</b> / 毎週月曜: <b>los lunes</b>"),
    ("martes", "マルテス", "男性名詞 [男]", "① 火曜日（el martes）", "・<b>El martes tengo clase de español.</b>（火曜日にスペイン語の授業があります）", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el martes</b> / 複数: <b>los martes</b>"),
    ("miércoles", "ミエルコレス", "男性名詞 [男]", "① 水曜日（el miércoles）", "・<b>El miércoles voy al dentista.</b>（水曜日に歯医者に行きます）", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el miércoles</b> / 複数: <b>los miércoles</b>"),
    ("jueves", "フエベス", "男性名詞 [男]", "① 木曜日（el jueves）", "・<b>El jueves es fiesta nacional.</b>（木曜日は祝日です）", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el jueves</b> / 複数: <b>los jueves</b>"),
    ("viernes", "ビエルネス", "男性名詞 [男]", "① 金曜日（el viernes）<br>② 【¡Por fin es viernes!】華金だ！", "・<b>¡Por fin es viernes!</b>（やっと金曜日だ！）", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el viernes</b> / 複数: <b>los viernes</b>"),
    ("sábado", "サバド", "男性名詞 [男]", "① 土曜日（el sábado）", "・<b>Los sábados me levanto tarde.</b>（土曜日は遅く起きます）", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el sábado</b> / 複数: <b>los sábados</b>"),
    ("domingo", "ドミンゴ", "男性名詞 [男]", "① 日曜日（el domingo）", "・<b>El domingo como con mi familia.</b>（日曜日は家族と食事します）", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el domingo</b> / 複数: <b>los domingos</b>"),

    # 10. 疑問詞 (8語)
    ("qué", "ケ", "代名詞 [疑]", "① 何、どんなもの<br>② 【¿Qué tal?】調子はどう？", "・<b>¿Qué haces hoy?</b>（今日何してるの？）<br>・<b>¿Qué tal todo?</b>（調子はどう？）", "疑問詞", "<b>【アクセント】</b> 疑問詞には必ずアクセント記号がつきます: qué"),
    ("quién", "キエン", "代名詞 [疑]", "① 誰、どなた（複数は quiénes）", "・<b>¿Quién es esa chica?</b>（あの子は誰？）", "疑問詞", "<b>【複数形】</b> 単数: <b>quién</b> / 複数: <b>quiénes</b>"),
    ("dónde", "ドンデ", "副詞 [疑]", "① どこ、どこで<br>② 【¿De dónde eres?】出身はどこ？", "・<b>¿Dónde vives?</b>（どこに住んでいますか？）<br>・<b>¿De dónde eres? - Soy de Tokio.</b>（ご出身は？ - 東京です）", "疑問詞", "<b>【前置詞結合】</b> ¿A dónde? (どこへ?) / ¿De dónde? (どこから/出身?)"),
    ("cuándo", "クアンド", "副詞 [疑]", "① いつ、何時に", "・<b>¿Cuándo es tu cumpleaños?</b>（誕生日はいつですか？）", "疑問詞", "<b>【アクセント】</b> 疑問詞: cuándo (いつ) / 接続詞: cuando (〜の時)"),
    ("cómo", "コモ", "副詞 [疑]", "① どのように、どうやって<br>② 【¿Cómo te llamas?】お名前は？", "・<b>¿Cómo se llega a la estación?</b>（駅へはどう行きますか？）", "疑問詞", "<b>【アクセント】</b> 疑問詞: cómo (どのように) / 接続詞: como (〜のように)"),
    ("por qué", "ポル ケ", "疑問句 [疑]", "① なぜ、どうして（理由を問う）", "・<b>¿Por qué estudias español?</b>（どうしてスペイン語を勉強しているの？）", "疑問詞", "<b>【区別】</b> 問い: <b>¿Por qué?</b> (2語・アクセント) / 答え: <b>porque</b> (1語)"),
    ("cuánto", "クアント", "形容詞・代名詞 [疑]", "① いくら、どれくらい（性数変化: cuántos/as）", "・<b>¿Cuánto cuesta esto?</b>（これはいくらですか？）<br>・<b>¿Cuántos años tienes?</b>（何歳ですか？）", "疑問詞", "<b>【性数変化】</b> cuánto / cuánta / cuántos / cuántas"),
    ("cuál", "クアル", "代名詞 [疑]", "① どれ、どちら、何（複数は cuáles）", "・<b>¿Cuál es tu comida favorita?</b>（一番好きな食べ物は何ですか？）", "疑問詞", "<b>【複数形】</b> 単数: <b>cuál</b> / 複数: <b>cuáles</b>")
]
