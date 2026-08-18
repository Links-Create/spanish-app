# -*- coding: utf-8 -*-
"""
スペイン語 最重要チャンク (定型フレーズ・コロケーション) 50選
単語単体ではなく「塊（チャンク）」で覚えることで、会話の流暢性を極限まで高めるデータ
"""

CHUNKS_DATA = [
    # ==========================================
    # 1. 義務・必要・希望チャンク (10選)
    # ==========================================
    ("tengo que + 動詞原形", "テンゴ ケ ...", "義務・必要", 
     "〜しなければならない、〜する必要がある", 
     "・<b>Tengo que estudiar español hoy.</b>（今日はスペイン語を勉強しなければなりません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo que</b>(〜せねばならない) + <b>estudiar</b>(勉強する) + <b>español</b>(スペイン語) + <b>hoy</b>(今日)</span>",
     "<b>【文法ポイント】</b> tener que + 原形 は最も日常で使われる「〜しなければならない」の表現。主語に合わせて tengo que, tienes que, tiene que... と活用します。"),

    ("hay que + 動詞原形", "アイ ケ ...", "義務・一般論", 
     "（一般的に/誰でも）〜しなければならない、〜すべきだ", 
     "・<b>Hay que practicar todos los días.</b>（毎日練習しなければなりません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hay que</b>(〜せねばならない [一般]) + <b>practicar</b>(練習する) + <b>todos los días</b>(毎日)</span>",
     "<b>【文法ポイント】</b> 人称に関係なく、社会のルールや一般的なアドバイスとして「〜する必要がある」と言う時に使います。"),

    ("me gustaría + 動詞原形", "メ グスタリア ...", "希望・丁寧", 
     "〜したいのですが、〜できたら嬉しいです（丁寧な希望）", 
     "・<b>Me gustaría visitar España algún día.</b>（いつかスペインを訪れたいのですが）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me gustaría</b>(〜したいのですが) + <b>visitar</b>(訪れる) + <b>España</b>(スペイン) + <b>algún día</b>(いつか)</span>",
     "<b>【文法ポイント】</b> quiero よりも非常に丁寧で上品な「〜したいです」の表現。レストランでの注文やビジネスでも重宝します。"),

    ("tener ganas de + 動詞原形", "テネール ガナス デ ...", "欲求・気分", 
     "（気分的に）〜したい、〜したい気分だ", 
     "・<b>Tengo ganas de comer paella.</b>（パエリアを食べたい気分です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tengo ganas de</b>(〜したい気分だ) + <b>comer</b>(食べる) + <b>paella</b>(パエリア)</span>",
     "<b>【文法ポイント】</b> 理屈や義務ではなく、直感や気分で「〜したいな〜」という時にネイティブが最もよく使う表現です。"),

    ("ir a + 動詞原形", "イール ア ...", "近接未来", 
     "〜する予定だ、〜するつもりだ（近接未来）", 
     "・<b>Voy a cocinar esta noche.</b>（今夜料理を作る予定です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy a</b>(〜する予定だ) + <b>cocinar</b>(料理する) + <b>esta noche</b>(今夜)</span>",
     "<b>【文法ポイント】</b> 英語の be going to に相当。voy a, vas a, va a, vamos a... と ir を現在活用させて後ろに動詞原形を置きます。"),

    ("acabar de + 動詞原形", "アカバール デ ...", "直近過去", 
     "たった今〜したばかりだ", 
     "・<b>Acabo de llegar a casa.</b>（たった今家に帰ってきたばかりです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Acabo de</b>(〜したばかりだ) + <b>llegar</b>(着く/帰宅する) + <b>a casa</b>(家に)</span>",
     "<b>【文法ポイント】</b> 直近に終わった動作を表現。acabo de, acabas de, acaba de... と活用します。"),

    ("empezar a + 動詞原形", "エンペサール ア ...", "開始", 
     "〜し始める", 
     "・<b>Empiezo a entender español.</b>（スペイン語が分かり始めてきました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Empiezo a</b>(〜し始める) + <b>entender</b>(理解する) + <b>español</b>(スペイン語)</span>",
     "<b>【文法ポイント】</b> 動作の開始を表す重要チャンク。empezar は e➔ie 不規則変化（empiezo, empiezas, empieza...）。"),

    ("dejar de + 動詞原形", "デハール デ ...", "中止・禁煙など", 
     "〜するのをやめる、やめる", 
     "・<b>Voy a dejar de fumar.</b>（タバコをやめるつもりです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy a</b>(〜するつもり) + <b>dejar de</b>(やめる) + <b>fumar</b>(喫煙する)</span>",
     "<b>【文法ポイント】</b> 習慣や現在行っている行動の中止を表します。"),

    ("estar a punto de + 動詞原形", "エスタール ア プント デ ...", "直前", 
     "まさに〜するところだ、今にも〜しそうだ", 
     "・<b>El tren está a punto de salir.</b>（電車が今まさに出発するところです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>El tren</b>(電車) + <b>está a punto de</b>(今にも〜しそうだ) + <b>salir</b>(出発する)</span>",
     "<b>【文法ポイント】</b> 直後に何かが起きる寸前の状態を表すドラマチックな表現です。"),

    ("volver a + 動詞原形", "ボルベール ア ...", "反復・再開", 
     "再び〜する、もう一度〜する", 
     "・<b>Quiero volver a verte.</b>（また君に会いたいよ）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Quiero</b>(〜したい) + <b>volver a</b>(再び〜する) + <b>verte</b>(君に会うこと)</span>",
     "<b>【文法ポイント】</b> otro vez を使わずに、volver a + 原形で「再び〜する」を表すスマートなネイティブ表現。"),

    # ==========================================
    # 2. 時間・順序・頻度チャンク (10選)
    # ==========================================
    ("antes de + 名詞/動詞原形", "アンテス デ ...", "時間・順序", 
     "〜の前に、〜する前に", 
     "・<b>Lávate las manos antes de comer.</b>（食べる前に手を洗ってね）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Lávate</b>(洗いなさい) + <b>las manos</b>(手を) + <b>antes de</b>(〜の前に) + <b>comer</b>(食べる)</span>",
     "<b>【文法ポイント】</b> 前置詞 de の後ろには名詞または動詞の原形が来ます。"),

    ("después de + 名詞/動詞原形", "デスプエス デ ...", "時間・順序", 
     "〜の後に、〜した後に", 
     "・<b>Vamos al café después de la clase.</b>（授業の後にカフェへ行きましょう）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Vamos al café</b>(カフェに行こう) + <b>después de</b>(〜の後に) + <b>la clase</b>(授業)</span>",
     "<b>【文法ポイント】</b> antes de の対義語。después de cenar（夕食後に）のように動詞原形も直接続きます。"),

    ("hace + 時間 + que ...", "アセ ... ケ", "期間・継続", 
     "〜前から…している、〜して…年になる", 
     "・<b>Hace dos años que estudio español.</b>（スペイン語を勉強して2年になります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hace dos años que</b>(2年前から〜だ) + <b>estudio</b>(勉強している) + <b>español</b>(スペイン語)</span>",
     "<b>【文法ポイント】</b> 過去から現在まで継続している期間を述べる最頻出構文。"),

    ("de vez en cuando", "デ ベス エン クアンド", "頻度", 
     "時々、たまに、折に触れて", 
     "・<b>Voy al cine de vez en cuando.</b>（たまに映画館に行きます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy al cine</b>(映画へ行く) + <b>de vez en cuando</b>(時々/たまに)</span>",
     "<b>【文法ポイント】</b> a veces とほぼ同義ですが、より自然で慣用的な「たまに」の表現。"),

    ("por primera vez", "ポル プリメラ ベス", "経験", 
     "初めて、初回に", 
     "・<b>Probé la paella por primera vez.</b>（初めてパエリアを食べました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Probé</b>(味わった/食べた) + <b>la paella</b>(パエリア) + <b>por primera vez</b>(初めて)</span>",
     "<b>【文法ポイント】</b> 旅行や自己紹介で「初めて〜した」と言いたいときの超重要チャンク。"),

    ("por fin", "ポル フィン", "時間・感情", 
     "ついに、やっと、とうとう", 
     "・<b>¡Por fin es viernes!</b>（やっと金曜日だ！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por fin</b>(ついに/やっと) + <b>es viernes</b>(金曜日だ)</span>",
     "<b>【文法ポイント】</b> 長く待ち望んでいたことが実現した時の喜びを込めて使います。"),

    ("al mismo tiempo", "アル ミスモ ティエンポ", "同時", 
     "同時に、それと同時に", 
     "・<b>No puedo hablar y escuchar al mismo tiempo.</b>（同時に話して聞くことはできません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>No puedo</b>(できない) + <b>hablar y escuchar</b>(話して聞く) + <b>al mismo tiempo</b>(同時に)</span>",
     "<b>【文法ポイント】</b> 2つの動作が並行していることを表す接続表現。"),

    ("de momento", "デ モメント", "現状", 
     "今のところ、当面は", 
     "・<b>De momento todo está bien.</b>（今のところすべて順調です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>De momento</b>(今のところ) + <b>todo</b>(すべて) + <b>está bien</b>(順調だ)</span>",
     "<b>【文法ポイント】</b> 会話やビジネスの状況報告で非常によく使われます。"),

    ("hoy en día", "オイ エン ディア", "時代・現代", 
     "今日（こんにち）では、最近では", 
     "・<b>Hoy en día mucha gente usa IA.</b>（最近では多くの人がAIを使っています）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Hoy en día</b>(今日では) + <b>mucha gente</b>(多くの人) + <b>usa IA</b>(AIを使う)</span>",
     "<b>【文法ポイント】</b> 現代社会のトレンドや昔との対比を語る時に便利です。"),

    ("cuanto antes", "クアント アンテス", "緊急・依頼", 
     "できるだけ早く、大至急", 
     "・<b>Llámame cuanto antes, por favor.</b>（できるだけ早く電話してください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llámame</b>(私に電話して) + <b>cuanto antes</b>(できるだけ早く) + <b>por favor</b>(お願いします)</span>",
     "<b>【文法ポイント】</b> lo antes posible と同じく「できるだけ早く」を表すスピーディーな表現。"),

    # ==========================================
    # 3. 意見・理由・接続・談話チャンク (10選)
    # ==========================================
    ("en mi opinión", "エン ミ オピニオン", "意見表明", 
     "私の意見では、私の考えでは", 
     "・<b>En mi opinión, es una gran oportunidad.</b>（私の意見では、これは素晴らしいチャンスです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>En mi opinión</b>(私の意見では) + <b>es</b>(〜だ) + <b>una gran oportunidad</b>(素晴らしい好機)</span>",
     "<b>【文法ポイント】</b> 会話で自分の考えをスマートに切り出す万能チャンク。"),

    ("a pesar de + 名詞/動詞原形", "ア ペサール デ ...", "逆接・譲歩", 
     "〜にもかかわらず", 
     "・<b>Salimos a pesar de la lluvia.</b>（雨にもかかわらず出かけました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Salimos</b>(出かけた [点過去]) + <b>a pesar de</b>(〜にもかかわらず) + <b>la lluvia</b>(雨)</span>",
     "<b>【文法ポイント】</b> 中級レベルで差がつく重要な譲歩表現。a pesar de que + 文 もよく使われます。"),

    ("por un lado / por otro lado", "ポル ウン ラド ...", "対比・論理", 
     "一方で〜、他方では…", 
     "・<b>Por un lado es caro, pero por otro lado es de gran calidad.</b>（一方で高いですが、他方では高品質です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Por un lado</b>(一方では) + <b>es caro</b>(高い) + <b>pero por otro lado</b>(しかし他方では) + <b>es de gran calidad</b>(高品質だ)</span>",
     "<b>【文法ポイント】</b> メリットとデメリットや2つの視点を比較する時の定番フレーズ。"),

    ("es decir", "エス デシール", "言換・説明", 
     "つまり、すなわち、要するに", 
     "・<b>Llego el viernes, es decir, mañana.</b>（金曜日、つまり明日に到着します）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llego</b>(着く) + <b>el viernes</b>(金曜日に) + <b>es decir</b>(つまり) + <b>mañana</b>(明日)</span>",
     "<b>【文法ポイント】</b> 相手にわかりやすく言い直す時の超便利つなぎ言葉。"),

    ("gracias a + 名詞", "グラシアス ア ...", "感謝・原因", 
     "〜のおかげで", 
     "・<b>Aprobé el examen gracias a tu ayuda.</b>（君の助けのおかげで試験に合格しました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Aprobé el examen</b>(試験に受かった) + <b>gracias a</b>(〜のおかげで) + <b>tu ayuda</b>(君の助け)</span>",
     "<b>【文法ポイント】</b> ポジティブな原因・理由を述べるチャンク。ネガティブな「〜のせいで」は por culpa de。"),

    ("por culpa de + 名詞", "ポル クルパ デ ...", "責任・理由", 
     "〜のせいで", 
     "・<b>Llegué tarde por culpa del tráfico.</b>（渋滞のせいで遅刻しました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Llegué tarde</b>(遅れて着いた) + <b>por culpa de</b>(〜のせいで) + <b>el tráfico</b>(交通渋滞)</span>",
     "<b>【文法ポイント】</b> 交通渋滞や悪天候など、悪い原因を伝える時に使います。"),

    ("estar de acuerdo (con)", "エスタール デ アクエルド", "賛同・同調", 
     "（〜に）賛成である、同感である", 
     "・<b>Estoy totalmente de acuerdo contigo.</b>（君に完全に同感・賛成です）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Estoy totalmente de acuerdo</b>(完全に賛成だ) + <b>contigo</b>(君と)</span>",
     "<b>【文法ポイント】</b> ディスカッションや日常会話での同調表現。反対なら No estoy de acuerdo。"),

    ("darse cuenta de (que)", "ダールセ クエンタ デ", "気づき・認識", 
     "〜に気づく、〜と認識する", 
     "・<b>Me di cuenta de que olvidé las llaves.</b>（鍵を忘れたことに気づきました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me di cuenta de que</b>(〜に気づいた [点過去]) + <b>olvidé</b>(忘れた) + <b>las llaves</b>(鍵)</span>",
     "<b>【文法ポイント】</b> 再帰動詞 darse cuenta de は「ハッと気づく」を表す超重要ネイティブ表現。"),

    ("tener sentido", "テネール センティード", "論理・納得", 
     "意味をなす、筋が通っている、なるほど", 
     "・<b>Ahora todo tiene sentido.</b>（今すべてが辻褄が合いました/納得いきました）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ahora</b>(今) + <b>todo</b>(すべてが) + <b>tiene sentido</b>(筋が通る/意味をなす)</span>",
     "<b>【文法ポイント】</b> 英語の make sense に相当する表現。No tiene sentido で「意味不明・おかしい」。"),

    ("valer la pena", "バレール ラ ペナ", "価値・評価", 
     "〜する価値がある、甲斐がある", 
     "・<b>Este libro vale la pena leerlo.</b>（この本は読む価値があります）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Este libro</b>(この本は) + <b>vale la pena</b>(価値がある) + <b>leerlo</b>(それを読むこと)</span>",
     "<b>【文法ポイント】</b> 旅行地や映画、努力に対して「行く価値がある！」「やった甲斐があった！」と絶賛する表現。"),

    # ==========================================
    # 4. 日常コミュニケーション・相槌チャンク (10選)
    # ==========================================
    ("¿Qué te parece si + 動詞現在形?", "ケ テ パレセ シ ...", "提案・お誘い", 
     "もし〜するのはどう？〜しない？", 
     "・<b>¿Qué te parece si vamos a cenar juntos?</b>（一緒に夕食を食べに行くのはどう？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Qué te parece si</b>(〜はどう?) + <b>vamos a cenar</b>(夕食に行く) + <b>juntos</b>(一緒に)</span>",
     "<b>【文法ポイント】</b> 友達をスマートに食事や遊びに誘う時の超定番フレーズ。"),

    ("por si acaso", "ポル シ アカソ", "用心・準備", 
     "念のため、万が一に備えて", 
     "・<b>Lleva un paraguas por si acaso.</b>（念のため傘を持っていきなさい）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Lleva</b>(持っていきなさい) + <b>un paraguas</b>(傘) + <b>por si acaso</b>(念のため)</span>",
     "<b>【文法ポイント】</b> 旅行や外出時の会話でネイティブが頻繁に口にする成句。"),

    ("sin duda (alguna)", "シン ドゥダ", "確信・強調", 
     "間違いなく、疑いなく、絶対に", 
     "・<b>Es sin duda el mejor restaurante.</b>（間違いなく最高のレストランです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Es</b>(〜だ) + <b>sin duda</b>(間違いなく) + <b>el mejor restaurante</b>(最高のレストラン)</span>",
     "<b>【文法ポイント】</b> 自分の意見を強く肯定する時の表現。"),

    ("más o menos", "マス オ メノス", "概算・曖昧", 
     "だいたい、およそ、まあまあ", 
     "・<b>¿Cómo estás? - Más o menos.</b>（調子はどう？ - まあまあかな）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cómo estás</b>(調子はどう) + <b>Más o menos</b>(まあまあ/だいたい)</span>",
     "<b>【文法ポイント】</b> 数量の「およそ10人（más o menos 10 personas）」や気分の「まあまあ」の両方に使えます。"),

    ("de verdad", "デ ベルダッ(ド)", "確認・強調", 
     "本当に、本気で、マジで", 
     "・<b>¿De verdad? ¡No me lo puedo creer!</b>（本当に？信じられない！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>De verdad</b>(本当に) + <b>No me lo puedo creer</b>(信じられない)</span>",
     "<b>【文法ポイント】</b> 相槌の「ほんとに！？」としても、副詞の「本当にありがとう（muchas gracias de verdad）」としても活躍。"),

    ("tener que ver con", "テネール ケ ベール コン", "関連・関係", 
     "〜と関係がある、関わりがある", 
     "・<b>Esto no tiene nada que ver conmigo.</b>（これは私とは何の関係もありません）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Esto</b>(これは) + <b>no tiene nada que ver con</b>(〜と何の関係もない) + <b>migo</b>(私と)</span>",
     "<b>【文法ポイント】</b> no tener nada que ver con で「〜と一切関係ない」という頻出成句になります。"),

    ("echar de menos (a alguien)", "エチャール デ メノス", "感情・恋しさ", 
     "（人や場所が）恋しい、いなくて寂しい", 
     "・<b>Te echo mucho de menos.</b>（君がいなくてとても寂しいよ / 会いたいよ）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Te</b>(君を) + <b>echo de menos</b>(恋しく思う) + <b>mucho</b>(とても)</span>",
     "<b>【文法ポイント】</b> スペインで「会いたい、寂しい（英語の I miss you）」を伝える最も代表的な表現。"),

    ("valerse por sí mismo", "バレールセ ポル シ ミスモ", "自立", 
     "自力でやっていく、自立する", 
     "・<b>Ya puede valerse por sí mismo.</b>（彼はもう自力でやっていけます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ya</b>(もう) + <b>puede</b>(〜できる) + <b>valerse por sí mismo</b>(自立する/自力でやる)</span>",
     "<b>【文法ポイント】</b> 成長や自立を語る時の慣用句。"),

    ("tener razón", "テネール ラソン", "正当性・納得", 
     "（人の言うことが）正しい、その通りだ", 
     "・<b>Tienes toda la razón.</b>（君の言う通りだよ/全く正しい）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Tienes</b>(持つ) + <b>toda la razón</b>(すべての正当性/全くその通り)</span>",
     "<b>【文法ポイント】</b> 相手の意見を肯定する時にネイティブが毎日使う最重要相槌フレーズ。"),

    ("hacer el favor de + 動詞原形", "アセール エル ファボール デ ...", "丁寧な依頼", 
     "〜していただけますか、〜してください（丁寧）", 
     "・<b>¿Me hace el favor de cerrar la puerta?</b>（ドアを閉めていただけますでしょうか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me hace el favor de</b>(〜していただけますか) + <b>cerrar la puerta</b>(ドアを閉める)</span>",
     "<b>【文法ポイント】</b> por favor よりさらに丁重にお願いする大人の依頼表現。"),

    # ==========================================
    # 5. トラブル・場所・移動チャンク (10選)
    # ==========================================
    ("perderse", "ペルデールセ", "迷子・紛失", 
     "道に迷う、迷子になる", 
     "・<b>Me he perdido, ¿dónde está el metro?</b>（道に迷いました、地下鉄はどこですか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me he perdido</b>(迷子になった [現在完了]) + <b>dónde está</b>(どこですか) + <b>el metro</b>(地下鉄)</span>",
     "<b>【文法ポイント】</b> 再帰動詞。旅行中に道を聞く時の必須フレーズ。"),

    ("¿A qué hora + 動詞...?", "ア ケ オラ ...", "時刻質問", 
     "何時に〜しますか？", 
     "・<b>¿A qué hora sale el tren?</b>（電車は何時に出発しますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>A qué hora</b>(何時に) + <b>sale</b>(出発する) + <b>el tren</b>(電車)</span>",
     "<b>【文法ポイント】</b> ¿Qué hora es?（今何時？）と区別。スケジュールや時間を尋ねる万能構文。"),

    ("¿Cuánto tiempo se tarda en + 原形?", "クアント ティエンポ セ タルダ エン ...", "所要時間", 
     "〜するのにどれくらい時間がかかりますか？", 
     "・<b>¿Cuánto tiempo se tarda en llegar a pie?</b>（歩いて着くのにどのくらいかかりますか？）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Cuánto tiempo</b>(どれくらいの時間) + <b>se tarda en</b>(〜に時間がかかる) + <b>llegar a pie</b>(徒歩で着く)</span>",
     "<b>【文法ポイント】</b> 移動や作業の所要時間を尋ねる定番の質問パターン。"),

    ("estar lleno de + 名詞", "エスタール ジェノ デ ...", "状態・満杯", 
     "〜でいっぱいである、満ちている", 
     "・<b>La plaza está llena de gente.</b>（広場は人でいっぱいです）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>La plaza</b>(広場は) + <b>está llena de</b>(〜でいっぱいだ) + <b>gente</b>(人)</span>",
     "<b>【文法ポイント】</b> lleno/a は主語の性数に合わせて変化します。"),

    ("a la derecha / a la izquierda", "ア ラ デレチャ / ア ラ イスキエルダ", "方向指示", 
     "右へ / 左へ、右側に / 左側に", 
     "・<b>Gira a la derecha en la esquina.</b>（角を右に曲がってください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Gira</b>(曲がって [命令]) + <b>a la derecha</b>(右へ) + <b>en la esquina</b>(角で)</span>",
     "<b>【文法ポイント】</b> 道案内で絶対に使われる方向指示チャンク。まっすぐは todo recto。"),

    ("todo recto", "トド レクト", "方向指示", 
     "まっすぐ、直進して", 
     "・<b>Sigue todo recto hasta la estación.</b>（駅までずっとまっすぐ進んでください）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Sigue</b>(進んで) + <b>todo recto</b>(まっすぐ) + <b>hasta la estación</b>(駅まで)</span>",
     "<b>【文法ポイント】</b> 道案内の基本表現。"),

    ("tener cuidado (con)", "テネール クイダード", "注意・警告", 
     "（〜に）気をつける、注意する", 
     "・<b>¡Ten cuidado con los coches!</b>（車に気をつけて！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Ten cuidado</b>(気をつけろ [命令]) + <b>con los coches</b>(車に)</span>",
     "<b>【文法ポイント】</b> 危険を警告する時の定番成句。¡Cuidado! 単体でも使えます。"),

    ("no pasa nada", "ノ パサ ナダ", "安心・慰め", 
     "大丈夫だよ、何でもないよ、気にしないで", 
     "・<b>- Lo siento mucho. - ¡No pasa nada!</b>（- ごめんなさい。 - 大丈夫、気にしないで！）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Lo siento mucho</b>(本当にごめんなさい) + <b>No pasa nada</b>(何でもないよ/大丈夫)</span>",
     "<b>【文法ポイント】</b> スペイン人が1日に何度も言う、超国民的ポジティブフレーズ。"),

    ("pedir la cuenta", "ペディール ラ クエンタ", "レストラン", 
     "お会計を頼む", 
     "・<b>Voy a pedir la cuenta.</b>（お会計をお願いしてきます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Voy a</b>(〜する) + <b>pedir la cuenta</b>(お会計を頼む)</span>",
     "<b>【文法ポイント】</b> レストランで欠かせない行動チャンク。"),

    ("quedarse en + 場所", "ケダールセ エン ...", "滞在・宿泊", 
     "〜にとどまる、滞在する、宿泊する", 
     "・<b>Me quedo en casa este fin de semana.</b>（今週末は家にいます）<br><span style='color:#64748b; font-size:0.9rem;'>└ 単語分解: <b>Me quedo en casa</b>(家に滞在する/いる) + <b>este fin de semana</b>(今週末)</span>",
     "<b>【文法ポイント】</b> 再帰動詞 quedarse は「ホテルに泊まる」「家でまったりする」に広く使われます。")
]
