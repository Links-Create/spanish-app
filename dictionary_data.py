# -*- coding: utf-8 -*-
"""
スペイン語 重要単語マスター データベース (221語)
全6人称活用 (Yo, Tú, Él/Ud, Nosotros, Vosotros, Ellos/Uds) ＆ 単語分解パーツ解説付き例文
"""

DICTIONARY_DATA = [
    # ==========================================
    # 1. 最重要基本動詞 (46語) - 全6人称活用＆単語分解つき
    # ==========================================
    ("tener", "テネール", "不規則動詞 [動]", 
     "① （物・人を）持っている、所有している<br>② （年齢が）〜歳である<br>③ （空腹・眠気などの感覚を）感じる<br>④ 【tener que + 原形】〜しなければならない<br>⑤ 【tener ganas de + 原形】〜したい", 
     "・<b>Tengo un coche nuevo.</b>（新しい車を持っています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo</b>(持っている) + <b>un</b>(1つの) + <b>coche</b>(車) + <b>nuevo</b>(新しい)</span><br>・<b>¿Cuántos años tienes? - Tengo 20 años.</b>（何歳ですか？ - 20歳です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuántos</b>(いくつの) + <b>años</b>(歳/年) + <b>tienes</b>(君は持っている)</span><br>・<b>Tengo que estudiar hoy.</b>（今日は勉強しなければなりません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo que</b>(〜せねばならない) + <b>estudiar</b>(勉強する) + <b>hoy</b>(今日)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo (私): <b>tengo</b> (テンゴ)<br>・Tú (君): <b>tienes</b> (ティエネス)<br>・Él/Ella/Ud (彼/彼女/あなた): <b>tiene</b> (ティエネ)<br>・Nosotros (私たち): <b>tenemos</b> (テネモス)<br>・Vosotros (君たち): <b>tenéis</b> (テネイス)<br>・Ellos/Uds (彼ら/あなた方): <b>tienen</b> (ティエネン)"),

    ("ser", "セール", "不規則動詞 [動]", 
     "① （本質・国籍・職業が）〜である<br>② （時刻・日付が）〜である<br>③ （素材・所属が）〜のものである<br>④ （イベントが）開催される", 
     "・<b>Yo soy japonés y soy estudiante.</b>（私は日本人で学生です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Yo</b>(私) + <b>soy</b>(〜です) + <b>japonés</b>(日本人) + <b>y</b>(そして) + <b>estudiante</b>(学生)</span><br>・<b>Son las tres de la tarde.</b>（午後3時です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Son</b>(〜時です) + <b>las tres</b>(3時) + <b>de la tarde</b>(午後の)</span><br>・<b>Este reloj es de oro.</b>（この時計は金製です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Este</b>(この) + <b>reloj</b>(時計) + <b>es de</b>(〜製です) + <b>oro</b>(金)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>soy</b> (ソイ)<br>・Tú: <b>eres</b> (エレス)<br>・Él/Ella/Ud: <b>es</b> (エス)<br>・Nosotros: <b>somos</b> (ソモス)<br>・Vosotros: <b>sois</b> (ソイス)<br>・Ellos/Uds: <b>son</b> (ソン)"),

    ("estar", "エスタール", "不規則動詞 [動]", 
     "① （一時的な状態・体調が）〜である<br>② （人・物が）〜にいる、ある（所在）<br>③ 【estar + 現在分詞】〜している最中だ<br>④ 【estar de acuerdo】賛成である", 
     "・<b>¿Cómo estás? - Estoy muy bien.</b>（元気？ - とても元気です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cómo</b>(どのように) + <b>estás</b>(君はいる/状態) + <b>Estoy</b>(私はいる) + <b>muy</b>(とても) + <b>bien</b>(良く)</span><br>・<b>¿Dónde está la estación?</b>（駅はどこですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Dónde</b>(どこに) + <b>está</b>(ありますか) + <b>la estación</b>(駅)</span><br>・<b>Estoy estudiando español.</b>（スペイン語を勉強しています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy</b>(現在) + <b>estudiando</b>(勉強中) + <b>español</b>(スペイン語)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>estoy</b> (エストイ)<br>・Tú: <b>estás</b> (エスタス)<br>・Él/Ella/Ud: <b>está</b> (エスタ)<br>・Nosotros: <b>estamos</b> (エスタモス)<br>・Vosotros: <b>estáis</b> (エスタイス)<br>・Ellos/Uds: <b>están</b> (エスタン)"),

    ("hacer", "アセール", "不規則動詞 [動]", 
     "① （物を）作る、製作する<br>② （行動・仕事を）する、行う<br>③ （天気が）〜である<br>④ 【hace + 時間】〜前", 
     "・<b>Hago la cena todos los días.</b>（毎日夕食を作ります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hago</b>(私は作る) + <b>la cena</b>(夕食) + <b>todos los días</b>(毎日)</span><br>・<b>Hoy hace muy buen tiempo.</b>（今日はとてもいい天気です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hoy</b>(今日) + <b>hace buen tiempo</b>(良い天気だ)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>hago</b> (アゴ)<br>・Tú: <b>haces</b> (アセス)<br>・Él/Ella/Ud: <b>hace</b> (アセ)<br>・Nosotros: <b>hacemos</b> (アセモス)<br>・Vosotros: <b>hacéis</b> (アセイス)<br>・Ellos/Uds: <b>hacen</b> (アセン)"),

    ("ir", "イール", "不規則動詞 [動]", 
     "① （場所へ）行く、向かう（a 〜）<br>② 【ir a + 原形】〜する予定だ（近接未来）<br>③ （物事が）進む、うまくいく<br>④ 【irse】立ち去る、帰る", 
     "・<b>Voy al supermercado en metro.</b>（地下鉄でスーパーに行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy</b>(私は行く) + <b>al</b>(〜へ) + <b>supermercado</b>(スーパー) + <b>en metro</b>(地下鉄で)</span><br>・<b>Mañana voy a viajar.</b>（明日旅行する予定です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mañana</b>(明日) + <b>voy a</b>(〜する予定だ) + <b>viajar</b>(旅行する)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>voy</b> (ボイ)<br>・Tú: <b>vas</b> (バス)<br>・Él/Ella/Ud: <b>va</b> (バ)<br>・Nosotros: <b>vamos</b> (バモス)<br>・Vosotros: <b>vais</b> (バイス)<br>・Ellos/Uds: <b>van</b> (バン)"),

    ("poder", "ポデール", "不規則動詞 [動]", 
     "① （能力・状況的に）〜できる<br>② （許可）〜してもよい<br>③ （依頼）〜してくれますか？", 
     "・<b>Puedo hablar un poco de español.</b>（スペイン語が少し話せます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Puedo</b>(私は〜できる) + <b>hablar</b>(話す) + <b>un poco de</b>(少しの) + <b>español</b>(スペイン語)</span><br>・<b>¿Puedo pagar con tarjeta?</b>（カードで払えますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Puedo</b>(〜できますか) + <b>pagar</b>(支払う) + <b>con tarjeta</b>(カードで)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (o➔ue)】</b><br>・Yo: <b>puedo</b> (プエド)<br>・Tú: <b>puedes</b> (プエデス)<br>・Él/Ella/Ud: <b>puede</b> (プエデ)<br>・Nosotros: <b>podemos</b> (ポデモス)<br>・Vosotros: <b>podéis</b> (ポデイス)<br>・Ellos/Uds: <b>pueden</b> (プエデン)"),

    ("querer", "ケレール", "不規則動詞 [動]", 
     "① （物が）欲しい<br>② （〜することを）欲する、〜したい<br>③ （人を）愛している、好いている", 
     "・<b>Quiero un café con leche, por favor.</b>（カフェラテを1つください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero</b>(私は欲しい) + <b>un café</b>(コーヒー) + <b>con leche</b>(ミルク入り) + <b>por favor</b>(お願いします)</span><br>・<b>Quiero aprender más.</b>（もっと学びたいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero</b>(〜したい) + <b>aprender</b>(学ぶ) + <b>más</b>(もっと)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>quiero</b> (キエロ)<br>・Tú: <b>quieres</b> (キエレス)<br>・Él/Ella/Ud: <b>quiere</b> (キエレ)<br>・Nosotros: <b>queremos</b> (ケレモス)<br>・Vosotros: <b>queréis</b> (ケレイス)<br>・Ellos/Uds: <b>quieren</b> (キエレン)"),

    ("saber", "サベール", "不規則動詞 [動]", 
     "① （情報・知識・事実を）知っている<br>② 【saber + 原形】（技術として）〜できる<br>③ （味が）〜の味がする", 
     "・<b>No sé la respuesta.</b>（答えを知りません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No</b>(〜ない) + <b>sé</b>(私は知っている [saber]) + <b>la respuesta</b>(答え)</span><br>・<b>¿Sabes nadar?</b>（泳げますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Sabes</b>(君はできるか) + <b>nadar</b>(泳ぐ)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>sé</b> (セ)<br>・Tú: <b>sabes</b> (サベス)<br>・Él/Ella/Ud: <b>sabe</b> (サベ)<br>・Nosotros: <b>sabemos</b> (サベモス)<br>・Vosotros: <b>sabéis</b> (サベイス)<br>・Ellos/Uds: <b>saben</b> (サベン)"),

    ("conocer", "コノセール", "不規則動詞 [動]", 
     "① （人・場所・街を）知っている、経験として知る<br>② （人と）知り合う、面識ができる", 
     "・<b>¿Conoces a María? - Sí, la conozco.</b>（マリアさんを知ってる？ - ええ、知っています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Conoces a</b>(〜を知っているか) + <b>María</b>(マリア) + <b>la</b>(彼女を) + <b>conozco</b>(知っている)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (yo不規則)】</b><br>・Yo: <b>conozco</b> (コノスコ)<br>・Tú: <b>conoces</b> (コノセス)<br>・Él/Ella/Ud: <b>conoce</b> (コノセ)<br>・Nosotros: <b>conocemos</b> (コノセモス)<br>・Vosotros: <b>conocéis</b> (コノセイス)<br>・Ellos/Uds: <b>conocen</b> (コノセン)"),

    ("dar", "ダール", "不規則動詞 [動]", 
     "① （人に物を）与える、あげる、渡す<br>② 【dar un paseo】散歩する<br>③ 【dar las gracias】お礼を言う", 
     "・<b>Te doy mi número de teléfono.</b>（私の電話番号を教えるよ）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Te</b>(君に) + <b>doy</b>(私はあげる) + <b>mi número</b>(私の番号) + <b>de teléfono</b>(電話の)</span><br>・<b>Vamos a dar un paseo.</b>（散歩に行きましょう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vamos a</b>(〜しよう) + <b>dar un paseo</b>(散歩する)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>doy</b> (ドイ)<br>・Tú: <b>das</b> (ダス)<br>・Él/Ella/Ud: <b>da</b> (ダ)<br>・Nosotros: <b>damos</b> (ダモス)<br>・Vosotros: <b>dais</b> (ダイス)<br>・Ellos/Uds: <b>dan</b> (ダン)"),

    ("decir", "デシール", "不規則動詞 [動]", 
     "① （言葉・意見を）言う、話す<br>② 【es decir】つまり、すなわち<br>③ 【¿Cómo se dice...?】〜は何と言いますか？", 
     "・<b>Dime la verdad.</b>（私に本当のことを言って）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Di</b>(言いなさい [命令]) + <b>me</b>(私に) + <b>la verdad</b>(真実/本当のこと)</span><br>・<b>¿Cómo se dice esto en español?</b>（これはスペイン語で何と言いますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cómo</b>(どう) + <b>se dice</b>(言われるか) + <b>esto</b>(これ) + <b>en español</b>(スペイン語で)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔i / yo:digo)】</b><br>・Yo: <b>digo</b> (ディゴ)<br>・Tú: <b>dices</b> (ディセス)<br>・Él/Ella/Ud: <b>dice</b> (ディセ)<br>・Nosotros: <b>decimos</b> (デシモス)<br>・Vosotros: <b>decís</b> (デシス)<br>・Ellos/Uds: <b>dicen</b> (ディセン)"),

    ("ver", "ベエール", "不規則動詞 [動]", 
     "① （目で）見る、眺める、見学する<br>② （人に）会う<br>③ 【¡Nos vemos!】また会おう！", 
     "・<b>Veo la televisión por la noche.</b>（夜にテレビを見ます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Veo</b>(私は見る) + <b>la televisión</b>(テレビ) + <b>por la noche</b>(夜に)</span><br>・<b>¡Nos vemos pronto!</b>（また近いうちに会おうね！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Nos vemos</b>(私たちは会う) + <b>pronto</b>(すぐに/近いうちに)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>veo</b> (ベオ)<br>・Tú: <b>ves</b> (ベス)<br>・Él/Ella/Ud: <b>ve</b> (ベ)<br>・Nosotros: <b>vemos</b> (ベモス)<br>・Vosotros: <b>veis</b> (ベイス)<br>・Ellos/Uds: <b>ven</b> (ベン)"),

    ("venir", "ベニール", "不規則動詞 [動]", 
     "① （こちらへ）来る<br>② （出身が）〜から来ている（de 〜）", 
     "・<b>¿Vienes a la fiesta hoy?</b>（今日のパーティーに来る？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vienes</b>(君は来る) + <b>a la fiesta</b>(パーティーへ) + <b>hoy</b>(今日)</span><br>・<b>Vengo de Japón.</b>（私は日本から来ました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vengo</b>(私は来る) + <b>de Japón</b>(日本から)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie / yo:vengo)】</b><br>・Yo: <b>vengo</b> (ベンゴ)<br>・Tú: <b>vienes</b> (ビエネス)<br>・Él/Ella/Ud: <b>viene</b> (ビエネ)<br>・Nosotros: <b>venimos</b> (ベニモス)<br>・Vosotros: <b>venís</b> (ベニス)<br>・Ellos/Uds: <b>vienen</b> (ビエネン)"),

    ("poner", "ポネール", "不規則動詞 [動]", 
     "① （物を場所に）置く、設置する<br>② （スイッチを）つける<br>③ 【ponerse】（服を）着る、（感情に）なる", 
     "・<b>Pongo el libro en la mesa.</b>（本を机の上に置きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Pongo</b>(私は置く) + <b>el libro</b>(本) + <b>en la mesa</b>(机の上に)</span><br>・<b>Me pongo el abrigo.</b>（コートを着ます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me pongo</b>(身につける) + <b>el abrigo</b>(コート)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (yo:pongo)】</b><br>・Yo: <b>pongo</b> (ポンゴ)<br>・Tú: <b>pones</b> (ポネス)<br>・Él/Ella/Ud: <b>pone</b> (ポネ)<br>・Nosotros: <b>ponemos</b> (ポネモス)<br>・Vosotros: <b>ponéis</b> (ポネイス)<br>・Ellos/Uds: <b>ponen</b> (ポネン)"),

    ("salir", "サリール", "不規則動詞 [動]", 
     "① （場所から）出る、出発する<br>② （友人と）出かける、遊びに行く<br>③ （太陽・月が）出る", 
     "・<b>El tren sale a las ocho.</b>（電車は8時に出発します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El tren</b>(電車) + <b>sale</b>(出発する) + <b>a las ocho</b>(8時に)</span><br>・<b>Salgo con mis amigos.</b>（友達と出かけます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Salgo</b>(私は出かける) + <b>con</b>(〜と) + <b>mis amigos</b>(私の友達)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (yo:salgo)】</b><br>・Yo: <b>salgo</b> (サルゴ)<br>・Tú: <b>sales</b> (サレス)<br>・Él/Ella/Ud: <b>sale</b> (サレ)<br>・Nosotros: <b>salimos</b> (サリモス)<br>・Vosotros: <b>salís</b> (サリス)<br>・Ellos/Uds: <b>salen</b> (サレン)"),

    ("traer", "トラエール", "不規則動詞 [動]", 
     "① （物をこちらに）持ってくる<br>② （人を連れて）連れてくる", 
     "・<b>¿Puedes traerme la cuenta, por favor?</b>（お会計を持ってきてくれますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Puedes</b>(〜できるか) + <b>traer</b>(持ってくる) + <b>me</b>(私に) + <b>la cuenta</b>(お会計)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (yo:traigo)】</b><br>・Yo: <b>traigo</b> (トライゴ)<br>・Tú: <b>traes</b> (トラエス)<br>・Él/Ella/Ud: <b>trae</b> (トラエ)<br>・Nosotros: <b>traemos</b> (トラエモス)<br>・Vosotros: <b>traéis</b> (トラエイス)<br>・Ellos/Uds: <b>traen</b> (トラエン)"),

    ("llevar", "ジェバール", "規則動詞 [動]", 
     "① （物をあちらへ）持っていく、運ぶ<br>② （服・靴・メガネを）身につけている<br>③ （時間を）〜過ごしている", 
     "・<b>Llevo una camisa blanca.</b>（白いシャツを着ています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llevo</b>(着ている) + <b>una camisa</b>(シャツ) + <b>blanca</b>(白い)</span><br>・<b>Llevo tres años en España.</b>（スペインに来て3年になります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llevo</b>(過ごす) + <b>tres años</b>(3年) + <b>en España</b>(スペインで)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>llevo</b> (ジェボ)<br>・Tú: <b>llevas</b> (ジェバス)<br>・Él/Ella/Ud: <b>lleva</b> (ジェバ)<br>・Nosotros: <b>llevamos</b> (ジェバモス)<br>・Vosotros: <b>lleváis</b> (ジェバイス)<br>・Ellos/Uds: <b>llevan</b> (ジェバン)"),

    ("hablar", "アブラール", "規則動詞 [動]", 
     "① （言語を）話す<br>② （人と）会話する（con 〜）", 
     "・<b>Hablo español e inglés.</b>（スペイン語と英語を話します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hablo</b>(私は話す) + <b>español</b>(スペイン語) + <b>e</b>(そして) + <b>inglés</b>(英語)</span><br>・<b>Quiero hablar contigo.</b>（君と話がしたいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero</b>(〜したい) + <b>hablar</b>(話す) + <b>contigo</b>(君と)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>hablo</b> (アブロ)<br>・Tú: <b>hablas</b> (アブラス)<br>・Él/Ella/Ud: <b>habla</b> (アブラ)<br>・Nosotros: <b>hablamos</b> (アブラモス)<br>・Vosotros: <b>habláis</b> (アブライス)<br>・Ellos/Uds: <b>hablan</b> (アブラン)"),

    ("comer", "コメール", "規則動詞 [動]", 
     "① （食事を）食べる<br>② （昼食を）とる", 
     "・<b>Como paella todos los domingos.</b>（毎週日曜日にパエリアを食べます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Como</b>(私は食べる) + <b>paella</b>(パエリア) + <b>todos los domingos</b>(毎週日曜日)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>como</b> (コモ)<br>・Tú: <b>comes</b> (コメス)<br>・Él/Ella/Ud: <b>come</b> (コメ)<br>・Nosotros: <b>comemos</b> (コメモス)<br>・Vosotros: <b>coméis</b> (コメイス)<br>・Ellos/Uds: <b>comen</b> (コメン)"),

    ("vivir", "ビビール", "規則動詞 [動]", 
     "① （場所に）住む、暮らす<br>② 生きる、生活する", 
     "・<b>Vivo en Tokio con mi familia.</b>（家族と東京に住んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vivo</b>(私は住む) + <b>en Tokio</b>(東京に) + <b>con mi familia</b>(家族と一緒に)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ir規則)】</b><br>・Yo: <b>vivo</b> (ビボ)<br>・Tú: <b>vives</b> (ビベス)<br>・Él/Ella/Ud: <b>vive</b> (ビベ)<br>・Nosotros: <b>vivimos</b> (ビビモス)<br>・Vosotros: <b>vivís</b> (ビビス)<br>・Ellos/Uds: <b>viven</b> (ビベン)"),

    ("beber", "ベベール", "規則動詞 [動]", 
     "① （飲み物を）飲む<br>② （お酒を）飲む", 
     "・<b>Bebo mucha agua todos los días.</b>（毎日たくさん水を飲みます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Bebo</b>(私は飲む) + <b>mucha agua</b>(たくさんの水) + <b>todos los días</b>(毎日)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>bebo</b> (ベボ)<br>・Tú: <b>bebes</b> (ベベス)<br>・Él/Ella/Ud: <b>bebe</b> (ベベ)<br>・Nosotros: <b>bebemos</b> (ベベモス)<br>・Vosotros: <b>bebéis</b> (ベベイス)<br>・Ellos/Uds: <b>beben</b> (ベベン)"),

    ("escribir", "エスクリビール", "規則動詞 [動]", 
     "① （文字・文章を）書く<br>② （手紙・メッセージを）送る", 
     "・<b>Escribo un correo a mi profesor.</b>（先生にメールを書きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Escribo</b>(私は書く) + <b>un correo</b>(メール) + <b>a mi profesor</b>(先生に)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ir規則)】</b><br>・Yo: <b>escribo</b> (エスクリボ)<br>・Tú: <b>escribes</b> (エスクリベス)<br>・Él/Ella/Ud: <b>escribe</b> (エスクリベ)<br>・Nosotros: <b>escribimos</b> (エスクリビモス)<br>・Vosotros: <b>escribís</b> (エスクリビス)<br>・Ellos/Uds: <b>escriben</b> (エスクリベン)"),

    ("leer", "レエール", "規則動詞 [動]", 
     "① （本・新聞などを）読む", 
     "・<b>Leo el periódico todas las mañanas.</b>（毎朝新聞を読みます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Leo</b>(私は読む) + <b>el periódico</b>(新聞) + <b>todas las mañanas</b>(毎朝)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>leo</b> (レオ)<br>・Tú: <b>lees</b> (レエス)<br>・Él/Ella/Ud: <b>lee</b> (レエ)<br>・Nosotros: <b>leemos</b> (レエモス)<br>・Vosotros: <b>leéis</b> (レエイス)<br>・Ellos/Uds: <b>leen</b> (レエン)"),

    ("escuchar", "エスクチャール", "規則動詞 [動]", 
     "① （音・音楽を意識して）聴く、耳を傾ける", 
     "・<b>Escucho música latina mientras cocino.</b>（料理をしながらラテン音楽を聴きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Escucho</b>(聴く) + <b>música latina</b>(ラテン音楽) + <b>mientras</b>(〜の間) + <b>cocino</b>(料理する)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>escucho</b> (エスクチョ)<br>・Tú: <b>escuchas</b> (エスクチャス)<br>・Él/Ella/Ud: <b>escucha</b> (エスクチャ)<br>・Nosotros: <b>escuchamos</b> (エスクチャモス)<br>・Vosotros: <b>escucháis</b> (エスクチャイス)<br>・Ellos/Uds: <b>escuchan</b> (エスクチャン)"),

    ("oír", "オイール", "不規則動詞 [動]", 
     "① （自然に音が耳に）聞こえる", 
     "・<b>No te oigo bien, ¿puedes repetir?</b>（よく聞こえません、もう一度言ってくれますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No te oigo</b>(君の声が聞こえない) + <b>bien</b>(良く) + <b>puedes repetir</b>(繰り返せますか)</span>", "基本動詞",
     "<b>【現在形 6人称変化】</b><br>・Yo: <b>oigo</b> (オイゴ)<br>・Tú: <b>oyes</b> (オジェス)<br>・Él/Ella/Ud: <b>oye</b> (オジェ)<br>・Nosotros: <b>oímos</b> (オイモス)<br>・Vosotros: <b>oís</b> (オイス)<br>・Ellos/Uds: <b>oyen</b> (オジェン)"),

    ("abrir", "アブリール", "規則動詞 [動]", 
     "① （ドア・窓・本などを）開ける、開く<br>② （店が）開店する", 
     "・<b>¿Puedes abrir la ventana?</b>（窓を開けてくれますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Puedes</b>(できるか) + <b>abrir</b>(開ける) + <b>la ventana</b>(窓)</span><br>・<b>La tienda abre a las diez.</b>（店は10時に開きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La tienda</b>(店) + <b>abre</b>(開く) + <b>a las diez</b>(10時に)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ir規則)】</b><br>・Yo: <b>abro</b> (アブロ)<br>・Tú: <b>abres</b> (アブレス)<br>・Él/Ella/Ud: <b>abre</b> (アブレ)<br>・Nosotros: <b>abrimos</b> (アブリモス)<br>・Vosotros: <b>abrís</b> (アブリス)<br>・Ellos/Uds: <b>abren</b> (アブレン)"),

    ("cerrar", "セラール", "不規則動詞 [動]", 
     "① （ドア・店などを）閉める、閉じる", 
     "・<b>Cierra la puerta, por favor.</b>（ドアを閉めてください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cierra</b>(閉めて [命令]) + <b>la puerta</b>(ドア) + <b>por favor</b>(お願いします)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>cierro</b> (シエロ)<br>・Tú: <b>cierras</b> (シエラス)<br>・Él/Ella/Ud: <b>cierra</b> (シエラ)<br>・Nosotros: <b>cerramos</b> (セラモス)<br>・Vosotros: <b>cerráis</b> (セライス)<br>・Ellos/Uds: <b>cierran</b> (シエラン)"),

    ("comprar", "コンプラール", "規則動詞 [動]", 
     "① （物を）買う、購入する", 
     "・<b>Compré un regalo para ti.</b>（君にプレゼントを買いました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Compré</b>(買った [点過去]) + <b>un regalo</b>(プレゼント) + <b>para ti</b>(君のために)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>compro</b> (コンプロ)<br>・Tú: <b>compras</b> (コンプラス)<br>・Él/Ella/Ud: <b>compra</b> (コンプラ)<br>・Nosotros: <b>compramos</b> (コンプラモス)<br>・Vosotros: <b>compráis</b> (コンプライス)<br>・Ellos/Uds: <b>compran</b> (コンプラン)"),

    ("vender", "ベンデール", "規則動詞 [動]", 
     "① （物を）売る、販売する", 
     "・<b>Ellos venden frutas frescas en el mercado.</b>（彼らは市場で新鮮な果物を売っています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Venden</b>(売る) + <b>frutas frescas</b>(新鮮な果物) + <b>en el mercado</b>(市場で)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>vendo</b> (ベンド)<br>・Tú: <b>vendes</b> (ベンデス)<br>・Él/Ella/Ud: <b>vende</b> (ベンデ)<br>・Nosotros: <b>vendemos</b> (ベンデモス)<br>・Vosotros: <b>vendéis</b> (ベンデイス)<br>・Ellos/Uds: <b>venden</b> (ベンデン)"),

    ("pagar", "パガール", "規則動詞 [動]", 
     "① （代金を）支払う、払う", 
     "・<b>¿Cómo quieres pagar? - En efectivo.</b>（お支払い方法は？ - 現金で）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cómo</b>(どう) + <b>quieres pagar</b>(払いたいか) + <b>En efectivo</b>(現金で)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>pago</b> (パゴ)<br>・Tú: <b>pagas</b> (パガス)<br>・Él/Ella/Ud: <b>paga</b> (パガ)<br>・Nosotros: <b>pagamos</b> (パガモス)<br>・Vosotros: <b>pagáis</b> (パガイス)<br>・Ellos/Uds: <b>pagan</b> (パガン)"),

    ("pedir", "ペディール", "不規則動詞 [動]", 
     "① （料理などを）注文する、頼む<br>② （手助け・許可を）求める、お願いする", 
     "・<b>Voy a pedir una pizza.</b>（ピザを注文します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy a</b>(〜する予定) + <b>pedir</b>(注文する) + <b>una pizza</b>(ピザ)</span><br>・<b>Quiero pedirte un favor.</b>（君にお願いがあるんだ）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero</b>(〜したい) + <b>pedir</b>(頼む) + <b>te</b>(君に) + <b>un favor</b>(お願い)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔i)】</b><br>・Yo: <b>pido</b> (ピド)<br>・Tú: <b>pides</b> (ピデス)<br>・Él/Ella/Ud: <b>pide</b> (ピデ)<br>・Nosotros: <b>pedimos</b> (ペディモス)<br>・Vosotros: <b>pedís</b> (ペディス)<br>・Ellos/Uds: <b>piden</b> (ピデン)"),

    ("preguntar", "プレグンタール", "規則動詞 [動]", 
     "① （人に質問を）尋ねる、質問する", 
     "・<b>¿Puedo preguntarte algo?</b>（ちょっと聞いてもいい？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Puedo</b>(〜できるか) + <b>preguntar</b>(尋ねる) + <b>te</b>(君に) + <b>algo</b>(何か)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>pregunto</b> (プレグント)<br>・Tú: <b>preguntas</b> (プレグンタス)<br>・Él/Ella/Ud: <b>pregunta</b> (プレグンタ)<br>・Nosotros: <b>preguntamos</b> (プレグンタモス)<br>・Vosotros: <b>preguntáis</b> (プレグンタイス)<br>・Ellos/Uds: <b>preguntan</b> (プレグンタン)"),

    ("responder", "レスポンデール", "規則動詞 [動]", 
     "① （質問・手紙に）答える、返事をする", 
     "・<b>Él no me respondió el mensaje.</b>（彼はメッセージに返信してくれませんでした）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Él</b>(彼は) + <b>no me respondió</b>(私に返信しなかった) + <b>el mensaje</b>(メッセージ)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>respondo</b> (レスポンド)<br>・Tú: <b>respondes</b> (レスポンデス)<br>・Él/Ella/Ud: <b>responde</b> (レスポンデ)<br>・Nosotros: <b>respondemos</b> (レスポンデモス)<br>・Vosotros: <b>respondéis</b> (レスポンデイス)<br>・Ellos/Uds: <b>responden</b> (レスポンデン)"),

    ("buscar", "ブスカール", "規則動詞 [動]", 
     "① （人・物を）探す、検索する", 
     "・<b>Estoy buscando mis gafas.</b>（メガネを探しています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy</b>(現在) + <b>buscando</b>(探している) + <b>mis gafas</b>(私のメガネ)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>busco</b> (ブスコ)<br>・Tú: <b>buscas</b> (ブスカス)<br>・Él/Ella/Ud: <b>busca</b> (ブスカ)<br>・Nosotros: <b>buscamos</b> (ブスカモス)<br>・Vosotros: <b>buscáis</b> (ブスカイス)<br>・Ellos/Uds: <b>buscan</b> (ブスカン)"),

    ("encontrar", "エンコントラール", "不規則動詞 [動]", 
     "① （探していた物を）見つける、発見する<br>② （人と偶然）出会う<br>③ 【encontrarse】〜な気分である", 
     "・<b>¡Por fin encontré mis llaves!</b>（やっと鍵を見つけた！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por fin</b>(ついに) + <b>encontré</b>(見つけた [点過去]) + <b>mis llaves</b>(私の鍵)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (o➔ue)】</b><br>・Yo: <b>encuentro</b> (エンクエントロ)<br>・Tú: <b>encuentras</b> (エンクエントラス)<br>・Él/Ella/Ud: <b>encuentra</b> (エンクエントラ)<br>・Nosotros: <b>encontramos</b> (エンコントラモス)<br>・Vosotros: <b>encontráis</b> (エンコントライス)<br>・Ellos/Uds: <b>encuentran</b> (エンクエントラン)"),

    ("pensar", "ペンサール", "不規則動詞 [動]", 
     "① （頭で）考える、思う<br>② 【pensar + 原形】〜するつもりである", 
     "・<b>¿Qué piensas de este plan?</b>（この計画についてどう思う？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Qué</b>(何を) + <b>piensas de</b>(〜について思うか) + <b>este plan</b>(この計画)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>pienso</b> (ピエンソ)<br>・Tú: <b>piensas</b> (ピエンサス)<br>・Él/Ella/Ud: <b>piensa</b> (ピエンサ)<br>・Nosotros: <b>pensamos</b> (ペンサモス)<br>・Vosotros: <b>pensáis</b> (ペンサイス)<br>・Ellos/Uds: <b>piensan</b> (ピエンサン)"),

    ("creer", "クレエール", "規則動詞 [動]", 
     "① （〜だと）信じる、思う<br>② （宗教などを）信じる", 
     "・<b>Creo que sí. / Creo que no.</b>（そう思います / そうは思いません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Creo que</b>(私は〜と思う) + <b>sí</b>(はい/そう) / <b>no</b>(いいえ/そうではない)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>creo</b> (クレオ)<br>・Tú: <b>crees</b> (クレエス)<br>・Él/Ella/Ud: <b>cree</b> (クレエ)<br>・Nosotros: <b>creemos</b> (クレエモス)<br>・Vosotros: <b>creéis</b> (クレエイス)<br>・Ellos/Uds: <b>creen</b> (クレエン)"),

    ("entender", "エンテンデール", "不規則動詞 [動]", 
     "① （言葉・意味・理由を）理解する、わかる", 
     "・<b>¿Entiendes lo que digo? - Sí, entiendo.</b>（私の言うことがわかる？ - ええ、わかります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Entiendes</b>(理解するか) + <b>lo que digo</b>(私の言うこと) + <b>entiendo</b>(理解する)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>entiendo</b> (エンティエンド)<br>・Tú: <b>entiendes</b> (エンティエンデス)<br>・Él/Ella/Ud: <b>entiende</b> (エンティエンデ)<br>・Nosotros: <b>entendemos</b> (エンテンデモス)<br>・Vosotros: <b>entendéis</b> (エンテンデイス)<br>・Ellos/Uds: <b>entienden</b> (エンティエンデン)"),

    ("comprender", "コンプレンデール", "規則動詞 [動]", 
     "① （深く本質を）理解する、把握する", 
     "・<b>Comprendo tu situación perfectamente.</b>（君の状況は痛いほどよく分かります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Comprendo</b>(理解する) + <b>tu situación</b>(君の状況) + <b>perfectamente</b>(完璧に)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-er規則)】</b><br>・Yo: <b>comprendo</b> (コンプレンド)<br>・Tú: <b>comprendes</b> (コンプレンデス)<br>・Él/Ella/Ud: <b>comprende</b> (コンプレンデ)<br>・Nosotros: <b>comprendemos</b> (コンプレンデモス)<br>・Vosotros: <b>comprendéis</b> (コンプレンデイス)<br>・Ellos/Uds: <b>comprenden</b> (コンプレンデン)"),

    ("ayudar", "アユダール", "規則動詞 [動]", 
     "① （人を）手伝う、助ける、援助する", 
     "・<b>¿Puedes ayudarme con esta maleta?</b>（このスーツケースを運ぶのを手伝ってくれますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Puedes</b>(できるか) + <b>ayudar</b>(手伝う) + <b>me</b>(私を) + <b>con esta maleta</b>(このスーツケースで)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>ayudo</b> (アユド)<br>・Tú: <b>ayudas</b> (アユダス)<br>・Él/Ella/Ud: <b>ayuda</b> (アユダ)<br>・Nosotros: <b>ayudamos</b> (アユダモス)<br>・Vosotros: <b>ayudáis</b> (アユダイス)<br>・Ellos/Uds: <b>ayudan</b> (アユダン)"),

    ("necesitar", "ネセシタール", "規則動詞 [動]", 
     "① （物・人を）必要とする<br>② 【necesitar + 原形】〜する必要がある", 
     "・<b>Necesito descansar un poco.</b>（少し休む必要があります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Necesito</b>(私は必要だ) + <b>descansar</b>(休む) + <b>un poco</b>(少し)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>necesito</b> (ネセシト)<br>・Tú: <b>necesitas</b> (ネセシタス)<br>・Él/Ella/Ud: <b>necesita</b> (ネセシタ)<br>・Nosotros: <b>necesitamos</b> (ネセシタモス)<br>・Vosotros: <b>necesitáis</b> (ネセシタイス)<br>・Ellos/Uds: <b>necesitan</b> (ネセシタン)"),

    ("esperar", "エスペラール", "規則動詞 [動]", 
     "① （人を）待つ<br>② （希望して）期待する、願う", 
     "・<b>Espérame un momento, por favor.</b>（ちょっと待ってください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Espera</b>(待って [命令]) + <b>me</b>(私を) + <b>un momento</b>(少しの間) + <b>por favor</b>(お願いします)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>espero</b> (エスペロ)<br>・Tú: <b>esperas</b> (エスペラス)<br>・Él/Ella/Ud: <b>espera</b> (エスペラ)<br>・Nosotros: <b>esperamos</b> (エスペラモス)<br>・Vosotros: <b>esperáis</b> (エスペライス)<br>・Ellos/Uds: <b>esperan</b> (エスペラン)"),

    ("empezar", "エンペサール", "不規則動詞 [動]", 
     "① （活動・仕事が）始まる、始める（a + 原形）", 
     "・<b>La película empieza a las siete.</b>（映画は7時に始まります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La película</b>(映画) + <b>empieza</b>(始まる) + <b>a las siete</b>(7時に)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (e➔ie)】</b><br>・Yo: <b>empiezo</b> (エンピエソ)<br>・Tú: <b>empiezas</b> (エンピエサス)<br>・Él/Ella/Ud: <b>empieza</b> (エンピエサ)<br>・Nosotros: <b>empezamos</b> (エンペサモス)<br>・Vosotros: <b>empezáis</b> (エンペサイス)<br>・Ellos/Uds: <b>empiezan</b> (エンピエサン)"),

    ("terminar", "テルミナール", "規則動詞 [動]", 
     "① （仕事・授業を）終える、終わる（de + 原形）", 
     "・<b>Terminé mi trabajo a las seis.</b>（6時に仕事を終えました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Terminé</b>(終えた [点過去]) + <b>mi trabajo</b>(私の仕事) + <b>a las seis</b>(6時に)</span>", "基本動詞",
     "<b>【現在形 6人称変化 (-ar規則)】</b><br>・Yo: <b>termino</b> (テルミノ)<br>・Tú: <b>terminas</b> (テルミナス)<br>・Él/Ella/Ud: <b>termina</b> (テルミナ)<br>・Nosotros: <b>terminamos</b> (テルミナモス)<br>・Vosotros: <b>termináis</b> (テルミナイス)<br>・Ellos/Uds: <b>terminan</b> (テルミナン)"),

    ("gustar", "グスタール", "規則動詞 [動]", 
     "① （物・事が人に）好まれる、好きだ", 
     "・<b>Me gusta mucho la comida española.</b>（スペイン料理が大好きです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me</b>(私に) + <b>gusta</b>(好まれる) + <b>mucho</b>(とても) + <b>la comida española</b>(スペイン料理)</span>", "基本動詞",
     "<b>【gustar型 活用】</b><br>・単数/動詞原形が主語: <b>gusta</b> (グスタ)<br>・複数が主語: <b>gustan</b> (グスタン)<br>※(A mí) me gusta, (A ti) te gusta, (A él) le gusta..."),

    ("encantar", "エンカンタール", "規則動詞 [動]", 
     "① （物・事が人に）大〜好きだ、たまらなく好きだ", 
     "・<b>¡Me encanta viajar por el mundo!</b>（世界中を旅するのが大好きです！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me encanta</b>(私は〜が大好きだ) + <b>viajar</b>(旅すること) + <b>por el mundo</b>(世界中を)</span>", "基本動詞",
     "<b>【gustar型 活用】</b><br>・単数/動詞原形が主語: <b>encanta</b> (エンカンタ)<br>・複数が主語: <b>encantan</b> (エンカンタン)"),

    # ==========================================
    # 2. 日常・生活・家庭名詞 (42語)
    # ==========================================
    ("casa", "カサ", "女性名詞 [女]", "① 家、我が家、住まい<br>② 【en casa】家で<br>③ 【a casa】家へ（帰宅）", "・<b>Estoy en casa descansando.</b>（家で休んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy</b>(私はいる) + <b>en casa</b>(家で) + <b>descansando</b>(休んでいる)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la casa</b> / 複数: <b>las casas</b>"),
    ("tiempo", "ティエンポ", "男性名詞 [男]", "① 時間、暇<br>② 天気、気候<br>③ 【a tiempo】時間通りに", "・<b>No tengo mucho tiempo.</b>（あまり時間がありません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No tengo</b>(持っていない) + <b>mucho tiempo</b>(たくさんの時間)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el tiempo</b> / 複数: <b>los tiempos</b>"),
    ("día", "ディア", "男性名詞 [男 ※語尾-aだが男性]", "① 日、1日、昼間<br>② 【buenos días】おはよう<br>③ 【todos los días】毎日", "・<b>¡Buenos días!</b>（おはようございます！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Buenos</b>(良い) + <b>días</b>(日々/朝)</span><br>・<b>Estudio todos los días.</b>（毎日勉強します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estudio</b>(私は勉強する) + <b>todos los días</b>(毎日)</span>", "日常・生活", "<b>【性数変化】</b> 男性名詞: <b>el día</b> / 複数: <b>los días</b>"),
    ("noche", "ノチェ", "女性名詞 [女]", "① 夜<br>② 【buenas noches】こんばんは、おやすみ<br>③ 【esta noche】今夜", "・<b>¡Buenas noches!</b>（おやすみなさい！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Buenas</b>(良い) + <b>noches</b>(夜)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la noche</b> / 複数: <b>las noches</b>"),
    ("tarde", "タルデ", "女性名詞 [女]", "① 午後、夕方<br>② 【buenas tardes】こんにちは<br>③ 【por la tarde】午後に", "・<b>¡Buenas tardes!</b>（こんにちは！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Buenas</b>(良い) + <b>tardes</b>(午後)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la tarde</b> / 複数: <b>las tardes</b>"),
    ("mañana", "マニャーナ", "女性名詞 [女]", "① 朝、午前中（la mañana）<br>② 明日（副詞: mañana）", "・<b>Por la mañana tomo café.</b>（朝はコーヒーを飲みます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por la mañana</b>(朝に) + <b>tomo</b>(飲む) + <b>café</b>(コーヒー)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la mañana</b> / 複数: <b>las mañanas</b>"),
    ("semana", "セマナ", "女性名詞 [女]", "① 週、1週間<br>② 【fin de semana】週末<br>③ 【la semana que viene】来週", "・<b>Buen fin de semana.</b>（良い週末を！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Buen</b>(良い) + <b>fin de semana</b>(週末)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la semana</b> / 複数: <b>las semanas</b>"),
    ("mes", "メス", "男性名詞 [男]", "① 月、1ヶ月", "・<b>El mes que viene voy a España.</b>（来月スペインに行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El mes que viene</b>(来月) + <b>voy a</b>(行く) + <b>España</b>(スペイン)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el mes</b> / 複数: <b>los meses</b> (-es付加)"),
    ("año", "アニョ", "男性名詞 [男]", "① 年、1年<br>② 年齢（歳）<br>③ 【¡Feliz Año Nuevo!】あけましておめでとう！", "・<b>Tengo veinte años.</b>（20歳です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo</b>(持つ) + <b>veinte</b>(20) + <b>años</b>(歳)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el año</b> / 複数: <b>los años</b>"),
    ("hora", "オラ", "女性名詞 [女]", "① 時間、時刻、1時間<br>② 【¿Qué hora es?】何時ですか？", "・<b>¿Qué hora es? - Son las dos.</b>（何時ですか？ - 2時です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Qué hora</b>(何時) + <b>es</b>(ですか) + <b>Son las dos</b>(2時です)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la hora</b> / 複数: <b>las horas</b>"),
    ("minuto", "ミヌート", "男性名詞 [男]", "① 分（60秒）<br>② 【un minuto】少々（待って）", "・<b>Espera un minuto, por favor.</b>（1分待ってください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Espera</b>(待って) + <b>un minuto</b>(1分)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el minuto</b> / 複数: <b>los minutos</b>"),
    ("dinero", "ディネロ", "男性名詞 [男]", "① お金、通貨、資金", "・<b>No tengo suficiente dinero.</b>（十分なお金がありません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No tengo</b>(持っていない) + <b>suficiente</b>(十分な) + <b>dinero</b>(お金)</span>", "日常・生活", "<b>【性数変化】</b> 不可算名詞: <b>el dinero</b>"),
    ("precio", "プレシオ", "男性名詞 [男]", "① 値段、価格、料金", "・<b>¿Cuál es el precio de este abrigo?</b>（このコートの値段はいくらですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuál es</b>(何ですか) + <b>el precio</b>(値段) + <b>de este abrigo</b>(このコートの)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el precio</b> / 複数: <b>los precios</b>"),
    ("tarjeta", "タルヘタ", "女性名詞 [女]", "① カード、クレジットカード（tarjeta de crédito）", "・<b>¿Aceptan tarjeta de crédito?</b>（クレジットカードは使えますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Aceptan</b>(受け付けますか) + <b>tarjeta de crédito</b>(クレジットカード)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la tarjeta</b> / 複数: <b>las tarjetas</b>"),
    ("efectivo", "エフェクティボ", "男性名詞 [男]", "① 現金、キャッシュ", "・<b>Prefiero pagar en efectivo.</b>（現金で払いたいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Prefiero</b>(〜を好む) + <b>pagar</b>(支払う) + <b>en efectivo</b>(現金で)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el efectivo</b>"),
    ("comida", "コミダ", "女性名詞 [女]", "① 食べ物、食事<br>② 昼食（スペインのメイン食）", "・<b>La comida española es deliciosa.</b>（スペイン料理はとても美味しいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La comida española</b>(スペイン料理) + <b>es</b>(〜です) + <b>deliciosa</b>(美味しい)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la comida</b> / 複数: <b>las comidas</b>"),
    ("agua", "アグア", "女性名詞 [女 ※単数形はel agua]", "① 水、飲料水（el agua）", "・<b>Un vaso de agua, por favor.</b>（お水をコップ1杯ください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Un vaso</b>(コップ1杯) + <b>de agua</b>(水の) + <b>por favor</b>(お願いします)</span>", "日常・生活", "<b>【特殊性数】</b> 単数: <b>el agua</b> (女性名詞だが発音上el) / 複数: <b>las aguas</b>"),
    ("pan", "パン", "男性名詞 [男]", "① パン", "・<b>Compro pan fresco todos los días.</b>（毎日焼きたてのパンを買います）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Compro</b>(買う) + <b>pan fresco</b>(新鮮なパン) + <b>todos los días</b>(毎日)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el pan</b> / 複数: <b>los panes</b>"),
    ("café", "カフェ", "男性名詞 [男]", "① コーヒー<br>② 喫茶店、カフェ", "・<b>Tomo una taza de café por la mañana.</b>（朝コーヒーを1杯飲みます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tomo</b>(飲む) + <b>una taza</b>(カップ1杯) + <b>de café</b>(コーヒーの)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el café</b> / 複数: <b>los cafés</b>"),
    ("leche", "レチェ", "女性名詞 [女]", "① 牛乳、ミルク<br>② 【café con leche】カフェラテ", "・<b>¿Tomas café con leche?</b>（ミルク入りコーヒーを飲みますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tomas</b>(飲むか) + <b>café con leche</b>(カフェラテ)</span>", "日常・生活", "<b>【性数変化】</b> 女性名詞: <b>la leche</b>"),
    ("té", "テ", "男性名詞 [男]", "① お茶、紅茶", "・<b>Prefiero el té verde.</b>（私は緑茶のほうが好きです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Prefiero</b>(好む) + <b>el té verde</b>(緑茶)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el té</b> / 複数: <b>los tés</b>"),
    ("vino", "ビノ", "男性名詞 [男]", "① ワイン、ぶどう酒（vino tinto 赤ワイン / blanco 白）", "・<b>Una copa de vino tinto, por favor.</b>（赤ワインをグラスで1杯ください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Una copa</b>(グラス1杯) + <b>de vino tinto</b>(赤ワインの)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el vino</b> / 複数: <b>los vinos</b>"),
    ("cerveza", "セルベサ", "女性名詞 [女]", "① ビール<br>② 【una caña】生ビール1杯", "・<b>¡Una cerveza bien fría, por favor!</b>（よく冷えたビールを1本ください！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Una cerveza</b>(ビール1本) + <b>bien fría</b>(よく冷えた)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la cerveza</b> / 複数: <b>las cervezas</b>"),
    ("carne", "カルネ", "女性名詞 [女]", "① 肉、肉料理", "・<b>Me gusta la carne asada.</b>（焼肉が好きです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me gusta</b>(好きだ) + <b>la carne asada</b>(ロースト肉/焼肉)</span>", "日常・生活", "<b>【性数変化】</b> 女性名詞: <b>la carne</b>"),
    ("pescado", "ペスカド", "男性名詞 [男]", "① 魚、魚料理（※生きた魚は pez）", "・<b>En España comen mucho pescado fresco.</b>（スペインでは新鮮な魚をたくさん食べます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>En España</b>(スペインでは) + <b>comen</b>(食べる) + <b>pescado fresco</b>(新鮮な魚)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el pescado</b> / 複数: <b>los pescados</b>"),
    ("arroz", "アロス", "男性名詞 [男]", "① 米、ご飯、米料理", "・<b>La paella se hace con arroz.</b>（パエリアはお米で作られます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La paella</b>(パエリア) + <b>se hace</b>(作られる) + <b>con arroz</b>(お米で)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el arroz</b> / 複数: <b>los arroces</b> (z➔c)"),
    ("fruta", "フルタ", "女性名詞 [女]", "① 果物、フルーツ", "・<b>Como fruta para el desayuno.</b>（朝食に果物を食べます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Como</b>(食べる) + <b>fruta</b>(果物) + <b>para el desayuno</b>(朝食のために)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la fruta</b> / 複数: <b>las frutas</b>"),
    ("manzana", "マンサナ", "女性名詞 [女]", "① りんご<br>② 街の1ブロック", "・<b>Una manzana al día es buena.</b>（1日1個のりんごは良い）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Una manzana</b>(りんご1個) + <b>al día</b>(1日につき) + <b>es buena</b>(良い)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la manzana</b> / 複数: <b>las manzanas</b>"),
    ("mesa", "メサ", "女性名詞 [女]", "① テーブル、机、食卓", "・<b>Una mesa para dos personas, por favor.</b>（2人用の席をお願いします）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Una mesa</b>(テーブル) + <b>para dos personas</b>(2人用の)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la mesa</b> / 複数: <b>las mesas</b>"),
    ("silla", "シージャ", "女性名詞 [女]", "① 椅子、腰掛け", "・<b>Toma una silla y siéntate.</b>（椅子を持ってきて座って）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Toma</b>(取って) + <b>una silla</b>(椅子) + <b>y</b>(そして) + <b>siéntate</b>(座りなさい)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la silla</b> / 複数: <b>las sillas</b>"),
    ("puerta", "プエルタ", "女性名詞 [女]", "① ドア、扉、門、搭乗口（空港のゲート）", "・<b>Cierra la puerta al salir.</b>（出る時にドアを閉めてね）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cierra</b>(閉めて) + <b>la puerta</b>(ドア) + <b>al salir</b>(出る時に)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la puerta</b> / 複数: <b>las puertas</b>"),
    ("ventana", "ベンタナ", "女性名詞 [女]", "① 窓", "・<b>Abre la ventana para ventilar.</b>（換気のために窓を開けて）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Abre</b>(開けて) + <b>la ventana</b>(窓) + <b>para ventilar</b>(換気するために)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la ventana</b> / 複数: <b>las ventanas</b>"),
    ("cama", "カマ", "女性名詞 [女]", "① ベッド、寝床", "・<b>Voy a la cama, tengo sueño.</b>（眠いのでベッドに行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy a</b>(行く) + <b>la cama</b>(ベッド) + <b>tengo sueño</b>(眠気がある)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la cama</b> / 複数: <b>las camas</b>"),
    ("ropa", "ロパ", "女性名詞 [女]", "① 衣服、服、洋服", "・<b>Compré ropa nueva para el viaje.</b>（旅行のために新しい服を買いました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Compré</b>(買った) + <b>ropa nueva</b>(新しい服) + <b>para el viaje</b>(旅行のために)</span>", "日常・生活", "<b>【性数変化】</b> 集合名詞: <b>la ropa</b>"),
    ("zapato", "サパト", "男性名詞 [男]", "① 靴、シューズ（通常複数は zapatos）", "・<b>Estos zapatos son muy cómodos.</b>（この靴はとても快適です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estos zapatos</b>(この靴) + <b>son</b>(〜です) + <b>muy cómodos</b>(とても快適な)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el zapato</b> / 複数: <b>los zapatos</b>"),
    ("libro", "リブロ", "男性名詞 [男]", "① 本、書籍、教科書", "・<b>Estoy leyendo un libro muy interesante.</b>（とても面白い本を読んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy leyendo</b>(読んでいる) + <b>un libro interesante</b>(面白い本)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el libro</b> / 複数: <b>los libros</b>"),
    ("carta", "カルタ", "女性名詞 [女]", "① 手紙<br>② レストランのメニュー表", "・<b>¿Nos trae la carta, por favor?</b>（メニューを持ってきてくれますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Nos trae</b>(私たちに持ってくる) + <b>la carta</b>(メニュー表)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la carta</b> / 複数: <b>las cartas</b>"),
    ("teléfono", "テレフォノ", "男性名詞 [男]", "① 電話、スマートフォン（teléfono móvil）", "・<b>¿Cuál es tu número de teléfono?</b>（君の電話番号は何番？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuál es</b>(何ですか) + <b>tu número</b>(君の番号) + <b>de teléfono</b>(電話の)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el teléfono</b> / 複数: <b>los teléfonos</b>"),
    ("móvil", "モビル", "男性名詞 [男]", "① 携帯電話、スマホ（スペインで頻用）", "・<b>Olvidé mi móvil en casa.</b>（家にスマホを忘れてきました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Olvidé</b>(忘れた [点過去]) + <b>mi móvil</b>(私のスマホ) + <b>en casa</b>(家で)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el móvil</b> / 複数: <b>los móviles</b>"),
    ("llave", "ジャベ", "女性名詞 [女]", "① 鍵、キー", "・<b>No encuentro las llaves de mi casa.</b>（家の鍵が見つかりません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No encuentro</b>(見つからない) + <b>las llaves</b>(鍵) + <b>de mi casa</b>(家の)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>la llave</b> / 複数: <b>las llaves</b>"),
    ("bolso", "ボルソ", "男性名詞 [男]", "① ハンドバッグ、鞄、バッグ", "・<b>Llevo la cartera en el bolso.</b>（バッグの中に財布を入れています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llevo</b>(持っている/入れる) + <b>la cartera</b>(財布) + <b>en el bolso</b>(バッグに)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el bolso</b> / 複数: <b>los bolsos</b>"),
    ("baño", "バニョ", "男性名詞 [男]", "① トイレ、浴室、お手洗い<br>② 【¿Dónde está el baño?】トイレはどこ？", "・<b>Perdón, ¿dónde está el baño?</b>（すみません、トイレはどこですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Perdón</b>(すみません) + <b>dónde está</b>(どこにありますか) + <b>el baño</b>(トイレ)</span>", "日常・生活", "<b>【性数変化】</b> 単数: <b>el baño</b> / 複数: <b>los baños</b>"),

    # ==========================================
    # 3. 人物・家族・職業名詞 (18語)
    # ==========================================
    ("persona", "ペルソナ", "女性名詞 [女]", "① 人、人物、人間（常に女性名詞）", "・<b>Ella es una persona muy amable.</b>（彼女はとても親切な人です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ella es</b>(彼女は〜です) + <b>una persona</b>(人) + <b>muy amable</b>(とても親切な)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>la persona</b> / 複数: <b>las personas</b>"),
    ("amigo", "アミゴ", "男性名詞 [男]", "① 友人、友達（女性の友達は amiga）", "・<b>Juan es mi mejor amigo.</b>（フアンは私の親友です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>es</b>(〜です) + <b>mi mejor amigo</b>(私の親友/最高の友)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>amigo</b> / 女単: <b>amiga</b> / 男複: <b>amigos</b> / 女複: <b>amigas</b>"),
    ("familia", "ファミリア", "女性名詞 [女]", "① 家族、親族", "・<b>Mi familia vive en Japón.</b>（私の家族は日本に住んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mi familia</b>(私の家族) + <b>vive</b>(住んでいる) + <b>en Japón</b>(日本に)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>la familia</b> / 複数: <b>las familias</b>"),
    ("padre", "パドレ", "男性名詞 [男]", "① 父親、お父さん（複数は padres 両親）", "・<b>Mis padres están bien de salud.</b>（私の両親は元気です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mis padres</b>(私の両親) + <b>están bien</b>(元気でいる)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>el padre</b> / 複数: <b>los padres</b> (両親/父親たち)"),
    ("madre", "マドレ", "女性名詞 [女]", "① 母親、お母さん", "・<b>Mi madre cocina muy rico.</b>（母は料理がとても上手です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mi madre</b>(私の母) + <b>cocina</b>(料理する) + <b>muy rico</b>(とても美味しく)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>la madre</b> / 複数: <b>las madres</b>"),
    ("hijo", "イホ", "男性名詞 [男]", "① 息子（娘は hija、子どもたちは hijos）", "・<b>Tengo dos hijos: un niño y una niña.</b>（私には息子と娘がいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo</b>(持つ) + <b>dos hijos</b>(2人の子ども) + <b>un niño</b>(男の子) + <b>una niña</b>(女の子)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>hijo</b> / 女単: <b>hija</b> / 複数: <b>hijos</b> (子どもたち)"),
    ("hermano", "エルマノ", "男性名詞 [男]", "① 兄弟、兄、弟（姉妹は hermana）", "・<b>Mi hermano mayor vive en Madrid.</b>（私の兄はマドリードに住んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mi hermano mayor</b>(私の兄) + <b>vive en</b>(住んでいる) + <b>Madrid</b>(マドリード)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>hermano</b> / 女単: <b>hermana</b> / 複数: <b>hermanos</b> (兄弟たち)"),
    ("abuelo", "アブエロ", "男性名詞 [男]", "① 祖父、おじいちゃん（祖母は abuela）", "・<b>Visito a mis abuelos en verano.</b>（夏に祖父母を訪ねます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Visito a</b>(〜を訪ねる) + <b>mis abuelos</b>(私の祖父母) + <b>en verano</b>(夏に)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>abuelo</b> / 女単: <b>abuela</b> / 複数: <b>abuelos</b> (祖父母)"),
    ("hombre", "オンブレ", "男性名詞 [男]", "① 男性、男の人、大人", "・<b>Aquel hombre es mi profesor.</b>（あの男性は私の先生です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Aquel hombre</b>(あの男性) + <b>es</b>(〜です) + <b>mi profesor</b>(私の先生)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>el hombre</b> / 複数: <b>los hombres</b>"),
    ("mujer", "ムヘール", "女性名詞 [女]", "① 女性、女の人<br>② 妻、奥さん", "・<b>Es una mujer muy trabajadora.</b>（彼女はとても働き者の女性です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es</b>(〜です) + <b>una mujer</b>(女性) + <b>muy trabajadora</b>(とても働き者の)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>la mujer</b> / 複数: <b>las mujeres</b>"),
    ("niño", "ニーニョ", "男性名詞 [男]", "① 男の子、子ども（女の子は niña）", "・<b>Los niños juegan en el parque.</b>（子どもたちが公園で遊んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Los niños</b>(子どもたち) + <b>juegan</b>(遊ぶ) + <b>en el parque</b>(公園で)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>niño</b> / 女単: <b>niña</b> / 複数: <b>niños</b> (子どもたち)"),
    ("chico", "チコ", "男性名詞 [男]", "① 少年、若い男の子（女の子は chica）", "・<b>Ese chico es muy simpático.</b>（その男の子はとても感じが良いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ese chico</b>(その男の子) + <b>es</b>(〜です) + <b>muy simpático</b>(とても感じが良い)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>chico</b> / 女単: <b>chica</b> / 男複: <b>chicos</b> / 女複: <b>chicas</b>"),
    ("profesor", "プロフェソール", "男性名詞 [男]", "① 教師、先生、教授（女性は profesora）", "・<b>El profesor explica muy bien.</b>（先生はとても分かりやすく説明してくれます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El profesor</b>(先生) + <b>explica</b>(説明する) + <b>muy bien</b>(とても上手に)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>profesor</b> / 女単: <b>profesora</b> / 男複: <b>profesores</b> / 女複: <b>profesoras</b>"),
    ("estudiante", "エストゥディアンテ", "名詞 [男女同形]", "① 学生、生徒", "・<b>Soy estudiante de español.</b>（私はスペイン語の学生です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Soy</b>(私は〜です) + <b>estudiante</b>(学生) + <b>de español</b>(スペイン語の)</span>", "人物・家族", "<b>【男女同形】</b> 男性: <b>el estudiante</b> / 女性: <b>la estudiante</b> / 複数: <b>estudiantes</b>"),
    ("médico", "メディコ", "男性名詞 [男]", "① 医者、医師（女性医師は médica）", "・<b>Tengo que ir al médico hoy.</b>（今日お医者さんに行かなければなりません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo que ir</b>(行かねばならない) + <b>al médico</b>(医者に) + <b>hoy</b>(今日)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>médico</b> / 女単: <b>médica</b> / 複数: <b>médicos</b>"),
    ("camarero", "カマレロ", "男性名詞 [男]", "① ウェイター、給仕（女性は camarera）", "・<b>¡Camarero, la cuenta por favor!</b>（店員さん、お会計をお願いします！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Camarero</b>(店員さん) + <b>la cuenta</b>(お会計) + <b>por favor</b>(お願いします)</span>", "人物・家族", "<b>【男女・性数】</b> 男単: <b>camarero</b> / 女単: <b>camarera</b> / 複数: <b>camareros</b>"),
    ("nombre", "ノンブレ", "男性名詞 [男]", "① 名前、氏名<br>② 【¿Cómo es tu nombre?】名前は何？", "・<b>Mi nombre es Taro Yamada.</b>（私の名前は山田太郎です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mi nombre</b>(私の名前) + <b>es</b>(〜です) + <b>Taro Yamada</b>(山田太郎)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>el nombre</b> / 複数: <b>los nombres</b>"),
    ("apellido", "アペジード", "男性名詞 [男]", "① 苗字、姓", "・<b>¿Cómo se escribe tu apellido?</b>（苗字はどう書きますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cómo se escribe</b>(どう書かれますか) + <b>tu apellido</b>(君の苗字)</span>", "人物・家族", "<b>【性数変化】</b> 単数: <b>el apellido</b> / 複数: <b>los apellidos</b>"),

    # ==========================================
    # 4. 街・旅行・交通・場所名詞 (22語)
    # ==========================================
    ("ciudad", "シウダッ(ド)", "女性名詞 [女]", "① 都市、街、都会", "・<b>Madrid es una ciudad hermosa.</b>（マドリードは美しい街です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Madrid</b>(マドリード) + <b>es</b>(〜です) + <b>una ciudad hermosa</b>(美しい街)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la ciudad</b> / 複数: <b>las ciudades</b>"),
    ("país", "パイス", "男性名詞 [男]", "① 国、国家", "・<b>España es un país fascinante.</b>（スペインは魅力的な国です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>España</b>(スペイン) + <b>es</b>(〜です) + <b>un país fascinante</b>(魅力的な国)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el país</b> / 複数: <b>los países</b>"),
    ("calle", "カジェ", "女性名詞 [女]", "① 通り、道、街路", "・<b>¿En qué calle está?</b>（何通りにありますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>En qué calle</b>(何通りに) + <b>está</b>(ありますか)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la calle</b> / 複数: <b>las calles</b>"),
    ("plaza", "プラサ", "女性名詞 [女]", "① 広場（例: Plaza Mayor マヨール広場）", "・<b>Nos vemos en la plaza.</b>（広場で会いましょう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Nos vemos</b>(会う) + <b>en la plaza</b>(広場で)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la plaza</b> / 複数: <b>las plazas</b>"),
    ("estación", "エスタシオン", "女性名詞 [女]", "① 駅（estación de tren 電車駅）<br>② 季節（estaciones del año 四季）", "・<b>El hotel está cerca de la estación.</b>（ホテルは駅の近くにあります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El hotel</b>(ホテル) + <b>está cerca de</b>(〜の近くにある) + <b>la estación</b>(駅)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la estación</b> / 複数: <b>las estaciones</b>"),
    ("aeropuerto", "アエロプエルト", "男性名詞 [男]", "① 空港", "・<b>Voy al aeropuerto en taxi.</b>（タクシーで空港に行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy al aeropuerto</b>(空港へ行く) + <b>en taxi</b>(タクシーで)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el aeropuerto</b> / 複数: <b>los aeropuertos</b>"),
    ("hotel", "オテル", "男性名詞 [男]", "① ホテル、宿", "・<b>Tengo una reserva en este hotel.</b>（このホテルに予約があります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo</b>(持つ) + <b>una reserva</b>(予約) + <b>en este hotel</b>(このホテルに)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el hotel</b> / 複数: <b>los hoteles</b>"),
    ("restaurante", "レスタウランテ", "男性名詞 [男]", "① レストラン、飲食店", "・<b>Vamos a cenar a un restaurante.</b>（レストランへ夕食に行きましょう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vamos a cenar</b>(夕食に行こう) + <b>a un restaurante</b>(レストランへ)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el restaurante</b> / 複数: <b>los restaurantes</b>"),
    ("tienda", "ティエンダ", "女性名詞 [女]", "① 店、売店、ショップ", "・<b>Esta tienda vende ropa muy bonita.</b>（この店は可愛い服を売っています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Esta tienda</b>(この店) + <b>vende</b>(売る) + <b>ropa bonita</b>(可愛い服)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la tienda</b> / 複数: <b>las tiendas</b>"),
    ("supermercado", "スペルメルカード", "男性名詞 [男]", "① スーパーマーケット", "・<b>Voy al supermercado a comprar comida.</b>（食べ物を買いにスーパーへ行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy al supermercado</b>(スーパーへ行く) + <b>a comprar</b>(買いに) + <b>comida</b>(食べ物)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el supermercado</b> / 複数: <b>los supermercados</b>"),
    ("museo", "ムセオ", "男性名詞 [男]", "① 博物館、美術館（Museo del Prado プラド美術館）", "・<b>Ayer visité el museo.</b>（昨日美術館を訪れました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ayer</b>(昨日) + <b>visité</b>(訪れた [点過去]) + <b>el museo</b>(美術館)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el museo</b> / 複数: <b>los museos</b>"),
    ("playa", "プラジャ", "女性名詞 [女]", "① 砂浜、ビーチ、海岸", "・<b>Me encanta nadar en la playa.</b>（ビーチで泳ぐのが大好きです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me encanta</b>(大好きだ) + <b>nadar</b>(泳ぐこと) + <b>en la playa</b>(ビーチで)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la playa</b> / 複数: <b>las playas</b>"),
    ("parque", "パルケ", "男性名詞 [男]", "① 公園", "・<b>Paseo por el parque todos los días.</b>（毎日公園を散歩します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Paseo por</b>(〜を通って散歩する) + <b>el parque</b>(公園)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el parque</b> / 複数: <b>los parques</b>"),
    ("tren", "トレン", "男性名詞 [男]", "① 電車、列車、鉄道", "・<b>Viajo en tren a Barcelona.</b>（バルセロナへ電車で旅します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Viajo</b>(旅する) + <b>en tren</b>(電車で) + <b>a Barcelona</b>(バルセロナへ)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el tren</b> / 複数: <b>los trenes</b>"),
    ("autobús", "アウトブス", "男性名詞 [男]", "① バス、路線バス", "・<b>El autobús va al centro.</b>（バスは中心部へ行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El autobús</b>(バス) + <b>va al centro</b>(中心部へ行く)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el autobús</b> / 複数: <b>los autobuses</b>"),
    ("metro", "メトロ", "男性名詞 [男]", "① 地下鉄", "・<b>Es más rápido ir en metro.</b>（地下鉄で行くほうが早いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es más rápido</b>(より速い) + <b>ir en metro</b>(地下鉄で行くこと)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el metro</b>"),
    ("taxi", "タクシ", "男性名詞 [男]", "① タクシー", "・<b>Vamos a tomar un taxi.</b>（タクシーに乗りましょう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vamos a</b>(〜しよう) + <b>tomar un taxi</b>(タクシーに乗る)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el taxi</b> / 複数: <b>los taxis</b>"),
    ("coche", "コチェ", "男性名詞 [男]", "① 自動車、車（中南米では auto / carro）", "・<b>Voy al trabajo en coche.</b>（車で通勤します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy al trabajo</b>(仕事に行く) + <b>en coche</b>(車で)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el coche</b> / 複数: <b>los coches</b>"),
    ("avión", "アビオン", "男性名詞 [男]", "① 飛行機", "・<b>El avión sale a las tres.</b>（飛行機は3時に出発します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El avión</b>(飛行機) + <b>sale</b>(出発する) + <b>a las tres</b>(3時に)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el avión</b> / 複数: <b>los aviones</b>"),
    ("billete", "ビジェテ", "男性名詞 [男]", "① 切符、チケット、紙幣（中南米では boleto）", "・<b>Un billete de ida y vuelta, por favor.</b>（往復切符を1枚ください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Un billete</b>(切符1枚) + <b>de ida y vuelta</b>(往復の)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el billete</b> / 複数: <b>los billetes</b>"),
    ("viaje", "ビアヘ", "男性名詞 [男]", "① 旅行、旅<br>② 【¡Buen viaje!】良い旅を！", "・<b>¡Buen viaje a España!</b>（スペインへの良い旅を！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Buen viaje</b>(良い旅を) + <b>a España</b>(スペインへ)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>el viaje</b> / 複数: <b>los viajes</b>"),
    ("maleta", "マレタ", "女性名詞 [女]", "① スーツケース、旅行カバン", "・<b>Tengo que preparar mi maleta.</b>（スーツケースを準備しなきゃ）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo que preparar</b>(準備せねばならない) + <b>mi maleta</b>(私のスーツケース)</span>", "街・旅行", "<b>【性数変化】</b> 単数: <b>la maleta</b> / 複数: <b>las maletas</b>"),

    # ==========================================
    # 5. 性格・感情・評価・状態形容詞 (30語)
    # ==========================================
    ("bueno", "ブエノ", "形容詞 [形]", "① 良い、優れた（ser bueno）<br>② 優しい、親切な<br>③ 美味しい（estar bueno）", "・<b>Es un buen libro.</b>（良い本です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es</b>(〜です) + <b>un buen libro</b>(良い本)</span><br>・<b>La sopa está muy buena.</b>（スープがとても美味しいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La sopa</b>(スープ) + <b>está muy buena</b>(とても美味しい/状態)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>bueno (buen)</b> / 女単: <b>buena</b> / 男複: <b>buenos</b> / 女複: <b>buenas</b>"),
    ("malo", "マロ", "形容詞 [形]", "① 悪い、有害な<br>② 体調が悪い（estar malo）<br>③ 不味い（estar malo）", "・<b>Fumar es malo para la salud.</b>（喫煙は健康に悪いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Fumar</b>(喫煙) + <b>es malo</b>(悪いです) + <b>para la salud</b>(健康のために)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>malo (mal)</b> / 女単: <b>mala</b> / 男複: <b>malos</b> / 女複: <b>malas</b>"),
    ("grande", "グランデ", "形容詞 [形]", "① 大きい、広い<br>② 偉大な（名詞の前で gran）", "・<b>Mi casa tiene una cocina grande.</b>（私の家には広いキッチンがあります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mi casa</b>(私の家) + <b>tiene</b>(持つ) + <b>una cocina grande</b>(広い台所)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>grande (gran)</b> / 複数: <b>grandes</b>"),
    ("pequeño", "ペケーニョ", "形容詞 [形]", "① 小さい、狭い<br>② 幼い、年下の", "・<b>Vivo en un apartamento pequeño.</b>（小さなアパートに住んでいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vivo en</b>(〜に住む) + <b>un apartamento pequeño</b>(小さなアパート)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>pequeño</b> / 女単: <b>pequeña</b> / 男複: <b>pequeños</b> / 女複: <b>pequeñas</b>"),
    ("nuevo", "ヌエボ", "形容詞 [形]", "① 新しい、新品の", "・<b>Compré un coche nuevo.</b>（新しい車を買いました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Compré</b>(買った) + <b>un coche nuevo</b>(新しい車)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>nuevo</b> / 女単: <b>nueva</b> / 男複: <b>nuevos</b> / 女複: <b>nuevas</b>"),
    ("viejo", "ビエホ", "形容詞 [形]", "① 古い、年をとった<br>② 【un viejo amigo】旧友", "・<b>Es un edificio muy viejo.</b>（とても古い建物です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es</b>(〜です) + <b>un edificio viejo</b>(古い建物)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>viejo</b> / 女単: <b>vieja</b> / 男複: <b>viejos</b> / 女複: <b>viejas</b>"),
    ("bonito", "ボニート", "形容詞 [形]", "① きれいな、美しい、可愛い", "・<b>¡Qué flores tan bonitas!</b>（なんて綺麗なお花！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Qué flores</b>(何という花) + <b>tan bonitas</b>(とても綺麗な)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>bonito</b> / 女単: <b>bonita</b> / 男複: <b>bonitos</b> / 女複: <b>bonitas</b>"),
    ("hermoso", "エルモソ", "形容詞 [形]", "① 美しい、見事な、素晴らしい", "・<b>Es una vista hermosa.</b>（見事な景色です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es</b>(〜です) + <b>una vista hermosa</b>(美しい眺め)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>hermoso</b> / 女単: <b>hermosa</b> / 男複: <b>hermosos</b> / 女複: <b>hermosas</b>"),
    ("feo", "フェオ", "形容詞 [形]", "① 醜い、見苦しい、不格好な", "・<b>Hoy hace un día feo.</b>（今日は嫌な天気です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hoy hace</b>(今日は〜だ) + <b>un día feo</b>(嫌な/崩れた日)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>feo</b> / 女単: <b>fea</b> / 男複: <b>feos</b> / 女複: <b>feas</b>"),
    ("fácil", "ファシル", "形容詞 [形]", "① 簡単な、易しい", "・<b>El examen fue muy fácil.</b>（試験はとても簡単でした）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El examen</b>(試験) + <b>fue</b>(〜だった [点過去]) + <b>muy fácil</b>(とても簡単)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>fácil</b> / 複数: <b>fáciles</b>"),
    ("difícil", "ディフィシル", "形容詞 [形]", "① 難しい、困難な", "・<b>La pronunciación no es difícil.</b>（発音は難しくありません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La pronunciación</b>(発音) + <b>no es difícil</b>(難しくない)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>difícil</b> / 複数: <b>difíciles</b>"),
    ("importante", "インポルタンテ", "形容詞 [形]", "① 重要な、大切な", "・<b>Es una reunión muy importante.</b>（とても重要な会議です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es</b>(〜です) + <b>una reunión importante</b>(重要な会議)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>importante</b> / 複数: <b>importantes</b>"),
    ("necesario", "ネセサリオ", "形容詞 [形]", "① 必要な、不可欠な", "・<b>Es necesario practicar todos los días.</b>（毎日練習することが必要です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es necesario</b>(必要です) + <b>practicar</b>(練習すること)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>necesario</b> / 女単: <b>necesaria</b> / 男複: <b>necesarios</b> / 女複: <b>necesarias</b>"),
    ("posible", "ポシブレ", "形容詞 [形]", "① 可能な、あり得る<br>② 【lo antes posible】できるだけ早く", "・<b>Llámame lo antes posible.</b>（できるだけ早く電話して）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llámame</b>(電話して) + <b>lo antes posible</b>(可能な限り早く)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>posible</b> / 複数: <b>posibles</b>"),
    ("imposible", "インポシブレ", "形容詞 [形]", "① 不可能な、あり得ない", "・<b>Nada es imposible.</b>（不可能なことは何もない）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Nada</b>(何ものも) + <b>es imposible</b>(不可能ではない)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>imposible</b> / 複数: <b>imposibles</b>"),
    ("caro", "カロ", "形容詞 [形]", "① （値段が）高い、高価な", "・<b>Este restaurante es un poco caro.</b>（このレストランは少し高いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Este restaurante</b>(この店) + <b>es un poco caro</b>(少し高い)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>caro</b> / 女単: <b>cara</b> / 男複: <b>caros</b> / 女複: <b>caras</b>"),
    ("barato", "バラト", "形容詞 [形]", "① （値段が）安い、お手頃な", "・<b>Encontré un hotel muy barato.</b>（とても安いホテルを見つけました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Encontré</b>(見つけた) + <b>un hotel barato</b>(安いホテル)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>barato</b> / 女単: <b>barata</b> / 男複: <b>baratos</b> / 女複: <b>baratas</b>"),
    ("rápido", "ラピド", "形容詞・副詞 [形/副]", "① 速い、素早い、迅速な", "・<b>El AVE es un tren muy rápido.</b>（AVEはとても速い列車です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El AVE</b>(スペイン新幹線) + <b>es un tren rápido</b>(速い列車です)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>rápido</b> / 女単: <b>rápida</b> / 男複: <b>rápidos</b> / 女複: <b>rápidas</b>"),
    ("lento", "レント", "形容詞 [形]", "① 遅い、ゆっくりした", "・<b>El autobús va muy lento.</b>（バスがとても遅いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El autobús</b>(バス) + <b>va muy lento</b>(とても遅く進む)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>lento</b> / 女単: <b>lenta</b> / 男複: <b>lentos</b> / 女複: <b>lentas</b>"),
    ("contento", "コンテント", "形容詞 [形]", "① 満足した、喜んでいる、嬉しい（estar）", "・<b>Estoy muy contento con mis notas.</b>（成績に満足しています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy contento</b>(満足している) + <b>con mis notas</b>(私の成績に)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>contento</b> / 女単: <b>contenta</b> / 男複: <b>contentos</b> / 女複: <b>contentas</b>"),
    ("feliz", "フェリス", "形容詞 [形]", "① 幸せな、幸福な<br>② 【¡Feliz cumpleaños!】お誕生日おめでとう！", "・<b>¡Feliz cumpleaños, amigo!</b>（誕生日おめでとう！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Feliz</b>(幸せな) + <b>cumpleaños</b>(誕生日) + <b>amigo</b>(友よ)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>feliz</b> / 複数: <b>felices</b> (z➔c)"),
    ("triste", "トリステ", "形容詞 [形]", "① 悲しい、憂鬱な", "・<b>¿Por qué estás triste hoy?</b>（どうして今日悲しそうなの？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por qué</b>(なぜ) + <b>estás triste</b>(悲しい状態なのか) + <b>hoy</b>(今日)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>triste</b> / 複数: <b>tristes</b>"),
    ("cansado", "カンサード", "形容詞 [形]", "① 疲れている、くたくたな（estar）", "・<b>Estoy muy cansado de trabajar.</b>（働きすぎて疲れています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy cansado</b>(疲れている) + <b>de trabajar</b>(働くことで)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>cansado</b> / 女単: <b>cansada</b> / 男複: <b>cansados</b> / 女複: <b>cansadas</b>"),
    ("ocupado", "オクパード", "形容詞 [形]", "① 忙しい、ふさがっている（estar）", "・<b>Esta semana estoy muy ocupado.</b>（今週はとても忙しいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Esta semana</b>(今週) + <b>estoy ocupado</b>(私は忙しい)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>ocupado</b> / 女単: <b>ocupada</b> / 男複: <b>ocupados</b> / 女複: <b>ocupadas</b>"),
    ("libre", "リブレ", "形容詞 [形]", "① 自由な、暇な、空いている", "・<b>¿Estás libre esta tarde?</b>（今日の午後空いてる？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estás libre</b>(君は空いているか) + <b>esta tarde</b>(今日の午後)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>libre</b> / 複数: <b>libres</b>"),
    ("limpio", "リンピオ", "形容詞 [形]", "① 清潔な、綺麗な、汚れていない", "・<b>La habitación está muy limpia.</b>（部屋はとても綺麗です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La habitación</b>(部屋) + <b>está limpia</b>(綺麗である)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>limpio</b> / 女単: <b>limpia</b> / 男複: <b>limpios</b> / 女複: <b>limpias</b>"),
    ("sucio", "スシオ", "形容詞 [形]", "① 汚れた、不潔な", "・<b>Mis zapatos están sucios.</b>（靴が汚れています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mis zapatos</b>(私の靴) + <b>están sucios</b>(汚れている)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>sucio</b> / 女単: <b>sucia</b> / 男複: <b>sucios</b> / 女複: <b>sucias</b>"),
    ("caliente", "カリエンテ", "形容詞 [形]", "① 熱い、温かい", "・<b>Cuidado, el café está caliente.</b>（気をつけて、コーヒーが熱いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuidado</b>(気をつけて) + <b>el café</b>(コーヒー) + <b>está caliente</b>(熱い)</span>", "形容詞", "<b>【男女同形】</b> 単数: <b>caliente</b> / 複数: <b>calientes</b>"),
    ("frío", "フリオ", "形容詞・名詞 [形/男]", "① 冷たい、寒い<br>② 寒さ（Tengo frío 寒い）", "・<b>Quiero agua bien fría.</b>（よく冷えた水が欲しいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero</b>(欲しい) + <b>agua fría</b>(冷たい水)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>frío</b> / 女単: <b>fría</b> / 男複: <b>fríos</b> / 女複: <b>frías</b>"),
    ("simpático", "シンパティコ", "形容詞 [形]", "① 感じの良い、親しみやすい、優しい", "・<b>Los españoles son simpáticos.</b>（スペイン人は親しみやすいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Los españoles</b>(スペイン人) + <b>son simpáticos</b>(親しみやすい)</span>", "形容詞", "<b>【男女・性数】</b> 男単: <b>simpático</b> / 女単: <b>simpática</b> / 男複: <b>simpáticos</b> / 女複: <b>simpáticas</b>"),

    # ==========================================
    # 6. 副詞・前置詞・接続詞・重要表現 (34語)
    # ==========================================
    ("aquí", "アキ", "副詞 [副]", "① ここ、こちら（話し手の近く）", "・<b>Ven aquí, por favor.</b>（ここに来てください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ven</b>(来て [命令]) + <b>aquí</b>(ここへ) + <b>por favor</b>(お願いします)</span>", "副詞・前置詞", "<b>【位置対応】</b> aquí (ここ) ➔ ahí (そこ) ➔ allí (あそこ)"),
    ("ahí", "アイ", "副詞 [副]", "① そこ（聞き手の近く）", "・<b>Déjalo ahí, por favor.</b>（そこに置いておいて）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Déjalo</b>(それを置いて) + <b>ahí</b>(そこに)</span>", "副詞・前置詞", "<b>【位置対応】</b> aquí (ここ) ➔ ahí (そこ) ➔ allí (あそこ)"),
    ("allí", "アジー", "副詞 [副]", "① あそこ、向こう（双方から離れた場所）", "・<b>Mi casa está allí.</b>（私の家はあそこにあります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mi casa</b>(私の家) + <b>está allí</b>(あそこにある)</span>", "副詞・前置詞", "<b>【位置対応】</b> aquí (ここ) ➔ ahí (そこ) ➔ allí (あそこ)"),
    ("ahora", "アオラ", "副詞 [副]", "① 今、現在<br>② 【ahora mismo】今すぐ", "・<b>Ahora estoy estudiando.</b>（今勉強しているところです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ahora</b>(今) + <b>estoy estudiando</b>(勉強中だ)</span>", "副詞・前置詞", "<b>【派生表現】</b> ahora mismo (たった今/今すぐ)"),
    ("hoy", "オイ", "副詞 [副]", "① 今日、本日", "・<b>Hoy es un día especial.</b>（今日は特別な日です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hoy es</b>(今日は〜だ) + <b>un día especial</b>(特別な日)</span>", "副詞・前置詞", "<b>【時間対比】</b> ayer (昨日) ➔ hoy (今日) ➔ mañana (明日)"),
    ("ayer", "アジェール", "副詞 [副]", "① 昨日", "・<b>Ayer fui al cine con María.</b>（昨日マリアと映画に行きました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ayer fui</b>(昨日私は行った) + <b>al cine</b>(映画館へ) + <b>con María</b>(マリアと)</span>", "副詞・前置詞", "<b>【時間対比】</b> anteayer (一昨日) ➔ ayer (昨日) ➔ hoy (今日)"),
    ("mañana", "マニャーナ", "副詞 [副]", "① 明日", "・<b>Mañana tengo un examen.</b>（明日テストがあります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Mañana</b>(明日) + <b>tengo</b>(持つ) + <b>un examen</b>(テスト)</span>", "副詞・前置詞", "<b>【時間対比】</b> hoy (今日) ➔ mañana (明日) ➔ pasado mañana (明後日)"),
    ("siempre", "シエンプレ", "副詞 [副]", "① いつも、常に、いつでも", "・<b>Siempre desayuno a las siete.</b>（いつも7時に朝食をとります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Siempre</b>(いつも) + <b>desayuno</b>(朝食をとる) + <b>a las siete</b>(7時に)</span>", "副詞・前置詞", "<b>【頻度対比】</b> siempre (100%) ➔ a veces (50%) ➔ nunca (0%)"),
    ("nunca", "ヌンカ", "副詞 [副]", "① 決して〜ない、一度も〜ない", "・<b>Nunca he estado en México.</b>（一度もメキシコに行ったことがありません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Nunca</b>(決して〜ない) + <b>he estado</b>(行ったことがある [現在完了]) + <b>en México</b>(メキシコに)</span>", "副詞・前置詞", "<b>【頻度対比】</b> nunca / jamás (決して〜ない)"),
    ("a veces", "ア ベセス", "副詞句 [副]", "① 時々、たまに", "・<b>A veces voy al gimnasio.</b>（時々ジムへ行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>A veces</b>(時々) + <b>voy al gimnasio</b>(ジムへ行く)</span>", "副詞・前置詞", "<b>【頻度対比】</b> siempre (いつも) ➔ a veces (時々)"),
    ("también", "タンビエン", "副詞 [副]", "① 〜もまた、同様に（肯定の同調）", "・<b>Yo también quiero ir a España.</b>（私もスペインに行きたいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Yo también</b>(私もまた) + <b>quiero ir</b>(行きたい)</span>", "副詞・前置詞", "<b>【対比】</b> 肯定: también (〜も) / 否定: tampoco (〜も…ない)"),
    ("tampoco", "タンポコ", "副詞 [副]", "① 〜もまた…ない（否定の同調）", "・<b>Yo tampoco lo sé.</b>（私もそれを知りません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Yo tampoco</b>(私もまた〜ない) + <b>lo sé</b>(それを知っている)</span>", "副詞・前置詞", "<b>【対比】</b> 肯定: también (〜も) / 否定: tampoco (〜も…ない)"),
    ("mucho", "ムチョ", "副詞・形容詞 [副/形]", "① たくさん、大いに、非常に", "・<b>Muchas gracias por todo.</b>（いろいろ本当にありがとう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Muchas gracias</b>(多大なる感謝) + <b>por todo</b>(すべてのことに対して)</span>", "副詞・前置詞", "<b>【性数変化(形容詞時)】</b> mucho / mucha / muchos / muchas"),
    ("poco", "ポコ", "副詞・形容詞 [副/形]", "① 少し、わずか<br>② 【un poco de】少しの〜", "・<b>Hablo un poco de español.</b>（スペイン語が少し話せます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hablo</b>(話す) + <b>un poco de</b>(少しの) + <b>español</b>(スペイン語)</span>", "副詞・前置詞", "<b>【性数変化(形容詞時)】</b> poco / poca / pocos / pocas"),
    ("muy", "ムイ", "副詞 [副]", "① とても、大変（形容詞・副詞を修飾）", "・<b>Estoy muy contento hoy.</b>（今日はとても嬉しいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy</b>(私は〜だ) + <b>muy contento</b>(とても満足している)</span>", "副詞・前置詞", "<b>【使い分け】</b> muy + 形容詞/副詞 (例: muy bien, muy bonito)"),
    ("más", "マス", "副詞 [副]", "① もっと、より多く（比較級を作る）", "・<b>Quiero aprender más español.</b>（もっとスペイン語を学びたいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero aprender</b>(学びたい) + <b>más</b>(もっと)</span>", "副詞・前置詞", "<b>【比較級】</b> más + 形容詞 + que (〜より…だ)"),
    ("menos", "メノス", "副詞 [副]", "① より少なく、〜を除いて", "・<b>Cuesta menos de diez euros.</b>（10ユーロ未満です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuesta</b>(費用がかかる) + <b>menos de diez euros</b>(10ユーロ未満)</span>", "副詞・前置詞", "<b>【劣等比較】</b> menos + 形容詞 + que (〜より…でない)"),
    ("ya", "ジャ", "副詞 [副]", "① もう、すでに<br>② 今すぐ<br>③ 【ya no】もう〜ない", "・<b>¿Ya has comido? - Sí, ya comí.</b>（もうご飯食べた？ - うん、もう食べたよ）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ya has comido</b>(もう食べたか) + <b>ya comí</b>(もう食べた)</span>", "副詞・前置詞", "<b>【重要成句】</b> ya no (もう〜ない) / ya veo (なるほど)"),
    ("todavía", "トダビア", "副詞 [副]", "① まだ、依然として<br>② 【todavía no】まだ〜ない", "・<b>Todavía no he terminado.</b>（まだ終わっていません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Todavía no</b>(まだ〜ない) + <b>he terminado</b>(終えた [完了])</span>", "副詞・前置詞", "<b>【重要成句】</b> todavía no (まだ〜ない)"),
    ("casi", "カシ", "副詞 [副]", "① ほとんど、もう少しで、ほぼ", "・<b>Ya son casi las diez.</b>（もうほぼ10時です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ya son</b>(もう〜だ) + <b>casi las diez</b>(ほぼ10時)</span>", "副詞・前置詞", "<b>【用法】</b> casi todos (ほぼ全員) / casi nunca (めったに〜ない)"),
    ("bien", "ビエン", "副詞 [副]", "① よく、上手に、元気に", "・<b>¡Muy bien hecho!</b>（よくできました！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Muy bien</b>(とても良く) + <b>hecho</b>(なされた)</span>", "副詞・前置詞", "<b>【対比】</b> bien (良く) ⇄ mal (悪く)"),
    ("mal", "マル", "副詞 [副]", "① 悪く、下手に、具合悪く", "・<b>Me siento mal hoy.</b>（今日は気分が悪いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me siento mal</b>(私は気分が悪い) + <b>hoy</b>(今日)</span>", "副詞・前置詞", "<b>【対比】</b> bien (良く) ⇄ mal (悪く)"),
    ("con", "コン", "前置詞 [前]", "① 〜と一緒に、〜を使って（手段）<br>② 【conmigo】私と / 【contigo】君と", "・<b>Voy con mi familia.</b>（家族と一緒に行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy</b>(行く) + <b>con mi familia</b>(家族と一緒に)</span>", "副詞・前置詞", "<b>【特殊形】</b> conmigo (私と) / contigo (君と) / consigo (彼自身と)"),
    ("sin", "シン", "前置詞 [前]", "① 〜なしで、〜を持たずに", "・<b>Un café sin azúcar, por favor.</b>（砂糖なしのコーヒーをお願いします）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Un café</b>(コーヒー) + <b>sin azúcar</b>(砂糖なしで)</span>", "副詞・前置詞", "<b>【対比】</b> con (〜と一緒に) ⇄ sin (〜なしで)"),
    ("en", "エン", "前置詞 [前]", "① 〜の中で、〜で（場所・時・手段）", "・<b>Estoy en casa.</b>（家にいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy</b>(私はいる) + <b>en casa</b>(家の中に)</span>", "副詞・前置詞", "<b>【用法】</b> 所在(en Tokio) / 交通手段(en autobús)"),
    ("a", "ア", "前置詞 [前]", "① 〜へ（方向・目的地）<br>② 〜に（時刻・対象）", "・<b>Voy a la estación a las ocho.</b>（8時に駅へ行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy a</b>(〜へ行く) + <b>la estación</b>(駅) + <b>a las ocho</b>(8時に)</span>", "副詞・前置詞", "<b>【結合則】</b> a + el ➔ <b>al</b> (例: al cine)"),
    ("de", "デ", "前置詞 [前]", "① 〜の（所有・素材）<br>② 〜から（出身・起点）", "・<b>Soy de Japón.</b>（日本出身です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Soy</b>(私は〜です) + <b>de Japón</b>(日本出身/日本から)</span>", "副詞・前置詞", "<b>【結合則】</b> de + el ➔ <b>del</b> (例: del profesor)"),
    ("para", "パラ", "前置詞 [前]", "① 〜のために（目的・受取人）<br>② 〜に向けて（目的地）<br>③ 〜までに（期限）", "・<b>Estudio para trabajar en España.</b>（スペインで働くために勉強しています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estudio</b>(勉強する) + <b>para trabajar</b>(働くために [目的]) + <b>en España</b>(スペインで)</span>", "副詞・前置詞", "<b>【porとの違い】</b> para: 矢印の先（目的・期限・宛先）"),
    ("por", "ポル", "前置詞 [前]", "① 〜によって（原因・手段）<br>② 〜を通って（通過）<br>③ 〜に対して（感謝・交換）", "・<b>Muchas gracias por tu ayuda.</b>（手伝ってくれて本当にありがとう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Muchas gracias</b>(大感謝) + <b>por tu ayuda</b>(君の助けに対して [理由・対象])</span>", "副詞・前置詞", "<b>【paraとの違い】</b> por: 原因・理由・手段・通過・交換"),
    ("porque", "ポルケ", "接続詞 [接]", "① なぜなら〜だから（理由を答える）", "・<b>No voy porque estoy cansado.</b>（疲れているので行きません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No voy</b>(私は行かない) + <b>porque</b>(なぜなら) + <b>estoy cansado</b>(疲れているから)</span>", "副詞・前置詞", "<b>【対比】</b> 問い: ¿Por qué? (なぜ?) ➔ 答え: Porque... (〜だから)"),
    ("pero", "ペロ", "接続詞 [接]", "① しかし、だが（逆接）", "・<b>Es caro, pero muy bueno.</b>（高いですが、とても良いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es caro</b>(高い) + <b>pero</b>(しかし) + <b>muy bueno</b>(とても良い)</span>", "副詞・前置詞", "<b>【用法】</b> 文と文をつなぐ逆接接続詞"),
    ("y", "イ", "接続詞 [接]", "① そして、〜と（並列）", "・<b>Hablo japonés y español.</b>（日本語とスペイン語を話します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hablo</b>(話す) + <b>japonés</b>(日本語) + <b>y</b>(そして) + <b>español</b>(スペイン語)</span>", "副詞・前置詞", "<b>【発音規則】</b> i / hi で始まる語の前では <b>e</b> に変化 (例: español e inglés)"),
    ("o", "オ", "接続詞 [接]", "① または、あるいは（選択）", "・<b>¿Prefieres té o café?</b>（お茶とコーヒー、どちらがいい？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Prefieres</b>(好むか) + <b>té</b>(お茶) + <b>o</b>(または) + <b>café</b>(コーヒー)</span>", "副詞・前置詞", "<b>【発音規則】</b> o / ho で始まる語の前では <b>u</b> に変化 (例: siete u ocho)"),
    ("si", "シ", "接続詞 [接]", "① もし〜ならば（条件）", "・<b>Si tienes tiempo, vamos a comer.</b>（もし時間があれば、ご飯食べに行こう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Si</b>(もし) + <b>tienes tiempo</b>(時間があるなら) + <b>vamos a comer</b>(食べに行こう)</span>", "副詞・前置詞", "<b>【注意】</b> アクセント記号なし: si (もし) / あり: sí (はい/Yes)")
]

# 挨拶・身体・曜日・疑問詞
DICTIONARY_DATA += [
    # 7. 挨拶・基本コミュニケーション表現 (8語)
    ("hola", "オラ", "間投詞 [間]", "① こんにちは、やあ（親しい挨拶）", "・<b>¡Hola! ¿Cómo estás?</b>（やあ！元気？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hola</b>(やあ) + <b>Cómo estás</b>(調子はどう?)</span>", "挨拶・基本表現", "<b>【発音】</b> h は無音。いつでも使える最も一般的な挨拶"),
    ("adiós", "アディオス", "間投詞 [間]", "① さようなら、バイバイ", "・<b>¡Adiós! ¡Que tengas un buen día!</b>（さようなら！良い1日を！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Adiós</b>(さようなら) + <b>Que tengas buen día</b>(良い1日を過ごせますように)</span>", "挨拶・基本表現", "<b>【別表現】</b> ¡Hasta luego! (また後で) / ¡Hasta pronto! (また近いうちに)"),
    ("por favor", "ポル ファボール", "副詞句 [副]", "① お願いします、どうぞ（please）", "・<b>La cuenta, por favor.</b>（お会計をお願いします）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La cuenta</b>(お会計) + <b>por favor</b>(お願いします)</span>", "挨拶・基本表現", "<b>【用法】</b> 依頼の末尾や先頭につけて丁寧にする表現"),
    ("de nada", "デ ナダ", "慣用句 [間]", "① どういたしまして、お気になさらず", "・<b>- ¡Muchas gracias! - De nada.</b>（- ありがとう！ - どういたしまして）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Muchas gracias</b>(ありがとう) + <b>De nada</b>(どういたしまして)</span>", "挨拶・基本表現", "<b>【別表現】</b> No hay de qué. (どういたしまして)"),
    ("perdón", "ペルドン", "間投詞 [間]", "① ごめんなさい、すみません（軽い謝罪・呼びかけ）", "・<b>¡Perdón! No fue mi intención.</b>（ごめんなさい！そんなつもりじゃなかったんです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Perdón</b>(ごめんなさい) + <b>no fue mi intención</b>(そんな意図ではなかった)</span>", "挨拶・基本表現", "<b>【用法】</b> 軽くぶつかった時や呼びかけに使う"),
    ("disculpe", "ディスクルペ", "動詞活用 [間]", "① すみません、失礼します（丁寧な呼びかけ）", "・<b>Disculpe, ¿dónde está la parada?</b>（すみません、バス停はどこですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Disculpe</b>(すみません [丁寧]) + <b>dónde está</b>(どこですか) + <b>la parada</b>(停留所)</span>", "挨拶・基本表現", "<b>【用法】</b> usted に対する丁寧な呼びかけ"),
    ("mucho gusto", "ムチョ グスト", "慣用句 [間]", "① はじめまして、お会いできて嬉しいです", "・<b>- Soy Taro. - Mucho gusto.</b>（- タロウです。 - はじめまして）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Soy Taro</b>(タロウです) + <b>Mucho gusto</b>(はじめまして/大きな喜びです)</span>", "挨拶・基本表現", "<b>【同義】</b> Encantado (男性) / Encantada (女性)"),
    ("bienvenido", "ビエンベニード", "形容詞・間投詞 [形/間]", "① ようこそ、歓迎します（女性には bienvenida）", "・<b>¡Bienvenidos a España!</b>（スペインへようこそ！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Bienvenidos</b>(歓迎します [複数]) + <b>a España</b>(スペインへ)</span>", "挨拶・基本表現", "<b>【男女・性数】</b> 男単: bienvenido / 女単: bienvenida / 複: bienvenidos"),

    # 8. 身体・健康名詞 (6語)
    ("cabeza", "カベサ", "女性名詞 [女]", "① 頭、頭部<br>② 【me duele la cabeza】頭が痛い", "・<b>Me duele mucho la cabeza.</b>（頭がとても痛いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me duele</b>(私にとって痛む) + <b>mucho</b>(とても) + <b>la cabeza</b>(頭が)</span>", "身体・健康", "<b>【性数変化】</b> 単数: <b>la cabeza</b> / 複数: <b>las cabezas</b>"),
    ("mano", "マノ", "女性名詞 [女 ※語尾-oだが女性]", "① 手（※女性名詞: la mano）", "・<b>Lávate las manos antes de comer.</b>（食べる前に手を洗ってね）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Lávate</b>(洗いなさい) + <b>las manos</b>(手を) + <b>antes de comer</b>(食べる前に)</span>", "身体・健康", "<b>【性数変化】</b> 女性名詞: <b>la mano</b> / 複数: <b>las manos</b>"),
    ("ojo", "オホ", "男性名詞 [男]", "① 目、瞳（複数は ojos）<br>② 【¡Ojo!】気をつけて！注意！", "・<b>Tiene los ojos azules.</b>（彼女は青い目をしています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tiene</b>(持っている) + <b>los ojos azules</b>(青い目)</span>", "身体・健康", "<b>【性数変化】</b> 単数: <b>el ojo</b> / 複数: <b>los ojos</b>"),
    ("boca", "ボカ", "女性名詞 [女]", "① 口、口元、地下鉄の入り口", "・<b>Abre la boca, por favor.</b>（口を開けてください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Abre</b>(開けて) + <b>la boca</b>(口を) + <b>por favor</b>(お願いします)</span>", "身体・健康", "<b>【性数変化】</b> 単数: <b>la boca</b> / 複数: <b>las bocas</b>"),
    ("corazón", "コラソン", "男性名詞 [男]", "① 心臓、心、ハート、愛情表現（愛しい人）", "・<b>Te quiero con todo mi corazón.</b>（心から君を愛しています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Te quiero</b>(君を愛している) + <b>con todo mi corazón</b>(私の心のすべてで)</span>", "身体・健康", "<b>【性数変化】</b> 単数: <b>el corazón</b> / 複数: <b>los corazones</b>"),
    ("cuerpo", "クエルポ", "男性名詞 [男]", "① 身体、体、胴体", "・<b>El ejercicio es bueno para el cuerpo.</b>（運動は体に良いです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El ejercicio</b>(運動) + <b>es bueno</b>(良い) + <b>para el cuerpo</b>(体のために)</span>", "身体・健康", "<b>【性数変化】</b> 単数: <b>el cuerpo</b> / 複数: <b>los cuerpos</b>"),

    # 9. 曜日・暦名詞 (7語)
    ("lunes", "ルネス", "男性名詞 [男]", "① 月曜日（el lunes）", "・<b>Nos vemos el lunes.</b>（月曜日に会いましょう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Nos vemos</b>(会おう) + <b>el lunes</b>(月曜日に)</span>", "暦・曜日", "<b>【冠詞】</b> 曜日には定冠詞をつける: <b>el lunes</b> / 毎週月曜: <b>los lunes</b>"),
    ("martes", "マルテス", "男性名詞 [男]", "① 火曜日（el martes）", "・<b>El martes tengo clase de español.</b>（火曜日にスペイン語の授業があります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El martes</b>(火曜日に) + <b>tengo clase</b>(授業がある)</span>", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el martes</b> / 複数: <b>los martes</b>"),
    ("miércoles", "ミエルコレス", "男性名詞 [男]", "① 水曜日（el miércoles）", "・<b>El miércoles voy al médico.</b>（水曜日にお医者さんに行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El miércoles</b>(水曜日に) + <b>voy al médico</b>(医者に行く)</span>", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el miércoles</b> / 複数: <b>los构miercoles</b>"),
    ("jueves", "フエベス", "男性名詞 [男]", "① 木曜日（el jueves）", "・<b>El jueves es fiesta nacional.</b>（木曜日は祝日です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El jueves</b>(木曜日は) + <b>es fiesta</b>(祝日/お祭りです)</span>", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el jueves</b> / 複数: <b>los jueves</b>"),
    ("viernes", "ビエルネス", "男性名詞 [男]", "① 金曜日（el viernes）<br>② 【¡Por fin es viernes!】華金だ！", "・<b>¡Por fin es viernes!</b>（やっと金曜日だ！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por fin</b>(ついに) + <b>es viernes</b>(金曜日だ)</span>", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el viernes</b> / 複数: <b>los viernes</b>"),
    ("sábado", "サバド", "男性名詞 [男]", "① 土曜日（el sábado）", "・<b>Los sábados me levanto tarde.</b>（土曜日は遅く起きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Los sábados</b>(毎週土曜日は) + <b>me levanto tarde</b>(遅く起きる)</span>", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el sábado</b> / 複数: <b>los sábados</b>"),
    ("domingo", "ドミンゴ", "男性名詞 [男]", "① 日曜日（el domingo）", "・<b>El domingo como con mi familia.</b>（日曜日は家族と食事します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El domingo</b>(日曜日に) + <b>como con</b>(〜と一緒に食べる) + <b>mi familia</b>(私の家族)</span>", "暦・曜日", "<b>【冠詞】</b> 単数: <b>el domingo</b> / 複数: <b>los domingos</b>"),

    # 10. 疑問詞 (8語)
    ("qué", "ケ", "代名詞 [疑]", "① 何、どんなもの<br>② 【¿Qué tal?】調子はどう？", "・<b>¿Qué haces hoy?</b>（今日何してるの？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Qué</b>(何を) + <b>haces</b>(君はする) + <b>hoy</b>(今日)</span><br>・<b>¿Qué tal todo?</b>（調子はどう？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Qué tal</b>(どうですか) + <b>todo</b>(すべて)</span>", "疑問詞", "<b>【アクセント】</b> 疑問詞には必ずアクセント記号がつきます: qué"),
    ("quién", "キエン", "代名詞 [疑]", "① 誰、どなた（複数は quiénes）", "・<b>¿Quién es esa chica?</b>（あの子は誰？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quién</b>(誰) + <b>es</b>(〜ですか) + <b>esa chica</b>(その女の子)</span>", "疑問詞", "<b>【複数形】</b> 単数: <b>quién</b> / 複数: <b>quiénes</b>"),
    ("dónde", "ドンデ", "副詞 [疑]", "① どこ、どこで<br>② 【¿De dónde eres?】出身はどこ？", "・<b>¿Dónde vives?</b>（どこに住んでいますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Dónde</b>(どこに) + <b>vives</b>(君は住んでいるか)</span><br>・<b>¿De dónde eres? - Soy de Tokio.</b>（ご出身は？ - 東京です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>De dónde</b>(どこから/出身) + <b>eres</b>(君は〜か)</span>", "疑問詞", "<b>【前置詞結合】</b> ¿A dónde? (どこへ?) / ¿De dónde? (どこから/出身?)"),
    ("cuándo", "クアンド", "副詞 [疑]", "① いつ、何時に", "・<b>¿Cuándo es tu cumpleaños?</b>（誕生日はいつですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuándo</b>(いつ) + <b>es</b>(ですか) + <b>tu cumpleaños</b>(君の誕生日)</span>", "疑問詞", "<b>【アクセント】</b> 疑問詞: cuándo (いつ) / 接続詞: cuando (〜の時)"),
    ("cómo", "コモ", "副詞 [疑]", "① どのように、どうやって<br>② 【¿Cómo te llamas?】お名前は？", "・<b>¿Cómo se llega a la estación?</b>（駅へはどう行きますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cómo se llega</b>(どうやって着くか) + <b>a la estación</b>(駅へ)</span>", "疑問詞", "<b>【アクセント】</b> 疑問詞: cómo (どのように) / 接続詞: como (〜のように)"),
    ("por qué", "ポル ケ", "疑問句 [疑]", "① なぜ、どうして（理由を問う）", "・<b>¿Por qué estudias español?</b>（どうしてスペイン語を勉強しているの？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por qué</b>(なぜ) + <b>estudias</b>(勉強するのか) + <b>español</b>(スペイン語を)</span>", "疑問詞", "<b>【区別】</b> 問い: <b>¿Por qué?</b> (2語・アクセント) / 答え: <b>porque</b> (1語)"),
    ("cuánto", "クアント", "形容詞・代名詞 [疑]", "① いくら、どれくらい（性数変化: cuántos/as）", "・<b>¿Cuánto cuesta esto?</b>（これはいくらですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuánto</b>(いくら) + <b>cuesta</b>(費用がかかる) + <b>esto</b>(これ)</span>", "疑問詞", "<b>【性数変化】</b> cuánto / cuánta / cuántos / cuántas"),
    ("cuál", "クアル", "代名詞 [疑]", "① どれ、どちら、何（複数は cuáles）", "・<b>¿Cuál es tu comida favorita?</b>（一番好きな食べ物は何ですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuál es</b>(何ですか) + <b>tu comida favorita</b>(君の大好きな食べ物)</span>", "疑問詞", "<b>【複数形】</b> 単数: <b>cuál</b> / 複数: <b>cuáles</b>")
]
