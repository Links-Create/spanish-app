import sqlite3
import os
import json
import datetime

TECH_DB_PATH = "tech_master.db"

# ==========================================
# 1. 非エンジニア向け 厳選用語マスターデータ
# （日常の例え話 ＋ 正確な公式定義つき）
# ==========================================
TECH_TERMS_DATA = [
    # --- 🤖 生成AI & 業務活用 ---
    {
        "category": "🤖 生成AI & 業務活用",
        "term": "RAG (検索拡張生成)",
        "english_full": "Retrieval-Augmented Generation",
        "reading": "ラグ / アールエージー",
        "metaphor": "『教科書持ち込みOKのテスト（カンニングペーパー付きAI）』。AIに社内データを全部丸暗記させるのではなく、自社の最新マニュアルを机の上に広げて、それを見ながら答えさせる仕組み。",
        "official_definition": "大規模言語モデル（LLM）が回答を生成する際、外部の文書データベースから関連情報を検索・抽出し、その内容をプロンプトに動的に付与して回答精度と最新性を担保する技術。",
        "business_impact": "社内規程の変更に即日対応可能。AIの適当な嘘（ハルシネーション）を激減させ、社内問い合わせ業務やカスタマーサポートの工数を最大70%削減できる。",
        "meeting_phrase": "「自社データを参照させたいのですが、ファインチューニングではなくRAG構成で小さくPoC（検証）から始めませんか？」",
        "pitfall_warning": "元となるマニュアルやPDFのフォーマットが崩れていると検索精度が落ちるため、社内文書の整理（前処理）が不可欠です。",
        "quiz_sentence": "社内データをAIに直接学習させず、都度マニュアルを検索して参照させながら正確に回答させる仕組みを[___]という。",
        "quiz_options": "RAG (検索拡張生成), ファインチューニング, プロンプトインジェクション, LoRA",
        "correct_answer": "RAG (検索拡張生成)"
    },
    {
        "category": "🤖 生成AI & 業務活用",
        "term": "ハルシネーション",
        "english_full": "Hallucination (幻覚)",
        "reading": "ハルシネーション",
        "metaphor": "『知ったかぶりでスラスラ嘘をつく後輩』。AIは言葉のつながりの確率で文章を作っているだけなので、本当は知らないことでも自信満々に架空の事実をでっち上げてしまう現象。",
        "official_definition": "AI（特に大規模言語モデル）が、学習データに含まれない事実無根の情報や誤った推論を、あたかも真実であるかのように出力してしまう現象。",
        "business_impact": "法律・医療・社内規定など正確性が求められる業務で鵜呑みにすると、重大な誤判断や対外的な信用失墜につながる。",
        "meeting_phrase": "「この用途ではハルシネーションが許容されないため、RAGによる根拠引用と、人間の最終チェック（Human-in-the-loop）を必須にしましょう。」",
        "pitfall_warning": "「最新のモデルならハルシネーションはゼロになる」と過信するのは禁物です。",
        "quiz_sentence": "生成AIがもっともらしい嘘や事実と異なる情報を自信満々に出力してしまう現象を[___]という。",
        "quiz_options": "ハルシネーション, オーバーフィッティング, ドリフト, トークンエラー",
        "correct_answer": "ハルシネーション"
    },
    {
        "category": "🤖 生成AI & 業務活用",
        "term": "プロンプトエンジニアリング",
        "english_full": "Prompt Engineering",
        "reading": "プロンプト エンジニアリング",
        "metaphor": "『新人バイトへの神・指示書』。「適当によろしく！」と丸投げするのではなく、「あなたは接客係です。クレーム対応の返信を、敬語で、3行以内で書いて」と具体的に指示して100点のアウトプットを引き出す技術。",
        "official_definition": "生成AIから望む精度と形式の出力を得るために、入力文（プロンプト）の指示内容、役割（ロール）、前提条件、制約事項、出力フォーマット等を最適に設計・構築する技術。",
        "business_impact": "指示の出し方一つでAIのアウトプット品質が10倍変わる。社内でテンプレ共有することで、全社的な業務効率が劇的に向上する。",
        "meeting_phrase": "「まずは現場でよく使うプロンプトをテンプレート化し、全社ポータルでナレッジ共有しましょう。」",
        "pitfall_warning": "長すぎる指示や曖昧な指示はAIを混乱させるため、「役割」「制約条件」「出力形式の具体例（Few-shot）」を整理して渡すのがコツです。",
        "quiz_sentence": "AIから高精度で意図通りの回答を引き出すために、入力する指示文や前提条件を工夫・設計する技術を[___]という。",
        "quiz_options": "プロンプトエンジニアリング, リバースエンジニアリング, ファインチューニング, アノテーション",
        "correct_answer": "プロンプトエンジニアリング"
    },
    {
        "category": "🤖 生成AI & 業務活用",
        "term": "トークン (Token)",
        "english_full": "Token",
        "reading": "トークン",
        "metaphor": "『AIにとっての文字数メーター（タクシーの料金メーター）』。AIが言葉を食べる「一口のサイズ」。日本語だと「ひらがな1文字≒1トークン」「漢字1文字≒2〜3トークン」程度で換算され、料金が決まる。",
        "official_definition": "自然言語処理およびLLMがテキストを処理・認識する際の最小構成単位。APIの利用料金（従量課金）やモデルの最大入力可能文字数（コンテキスト長）の基準となる。",
        "business_impact": "AIの従量課金コストや、一度に読み込める文書量（コンテキスト長）の上限を決定づける重要単位。",
        "meeting_phrase": "「このAPIは100万トークンあたり数ドルの従量課金なので、月間リクエスト数から試算するとランニングコストは月数万円に収まります。」",
        "pitfall_warning": "英語に比べて日本語はトークン消費が約1.5〜2倍多くなるため、コスト見積もり時は日本語換算係数を考慮する必要があります。",
        "quiz_sentence": "生成AIがテキストを処理する際の最小単位であり、APIの利用料金や入力文字数制限の基準となる単位を[___]という。",
        "quiz_options": "トークン, バイト, パラメータ, エポック",
        "correct_answer": "トークン"
    },
    {
        "category": "🤖 生成AI & 業務活用",
        "term": "マルチモーダル",
        "english_full": "Multimodal AI",
        "reading": "マルチモーダル",
        "metaphor": "『目・耳・口・手がぜんぶ揃った万能ロボット』。文字しか読めないAIから進化し、写真・図面・動画・音声も人間と同じように同時に見て聞いて理解できること。",
        "official_definition": "テキストだけでなく、画像、音声、動画など複数の異なるモダリティ（データ形式）を統合的に入力・処理・出力できるAIモデルの性質。",
        "business_impact": "手書きの領収書や請求書、製品の写真、音声議事録などをそのままAIに放り込むだけで、データ抽出・異常検知・要約が一瞬で完了する。",
        "meeting_phrase": "「マルチモーダルAIを活用して、現場からスマホで送られた設備写真から破損箇所を自動判定させましょう。」",
        "pitfall_warning": "画像や動画の処理はテキスト処理に比べてAPIコストや処理時間が大きくなる点に注意が必要です。",
        "quiz_sentence": "テキストだけでなく、画像・音声・動画など複数の異なる種類のデータを統合して理解・処理できるAIの性質を[___]という。",
        "quiz_options": "マルチモーダル, マルチスレッド, ハイブリッドクラウド, クロスプラットフォーム",
        "correct_answer": "マルチモーダル"
    },
    {
        "category": "🤖 生成AI & 業務活用",
        "term": "ファインチューニング",
        "english_full": "Fine-tuning (微調整)",
        "reading": "ファインチューニング",
        "metaphor": "『一般大学を出た新人に、自社特有の業界ルールをみっちり追加研修すること』。頭のいいAIの脳みその神経回路そのものを、専門データで書き換えて業界専門家にする。",
        "official_definition": "既存の学習済み基盤モデルに対し、特定用途や専門分野に特化したデータセットを追加で学習させ、モデルの重みパラメータ自体を微調整・最適化する手法。",
        "business_impact": "特定のトーン＆マナー（文体）や特殊な専門タスクにおいて、汎用AIでは出せない高い精度を実現できる。",
        "meeting_phrase": "「社内文書の検索ならRAGで十分です。業界特有の専門用語の文体再現が必要な段階でファインチューニングを検討しましょう。」",
        "pitfall_warning": "良質な学習データが数千〜数万件必要で、作成コストと時間がかかるため、安易に最初から選ぶのは地雷です。",
        "quiz_sentence": "既存の大規模言語モデルに対して特定の業務や専門分野のデータを追加学習させ、モデル自体のパラメータを微調整する手法を[___]という。",
        "quiz_options": "ファインチューニング, RAG, プロンプトインジェクション, ベクター検索",
        "correct_answer": "ファインチューニング"
    },

    # --- 💼 DX & クラウド・システム刷新 ---
    {
        "category": "💼 DX & クラウド・システム刷新",
        "term": "SaaS / PaaS / IaaS",
        "english_full": "Software/Platform/Infrastructure as a Service",
        "reading": "サース / パース / イアース",
        "metaphor": "『ピザの提供形態』。SaaS＝デリバリーピザ（すぐ食べるだけ）、PaaS＝生地とピザ窯のレンタル（好きな具を乗せて焼くだけ）、IaaS＝厨房スペースのレンタル（道具も食材も全部自分で持ち込み）。",
        "official_definition": "クラウドサービスの提供レイヤー。SaaS＝完成済みソフトウェア（ブラウザで利用）、PaaS＝アプリ開発用の実行基盤環境、IaaS＝仮想サーバーやネットワーク等のITインフラ資源。",
        "business_impact": "自社でサーバー機械を買わずにクラウド利用することで、初期投資ゼロ・即日導入・柔軟なスケールが可能になる。",
        "meeting_phrase": "「標準業務はSaaS（Salesforceやfreee等）を活用し、差別化したい独自機能だけをIaaS/PaaS（AWSやGCP）上に構築するのがベストです。」",
        "pitfall_warning": "SaaSを導入しただけで満足し、現場の業務プロセスを変えないと『使われないDX（宝の持ち腐れ）』になります。",
        "quiz_sentence": "インターネット経由でブラウザから即座に利用できるソフトウェアサービス（例: Slack, Gmail, Salesforce）を[___]という。",
        "quiz_options": "SaaS, IaaS, PaaS, オンプレミス",
        "correct_answer": "SaaS"
    },
    {
        "category": "💼 DX & クラウド・システム刷新",
        "term": "API連携",
        "english_full": "Application Programming Interface",
        "reading": "エーピーアイ れんけい",
        "metaphor": "『レストランの注文受付ウェイター』。客席（自社システム）と厨房（外部の決済や配送システム）の間で、注文と料理（データ）をルール通りに自動で受け渡ししてくれる共通の窓口。",
        "official_definition": "異なるソフトウェアやシステム同士が、データや機能を相互に自動で呼び出し・連携するための標準的な接続仕様およびインターフェース。",
        "business_impact": "「人が手作業でCSVをダウンロードし、別のシステムに手入力でアップロードする」という無駄な作業を完全ゼロ・自動化できる。",
        "meeting_phrase": "「新システム選定の必須要件として、既存の基幹システムとAPIでリアルタイム連携できるかを確認してください。」",
        "pitfall_warning": "API利用には回数制限（レートリミット）や仕様変更リスクがあるため、エラー時の自動再試行設計が必要です。",
        "quiz_sentence": "異なるソフトウェアやWebサービス同士が、互いにデータや機能を自動でやり取りするための接続窓口・共通ルールを[___]という。",
        "quiz_options": "API, GUI, SDK, URL",
        "correct_answer": "API"
    },
    {
        "category": "💼 DX & クラウド・システム刷新",
        "term": "アジャイル開発 vs ウォーターフォール",
        "english_full": "Agile vs Waterfall",
        "reading": "アジャイル / ウォーターフォール",
        "metaphor": "ウォーターフォール＝『設計図を1年かけて引く注文住宅』。アジャイル＝『まずは1部屋（最小機能）作って住みながら、毎週家具や部屋を増築していく方式』。",
        "official_definition": "ウォーターフォール＝要件定義・設計・開発・テストを直線的・段階的に進める従来型手法。アジャイル＝1〜2週間単位の短い反復（スプリント）で開発とリリースを繰り返し、柔軟に仕様変更に対応する手法。",
        "business_impact": "変化の激しいAI・新規事業では、アジャイルを採用することで数週間で動くものをリリースし、ユーザーの反応を見ながら素早く軌道修正できる。",
        "meeting_phrase": "「仕様が途中で変わる可能性が高い新規プロジェクトですので、ウォーターフォールではなくアジャイルで進めましょう。」",
        "pitfall_warning": "アジャイルは「計画がない」ことではありません。毎週の優先順位付けとスプリント管理が厳格に求められます。",
        "quiz_sentence": "短い期間（1〜2週間単位）で小さく開発・リリース・改善を繰り返しながら、変化に柔軟に対応する開発手法を[___]という。",
        "quiz_options": "アジャイル開発, ウォーターフォール開発, V字モデル, スクラッチ開発",
        "correct_answer": "アジャイル開発"
    },
    {
        "category": "💼 DX & クラウド・システム刷新",
        "term": "MVP (実用最小限の製品)",
        "english_full": "Minimum Viable Product",
        "reading": "エムブイピー",
        "metaphor": "『高級セダンを作る前に、まずはスケボーを作って「走れるか」試すこと』。大金をかけて完成品を作る前に、一番大事な機能だけを持った最小の試作品で客が喜ぶかテストする。",
        "official_definition": "顧客に価値を提供できる最小限の機能だけを備えた製品・サービス。最短期間・最小コストで仮説検証（ユーザーの需要確認）を行うために開発される。",
        "business_impact": "莫大な開発費を投じる前に、顧客が本当にお金を払ってくれるか（ニーズがあるか）を最小限のコストと時間で検証できる。",
        "meeting_phrase": "「最初から全機能を盛り込まず、まずはコア価値だけを検証できるMVPを1ヶ月で作りましょう。」",
        "pitfall_warning": "単なる「手抜きの未完成品」ではなく、「顧客に価値を提供できる最小限の完成度」であることが条件です。",
        "quiz_sentence": "新規事業やプロダクト開発において、顧客のニーズを最小限のコストと最短期間で検証するために作られる実用最小限の製品を[___]という。",
        "quiz_options": "MVP, PoC, KPI, KPI",
        "correct_answer": "MVP"
    },
    {
        "category": "💼 DX & クラウド・システム刷新",
        "term": "マイクロサービス",
        "english_full": "Microservices Architecture",
        "reading": "マイクロサービス",
        "metaphor": "『巨大なデパートではなく、専門店街（独立したお店の集まり）』。「決済」「会員管理」「商品検索」が別々のお店として動いているので、1つが壊れても全体は潰れない。",
        "official_definition": "システム全体を単一のプログラム（モノリス）で構築せず、独立して開発・デプロイ可能な小さなサービス群をAPIで疎結合に連携させるアーキテクチャ。",
        "business_impact": "一部の機能だけを頻繁にアップデートでき、アクセス急増時もその機能だけサーバーを増強できるため、開発速度と耐障害性が大幅に向上する。",
        "meeting_phrase": "「将来の事業拡大を見据え、初期から密結合なモノリスではなくマイクロサービス指向で疎結合に設計しましょう。」",
        "pitfall_warning": "サービス間の通信や運用管理が複雑になるため、小規模なシステムで無理に導入すると逆に開発コストが増大します。",
        "quiz_sentence": "システム全体を巨大な単一のプログラムで作るのではなく、機能ごとに独立した小さなサービスを組み合わせるアーキテクチャを[___]という。",
        "quiz_options": "マイクロサービス, モノリス, サーバーレス, オンプレミス",
        "correct_answer": "マイクロサービス"
    },

    # --- 🔒 セキュリティ & リスク管理 ---
    {
        "category": "🔒 セキュリティ & リスク管理",
        "term": "ゼロトラスト",
        "english_full": "Zero Trust Security",
        "reading": "ゼロトラスト",
        "metaphor": "『社内の人間でも、全室で毎回指紋認証を求める超厳重セキュリティ』。「一度ビルの受付を通ったから社内は安全」という考えを捨て、社長でも同僚でも毎回疑って身元を確認する。",
        "official_definition": "「社内ネットワークは信頼できる」という境界防御の前提を廃止し、「すべてのアクセス・端末・ユーザーを常に疑い、毎回厳格に検証・認証・認可する」セキュリティ概念。",
        "business_impact": "テレワークの普及やクラウド利用が進む中、社内ネットワークへの侵入を前提とした被害極小化と安全なリモートワーク環境を両立できる。",
        "meeting_phrase": "「VPNによる境界防御の限界を踏まえ、ID・端末・アクセスの都度認証を行うゼロトラストモデルへ移行しましょう。」",
        "pitfall_warning": "ゼロトラストは特定の製品名ではなく「決して信頼せず、常に検証する」というセキュリティの基本方針・概念です。",
        "quiz_sentence": "「社内ネットワークは安全」という従来の前提を捨て、「すべての通信・端末・ユーザーを信用せず常に検証する」セキュリティ概念を[___]という。",
        "quiz_options": "ゼロトラスト, 境界防御, VPN, ファイアウォール",
        "correct_answer": "ゼロトラスト"
    },
    {
        "category": "🔒 セキュリティ & リスク管理",
        "term": "2要素認証 (2FA / MFA)",
        "english_full": "Two-Factor / Multi-Factor Authentication",
        "reading": "にようそ にんしょう / エムエフエー",
        "metaphor": "『合言葉（パスワード）＋ スマホに届く暗証番号の「2重ロック」』。仮に合言葉の鍵が盗まれても、手元のスマホがないと絶対にドアが開かない仕組み。",
        "official_definition": "知識情報（パスワード等）、所持情報（スマホ、SMSコード、トークン等）、生体情報（指紋、顔認証等）の異なる3要素のうち、2つ以上を組み合わせて本人確認を行う認証方式。",
        "business_impact": "仮に社員のパスワードが漏洩・推測されても、第三者による不正ログインを99.9%防ぐことができる最強の防御策。",
        "meeting_phrase": "「全社員のGoogle Workspaceおよび主要SaaSへのログインには、MFA（2要素認証）を必須化設定してください。」",
        "pitfall_warning": "SMS認証はSIMスワップ詐欺に弱いため、認証アプリ（Google Authenticator等）や物理セキュリティキーの利用が推奨されます。",
        "quiz_sentence": "パスワード（知識情報）に加え、スマホへの通知（所持情報）や生体認証（生体情報）など異なる2つの要素を組み合わせて認証する仕組みを[___]という。",
        "quiz_options": "2要素認証 (MFA), シングルサインオン (SSO), OAuth, パスワードレス",
        "correct_answer": "2要素認証 (MFA)"
    },
    {
        "category": "🔒 セキュリティ & リスク管理",
        "term": "ランサムウェア",
        "english_full": "Ransomware",
        "reading": "ランサムウェア",
        "metaphor": "『会社の金庫を勝手に別の南京錠でロックするデジタル誘拐犯』。パソコン内のデータを勝手に暗号化して開けなくし、「元に戻したければ身代金を払え」と脅す凶悪ウイルス。",
        "official_definition": "感染した端末やサーバーのデータを強制的に暗号化して利用不能にし、暗号解除（復号）と引き換えに金銭（暗号資産等）を要求する悪意あるマルウェア。",
        "business_impact": "病院で電子カルテが停止して診療不能になったり、大企業で工場が数日停止して数十億円の損害が出るなど、事業継続に致命傷を与える。",
        "meeting_phrase": "「ランサムウェア対策として、感染を前提としたEDRの導入と、ネットワークから切り離した不変バックアップ（Immutable Backup）を確保しましょう。」",
        "pitfall_warning": "身代金を支払ってもデータが復旧される保証はなく、犯罪組織へ資金提供することになるため支払いは厳禁です。",
        "quiz_sentence": "感染したコンピュータのデータを勝手に暗号化して利用不能にし、復号と引き換えに身代金を要求するマルウェアを[___]という。",
        "quiz_options": "ランサムウェア, スパイウェア, アドウェア, トロイの木馬",
        "correct_answer": "ランサムウェア"
    },
    {
        "category": "🔒 セキュリティ & リスク管理",
        "term": "EDR (エンドポイント検知・対処)",
        "english_full": "Endpoint Detection and Response",
        "reading": "イーディーアール",
        "metaphor": "『全社員のパソコンに常駐する24時間専属の警備員』。門番（従来のウイルス対策ソフト）をすり抜けて侵入した泥棒の怪しい動きを即座に見つけ、そのパソコンの通信を秒速で遮断する。",
        "official_definition": "エンドポイント（PC、サーバー端末）の挙動ログを常時収集・監視し、ウイルス侵入後の異常な振る舞いを早期検知・自動隔離・原因調査するセキュリティソリューション。",
        "business_impact": "万が一マルウェアに侵入されても、被害が他端末に広がる前に数分で封じ込め、侵入経路と影響範囲を完全特定できる。",
        "meeting_phrase": "「従来のアンチウイルス（EPP）だけでなく、すり抜け後の検知・隔離が可能なEDRを全端末に配備しましょう。」",
        "pitfall_warning": "導入しただけではアラートが鳴り止まないため、24時間監視・対応してくれるSOC（セキュリティ監視センター）の運用体制が必要です。",
        "quiz_sentence": "社員のPCやサーバー（端末）上の挙動を常時監視し、ウイルス侵入後の不審な動きを早期検知・隔離・調査する仕組みを[___]という。",
        "quiz_options": "EDR, EPP, WAF, VPN",
        "correct_answer": "EDR"
    },
    {
        "category": "🔒 セキュリティ & リスク管理",
        "term": "シャドーIT",
        "english_full": "Shadow IT",
        "reading": "シャドー アイティー",
        "metaphor": "『会社の許可なく、個人LINEや私用クラウドで仕事データを送る裏口業務』。情シスの目が届かないところで勝手に無料ツールや個人スマホを使うこと。",
        "official_definition": "企業の情報システム部門の把握や承認を得ずに、従業員が私用のIT機器（スマホ、PC）や無料クラウドサービスを業務に無断利用する行為。",
        "business_impact": "個人アカウント経由で顧客情報や機密データが社外に流出する最大の温床となる。退職者がデータを持ち出すリスクも高い。",
        "meeting_phrase": "「単に個人利用を禁止するだけでなく、業務で使いやすい公認の生成AIやクラウドストレージを会社から支給することが一番のシャドーIT防止策です。」",
        "pitfall_warning": "厳しく禁止しすぎると現場の業務効率が落ち、隠れてコソコソ使う『真のシャドーIT』が増えるため、利便性とのバランスが重要です。",
        "quiz_sentence": "情報システム部門の把握や許可を得ずに、社員が私用の端末やクラウドサービスを業務に利用する行為を[___]という。",
        "quiz_options": "シャドーIT, BYOD, ソーシャルエンジニアリング, スプーフィング",
        "correct_answer": "シャドーIT"
    },

    # --- 🐍 Python & データ活用・自動化 ---
    {
        "category": "🐍 Python & データ活用・自動化",
        "term": "Pandas (パンダス)",
        "english_full": "Python Data Analysis Library (Pandas)",
        "reading": "パンダス",
        "metaphor": "『Excelがスーパーサイヤ人化した超高速ツール』。Excelなら固まる100万行のデータでも、0.1秒で複数表の結合（VLOOKUP）、集計（ピボット）、不要データのゴミ掃除を完了させる。",
        "official_definition": "Pythonでテーブル形式のデータ（行と列からなる表データ）を効率的に操作、加工、集計、分析するための最も標準的なデータ解析ライブラリ。",
        "business_impact": "毎月数時間かかっていた売上レポート集計や顧客データ突合のルーチンワークが、ボタン1つ（1秒）で終わるようになる。",
        "meeting_phrase": "「Excelの手作業集計でミスが多発しているため、PythonのPandasを使ってデータ前処理と月次レポートを自動化しましょう。」",
        "pitfall_warning": "データのカラム名（列名）や日付フォーマットがバラバラだとエラーになるため、入力ルールの統一が必要です。",
        "quiz_sentence": "Pythonで表形式データ（ExcelやCSV）を高速に読み込み、集計・加工・結合などを自由自在に行うための最重要ライブラリは[___]である。",
        "quiz_options": "Pandas, NumPy, Matplotlib, Requests",
        "correct_answer": "Pandas"
    },
    {
        "category": "🐍 Python & データ活用・自動化",
        "term": "Webスクレイピング",
        "english_full": "Web Scraping",
        "reading": "ウェブ スクレイピング",
        "metaphor": "『ネット上の情報を24時間自動でコピペして集めてくれるロボット』。競合他社のWebサイトを自動で見回り、価格や商品情報を一瞬で収集・整理する。",
        "official_definition": "WebサイトのHTML構造をプログラムで自動解析し、特定のテキスト、画像、価格データなどを抽出・収集して保存する技術。",
        "business_impact": "競合の価格変動をリアルタイムで検知して自社の価格戦略を最適化したり、業界トレンドの市場調査を完全自動化できる。",
        "meeting_phrase": "「競合他社の公開価格データをPythonで自動スクレイピングし、日次でダッシュボードに反映させています。」",
        "pitfall_warning": "相手サイトの利用規約で禁止されている場合や、過度なアクセスでサーバーに負荷をかけると法的な問題（業務妨害）になるため注意が必要です。",
        "quiz_sentence": "WebサイトからHTMLプログラムを自動解析し、必要なテキストや画像などのデータを抽出・収集する技術を[___]という。",
        "quiz_options": "Webスクレイピング, Webクローリング, APIリクエスト, フィッシング",
        "correct_answer": "Webスクレイピング"
    },
    {
        "category": "🐍 Python & データ活用・自動化",
        "term": "Jupyter Notebook",
        "english_full": "Jupyter Notebook",
        "reading": "ジュピター ノートブック",
        "metaphor": "『実験ノートのようなプログラミング画面』。1行コードを書いて実行すると、その真下にすぐグラフや表が出るため、試行錯誤しながらデータ分析ができる。",
        "official_definition": "Webブラウザ上でPythonコードの記述、実行、対話的なデータ可視化（グラフ・表）、メモの記述を統合して行えるデータ分析用の開発環境。",
        "business_impact": "データサイエンティストが分析したグラフや結果をそのまま社内プレゼン資料や共有レポートとして活用できる。",
        "meeting_phrase": "「分析の途中結果やグラフはJupyter Notebook上にまとめてありますので、こちらの画面を見ながら議論しましょう。」",
        "pitfall_warning": "コードの実行順序がバラバラになると再現性がなくなるため、最終的には上から順に再実行（Run All）して確認するルールが大切です。",
        "quiz_sentence": "ブラウザ上でコードの記述、実行、表やグラフの可視化を対話的に行える、データ分析で最も広く使われているPython実行環境は[___]である。",
        "quiz_options": "Jupyter Notebook, VS Code, PyCharm, Terminal",
        "correct_answer": "Jupyter Notebook"
    },
    {
        "category": "🐍 Python & データ活用・自動化",
        "term": "データクレンジング",
        "english_full": "Data Cleansing",
        "reading": "データ クレンジング",
        "metaphor": "『料理の下ごしらえ（野菜の泥落とし）』。全角・半角の混在や表記ゆれ（`株式会社`と`(株)`）、重複などのゴミデータを綺麗に掃除して整えること。",
        "official_definition": "データベース内の誤記、表記ゆれ、重複、欠損値、フォーマット不一致などの不整合データを取り除き、正確で分析可能な品質に整備・標準化する前処理作業。",
        "business_impact": "「ゴミデータを入れたらゴミ結果しか出ない（Garbage In, Garbage Out）」。AIやデータ分析プロジェクトの成功の8割はこの前処理で決まる。",
        "meeting_phrase": "「AI導入の前に、まずは社内顧客データベースのデータクレンジングと名寄せを徹底的に行いましょう。」",
        "pitfall_warning": "地味で工数がかかるため過小評価されがちですが、ここをサボると後からシステム全体の再構築が必要になります。",
        "quiz_sentence": "データベース内の表記ゆれ、重複データ、欠損値、誤入力などを取り除き、分析やAIで使える綺麗な状態に整える作業を[___]という。",
        "quiz_options": "データクレンジング, データマイニング, データレイク, 暗号化",
        "correct_answer": "データクレンジング"
    },

    # --- 🌐 Web・IT基礎 & ネットワーク ---
    {
        "category": "🌐 Web・IT基礎 & ネットワーク",
        "term": "HTTPステータスコード (200, 404, 500)",
        "english_full": "HTTP Status Code",
        "reading": "エイチティーティーピー ステータスコード",
        "metaphor": "『Webサーバーからの3大返事』。200＝「OK！ページあります」、404＝「探した人のミス（URLが間違ってる/リンク切れ）」、500＝「店側のミス（サーバーが故障・パンク中）」。",
        "official_definition": "Webブラウザからの要求（リクエスト）に対して、Webサーバーが処理結果の状態を3桁の数字で通知するレスポンスコード。",
        "business_impact": "障害発生時に「400番台（クライアント側の問題）」か「500番台（自社サーバー側の問題）」かを瞬時に見分けることで、原因特定と初動対応を迅速化できる。",
        "meeting_phrase": "「500エラー（Internal Server Error）が急増しているので、直近のデプロイをロールバック（巻き戻し）しましょう。」",
        "pitfall_warning": "404エラーはお客様が誤ったURLを入力した場合にも出るため、自社システム停止と混同しないよう切り分けが必要です。",
        "quiz_sentence": "Webサーバーにリクエストを送った際、サーバー側のプログラムの不具合や故障によって処理に失敗したことを表すHTTPステータスコードは[___]である。",
        "quiz_options": "500 (Internal Server Error), 404 (Not Found), 200 (OK), 403 (Forbidden)",
        "correct_answer": "500 (Internal Server Error)"
    },
    {
        "category": "🌐 Web・IT基礎 & ネットワーク",
        "term": "キャッシュ (Cache)",
        "english_full": "Cache",
        "reading": "キャッシュ",
        "metaphor": "『よく使う書類を奥の倉庫に取りに行かず、デスクの上に置いておくこと』。一度読み込んだ画像やWebページを手元に保存しておき、2回目以降を爆速で開く仕組み。",
        "official_definition": "一度取得・計算したデータを一時的に高速な記憶領域に保持しておき、次回以降の同一データへのアクセスを高速化・サーバー負荷軽減する仕組み。",
        "business_impact": "Webサイトの表示速度が劇的に速くなり、ユーザー離脱率を下げるとともに、サーバーの負荷と通信コストを大幅に削減できる。",
        "meeting_phrase": "「Webサイトのデザイン変更が反映されないお客様には、ブラウザのキャッシュクリア（Shift+F5）を案内してください。」",
        "pitfall_warning": "古いキャッシュが残り続けると、最新の価格や在庫情報が正しく表示されないトラブルが起きるため、適切な有効期限設定が必要です。",
        "quiz_sentence": "一度アクセスしたWebページのデータなどを一時的に手元に保存し、次回以降のアクセスを高速化する仕組みを[___]という。",
        "quiz_options": "キャッシュ, クッキー, セッション, プロキシ",
        "correct_answer": "キャッシュ"
    },
    {
        "category": "🌐 Web・IT基礎 & ネットワーク",
        "term": "Docker (コンテナ)",
        "english_full": "Docker Container",
        "reading": "ドッカー",
        "metaphor": "『家具・家電付きの引っ越しコンテナ』。プログラムを動かすのに必要な道具を全部1つの箱に詰めることで、どのパソコンやクラウドに持って行っても一瞬で全く同じように動く。",
        "official_definition": "アプリケーションとその実行に必要な環境（OSライブラリ、設定ファイル等）を1つの独立したコンテナとしてパッケージ化し、どのインフラ環境でも均一な動作を保証するコンテナ型仮想化技術。",
        "business_impact": "「開発者のPCでは動いたのに、本番サーバーでは動かない」というエンジニアあるあるのトラブルを完全撲滅し、開発・リリース速度を劇的に加速する。",
        "meeting_phrase": "「本番環境と開発環境の差異をなくすため、全サービスをDockerコンテナ化してデプロイを自動化しましょう。」",
        "pitfall_warning": "コンテナ自体の容量が肥大化しないよう、不要なファイルを含めないスリムな設計が推奨されます。",
        "quiz_sentence": "アプリケーションとその実行に必要なすべての環境を1つの独立した箱にパッケージ化し、どの環境でも同じ動作を保証する仮想化技術を[___]という。",
        "quiz_options": "Docker (コンテナ), 仮想マシン (VM), オンプレミス, Git",
        "correct_answer": "Docker (コンテナ)"
    }
]

# (想定問答、トレードオフ、チートシートデータは既存のものを引き継ぎ)
MEETING_SCENARIOS_DATA = [
    {
        "category": "🤖 生成AIの業務導入",
        "title": "役員からの「ChatGPTに社内データを全部読み込ませよう」提案への対応",
        "counterpart": "専務取締役（非IT部門）",
        "counterpart_statement": "「ChatGPTって本当にすごいね！うちの顧客リストと過去の機密提案書を全部読み込ませて、自動で新しい営業企画書を作らせようよ！」",
        "best_response": "「専務、素晴らしいアイデアですね！ただし一般の無料版・個人版ChatGPTにそのまま入力すると、他社のAI学習データとして情報漏洩する規約上のリスクがあります。法人向けのAzure OpenAI環境（データ非保持契約）を用意するか、自社データを外に出さない『RAG（検索拡張生成）』の仕組みを組んで安全に活用しましょう。」",
        "key_point": "否定から入らず着眼点を褒めた上で、「規約上の漏洩リスク」と「代替のエンタープライズ安全策」をセットで提示してプロジェクトを前に進める。"
    },
    {
        "category": "🤖 生成AIの業務導入",
        "title": "受託開発ベンダーからの「ファインチューニング推奨」への切り返し",
        "counterpart": "AI受託開発ベンダーの営業担当",
        "counterpart_statement": "「御社の社内マニュアルQAシステムですが、最新モデルをファインチューニングして専用モデルを独自構築するのが最も高精度でおすすめです！」",
        "best_response": "「ご提案ありがとうございます。ただ、当社の社内規程や商品情報は毎月頻繁に改定されます。ファインチューニングだと改定のたびに再学習コストと工数がかさみませんか？まずは文書を差し替えるだけで即時反映できる『RAG（ベクター検索）』でPoC（検証）を実施し、精度が不足した場合にファインチューニングを検討したいのですが、いかがでしょうか？」",
        "key_point": "「マニュアルの改定頻度」と「再学習コスト」を突っ込み、不要な高額開発を回避して小さくRAGから始めるよう主導権を握る。"
    },
    {
        "category": "💼 DX & システム開発",
        "title": "現場リーダーからの「今の業務フローをそのまま全部システム化して」要望への対応",
        "counterpart": "営業部リーダー",
        "counterpart_statement": "「新しいシステムを作るなら、今うちの部署でやってるハンコ承認とExcelの細かい集計手順を、そのまま100%完全再現できるように作ってください！」",
        "best_response": "「現状の手順を大切にされているのはよく分かります。ただ、従来の紙やExcelの作業手順をそのままシステム化すると、莫大な開発費がかかる上に手作業の無駄が残ってしまいます（デジタル化してもDXにならない）。まずは『業務プロセスそのもの（本当にこの承認が必要か）』を標準化・スリム化し、標準的なSaaS機能に業務を合わせる（Fit to Standard）方針で進めませんか？」",
        "key_point": "「現状プロセスの完全コピー」は失敗DXの典型。業務のスリム化（BPR）と標準SaaSの活用を提案する。"
    },
    {
        "category": "🔒 セキュリティ監査",
        "title": "取引先監査役からの「テレワーク環境のセキュリティ対策」質問への回答",
        "counterpart": "大手取引先のセキュリティ監査役",
        "counterpart_statement": "「御社は全社員がフルリモートワークとのことですが、社外から社内情報にアクセスする際のセキュリティはどのように担保されていますか？VPNだけですか？」",
        "best_response": "「ご質問ありがとうございます。当社ではVPNのみの境界防御に依存せず、『ゼロトラスト』の考え方を採用しています。全社員のクラウドアクセスには2要素認証（MFA）を必須化し、全PCにEDRを導入して不審な挙動を24時間監視・自動隔離できる体制を整えております。」",
        "key_point": "「VPNだけ」と答えると脆弱と見なされる。ゼロトラスト、MFA、EDRの3点セットを提示して取引先を安心させる。"
    }
]

TRADEOFFS_DATA = [
    {
        "title": "社内文書検索AIの構築方式",
        "scenario": "社内マニュアルや商品データが毎月頻繁に更新される環境で、社内QAボットを作りたい。どっちを選ぶ？",
        "option_a": "RAG (検索拡張生成 / カンニングペーパー方式)",
        "option_b": "ファインチューニング (モデル独自追加学習方式)",
        "correct_option": "RAG (検索拡張生成 / カンニングペーパー方式)",
        "decision_reason": "頻繁に改定される文書の場合、ファインチューニングだと都度莫大な再学習費用と時間がかかります。RAGならファイルをフォルダに放り込むだけで即座に最新回答が反映されるため圧倒的に有利です。"
    },
    {
        "title": "リモートワーク時代のセキュリティ基盤",
        "scenario": "社員が自宅やカフェ、コワーキングスペースなど様々な場所からクラウドを利用する環境。どっちを選ぶ？",
        "option_a": "ゼロトラスト (ID・端末ごとの都度認証 ＋ EDR監視)",
        "option_b": "従来の境界防御 (社内VPN接続の一括信用)",
        "correct_option": "ゼロトラスト (ID・端末ごとの都度認証 ＋ EDR監視)",
        "decision_reason": "VPNは一度侵入を許すと社内ネットワーク全体を自由に探索されてしまいます。ゼロトラストなら「全員を毎回疑う」ため、ID盗難や端末紛失時の被害を最小限に食い止められます。"
    },
    {
        "title": "新規事業サービスの初期開発手法",
        "scenario": "顧客ニーズがまだ不確実で、市場の反応を見ながら素早く改善したい新規Webサービス。どっちを選ぶ？",
        "option_a": "アジャイル開発 (1〜2週間単位で小さくMVPをリリース)",
        "option_b": "ウォーターフォール開発 (半年かけて要件定義から完璧に設計)",
        "correct_option": "アジャイル開発 (1〜2週間単位で小さくMVPをリリース)",
        "decision_reason": "新規事業でウォーターフォールを採用すると、半年後に完成した時点で「顧客に全く求められていなかった」という大赤字リスクがあります。アジャイルなら最小限の機能（MVP）ですぐに仮説検証できます。"
    },
    {
        "title": "大量データ（100万行）の月次集計処理",
        "scenario": "全国店舗の売上データ100万行を毎月集計・突合してレポートを作成したい。どっちを選ぶ？",
        "option_a": "Python (Pandasによる一括自動処理)",
        "option_b": "Excel (VLOOKUPとピボットテーブルの手動操作)",
        "correct_option": "Python (Pandasによる一括自動処理)",
        "decision_reason": "Excelは数十万行を超えると動作が極端に重くなりフリーズします。PythonのPandasを使えば100万行でも0.1秒で処理でき、毎月の作業をワンクリックで完全自動化できます。"
    }
]

CHEAT_SHEETS_DATA = [
    {
        "theme": "🤖 生成AI・LLM導入プロジェクトの打ち合わせ",
        "must_know_terms": "1. RAG（社内マニュアル見ながら回答する仕組み）\n2. ハルシネーション（AIの知ったかぶり嘘）\n3. トークン数（文字数・利用料金の単位）\n4. Azure OpenAI（データが学習に使われない法人向け安全環境）\n5. プロンプト（AIへの指示文）",
        "trap_questions": "・「社内データの更新頻度に対して、再学習コストや運用工数はどれくらいかかりますか？（RAGで十分では？）」\n・「出力の正確性を担保するための、人間のチェック体制（Human-in-the-loop）はどう設計しますか？」\n・「APIのトークン消費量と月額ランニングコストのシミュレーションはどうなっていますか？」",
        "ng_behavior": "「ChatGPTって何でも完璧に自動でやってくれるんですよね？」と全知全能を期待して話すのは禁物。AIは『確率で最もらしい言葉を返すアシスタント』であることを前提に話しましょう。"
    },
    {
        "theme": "🔒 セキュリティ監査・システム更新の打ち合わせ",
        "must_know_terms": "1. ゼロトラスト（社内も疑って毎回認証する標準方針）\n2. 2要素認証/MFA（パスワード＋スマホ通知の2重鍵）\n3. EDR（PCに入り込んだウイルスを検知・即隔離する警備員）\n4. ランサムウェア（データを暗号化して身代金を要求するウイルス）\n5. シャドーIT（社員が勝手に個人スマホや私用クラウドを使う裏口業務）",
        "trap_questions": "・「VPNが突破された場合の、侵入拡大を防ぐ対策（EDRや端末隔離）はどうなっていますか？」\n・「万が一ランサムウェアに感染した場合、オフラインバックアップから何時間で復旧できますか？」\n・「社内でのChatGPT等の私的利用（シャドーIT）を防ぐための、公認ガイドラインとツール支給はありますか？」",
        "ng_behavior": "「うちはウイルス対策ソフト（アンチウイルス）が入っているから大丈夫」と言うのは時代遅れ。現代は『侵入されることを前提とした対策（EDRやゼロトラスト）』が常識です。"
    },
    {
        "theme": "💼 DXシステム刷新・クラウド移行の打ち合わせ",
        "must_know_terms": "1. SaaS（月額ですぐ使える完成品ソフトウェア）\n2. API連携（システム同士を自動でつなぐ窓口）\n3. アジャイル（小さく作って素早く改善する手法）\n4. MVP（最小限の機能で作る実用製品）\n5. レガシーシステム（古くてブラックボックス化した既存システム）",
        "trap_questions": "・「今の業務手順をそのままシステム化するのではなく、標準SaaSの機能に業務を合わせる（Fit to Standard）検討はしましたか？」\n・「他システムとのデータ連携は、手作業CSVではなくAPIで自動化できますか？」\n・「最初から100点の巨大システムを作らず、まずはMVPで小さく検証しませんか？」",
        "ng_behavior": "「今のExcelの作業手順と画面を1ミリも変えずに完全再現してください」と要求するのは大失敗DXの典型です。"
    }
]

def init_and_seed_tech_master_db(db_path=TECH_DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tech_terms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        term TEXT NOT NULL UNIQUE,
        english_full TEXT,
        reading TEXT NOT NULL,
        metaphor TEXT NOT NULL,
        official_definition TEXT,
        business_impact TEXT NOT NULL,
        meeting_phrase TEXT NOT NULL,
        pitfall_warning TEXT NOT NULL,
        quiz_sentence TEXT NOT NULL,
        quiz_options TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        repetitions INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        ease_factor REAL DEFAULT 2.5,
        next_review_date TEXT,
        mistake_count INTEGER DEFAULT 0,
        created_at TEXT
    )
    ''')

    # カラム存在確認 (official_definition)
    cursor.execute("PRAGMA table_info(tech_terms)")
    cols = [c[1] for c in cursor.fetchall()]
    if "official_definition" not in cols:
        try:
            cursor.execute("ALTER TABLE tech_terms ADD COLUMN official_definition TEXT")
        except Exception:
            pass

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS meeting_scenarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        title TEXT NOT NULL UNIQUE,
        counterpart TEXT NOT NULL,
        counterpart_statement TEXT NOT NULL,
        best_response TEXT NOT NULL,
        key_point TEXT NOT NULL,
        repetitions INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        ease_factor REAL DEFAULT 2.5,
        next_review_date TEXT,
        mistake_count INTEGER DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tradeoffs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        scenario TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        correct_option TEXT NOT NULL,
        decision_reason TEXT NOT NULL,
        repetitions INTEGER DEFAULT 0,
        interval_days INTEGER DEFAULT 0,
        ease_factor REAL DEFAULT 2.5,
        next_review_date TEXT,
        mistake_count INTEGER DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cheat_sheets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        theme TEXT NOT NULL UNIQUE,
        must_know_terms TEXT NOT NULL,
        trap_questions TEXT NOT NULL,
        ng_behavior TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS study_time_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        study_date TEXT NOT NULL,
        seconds REAL NOT NULL,
        category TEXT NOT NULL,
        item_count INTEGER DEFAULT 1,
        created_at TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS study_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        is_correct INTEGER NOT NULL,
        reviewed_at TEXT NOT NULL,
        item_type TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_state (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    now_iso = datetime.datetime.now().isoformat()
    today_iso = datetime.date.today().isoformat()

    for item in TECH_TERMS_DATA:
        cursor.execute('''
        INSERT INTO tech_terms (category, term, english_full, reading, metaphor, official_definition, business_impact, meeting_phrase, pitfall_warning, quiz_sentence, quiz_options, correct_answer, next_review_date, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(term) DO UPDATE SET
            category = excluded.category,
            english_full = excluded.english_full,
            reading = excluded.reading,
            metaphor = excluded.metaphor,
            official_definition = excluded.official_definition,
            business_impact = excluded.business_impact,
            meeting_phrase = excluded.meeting_phrase,
            pitfall_warning = excluded.pitfall_warning,
            quiz_sentence = excluded.quiz_sentence,
            quiz_options = excluded.quiz_options,
            correct_answer = excluded.correct_answer
        ''', (
            item["category"], item["term"], item["english_full"], item["reading"],
            item["metaphor"], item.get("official_definition", ""), item["business_impact"], item["meeting_phrase"], item["pitfall_warning"],
            item["quiz_sentence"], item["quiz_options"], item["correct_answer"],
            today_iso, now_iso
        ))

    for item in MEETING_SCENARIOS_DATA:
        cursor.execute('''
        INSERT INTO meeting_scenarios (category, title, counterpart, counterpart_statement, best_response, key_point, next_review_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(title) DO UPDATE SET
            category = excluded.category,
            counterpart = excluded.counterpart,
            counterpart_statement = excluded.counterpart_statement,
            best_response = excluded.best_response,
            key_point = excluded.key_point
        ''', (
            item["category"], item["title"], item["counterpart"], item["counterpart_statement"],
            item["best_response"], item["key_point"], today_iso
        ))

    for item in TRADEOFFS_DATA:
        cursor.execute('''
        INSERT INTO tradeoffs (title, scenario, option_a, option_b, correct_option, decision_reason, next_review_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(title) DO UPDATE SET
            scenario = excluded.scenario,
            option_a = excluded.option_a,
            option_b = excluded.option_b,
            correct_option = excluded.correct_option,
            decision_reason = excluded.decision_reason
        ''', (
            item["title"], item["scenario"], item["option_a"], item["option_b"],
            item["correct_option"], item["decision_reason"], today_iso
        ))

    for item in CHEAT_SHEETS_DATA:
        cursor.execute('''
        INSERT INTO cheat_sheets (theme, must_know_terms, trap_questions, ng_behavior)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(theme) DO UPDATE SET
            must_know_terms = excluded.must_know_terms,
            trap_questions = excluded.trap_questions,
            ng_behavior = excluded.ng_behavior
        ''', (
            item["theme"], item["must_know_terms"], item["trap_questions"], item["ng_behavior"]
        ))

    conn.commit()
    conn.close()
    print("✅ TechMaster database successfully seeded with definitions and metaphors!")

if __name__ == "__main__":
    init_and_seed_tech_master_db()
