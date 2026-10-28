import os
import base64
import json
import urllib.request
import subprocess
from datetime import datetime

def get_git_info():
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8').strip()
        build_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        return f"v-{commit_hash} ({build_time})"
    except Exception:
        return "v-1.3.1"

build_version_info = get_git_info()

base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, "public", "images")

# Load all images dynamically
images_dict = {}
if os.path.exists(img_dir):
    for fname in sorted(os.listdir(img_dir)):
        if fname.startswith('.') or not (fname.endswith('.png') or fname.endswith('.webp') or fname.endswith('.jpg') or fname.endswith('.jpeg')):
            continue
        p = os.path.join(img_dir, fname)
        with open(p, "rb") as f:
            images_dict[fname] = base64.b64encode(f.read()).decode("utf-8")

print(f"Loaded {len(images_dict)} images for Worker bundle.")

audio_dir = os.path.join(base_dir, "public", "audio")
audio_files = ["adam.mp3", "oliver.mp3", "sofia.mp3", "xiaosi.mp3", "xiaosu.mp3"]
audio_dict = {}
for name in audio_files:
    p = os.path.join(audio_dir, name)
    if os.path.exists(p):
        with open(p, "rb") as f:
            audio_dict[name] = base64.b64encode(f.read()).decode("utf-8")
print(f"Loaded {len(audio_dict)} audio files for Worker bundle.")

translations = {
    "en": {
        "title": "Workout Timer: Voice Coach - High Intensity Interval Training, Apple TV & Gym Clock",
        "desc": "Next-gen workout timer with studio voice coaches in 4 languages, 7 curated video coach programs, Apple TV living room cinema mode, Apple Watch & AirPods heart rate sync, and 100% offline privacy.",
        "keywords": "workout timer, apple tv workout, tvos fitness timer, interval timer, hiit timer, tabata timer, voice coach, apple watch workout, dynamic island timer, boxing timer, gym clock, 10 min abs, core workout, live activity",
        "brand_name": "Workout Timer",
        "nav_tv": "Apple TV",
        "nav_programs": "Programs",
        "nav_features": "Features",
        "nav_coaches": "Coaches",
        "nav_faq": "FAQ",
        "nav_support": "Support",
        "nav_privacy": "Privacy",
        "hero_badge": "✨ NEW IN V1.3.1 • NOW ON APPLE TV • UNIVERSAL PURCHASE",
        "hero_title": "Train Like an Athlete on <span>Every Apple Screen</span>",
        "hero_sub": "The ultimate interval timer featuring studio-recorded voice trainers, 7 guided coach video programs, a giant 10-foot Apple TV living room clock, Apple Watch & AirPods live heart rate sync, and complete offline privacy.",
        "pills": [
            "📺 Apple TV 4K Living Room UI",
            "📱 7 Guided Coach Programs",
            "⌚️ Apple Watch & AirPods Pro Live HR",
            "🏝️ Dynamic Island Live Activity",
            "🔒 100% Offline & Pure Privacy"
        ],
        "cta_app_store": "Download on the App Store",
        "cta_watch_video": "Watch Video Demo",
        "cta_note": "Universal Purchase: iPhone, iPad, Apple Watch & Apple TV • iOS 17+, tvOS 17+, watchOS 10+",
        "gallery_hint": "👈 Swipe horizontally to preview app screens 👉",
        
        # Apple TV Spotlight Section
        "sec_tv_badge": "NOW ON APPLE TV",
        "sec_tv_title": "Turn Your Living Room into a Boutique Gym",
        "sec_tv_sub": "Designed from the ground up for tvOS 17+ with Siri Remote navigation. Giant 4K countdown ring readable from 10 feet away, split-screen video coaching, and zero distractions.",
        "tv_tab_programs": "7 Coach Programs",
        "tv_tab_ring": "Giant 10-Foot Ring",
        "tv_tab_cinema": "Cinema Video Player",
        "tv_feat_1_title": "Giant 4K Countdown Ring",
        "tv_feat_1_desc": "Crisp GPU-rendered countdown ring and bold digits easily readable across any living room, garage gym, or fitness studio.",
        "tv_feat_2_title": "Siri Remote Navigation",
        "tv_feat_2_desc": "Effortless clickpad control: launch classic Tabata, adjust intervals on the fly, or scrub through 7 coach video routines.",
        "tv_feat_3_title": "Split Cinema Guidance",
        "tv_feat_3_desc": "Continuous form guidance with smooth looping video on the big screen so you stay locked in through every repetition.",

        # 7 Programs Section
        "sec_programs_badge": "GUIDED CURRICULUM",
        "sec_programs_title": "7 Curated Coach Video Programs",
        "sec_programs_sub": "Standard looping video demonstrations during Work, paired with intelligent 'UP NEXT' rest previews so you transition seamlessly between movements.",
        "up_next_badge": "REST PREVIEW INNOVATION",
        "up_next_title": "Never Wonder What's Coming Next",
        "up_next_desc": "During rest intervals, the screen automatically shifts to an 'UP NEXT' preview of the upcoming exercise. Catch your breath, hydrate, and get into position before the next work bell rings.",
        "programs": [
            {"title": "10-Min Abs", "coach": "Coach Hannah", "rounds": "12 Rounds", "type": "Core & Obliques", "desc": "High-efficiency core burner targeting upper abs, lower abs, and obliques with zero-jerk video guidance."},
            {"title": "Core & Strength", "coach": "Coach Marcus", "rounds": "10 Rounds", "type": "Stability & Strength", "desc": "Functional core endurance, anti-rotation control, and deep abdominal wall activation."},
            {"title": "Full Body Cardio Burn", "coach": "Coach Chloe", "rounds": "14 Rounds", "type": "High-Intensity Fat Burn", "desc": "Explosive dynamic movements designed to maximize calorie burn and metabolic conditioning."},
            {"title": "Leg & Glute Power", "coach": "Coach Ryan", "rounds": "12 Rounds", "type": "Lower Body Power", "desc": "Squats, lunges, and plyometric pulses to build lower chain strength and explosive athleticism."},
            {"title": "Upper Body Pump", "coach": "Coach Ryan", "rounds": "10 Rounds", "type": "Chest, Back & Arms", "desc": "Bodyweight push-pull conditioning for shoulder stability, chest power, and arm endurance."},
            {"title": "Tabata Supercharged", "coach": "Coach Elena", "rounds": "8 Rounds", "type": "20s Work / 10s Rest", "desc": "The scientifically proven 4-minute maximum oxygen uptake protocol for peak cardiovascular capacity."},
            {"title": "Boxing Conditioning", "coach": "Coach Elena", "rounds": "6 Rounds", "type": "3-Min Rounds / 1-Min Rest", "desc": "Authentic fighter rhythm: three-minute high-output rounds paired with 60-second recovery intervals."}
        ],

        # Multi-Device Ecosystem Section
        "sec_ecosystem_badge": "APPLE ECOSYSTEM SYNERGY",
        "sec_ecosystem_title": "One App. One Purchase. Every Apple Device.",
        "sec_ecosystem_sub": "Workout Timer runs natively across iPhone, Apple TV, Apple Watch, and iPad. Buy once, own forever across all your screens.",
        "ecosystem_devices": [
            {"name": "Apple TV", "icon": "📺", "tag": "Living Room 10-Foot UI", "desc": "Big screen cinema workouts and giant gym clock with Siri Remote navigation."},
            {"name": "iPhone", "icon": "📱", "tag": "Dynamic Island & 50:50 Mode", "desc": "Live Activity tracking on Lock Screen and split landscape gym display."},
            {"name": "Apple Watch", "icon": "⌚️", "tag": "Standalone Wrist Timer", "desc": "Tactile wrist haptics, standalone offline timer, and live heart rate streaming."},
            {"name": "iPad", "icon": "💻", "tag": "13-Inch Gym Display", "desc": "Expansive gym mat display with split video and giant high-visibility digits."}
        ],

        # Video Demo Section
        "sec_video_badge": "APP DEMO",
        "sec_video_title": "Experience Workout Timer in Action",
        "sec_video_sub": "Watch Coach Hannah guide the 10-Min Abs routine, explore 50:50 Cinema Mode, and see Apple Watch & AirPods live sync in real-time.",

        # Features Section
        "sec_features_title": "Engineered for Athletic Excellence",
        "sec_features_sub": "Everything athletes need for Tabata, HIIT, Boxing, AMRAP, and Core Workouts.",
        "features": [
            {"icon": "🎙️", "title": "5 Studio Human Coaches", "desc": "Real studio-recorded voice coaches in English (US & UK), Spanish (LatAm), and Chinese (Traditional & Simplified) guide every work, rest, and countdown."},
            {"icon": "📺", "title": "Apple TV 10-Foot Living Room UI", "desc": "Native tvOS experience with giant 4K countdown ring, Siri Remote navigation, and cinema split-screen coaching."},
            {"icon": "⌚️", "title": "Apple Watch & AirPods Live Sync", "desc": "Standalone watchOS app with wrist haptic cues, plus live streaming heart rate and active calories from Apple Watch and AirPods Pro."},
            {"icon": "🏝️", "title": "Dynamic Island & Live Activity", "desc": "Track your interval progression directly from your Lock Screen and Dynamic Island with hardware-accelerated GPU progress bars."},
            {"icon": "🎬", "title": "Post-Workout Celebration Videos", "desc": "Celebrate every breakthrough! Your chosen coach congratulates you with a full-screen motivational video after each completed session."},
            {"icon": "⏱️", "title": "Free Custom Interval Timer", "desc": "Launch instantly into classic Tabata (20s/10s), HIIT (40s/20s), or 3-minute Boxing rounds, or customize your own sets and cycles."},
            {"icon": "🎵", "title": "Smart Audio Ducking", "desc": "Automatically ducks background Spotify or Apple Music volume during voice announcements and countdowns, then restores it smoothly."},
            {"icon": "🔒", "title": "100% Offline & Pure Privacy", "desc": "No account creation, no analytics tracking, no forced subscriptions, and zero advertising. Your training data stays strictly on your device."}
        ],

        # Coaches Section
        "sec_coaches_title": "Meet Your Studio Trainers",
        "sec_coaches_sub": "Five dedicated voice coaches recorded in pristine studio audio.",
        "coach_xiaosu": "Coach XiaoSu",
        "coach_xiaosu_sub": "Mandarin Chinese • Energetic & Warm",
        "coach_xiaosi": "Coach XiaoSi",
        "coach_xiaosi_sub": "Taiwanese Mandarin • Passionate & Sharp",
        "coach_oliver": "Coach Oliver",
        "coach_oliver_sub": "British English • Crisp & Motivating",
        "coach_sofia": "Coach Sofia",
        "coach_sofia_sub": "Spanish (LatAm) • Enérgica e Inspiradora",
        "coach_adam": "Coach Adam",
        "coach_adam_sub": "US English • Confident & Powerful",

        # Reviews & FAQ
        "review_1": "The Apple TV app completely transformed my living room workouts. The giant timer ring is so easy to see from my yoga mat!",
        "review_2": "The voice coaches make such a huge difference. I finally feel like I am in a real studio class without annoying ads.",
        "review_3": "The UP NEXT preview during rest intervals is pure genius. I never lose momentum or scramble for position.",
        "sec_faq_title": "Frequently Asked Questions",
        "sec_faq_sub": "Everything you need to know about Workout Timer.",
        "faqs": [
            {
                "q": "Is the new Apple TV app included in the same purchase?",
                "a": "Yes! Workout Timer features Apple Universal Purchase. A single download gives you complete access to iPhone, iPad, Apple Watch, and Apple TV at no additional cost."
            },
            {
                "q": "Does Workout Timer require a monthly subscription?",
                "a": "No. Workout Timer is a single, one-time purchase. There are no recurring subscriptions, no hidden fees, and absolutely no ads. Buy it once, and own all studio voice coaches and features forever."
            },
            {
                "q": "How does the Apple Watch & AirPods heart rate monitoring work?",
                "a": "The app includes a dedicated standalone Apple Watch app that delivers tactile haptic taps on your wrist. When paired with iPhone, it streams live heart rate and active calories to your circular timer ring and Dynamic Island. AirPods Pro heart rate tracking is also supported via Apple HealthKit."
            },
            {
                "q": "Can I listen to my own music while the timer is running?",
                "a": "Yes! The app features intelligent Audio Ducking: whenever your coach announces a countdown or interval transition, it automatically lowers background Spotify or Apple Music volume, then immediately restores it."
            },
            {
                "q": "What are the 7 Coach Programs and UP NEXT preview?",
                "a": "The app includes 7 curated video curriculum programs (including 10-Min Abs, Full Body Cardio, Tabata, and Boxing). During Work intervals, video movements loop smoothly; during Rest intervals, the screen previews the upcoming movement with an 'UP NEXT' badge so you can transition seamlessly."
            },
            {
                "q": "Does Workout Timer work offline without an internet connection?",
                "a": "Yes! The core interval timer, voice coach audio, presets, and downloaded video programs run 100% offline. No internet connection, cellular data, or user account is required."
            }
        ],
        "support_title": "Need Help or Have Feedback?",
        "support_sub": "We are dedicated to providing the cleanest, most athletic workout timer experience across all Apple devices. For questions or feature suggestions:",
        "support_btn": "✉️ Contact Support: help@appengine.fun",
        "footer_rights": "© 2026 Workout Timer: Voice Coach. An AE Interactive Original Production. All rights reserved."
    },

    "zh-Hant": {
        "title": "間歇計時器：真人語音教練 (Workout Timer) - Apple TV 客廳運動鐘 / Tabata / HIIT 健身倒數鐘",
        "desc": "專為 Tabata、HIIT 與循環訓練打造的次世代運動計時器！全新登陸 Apple TV 客廳 10 呎巨幕，支援 iPhone、iPad、Apple Watch 通用購買。錄音室真人教練原聲伴練、7 大精選影音課表、AirPods 即時心率與 100% 離線純淨隱私。",
        "keywords": "間歇計時器, Apple TV健身, tvOS運動計時, Tabata計時器, HIIT訓練計時, 語音教練, 健身房計時器, 動態島即時動態, Apple Watch健身計時, 核心腹肌課表, 10分鐘腹肌, 拳擊計時器, 離線運動計時, 無廣告計時器",
        "brand_name": "間歇計時器",
        "nav_tv": "Apple TV",
        "nav_programs": "精選課表",
        "nav_features": "核心特色",
        "nav_coaches": "語音教練",
        "nav_faq": "常見問題",
        "nav_support": "技術支援",
        "nav_privacy": "隱私權政策",
        "hero_badge": "✨ V1.3.1 全新發表 • 現已登陸 APPLE TV • 通用購買",
        "hero_title": "全面釋放體能極限，在 <span>每個 Apple 螢幕</span> 與真人教練同行",
        "hero_sub": "告別單調的機械提示音！錄音室真人教練多國原聲伴練、全新 Apple TV 客廳 10 呎巨幕倒數鐘、7 大精選影片課表，搭配 Apple Watch 獨立手錶與 AirPods 即時心率，100% 離線無廣告守護您的隱私。",
        "pills": [
            "📺 Apple TV 客廳 10 呎巨幕 UI",
            "📱 7 大真人教練影音課表",
            "⌚️ Apple Watch & AirPods 即時心率",
            "🏝️ 動態島 & 鎖定畫面即時動態",
            "🔒 100% 離線純淨無廣告"
        ],
        "cta_app_store": "前往 App Store 免費下載",
        "cta_watch_video": "觀看實機影片",
        "cta_note": "通用購買：iPhone、iPad、Apple Watch 與 Apple TV • 支援 iOS 17+, tvOS 17+, watchOS 10+",
        "gallery_hint": "👈 左右滑動檢視實機操作畫面 👉",

        # Apple TV Spotlight Section
        "sec_tv_badge": "全新登陸 APPLE TV",
        "sec_tv_title": "客廳化身專屬精品健身房",
        "sec_tv_sub": "為 tvOS 17+ 與 Siri Remote 專屬打造！4K 超大清晰倒數環、分割畫面教練動作示範，5 米之外一目了然，客廳運動就像上私教課。",
        "tv_tab_programs": "7 大影音課表",
        "tv_tab_ring": "10 呎超大時鐘",
        "tv_tab_cinema": "全螢幕影音播放",
        "tv_feat_1_title": "4K 巨幕高對比倒數環",
        "tv_feat_1_desc": "GPU 硬體加速渲染的超大倒數環與粗體數字，站在瑜珈墊或客廳任何角落都能一秒掌握剩餘秒數。",
        "tv_feat_2_title": "Siri Remote 遙控極簡操控",
        "tv_feat_2_desc": "針對 Apple TV 焦點引擎深度最佳化，點按即可秒開 Tabata、微調間歇秒數或切換 7 大專業課表。",
        "tv_feat_3_title": "左右分割動態示範視窗",
        "tv_feat_3_desc": "左側播放標準動作示範，右側大時鐘掌控全場，無縫循環播放，動作節奏絕不掉拍。",

        # 7 Programs Section
        "sec_programs_badge": "精選指導課表",
        "sec_programs_title": "7 大專業真人教練影音課表",
        "sec_programs_sub": "訓練期間循環播放標準動作示範，休息時自動提前播放「UP NEXT」下一動預習，喝水調整從容就位。",
        "up_next_badge": "獨家「UP NEXT」預習創新",
        "up_next_title": "休息喘息，提早做好下一動就位準備",
        "up_next_desc": "當進入休息倒數時，畫面會自動淡入下一組動作的預習影片與動作名稱。喝水調整呼吸時一眼看懂，哨音響起立刻完美銜接。",
        "programs": [
            {"title": "10 分鐘腹肌雕塑", "coach": "Hannah 教練", "rounds": "12 輪動作", "type": "核心與側腹", "desc": "高效率 10 分鐘核心轟炸，涵蓋上腹、下腹與側腹肌群，動作無縫平滑循環。"},
            {"title": "核心肌力強化", "coach": "Marcus 教練", "rounds": "10 輪動作", "type": "深層核心穩定", "desc": "針對抗旋轉與深層核心肌群設計，全面提升軀幹穩定度與運動爆發力。"},
            {"title": "全身有氧燃脂", "coach": "Chloe 教練", "rounds": "14 輪動作", "type": "高強度全身燃脂", "desc": "節奏明快的多關節動態訓練，最大化觸發運動後過量氧耗 (EPOC) 燃脂效應。"},
            {"title": "腿部臀部力量", "coach": "Ryan 教練", "rounds": "12 輪動作", "type": "下肢爆發力", "desc": "深蹲、弓步蹲與增強式跳躍訓練，鍛鍊強健下肢鏈條與蜜桃臀線條。"},
            {"title": "上半身肌力訓練", "coach": "Ryan 教練", "rounds": "10 輪動作", "type": "胸背手臂耐力", "desc": "徒手伏地挺身與核心推拉控制，雕塑精實肩背與手臂肌肉耐力。"},
            {"title": "極限 Tabata 突破", "coach": "Elena 教練", "rounds": "8 輪動作", "type": "20s 衝刺 / 10s 休息", "desc": "經典 4 分鐘高強度間歇協議，在極短時間內挑戰最大攝氧量 (VO2 Max)。"},
            {"title": "拳擊實戰體能", "coach": "Elena 教練", "rounds": "6 輪回合", "type": "3 分鐘回合 / 1 分鐘休息", "desc": "比照專業拳擊選手體能規格，3 分鐘高頻出拳步法搭配 60 秒充裕恢復。"}
        ],

        # Multi-Device Ecosystem Section
        "sec_ecosystem_badge": "APPLE 生態系完整支援",
        "sec_ecosystem_title": "一次購買，全設備通用 (Universal Purchase)",
        "sec_ecosystem_sub": "Workout Timer 原生深度適配 iPhone、Apple TV、Apple Watch 與 iPad。單次購買即可在所有 Apple 設備上終身使用。",
        "ecosystem_devices": [
            {"name": "Apple TV", "icon": "📺", "tag": "客廳 10 呎運動巨幕", "desc": "為電視大螢幕打造的沉浸式劇院介面，Siri Remote 一按即練。"},
            {"name": "iPhone", "icon": "📱", "tag": "動態島 & 50:50 巨幕模式", "desc": "鎖定畫面即時動態進度環，橫向自動切換 50:50 健身房大時鐘。"},
            {"name": "Apple Watch", "icon": "⌚️", "tag": "手腕觸覺回饋獨立手錶", "desc": "震動提醒換組，即時串流即時心率區間與動態卡路里。"},
            {"name": "iPad", "icon": "💻", "tag": "13 吋大螢幕瑜珈墊全幅", "desc": "瑜珈墊前的全幅大視野，分割畫面呈現細膩動作指導與清晰倒數。"}
        ],

        # Video Demo Section
        "sec_video_badge": "實機功能展示",
        "sec_video_title": "親身體驗 Workout Timer 的流暢實機操作",
        "sec_video_sub": "觀看 Hannah 教練 10 分鐘腹肌示範、50:50 橫向劇院巨幕模式，以及 Apple Watch 與 AirPods 即時心率串流。",

        # Features Section
        "sec_features_title": "專為極致運動表現打造",
        "sec_features_sub": "滿足 Tabata、高強度間歇 (HIIT)、拳擊回合、AMRAP 與腹肌雕塑的所有需求。",
        "features": [
            {"icon": "🎙️", "title": "錄音室真人教練原聲", "desc": "提供台灣繁中（小司）、中文（小酥）、英式英語（Oliver）、美式英語（Adam）與西語（Sofia），全程語音陪伴每個訓練與休息倒數。"},
            {"icon": "📺", "title": "Apple TV 客廳 10 呎巨幕", "desc": "專為 tvOS 17+ 設計！超大粗體數字在 5 公尺外清晰可辨，Siri 遙控器輕鬆點選開練。"},
            {"icon": "⌚️", "title": "Apple Watch & AirPods 同步", "desc": "具備專屬 watchOS 獨立手錶 App 提供手腕觸覺回饋，並可即時串流 Apple Watch 與 AirPods Pro 的即時心率與活動卡路里。"},
            {"icon": "🏝️", "title": "動態島與鎖定畫面即時動態", "desc": "無需解鎖 iPhone，鎖定畫面與動態島即能顯示高硬體加速進度環、當前階段與剩餘秒數，抬手即看超省電。"},
            {"icon": "🎬", "title": "訓練完成真人慶祝影片", "desc": "為每一次全力以赴喝采！每次完成高強度訓練後，教練將親自以高畫質影片為您擊掌祝賀，點燃下一次挑戰的動力。"},
            {"icon": "⏱️", "title": "免費自訂間歇與經典預設", "desc": "秒開 Tabata (20s/10s)、經典 HIIT (40s/20s)、拳擊 3 分鐘回合，亦可自由設定組數、大循環與休息間隔。"},
            {"icon": "🎵", "title": "智慧音樂避讓 (Audio Ducking)", "desc": "播報倒數或換組時自動降低 Spotify 或 Apple Music 背景音樂，播報完畢平滑恢復，節奏不中斷。"},
            {"icon": "🔒", "title": "100% 離線純淨與隱私守護", "desc": "無需註冊帳號、無任何第三方追蹤分析、無廣告干擾。您的個人運動數據完全只保存在您的設備本機。"}
        ],

        # Coaches Section
        "sec_coaches_title": "認識您的專屬錄音室教練團",
        "sec_coaches_sub": "5 位具備專業動力的真人錄音室教練，隨時為您帶練。",
        "coach_xiaosu": "小酥教練",
        "coach_xiaosu_sub": "中文普通話 • 陽光溫暖、鼓舞人心",
        "coach_xiaosi": "小司教練",
        "coach_xiaosi_sub": "台灣繁體中文 • 專業幹練、節奏明快",
        "coach_oliver": "Oliver 教練",
        "coach_oliver_sub": "英式英語 (British) • 英倫活力、指令明確",
        "coach_sofia": "Sofia 教練",
        "coach_sofia_sub": "西班牙語 (LatAm) • 熱情洋溢、力量充沛",
        "coach_adam": "Adam 教練",
        "coach_adam_sub": "美式英語 (US) • 堅定沉穩、專業激勵",

        # Reviews & FAQ
        "review_1": "Apple TV 版本太驚艷了！客廳大電視上的倒數圈在遠處瑜珈墊上看超級清楚，完全不用低頭盯手機！",
        "review_2": "教練語音真的差很多，比起單調的嗶嗶聲，現在終於有在健身房上課的激勵感了，而且沒有惱人的廣告。",
        "review_3": "10 分鐘腹肌課表的 UP NEXT 預習超級貼心，休息喝水時能提早知道下一個動作，轉換節奏非常順暢！",
        "sec_faq_title": "常見問題解答 (FAQ)",
        "sec_faq_sub": "關於間歇計時器的核心功能與常見疑問。",
        "faqs": [
            {
                "q": "全新的 Apple TV 版本需要另外付費購買嗎？",
                "a": "完全不需要！Workout Timer 支援 Apple「通用購買 (Universal Purchase)」。您只需購買一次，即可在 iPhone、iPad、Apple Watch 與 Apple TV 上自動獲得完整使用權限，無任何額外費用。"
            },
            {
                "q": "這款計時器需要付費訂閱嗎？",
                "a": "不需要！Workout Timer 採一次性買斷制。沒有任何月費訂閱、沒有隱藏費用，也絕對沒有廣告干擾。一次付費，終身擁有所有錄音室真人教練與功能更新。"
            },
            {
                "q": "Apple Watch 與 AirPods 心率是如何運作的？",
                "a": "本 App 包含專屬的 Apple Watch 獨立手錶 App，在訓練換組時會於手腕提供震動提醒。搭配 iPhone 使用時，可透過 Apple HealthKit 即時串流 Apple Watch 或 AirPods Pro 偵測的心率與卡路里至主畫面與動態島。"
            },
            {
                "q": "邊計時可以邊播放 Spotify 或 Apple Music 嗎？",
                "a": "完全可以！App 內建智慧音訊避讓 (Audio Ducking)：當教練開口播報倒數或換組時，會自動微調降低音樂音量，播報完畢立即平滑恢復，運動節奏不中斷。"
            },
            {
                "q": "什麼是 7 大精選影音課表與 UP NEXT 預習？",
                "a": "這是由專業教練研發的 7 大科學循環課表（包括 10 分鐘腹肌、全身燃脂、Tabata 與拳擊等）。訓練時循環播放標準動作示範，休息時會自動提前播放下一組動作並標示「UP NEXT」，讓您在喝水喘氣時做好預習。"
            },
            {
                "q": "沒有網路或在離線狀態下可以使用嗎？",
                "a": "完全可以！核心計時器、錄音室教練語音與已下載的課表均 100% 離線運行。無需網路連線、無手機訊號要求，也無需註冊任何帳號。"
            }
        ],
        "support_title": "需要協助或提供寶貴建議？",
        "support_sub": "我們致力於打造 Apple 全設備上最順手專業的運動計時器。如果您有任何使用問題或功能建議，歡迎聯絡：",
        "support_btn": "✉️ 聯繫技術支援：help@appengine.fun",
        "footer_rights": "© 2026 間歇計時器：語音教練 (Workout Timer)。保留所有權利。"
    },

    "zh-Hans": {
        "title": "间歇计时器：真人语音教练 (Workout Timer) - Apple TV 客厅运动钟 / Tabata / HIIT 健身倒数钟",
        "desc": "专为 Tabata、HIIT 与循环训练打造的次世代运动计时器！全新登陆 Apple TV 客厅 10 尺巨幕，支持 iPhone、iPad、Apple Watch 通用购买。录音室真人教练原声伴练、7 大精选视频课表、AirPods 实时心率与 100% 离线纯净隐私。",
        "keywords": "间歇计时器, Apple TV健身, tvOS运动计时, Tabata计时器, HIIT训练计时, 语音教练, 健身房计时器, 动态岛实时活动, Apple Watch健身计时, 核心腹肌课表, 10分钟腹肌, 拳击计时器, 离线运动计时, 无广告计时器",
        "brand_name": "间歇计时器",
        "nav_tv": "Apple TV",
        "nav_programs": "精选课表",
        "nav_features": "核心特色",
        "nav_coaches": "语音教练",
        "nav_faq": "常见问题",
        "nav_support": "技术支持",
        "nav_privacy": "隐私政策",
        "hero_badge": "✨ V1.3.1 全新发布 • 现已登陆 APPLE TV • 通用购买",
        "hero_title": "全面释放体能极限，在 <span>每个 Apple 屏幕</span> 与真人教练同行",
        "hero_sub": "告别单调的机械提示音！录音室真人教练多国原声伴练、全新 Apple TV 客厅 10 尺巨幕倒数钟、7 大精选视频课表，搭配 Apple Watch 独立手表与 AirPods 实时心率，100% 离线无广告守护您的隐私。",
        "pills": [
            "📺 Apple TV 客厅 10 尺巨幕 UI",
            "📱 7 大真人教练影音课表",
            "⌚️ Apple Watch & AirPods 实时心率",
            "🏝️ 动态岛 & 锁屏实时活动",
            "🔒 100% 离线纯净无广告"
        ],
        "cta_app_store": "前往 App Store 免费下载",
        "cta_watch_video": "观看实机演示",
        "cta_note": "通用购买：iPhone、iPad、Apple Watch 与 Apple TV • 支持 iOS 17+, tvOS 17+, watchOS 10+",
        "gallery_hint": "👈 左右滑动查看实机操作画面 👉",

        # Apple TV Spotlight Section
        "sec_tv_badge": "全新登陆 APPLE TV",
        "sec_tv_title": "客厅化身专属精品健身房",
        "sec_tv_sub": "为 tvOS 17+ 与 Siri Remote 专属打造！4K 超大清晰倒数环、分屏教练动作示范，5 米之外一目了然，客厅运动就像上私教课。",
        "tv_tab_programs": "7 大影音课表",
        "tv_tab_ring": "10 尺超大时钟",
        "tv_tab_cinema": "全屏影音播放",
        "tv_feat_1_title": "4K 巨幕高对比倒数环",
        "tv_feat_1_desc": "GPU 硬件加速渲染的超大倒数环与粗体数字，站在瑜伽垫或客厅任何角落都能一秒掌握剩余秒数。",
        "tv_feat_2_title": "Siri Remote 极简交互控制",
        "tv_feat_2_desc": "针对 Apple TV 焦点引擎深度优化，点击即可秒开 Tabata、微调间歇秒数或切换 7 大专业课表。",
        "tv_feat_3_title": "左右分屏动态示范视窗",
        "tv_feat_3_desc": "左侧播放标准动作示范，右侧大时钟掌控全场，无缝循环播放，动作节奏绝不掉拍。",

        # 7 Programs Section
        "sec_programs_badge": "精选指导课表",
        "sec_programs_title": "7 大专业真人教练影音课表",
        "sec_programs_sub": "训练期间循环播放标准动作示范，休息时自动提前播放「UP NEXT」下一动预习，喝水调整从容就位。",
        "up_next_badge": "独家「UP NEXT」预习创新",
        "up_next_title": "休息喘息，提早做好下一动就位准备",
        "up_next_desc": "当进入休息倒数时，画面会自动淡入下一组动作的预习视频与动作名称。喝水调整呼吸时一眼看懂，哨音响起立刻完美衔接。",
        "programs": [
            {"title": "10 分钟腹肌雕塑", "coach": "Hannah 教练", "rounds": "12 轮动作", "type": "核心与侧腹", "desc": "高效率 10 分钟核心轰炸，涵盖上腹、下腹与侧腹肌群，动作平滑循环播放。"},
            {"title": "核心肌力强化", "coach": "Marcus 教练", "rounds": "10 轮动作", "type": "深层核心稳定", "desc": "针对抗旋转与深层核心肌群设计，全面提升躯干稳定度与运动爆发力。"},
            {"title": "全身有氧燃脂", "coach": "Chloe 教练", "rounds": "14 轮动作", "type": "高强度全身燃脂", "desc": "节奏明快的多关节动态训练，最大化触发运动后过量氧耗 (EPOC) 燃脂效应。"},
            {"title": "腿部臀部力量", "coach": "Ryan 教练", "rounds": "12 轮动作", "type": "下肢爆发力", "desc": "深蹲、弓步蹲与增强式跳跃训练，锻造强健下肢链条与挺拔体态。"},
            {"title": "上半身肌力训练", "coach": "Ryan 教练", "rounds": "10 轮动作", "type": "胸背手臂耐力", "desc": "自重俯卧撑与核心推拉控制，雕塑精实肩背与手臂肌肉耐力。"},
            {"title": "极限 Tabata 突破", "coach": "Elena 教练", "rounds": "8 轮动作", "type": "20s 冲刺 / 10s 休息", "desc": "经典 4 分钟高强度间歇协议，在极短时间内挑战最大摄氧量 (VO2 Max)。"},
            {"title": "拳击实战体能", "coach": "Elena 教练", "rounds": "6 轮回合", "type": "3 分钟回合 / 1 分钟休息", "desc": "比照专业拳击选手体能规格，3 分钟高频出拳步法搭配 60 秒充裕恢复。"}
        ],

        # Multi-Device Ecosystem Section
        "sec_ecosystem_badge": "APPLE 生态系统完整支持",
        "sec_ecosystem_title": "一次购买，全设备通用 (Universal Purchase)",
        "sec_ecosystem_sub": "Workout Timer 原生深度适配 iPhone、Apple TV、Apple Watch 与 iPad。单次购买即可在所有 Apple 设备上终身使用。",
        "ecosystem_devices": [
            {"name": "Apple TV", "icon": "📺", "tag": "客厅 10 尺运动巨幕", "desc": "为电视大屏幕打造的沉浸式影院界面，Siri Remote 一按即练。"},
            {"name": "iPhone", "icon": "📱", "tag": "动态岛 & 50:50 巨幕模式", "desc": "锁屏实时活动进度环，横屏自动切换 50:50 健身房大时钟。"},
            {"name": "Apple Watch", "icon": "⌚️", "tag": "手腕触感震动独立手表", "desc": "震动提醒换组，实时串流实时心率区间与动态卡路里。"},
            {"name": "iPad", "icon": "💻", "tag": "13 寸大屏瑜伽垫全幅", "desc": "瑜伽垫前的全幅大视野，分屏呈现细腻动作指导与清晰倒计时。"}
        ],

        # Video Demo Section
        "sec_video_badge": "实机功能展示",
        "sec_video_title": "亲身体验 Workout Timer 的流畅实机操作",
        "sec_video_sub": "观看 Hannah 教练 10 分钟腹肌示范、50:50 横向影院巨幕模式，以及 Apple Watch 与 AirPods 实时心率同步。",

        # Features Section
        "sec_features_title": "专为巅峰运动表现而生",
        "sec_features_sub": "全面满足 Tabata、高强度间歇 (HIIT)、拳击实战与腹肌雕塑的所有需求。",
        "features": [
            {"icon": "🎙️", "title": "录音室真人教练原声", "desc": "提供小酥（普通话）、小司（台湾繁体）、Oliver（英式英语）、Adam（美式英语）与 Sofia（西班牙语），全流程语音伴随每个阶段。"},
            {"icon": "📺", "title": "Apple TV 客厅 10 尺巨幕", "desc": "专为 tvOS 17+ 设计！超大数字在 5 米外清晰可见，Siri 遥控器轻松点选开练。"},
            {"icon": "⌚️", "title": "Apple Watch & AirPods 同步", "desc": "配备专属 watchOS 独立手表应用提供震动提醒，并可实时串流 Apple Watch 与 AirPods Pro 监测的心率与动态卡路里。"},
            {"icon": "🏝️", "title": "动态岛与锁屏实时活动", "desc": "无需点亮解锁手机，锁屏与动态岛即可呈现硬件加速进度环与倒数秒数，一瞥即知当前状态。"},
            {"icon": "🎬", "title": "训练完成真人庆祝视频", "desc": "为每一次拼搏喝彩！每次完成高强度训练，教练亲自以高清视频向您击掌祝贺，点燃下一次挑战动力。"},
            {"icon": "⏱️", "title": "免费自定义间歇与经典预设", "desc": "即刻开启 Tabata (20s/10s)、经典 HIIT (40s/20s)、拳击 3 分钟实战，自由设置工作时长与循环间歇。"},
            {"icon": "🎵", "title": "智能音乐避让 (Audio Ducking)", "desc": "播报倒数或换组时自动降低 Spotify 或 Apple Music 背景音乐，播报完毕平滑恢复，节奏不中断。"},
            {"icon": "🔒", "title": "100% 离线纯净与隐私保护", "desc": "无需注册账号、无第三方跟踪代码、无广告干扰。您的运动数据完全保留在设备本地。"}
        ],

        # Coaches Section
        "sec_coaches_title": "认识您的专属录音室教练团队",
        "sec_coaches_sub": "5 位高水准录音室教练随时准备为您开练。",
        "coach_xiaosu": "小酥教练",
        "coach_xiaosu_sub": "中文普通话 • 阳光温暖、鼓舞人心",
        "coach_xiaosi": "小司教练",
        "coach_xiaosi_sub": "台湾繁体 • 热情干练、节奏利落",
        "coach_oliver": "Oliver 教练",
        "coach_oliver_sub": "英式英语 • 活力充沛、指令清晰",
        "coach_sofia": "Sofia 教练",
        "coach_sofia_sub": "西班牙语 • 热情奔放、极具感染力",
        "coach_adam": "Adam 教练",
        "coach_adam_sub": "美式英语 • 沉稳有力、专业激励",

        # Reviews & FAQ
        "review_1": "Apple TV 版本太惊艳了！客厅大电视上的倒数圈在远处瑜伽垫上看超级清楚，完全不用低头盯手机！",
        "review_2": "语音教练真的非常赞，比以前听无聊的嘟嘟声有动力多了，感觉就像在上私教课，而且完全没有广告干扰。",
        "review_3": "10分钟腹肌课表在休息时会提前预览下一个动作，这个细节做得太好了，动作转换非常从容！",
        "sec_faq_title": "常见问题解答 (FAQ)",
        "sec_faq_sub": "关于间歇计时器的核心功能与常见疑问。",
        "faqs": [
            {
                "q": "全新的 Apple TV 版本需要另外付费购买吗？",
                "a": "完全不需要！Workout Timer 支持 Apple「通用购买 (Universal Purchase)」。您只需购买一次，即可在 iPhone、iPad、Apple Watch 与 Apple TV 上自动获得完整使用权限，无任何额外费用。"
            },
            {
                "q": "这款计时器需要付费订阅吗？",
                "a": "不需要！Workout Timer 采用一次性买断制。没有任何月费订阅、没有隐藏费用，也绝对没有广告干扰。一次付费，终身拥有所有录音室真人教练与功能更新。"
            },
            {
                "q": "Apple Watch 与 AirPods 心率是如何工作的？",
                "a": "本应用包含专用的 Apple Watch 独立手表应用，在换组时会在手腕提供触感震动。配合 iPhone 使用时，可通过 HealthKit 将 Apple Watch 或 AirPods Pro 测得的心率与卡路里传输至主屏与动态岛。"
            },
            {
                "q": "边计时可以边听音乐吗？",
                "a": "完全可以！应用内置智能音频避让 (Audio Ducking)：当教练播报倒计时或换组提示时，会自动微调降低音乐音量，播报完毕平滑恢复。"
            },
            {
                "q": "什么是 7 大精选视频课表与 UP NEXT 预习？",
                "a": "这是由专业教练设计的 7 大科学循环课表（包括 10 分钟腹肌、全身燃脂、Tabata 与拳击等）。训练时循环播放动作示范，休息时自动提前播放下一动并标注「UP NEXT」，助您从容做好就位准备。"
            },
            {
                "q": "没有网络或在离线状态下可以使用吗？",
                "a": "完全可以！核心计时器、录音室教练语音与已下载的课表均 100% 离线运行。无需网络连接、无蜂窝数据要求，也无需注册任何账号。"
            }
        ],
        "support_title": "需要帮助或反馈建议？",
        "support_sub": "我们致力于在所有 Apple 设备上提供极致畅快专业的运动计时体验。如有任何问题或需求建议，请随时联系：",
        "support_btn": "✉️ 联系支持团队：help@appengine.fun",
        "footer_rights": "© 2026 间歇计时器：语音教练 (Workout Timer)。保留所有权利。"
    },

    "es": {
        "title": "Workout Timer: Entrenador de Voz - Temporizador HIIT, Apple TV, Tabata y Reloj de Gimnasio",
        "desc": "Temporizador de intervalos de última generación con entrenadores de voz reales, 7 programas guiados en video, reloj de cine para Apple TV en tu sala, pulso en vivo con Apple Watch y AirPods, y privacidad 100% offline.",
        "keywords": "temporizador de intervalos, apple tv ejercicio, tvos reloj gimnasio, temporizador tabata, cronometro hiit, entrenador de voz, reloj gimnasio, pantalla gigante gym, apple watch temporizador, entrenamiento abdomen 10 min, dynamic island timer, cronometro boxeo",
        "brand_name": "Workout Timer",
        "nav_tv": "Apple TV",
        "nav_programs": "Programas",
        "nav_features": "Funciones",
        "nav_coaches": "Entrenadores",
        "nav_faq": "Preguntas",
        "nav_support": "Soporte",
        "nav_privacy": "Privacidad",
        "hero_badge": "✨ NOVEDAD V1.3.1 • YA DISPONIBLE EN APPLE TV • COMPRA UNIVERSAL",
        "hero_title": "Entrena al Máximo en <span>Cada Pantalla Apple</span>",
        "hero_sub": "El temporizador de intervalos definitivo con entrenadores de voz grabados en estudio, 7 programas guiados en video, reloj de 10 pies para Apple TV, sincronización de pulso con Apple Watch y AirPods, y máxima privacidad offline.",
        "pills": [
            "📺 Apple TV 4K para Sala y Gym",
            "📱 7 Programas Guiados en Video",
            "⌚️ Pulso en Vivo con Apple Watch y AirPods",
            "🏝️ Dynamic Island y Live Activities",
            "🔒 100% Offline y Sin Anuncios"
        ],
        "cta_app_store": "Descargar Gratis en el App Store",
        "cta_watch_video": "Ver Video Demo",
        "cta_note": "Compra Universal: iPhone, iPad, Apple Watch y Apple TV • Compatible con iOS 17+, tvOS 17+, watchOS 10+",
        "gallery_hint": "👈 Desliza horizontalmente para explorar las pantallas 👉",

        # Apple TV Spotlight Section
        "sec_tv_badge": "YA EN APPLE TV",
        "sec_tv_title": "Convierte tu Sala en un Gimnasio de Élite",
        "sec_tv_sub": "Diseñado exclusivamente para tvOS 17+ con navegación Siri Remote. Anillo gigante en 4K visible a 3 metros de distancia, pantalla dividida con video y cero distracciones.",
        "tv_tab_programs": "7 Programas en Video",
        "tv_tab_ring": "Reloj Gigante de 10 Pies",
        "tv_tab_cinema": "Reproductor Cine",
        "tv_feat_1_title": "Anillo 4K de Alto Contraste",
        "tv_feat_1_desc": "Dígitos y anillo de progreso nítidos renderizados por GPU, legibles desde cualquier ángulo de tu sala o colchoneta.",
        "tv_feat_2_title": "Control con Siri Remote",
        "tv_feat_2_desc": "Control táctil instantáneo: inicia un Tabata en un clic, ajusta intervalos sobre la marcha o explora los 7 programas.",
        "tv_feat_3_title": "Guía en Video Dividida",
        "tv_feat_3_desc": "Demostración continua de técnica con bucles de video en alta definición para no perder el ritmo en ninguna serie.",

        # 7 Programs Section
        "sec_programs_badge": "PLANES GUIADOS",
        "sec_programs_title": "7 Programas Profesionales en Video",
        "sec_programs_sub": "Bucles de video continuos durante la serie y vista previa inteligente 'UP NEXT' en el descanso para prepararte sin prisas.",
        "up_next_badge": "INNOVACIÓN DE DESCANSO 'UP NEXT'",
        "up_next_title": "Anticipa el Siguiente Ejercicio sin Pausas",
        "up_next_desc": "Al entrar en el descanso, la pantalla te muestra un adelanto en video del próximo movimiento. Respira, bebe agua y colócate antes de que suene la campana.",
        "programs": [
            {"title": "Abdomen en 10 Minutos", "coach": "Coach Hannah", "rounds": "12 Rondas", "type": "Core y Oblicuos", "desc": "Rutina intensa de 10 minutos para abdomen superior, inferior y oblicuos con bucles de video continuos."},
            {"title": "Fuerza y Core", "coach": "Coach Marcus", "rounds": "10 Rondas", "type": "Estabilidad y Fuerza", "desc": "Activación profunda de la pared abdominal y control antirrotación para máxima potencia funcional."},
            {"title": "Cardio Quema-Grasa Total", "coach": "Coach Chloe", "rounds": "14 Rondas", "type": "HIIT Intenso", "desc": "Movimientos dinámicos explosivos diseñados para elevar el consumo calórico y el acondicionamiento metabólico."},
            {"title": "Potencia de Piernas y Glúteos", "coach": "Coach Ryan", "rounds": "12 Rondas", "type": "Tren Inferior", "desc": "Sentadillas, zancadas y saltos pliométricos para desarrollar fuerza y explosividad en piernas y glúteos."},
            {"title": "Pump de Tren Superior", "coach": "Coach Ryan", "rounds": "10 Rondas", "type": "Pecho, Espalda y Brazos", "desc": "Flexiones con peso corporal y control de empuje-tracción para esculpir hombros, pecho y brazos."},
            {"title": "Tabata Supercargado", "coach": "Coach Elena", "rounds": "8 Rondas", "type": "20s Serie / 10s Descanso", "desc": "El protocolo científico de 4 minutos de máxima intensidad para expandir tu capacidad cardiovascular (VO2 Max)."},
            {"title": "Acondicionamiento de Boxeo", "coach": "Coach Elena", "rounds": "6 Rondas", "type": "Rondas 3 Min / Descanso 1 Min", "desc": "El ritmo auténtico del ring: tres minutos continuos de alta intensidad con un minuto de recuperación activa."}
        ],

        # Multi-Device Ecosystem Section
        "sec_ecosystem_badge": "ECOSISTEMA APPLE",
        "sec_ecosystem_title": "Una Sola App. Una Sola Compra. Todos tus Dispositivos.",
        "sec_ecosystem_sub": "Workout Timer funciona de forma nativa en iPhone, Apple TV, Apple Watch y iPad. Cómpralo una vez y disfrútalo en todas tus pantallas.",
        "ecosystem_devices": [
            {"name": "Apple TV", "icon": "📺", "tag": "Reloj de Sala de 10 Pies", "desc": "Experiencia inmersiva en la pantalla de tu televisor con navegación fluida vía Siri Remote."},
            {"name": "iPhone", "icon": "📱", "tag": "Dynamic Island y Modo 50:50", "desc": "Live Activity en pantalla de bloqueo y reloj gigante horizontal para el gimnasio."},
            {"name": "Apple Watch", "icon": "⌚️", "tag": "Reloj Autónomo Háptico", "desc": "Vibraciones en la muñeca, cronómetro offline y pulso cardíaco en tiempo real."},
            {"name": "iPad", "icon": "💻", "tag": "Pantalla de 13 Pulgadas", "desc": "Visión amplia frente a tu colchoneta con video dividido y números gigantes de alta visibilidad."}
        ],

        # Video Demo Section
        "sec_video_badge": "DEMO EN ACCIÓN",
        "sec_video_title": "Descubre Workout Timer en Acción",
        "sec_video_sub": "Mira la rutina de abdomen con la entrenadora Hannah, el Modo Cine 50:50 y la sincronización con Apple Watch y AirPods.",

        # Features Section
        "sec_features_title": "Diseñado para el Máximo Rendimiento",
        "sec_features_sub": "Todo lo que necesitas para entrenamientos Tabata, HIIT, Boxeo, AMRAP y Core.",
        "features": [
            {"icon": "🎙️", "title": "5 Entrenadores de Voz Reales", "desc": "Voces profesionales de estudio en Español latinoamericano, Inglés (EE.UU. y Reino Unido) y Chino que te guían en cada serie y descanso."},
            {"icon": "📺", "title": "Apple TV 4K para Sala y Gym", "desc": "Experiencia nativa en tvOS con reloj de 10 pies, control Siri Remote y demostraciones divididas."},
            {"icon": "⌚️", "title": "Apple Watch & AirPods Sync", "desc": "App independiente para watchOS con alertas hápticas en la muñeca y transmisión de pulso y calorías en tiempo real."},
            {"icon": "🏝️", "title": "Dynamic Island & Live Activity", "desc": "Sigue la cuenta atrás directamente desde tu pantalla de bloqueo y Dynamic Island con barras aceleradas por GPU sin gastar batería."},
            {"icon": "🎬", "title": "Video de Celebración al Terminar", "desc": "¡Celebra tu esfuerzo! Tu entrenador personal te felicita con un video motivacional real a pantalla completa tras cada sesión."},
            {"icon": "⏱️", "title": "Cronómetro Gratis y Personalizable", "desc": "Inicia al instante Tabata (20s/10s), HIIT (40s/20s) o rounds de Boxeo de 3 minutos, o personaliza tus propias series."},
            {"icon": "🎵", "title": "Atenuación Inteligente (Audio Ducking)", "desc": "Reduce automáticamente el volumen de Spotify o Apple Music durante los avisos de voz del entrenador y lo restaura suavemente."},
            {"icon": "🔒", "title": "100% Offline y Máxima Privacidad", "desc": "Sin cuentas, sin rastreadores de terceros y sin anuncios. Tus datos de entrenamiento permanecen estrictamente en tu dispositivo."}
        ],

        # Coaches Section
        "sec_coaches_title": "Conoce a tus Entrenadores de Estudio",
        "sec_coaches_sub": "Cinco entrenadores dedicados con audio grabado en estudio.",
        "coach_xiaosu": "Coach XiaoSu",
        "coach_xiaosu_sub": "Chino Mandarín • Energética y Cálida",
        "coach_xiaosi": "Coach XiaoSi",
        "coach_xiaosi_sub": "Mandarín de Taiwán • Profesional y Ágil",
        "coach_oliver": "Coach Oliver",
        "coach_oliver_sub": "Inglés Británico • Vigoroso y Preciso",
        "coach_sofia": "Coach Sofia",
        "coach_sofia_sub": "Español (Latinoamérica) • Enérgica e Inspiradora",
        "coach_adam": "Coach Adam",
        "coach_adam_sub": "Inglés Americano • Firme y Motivador",

        # Reviews & FAQ
        "review_1": "¡La versión para Apple TV es increíble! El anillo de tiempo se ve gigante desde mi colchoneta sin tener que mirar el móvil.",
        "review_2": "Los entrenadores de voz motivan muchísimo. Sientes que estás en una clase real sin los molestos anuncios de otras apps.",
        "review_3": "La vista previa UP NEXT durante los descansos es una maravilla. Sé exactamente qué ejercicio sigue antes de que suene la campana.",
        "sec_faq_title": "Preguntas Frecuentes (FAQ)",
        "sec_faq_sub": "Todo lo que necesitas saber sobre Workout Timer.",
        "faqs": [
            {
                "q": "¿La nueva app para Apple TV está incluida en la misma compra?",
                "a": "¡Sí! Workout Timer cuenta con Compra Universal de Apple. Con una única descarga tienes acceso completo en iPhone, iPad, Apple Watch y Apple TV sin costo adicional."
            },
            {
                "q": "¿Workout Timer requiere suscripción mensual?",
                "a": "No. Workout Timer es de pago único. No hay suscripciones recurrentes, no hay costos ocultos y no hay anuncios. Compra una vez y tendrás acceso de por vida a todos los entrenadores y funciones."
            },
            {
                "q": "¿Cómo funciona el pulso cardíaco con Apple Watch y AirPods?",
                "a": "La app incluye una app independiente para Apple Watch con toques hápticos. Al vincularse con iPhone, transmite el pulso en vivo y calorías quemadas al anillo de tiempo y a la Dynamic Island. También admite medición con AirPods Pro vía Apple HealthKit."
            },
            {
                "q": "¿Puedo escuchar mi propia música mientras uso el temporizador?",
                "a": "¡Totalmente! La app cuenta con Audio Ducking inteligente: cuando tu entrenador anuncia la cuenta atrás o el cambio de serie, baja automáticamente el volumen de Spotify o Apple Music y lo restaura de inmediato."
            },
            {
                "q": "¿Qué son los 7 Programas y la vista previa UP NEXT?",
                "a": "Son 7 planes estructurados en video (Abdomen 10 Min, Cardio Total, Tabata, Boxeo, etc.). Durante el ejercicio se muestra la técnica en bucle, y en el descanso aparece la vista previa 'UP NEXT' del siguiente ejercicio para que estés listo sin perder tiempo."
            },
            {
                "q": "¿Funciona sin conexión a internet?",
                "a": "¡Sí! El temporizador principal, las voces de estudio y los programas en video funcionan 100% offline. No se necesita conexión a internet, datos móviles ni registro de cuentas."
            }
        ],
        "support_title": "¿Necesitas Ayuda o Tienes Sugerencias?",
        "support_sub": "Estamos comprometidos con ofrecer la experiencia de cronómetro más limpia y profesional en el ecosistema Apple. Escríbenos a:",
        "support_btn": "✉️ Contactar Soporte: help@appengine.fun",
        "footer_rights": "© 2026 Workout Timer: Voice Coach. Una producción original de AE Interactive. Todos los derechos reservados."
    }
}

def generate_schema_json(lang_code):
    t = translations[lang_code]
    faq_elements = []
    for f in t["faqs"]:
        faq_elements.append({
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        })

    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "@id": "https://workout.appengine.fun/#app",
                "name": "Workout Timer: Voice Coach",
                "alternateName": ["間歇計時器", "Gym Clock", "Tabata Timer", "Apple TV Workout Clock"],
                "url": "https://workout.appengine.fun/",
                "image": "https://workout.appengine.fun/images/app_icon.png",
                "screenshot": [
                    "https://workout.appengine.fun/images/shot_tv_en.webp",
                    "https://workout.appengine.fun/images/shot_iphone_en.webp",
                    "https://workout.appengine.fun/images/shot_timer.png",
                    "https://workout.appengine.fun/images/shot_complete.png"
                ],
                "description": t["desc"],
                "applicationCategory": "HealthApplication, SportsApplication",
                "operatingSystem": "iOS 17.0+, iPadOS 17.0+, watchOS 10.0+, tvOS 17.0+",
                "downloadUrl": "https://apps.apple.com/app/id6811742209",
                "installUrl": "https://apps.apple.com/app/id6811742209",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock"
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "ratingCount": "168",
                    "bestRating": "5",
                    "worstRating": "1"
                },
                "author": {
                    "@type": "Organization",
                    "name": "App Engine",
                    "url": "https://workout.appengine.fun"
                }
            },
            {
                "@type": "FAQPage",
                "@id": f"https://workout.appengine.fun/?lang={lang_code}#faq",
                "mainEntity": faq_elements
            }
        ]
    }
    return json.dumps(schema_graph, ensure_ascii=False)

def generate_page(lang_code):
    t = translations[lang_code]
    schema_json = generate_schema_json(lang_code)

    # 1. Feature cards HTML
    features_html = ""
    for f in t["features"]:
        features_html += f"""
        <div class="feature-card">
          <div class="feature-icon">{f['icon']}</div>
          <h3>{f['title']}</h3>
          <p>{f['desc']}</p>
        </div>"""

    # 2. 7 Programs cards HTML
    programs_html = ""
    for idx, p in enumerate(t["programs"]):
        badge_num = f"#{idx+1:02d}"
        programs_html += f"""
        <div class="program-card">
          <div class="program-header">
            <span class="program-number">{badge_num}</span>
            <span class="program-rounds">{p['rounds']}</span>
          </div>
          <h3 class="program-title">{p['title']}</h3>
          <div class="program-meta">
            <span class="program-coach">👤 {p['coach']}</span>
            <span class="program-type">⚡️ {p['type']}</span>
          </div>
          <p class="program-desc">{p['desc']}</p>
        </div>"""

    # 3. Multi-Device Ecosystem HTML
    ecosystem_html = ""
    for dev in t["ecosystem_devices"]:
        ecosystem_html += f"""
        <div class="eco-card">
          <div class="eco-icon">{dev['icon']}</div>
          <div class="eco-title">{dev['name']}</div>
          <div class="eco-tag">{dev['tag']}</div>
          <div class="eco-desc">{dev['desc']}</div>
        </div>"""

    # 4. FAQ accordion HTML
    faqs_html = ""
    for idx, f in enumerate(t["faqs"]):
        open_attr = " open" if idx == 0 else ""
        faqs_html += f"""
        <details class="faq-item"{open_attr}>
          <summary class="faq-question">
            <span>{f['q']}</span>
            <span class="faq-arrow">▼</span>
          </summary>
          <div class="faq-answer">
            <p>{f['a']}</p>
          </div>
        </details>"""

    # 5. Hero pills HTML
    pills_html = "".join([f'<div class="pill">{p}</div>' for p in t["pills"]])

    # 6. Localized image mappings
    tv_img_default = f"/images/shot_tv_{lang_code}.webp"
    tv_img_ring = f"/images/shot_tv_ring_{lang_code}.webp"
    tv_img_coach = f"/images/shot_tv_coach_{lang_code}.webp"
    
    iphone_shot = f"/images/shot_iphone_{lang_code}.webp"
    iphone_programs_shot = f"/images/shot_iphone_programs_{lang_code}.webp"

    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>{t['title']}</title>
  <meta name="description" content="{t['desc']}">
  <meta name="keywords" content="{t['keywords']}">
  <meta name="author" content="App Engine">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="theme-color" content="#000000">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="{t['brand_name']}">
  <meta name="google-site-verification" content="HRRvFeLIuKlFbLFwaCkapTJm0bSMbifBHaQNFwfNL60">
  <meta name="apple-itunes-app" content="app-id=6811742209">
  
  <!-- Canonical & Multilingual SEO -->
  <link rel="canonical" href="https://workout.appengine.fun/?lang={lang_code}">
  <link rel="alternate" hreflang="en" href="https://workout.appengine.fun/?lang=en">
  <link rel="alternate" hreflang="zh-Hant" href="https://workout.appengine.fun/?lang=zh-Hant">
  <link rel="alternate" hreflang="zh-Hans" href="https://workout.appengine.fun/?lang=zh-Hans">
  <link rel="alternate" hreflang="es" href="https://workout.appengine.fun/?lang=es">
  <link rel="alternate" hreflang="x-default" href="https://workout.appengine.fun/">

  <!-- Open Graph / Social Media Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{t['brand_name']}">
  <meta property="og:url" content="https://workout.appengine.fun/?lang={lang_code}">
  <meta property="og:title" content="{t['title']}">
  <meta property="og:description" content="{t['desc']}">
  <meta property="og:image" content="https://workout.appengine.fun/images/og_preview.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Workout Timer: Voice Coach on Apple TV, iPhone, iPad, Apple Watch">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t['title']}">
  <meta name="twitter:description" content="{t['desc']}">
  <meta name="twitter:image" content="https://workout.appengine.fun/images/og_preview.png">

  <!-- Icons -->
  <link rel="icon" type="image/png" href="/images/app_icon.png">
  <link rel="apple-touch-icon" href="/images/app_icon.png">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {schema_json}
  </script>

  <style>
    :root {{
      --primary-green: #30D158;
      --primary-orange: #FF9F0A;
      --primary-blue: #0A84FF;
      --primary-red: #FF453A;
      --primary-cyan: #64D2FF;
      --bg-dark: #000000;
      --card-bg: rgba(22, 22, 28, 0.75);
      --card-border: rgba(255, 255, 255, 0.1);
      --text-main: #FFFFFF;
      --text-muted: #98989D;
    }}
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    }}
    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      line-height: 1.6;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(48, 209, 88, 0.12) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(10, 132, 255, 0.08) 0%, transparent 40%);
      background-repeat: no-repeat;
    }}

    /* Header / Nav */
    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 20px;
      max-width: 1200px;
      margin: 0 auto;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #fff;
    }}
    .brand img {{
      width: 40px;
      height: 40px;
      border-radius: 10px;
      box-shadow: 0 4px 14px rgba(48, 209, 88, 0.35);
    }}
    .brand-title {{
      font-size: 19px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }}
    .nav-right {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}
    .nav-links {{
      display: flex;
      gap: 20px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: #fff;
    }}
    .lang-picker {{
      display: flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 99px;
      padding: 4px 12px;
      font-size: 13px;
      font-weight: 700;
      gap: 8px;
    }}
    .lang-picker a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .lang-picker a.active {{
      color: var(--primary-green);
    }}
    @media (max-width: 860px) {{
      .nav-links {{
        display: none;
      }}
    }}

    /* Hero Section */
    .hero {{
      text-align: center;
      padding: 60px 20px 40px;
      max-width: 960px;
      margin: 0 auto;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(48, 209, 88, 0.12);
      color: var(--primary-green);
      padding: 7px 18px;
      border-radius: 99px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      margin-bottom: 24px;
      border: 1px solid rgba(48, 209, 88, 0.35);
      box-shadow: 0 0 20px rgba(48, 209, 88, 0.15);
    }}
    h1 {{
      font-size: clamp(34px, 5.8vw, 64px);
      font-weight: 900;
      letter-spacing: -1.8px;
      line-height: 1.1;
      margin-bottom: 22px;
    }}
    h1 span {{
      background: linear-gradient(135deg, #30D158 0%, #64D2FF 50%, #FF9F0A 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      font-size: clamp(16px, 2.2vw, 20px);
      color: var(--text-muted);
      max-width: 720px;
      margin: 0 auto 30px;
    }}
    .pills-container {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 36px;
    }}
    .pill {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 99px;
      padding: 8px 18px;
      font-size: 13px;
      font-weight: 700;
      color: #fff;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: transform 0.2s, border-color 0.2s;
    }}
    .pill:hover {{
      transform: translateY(-2px);
      border-color: rgba(48, 209, 88, 0.5);
    }}
    .cta-group {{
      display: inline-flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin-bottom: 6px;
    }}
    .cta-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      background: var(--primary-green);
      color: #000;
      padding: 16px 36px;
      border-radius: 99px;
      font-size: 17px;
      font-weight: 900;
      text-decoration: none;
      box-shadow: 0 10px 32px rgba(48, 209, 88, 0.45);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .cta-btn:hover, .cta-btn:active {{
      transform: scale(0.98);
      box-shadow: 0 14px 44px rgba(48, 209, 88, 0.65);
    }}
    .cta-apple-icon {{
      font-size: 22px;
    }}
    .cta-video-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
      padding: 16px 28px;
      border-radius: 99px;
      font-size: 16px;
      font-weight: 700;
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: background 0.2s, transform 0.2s, border-color 0.2s;
    }}
    .cta-video-btn:hover, .cta-video-btn:active {{
      background: rgba(255, 255, 255, 0.16);
      border-color: rgba(255, 255, 255, 0.4);
      transform: scale(0.98);
      color: #fff;
    }}
    .cta-video-icon {{
      color: #ff3b30;
      font-size: 18px;
    }}
    .cta-note {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 14px;
    }}

    /* Section Headers */
    .section-title {{
      text-align: center;
      max-width: 820px;
      margin: 0 auto 40px;
      padding: 0 20px;
    }}
    .section-title h2 {{
      font-size: clamp(28px, 4vw, 44px);
      font-weight: 900;
      letter-spacing: -1px;
      margin-bottom: 14px;
    }}
    .section-title p {{
      font-size: clamp(15px, 1.8vw, 18px);
      color: var(--text-muted);
    }}

    /* Apple TV Spotlight Section */
    .tv-spotlight-section {{
      max-width: 1100px;
      margin: 40px auto 80px;
      padding: 0 20px;
    }}
    .tv-bezel-container {{
      background: linear-gradient(180deg, #18181f 0%, #0d0d12 100%);
      border: 2px solid rgba(255, 255, 255, 0.15);
      border-radius: 28px;
      padding: 24px;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.9), 0 0 50px rgba(48, 209, 88, 0.1);
      position: relative;
    }}
    .tv-tabs {{
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}
    .tv-tab-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 10px 20px;
      border-radius: 99px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .tv-tab-btn.active {{
      background: var(--primary-green);
      color: #000;
      border-color: var(--primary-green);
      box-shadow: 0 4px 16px rgba(48, 209, 88, 0.4);
    }}
    .tv-screen-frame {{
      position: relative;
      width: 100%;
      padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
      border-radius: 16px;
      overflow: hidden;
      background: #000;
      box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1);
    }}
    .tv-screen-frame img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: opacity 0.3s ease;
    }}
    .tv-features-row {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 28px;
    }}
    .tv-feat-card {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 20px;
    }}
    .tv-feat-card h4 {{
      font-size: 16px;
      font-weight: 800;
      margin-bottom: 8px;
      color: var(--primary-cyan);
    }}
    .tv-feat-card p {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* 7 Curated Programs Section */
    .programs-section {{
      max-width: 1140px;
      margin: 40px auto 80px;
      padding: 0 20px;
    }}
    .up-next-banner {{
      background: linear-gradient(135deg, rgba(255, 159, 10, 0.15) 0%, rgba(48, 209, 88, 0.1) 100%);
      border: 1px solid rgba(255, 159, 10, 0.35);
      border-radius: 20px;
      padding: 24px 28px;
      margin-bottom: 36px;
      display: flex;
      align-items: center;
      gap: 24px;
    }}
    .up-next-icon {{
      font-size: 42px;
      flex-shrink: 0;
    }}
    .up-next-banner-content h4 {{
      font-size: 18px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 6px;
    }}
    .up-next-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 800;
      color: var(--primary-orange);
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}
    .up-next-banner-content p {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .programs-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
    }}
    .program-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 24px;
      transition: transform 0.25s, border-color 0.25s;
    }}
    .program-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(48, 209, 88, 0.4);
    }}
    .program-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .program-number {{
      font-size: 12px;
      font-weight: 800;
      color: var(--primary-green);
      background: rgba(48, 209, 88, 0.12);
      padding: 3px 10px;
      border-radius: 99px;
    }}
    .program-rounds {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.08);
      padding: 3px 10px;
      border-radius: 99px;
    }}
    .program-title {{
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 8px;
    }}
    .program-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .program-desc {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Ecosystem Multi-Device Section */
    .ecosystem-section {{
      max-width: 1140px;
      margin: 40px auto 80px;
      padding: 0 20px;
    }}
    .eco-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
    }}
    .eco-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 26px 20px;
      text-align: center;
      transition: transform 0.25s, border-color 0.25s;
    }}
    .eco-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(100, 210, 255, 0.4);
    }}
    .eco-icon {{
      font-size: 38px;
      margin-bottom: 14px;
    }}
    .eco-title {{
      font-size: 18px;
      font-weight: 800;
      margin-bottom: 6px;
    }}
    .eco-tag {{
      font-size: 12px;
      font-weight: 700;
      color: var(--primary-cyan);
      margin-bottom: 10px;
    }}
    .eco-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Gallery Showcase */
    .gallery-container {{
      position: relative;
      width: 100%;
      margin: 30px auto 70px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .gallery {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 24px;
      padding: 20px 24px 30px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      width: 100%;
      box-sizing: border-box;
    }}
    .gallery::-webkit-scrollbar {{
      display: none;
    }}
    .device-frame {{
      flex: 0 0 230px;
      width: 230px;
      max-width: 230px;
      scroll-snap-align: center;
      background: #111;
      border-radius: 34px;
      padding: 8px;
      border: 3px solid rgba(255, 255, 255, 0.16);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85);
      transition: transform 0.3s;
    }}
    .device-frame:hover {{
      transform: translateY(-6px);
    }}
    .device-frame img {{
      width: 100%;
      height: auto;
      border-radius: 28px;
      display: block;
    }}
    .gallery-hint {{
      text-align: center;
      color: var(--text-muted);
      font-size: 13px;
      margin-top: -10px;
    }}
    @media (min-width: 1280px) {{
      .gallery-hint {{
        display: none;
      }}
    }}

    /* Video Showcase Section & Cinema Modal */
    .video-showcase-section {{
      max-width: 960px;
      margin: 30px auto 70px;
      padding: 0 20px;
      box-sizing: border-box;
      text-align: center;
    }}
    .video-wrapper {{
      margin-top: 28px;
      width: 100%;
      display: flex;
      justify-content: center;
    }}
    .video-card {{
      position: relative;
      width: 100%;
      padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
      height: 0;
      border-radius: 22px;
      overflow: hidden;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.14);
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8);
    }}
    .video-card iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }}

    /* Cinema Video Lightbox Modal */
    .video-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease;
      padding: 24px;
      box-sizing: border-box;
    }}
    .video-modal.active {{
      opacity: 1;
      visibility: visible;
    }}
    .video-modal-backdrop {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }}
    .video-modal-dialog {{
      position: relative;
      width: 100%;
      max-width: 940px;
      z-index: 2;
      transform: scale(0.95);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .video-modal.active .video-modal-dialog {{
      transform: scale(1);
    }}
    .video-modal-close {{
      position: absolute;
      top: -48px;
      right: 0;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background 0.2s, transform 0.2s;
    }}
    .video-modal-close:hover {{
      background: rgba(255, 255, 255, 0.3);
      transform: scale(1.08);
    }}
    .video-modal-player-wrap {{
      position: relative;
      width: 100%;
      padding-bottom: 56.25%;
      height: 0;
      border-radius: 20px;
      overflow: hidden;
      background: #000;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.15);
    }}
    .video-modal-player-wrap iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }}

    /* Features Bento Grid */
    .features {{
      max-width: 1140px;
      margin: 40px auto 80px;
      padding: 0 20px;
    }}
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
    }}
    .feature-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 28px 24px;
      transition: transform 0.25s, border-color 0.25s;
    }}
    .feature-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(48, 209, 88, 0.45);
    }}
    .feature-icon {{
      font-size: 36px;
      margin-bottom: 16px;
    }}
    .feature-card h3 {{
      font-size: 19px;
      font-weight: 800;
      margin-bottom: 10px;
    }}
    .feature-card p {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Voice Coaches Section */
    .coaches-section {{
      max-width: 1140px;
      margin: 40px auto 80px;
      padding: 0 20px;
    }}
    .coaches-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
    }}
    .coach-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 22px 18px;
      text-align: center;
      transition: transform 0.25s, border-color 0.25s;
    }}
    .coach-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(255, 159, 10, 0.45);
    }}
    .coach-avatar-wrapper {{
      position: relative;
      width: 100px;
      height: 100px;
      margin: 0 auto 16px;
    }}
    .coach-avatar {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid rgba(255, 255, 255, 0.15);
    }}
    .play-audio-btn {{
      position: absolute;
      bottom: -4px;
      right: -4px;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--primary-green);
      border: 2px solid #000;
      color: #000;
      font-size: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(48, 209, 88, 0.4);
      transition: transform 0.2s, background 0.2s;
    }}
    .play-audio-btn:hover {{
      transform: scale(1.1);
    }}
    .play-audio-btn.playing {{
      background: var(--primary-orange);
    }}
    .coach-info h4 {{
      font-size: 17px;
      font-weight: 800;
      margin-bottom: 4px;
    }}
    .coach-info p {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* Social Proof Section */
    .social-proof-section {{
      max-width: 1100px;
      margin: 30px auto 80px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
    }}
    .review-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 24px;
    }}
    .stars {{
      color: #FFD60A;
      font-size: 18px;
      margin-bottom: 12px;
    }}
    .review-card p {{
      font-size: 15px;
      color: #fff;
      font-style: italic;
      margin-bottom: 14px;
      line-height: 1.5;
    }}
    .reviewer {{
      font-size: 13px;
      font-weight: 700;
      color: var(--text-muted);
    }}

    /* FAQ Section */
    .faq-section {{
      max-width: 860px;
      margin: 40px auto 80px;
      padding: 0 20px;
    }}
    .faq-item {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      margin-bottom: 14px;
      overflow: hidden;
      transition: border-color 0.2s;
    }}
    .faq-item:hover {{
      border-color: rgba(255, 255, 255, 0.2);
    }}
    .faq-question {{
      padding: 20px 24px;
      font-size: 17px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
      list-style: none;
    }}
    .faq-question::-webkit-details-marker {{
      display: none;
    }}
    .faq-arrow {{
      font-size: 12px;
      color: var(--text-muted);
      transition: transform 0.25s;
    }}
    .faq-item[open] .faq-arrow {{
      transform: rotate(180deg);
      color: var(--primary-green);
    }}
    .faq-answer {{
      padding: 0 24px 22px;
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Support Section */
    .support-section {{
      max-width: 800px;
      margin: 40px auto 90px;
      padding: 0 20px;
      text-align: center;
    }}
    .support-section h2 {{
      font-size: 28px;
      font-weight: 900;
      margin-bottom: 12px;
    }}
    .support-section p {{
      color: var(--text-muted);
      font-size: 15px;
      margin-bottom: 24px;
    }}
    .support-email {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #fff;
      padding: 14px 28px;
      border-radius: 99px;
      text-decoration: none;
      font-weight: 700;
      font-size: 15px;
      transition: background 0.2s, border-color 0.2s;
    }}
    .support-email:hover {{
      background: rgba(255, 255, 255, 0.16);
      border-color: rgba(48, 209, 88, 0.5);
    }}

    /* Sticky Bottom Download CTA */
    .sticky-cta {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      opacity: 0;
      pointer-events: none;
      z-index: 99;
      background: var(--primary-green);
      color: #000;
      padding: 14px 30px;
      border-radius: 99px;
      font-size: 15px;
      font-weight: 900;
      text-decoration: none;
      box-shadow: 0 10px 30px rgba(48, 209, 88, 0.5);
      display: flex;
      align-items: center;
      gap: 10px;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s;
    }}
    .sticky-cta.visible {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
      pointer-events: auto;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 50px 20px 40px;
      text-align: center;
      background: #050508;
    }}
    .footer-brand {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      margin-bottom: 20px;
    }}
    .footer-logo {{
      height: 28px;
      opacity: 0.85;
    }}
    .footer-tagline {{
      font-size: 12px;
      color: var(--text-muted);
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-weight: 700;
    }}
    footer p {{
      color: var(--text-muted);
      font-size: 13px;
    }}
    footer a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    footer a:hover {{
      color: var(--primary-green);
    }}

    /* Reveal Animation */
    .reveal {{
      opacity: 0;
      transform: translateY(24px);
      transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .reveal.active {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- Navigation -->
  <header>
    <nav>
      <a href="/?lang={lang_code}" class="brand">
        <img src="/images/app_icon.png" alt="{t['brand_name']}">
        <span class="brand-title">{t['brand_name']}</span>
      </a>
      <div class="nav-right">
        <div class="nav-links">
          <a href="#apple-tv">{t['nav_tv']}</a>
          <a href="#programs">{t['nav_programs']}</a>
          <a href="#features">{t['nav_features']}</a>
          <a href="#coaches">{t['nav_coaches']}</a>
          <a href="#faq">{t['nav_faq']}</a>
          <a href="/privacy?lang={lang_code}">{t['nav_privacy']}</a>
        </div>
        <div class="lang-picker">
          <a href="/?lang=en" class="{'active' if lang_code == 'en' else ''}">EN</a>
          <span>•</span>
          <a href="/?lang=zh-Hant" class="{'active' if lang_code == 'zh-Hant' else ''}">繁中</a>
          <span>•</span>
          <a href="/?lang=zh-Hans" class="{'active' if lang_code == 'zh-Hans' else ''}">简中</a>
          <span>•</span>
          <a href="/?lang=es" class="{'active' if lang_code == 'es' else ''}">ES</a>
        </div>
      </div>
    </nav>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="badge">{t['hero_badge']}</div>
    <h1>{t['hero_title']}</h1>
    <p>{t['hero_sub']}</p>
    
    <div class="pills-container">
      {pills_html}
    </div>

    <div>
      <div class="cta-group">
        <a href="https://apps.apple.com/app/id6811742209" class="cta-btn" target="_blank" rel="noopener noreferrer">
          <span class="cta-apple-icon"></span>
          <span>{t['cta_app_store']}</span>
        </a>
        <a href="https://www.youtube.com/watch?v=w05YC97VSYc" class="cta-video-btn" data-video-open="true" target="_blank" rel="noopener noreferrer">
          <span class="cta-video-icon">▶</span>
          <span>{t['cta_watch_video']}</span>
        </a>
      </div>
      <div class="cta-note">{t['cta_note']}</div>
    </div>
  </section>

  <!-- Apple TV Spotlight Section -->
  <section class="tv-spotlight-section" id="apple-tv">
    <div class="section-title">
      <div class="badge">{t['sec_tv_badge']}</div>
      <h2>{t['sec_tv_title']}</h2>
      <p>{t['sec_tv_sub']}</p>
    </div>

    <div class="tv-bezel-container">
      <div class="tv-tabs">
        <button class="tv-tab-btn active" data-tv-src="{tv_img_default}">{t['tv_tab_programs']}</button>
        <button class="tv-tab-btn" data-tv-src="{tv_img_ring}">{t['tv_tab_ring']}</button>
        <button class="tv-tab-btn" data-tv-src="{tv_img_coach}">{t['tv_tab_cinema']}</button>
      </div>
      <div class="tv-screen-frame">
        <img id="tvScreenImg" src="{tv_img_default}" alt="Apple TV Workout Timer Screen" loading="eager">
      </div>
      <div class="tv-features-row">
        <div class="tv-feat-card">
          <h4>4K {t['tv_feat_1_title']}</h4>
          <p>{t['tv_feat_1_desc']}</p>
        </div>
        <div class="tv-feat-card">
          <h4> {t['tv_feat_2_title']}</h4>
          <p>{t['tv_feat_2_desc']}</p>
        </div>
        <div class="tv-feat-card">
          <h4>🎬 {t['tv_feat_3_title']}</h4>
          <p>{t['tv_feat_3_desc']}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 7 Curated Coach Programs Section -->
  <section class="programs-section" id="programs">
    <div class="section-title">
      <div class="badge">{t['sec_programs_badge']}</div>
      <h2>{t['sec_programs_title']}</h2>
      <p>{t['sec_programs_sub']}</p>
    </div>

    <div class="up-next-banner">
      <div class="up-next-icon">💡</div>
      <div class="up-next-banner-content">
        <span class="up-next-badge">{t['up_next_badge']}</span>
        <h4>{t['up_next_title']}</h4>
        <p>{t['up_next_desc']}</p>
      </div>
    </div>

    <div class="programs-grid">
      {programs_html}
    </div>
  </section>

  <!-- Multi-Device Ecosystem Section -->
  <section class="ecosystem-section" id="ecosystem">
    <div class="section-title">
      <div class="badge">{t['sec_ecosystem_badge']}</div>
      <h2>{t['sec_ecosystem_title']}</h2>
      <p>{t['sec_ecosystem_sub']}</p>
    </div>
    <div class="eco-grid">
      {ecosystem_html}
    </div>
  </section>

  <!-- Device Gallery Showcase -->
  <div class="gallery-container">
    <div class="gallery">
      <div class="device-frame">
        <img src="{iphone_shot}" alt="Workout Timer iPhone Countdown Display" loading="lazy">
      </div>
      <div class="device-frame">
        <img src="{iphone_programs_shot}" alt="Workout Timer iPhone Coach Programs" loading="lazy">
      </div>
      <div class="device-frame">
        <img src="/images/shot_ipad.webp" alt="Workout Timer iPad Display" loading="lazy">
      </div>
      <div class="device-frame">
        <img src="/images/shot_watch.png" alt="Workout Timer Apple Watch App" loading="lazy">
      </div>
      <div class="device-frame">
        <img src="/images/shot_settings.png" alt="Settings & Voice Coach Picker" loading="lazy">
      </div>
    </div>
    <div class="gallery-hint">{t['gallery_hint']}</div>
  </div>

  <!-- Video Showcase Section -->
  <section class="video-showcase-section" id="video-demo">
    <div class="section-title">
      <div class="badge">{t['sec_video_badge']}</div>
      <h2>{t['sec_video_title']}</h2>
      <p>{t['sec_video_sub']}</p>
    </div>
    <div class="video-wrapper">
      <div class="video-card">
        <iframe src="https://www.youtube-nocookie.com/embed/w05YC97VSYc?rel=0" 
                title="Workout Timer Showcase Video" 
                loading="lazy" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                allowfullscreen></iframe>
      </div>
    </div>
  </section>

  <!-- Features Bento Grid -->
  <section class="features" id="features">
    <div class="section-title">
      <h2>{t['sec_features_title']}</h2>
      <p>{t['sec_features_sub']}</p>
    </div>
    <div class="features-grid">
      {features_html}
    </div>
  </section>

  <!-- Voice Coaches Section -->
  <section class="coaches-section" id="coaches">
    <div class="section-title">
      <h2>{t['sec_coaches_title']}</h2>
      <p>{t['sec_coaches_sub']}</p>
    </div>
    <div class="coaches-grid">
      <div class="coach-card">
        <div class="coach-avatar-wrapper">
          <img class="coach-avatar" src="/images/avatar_xiaosi.png" alt="Coach XiaoSi" loading="lazy">
          <button class="play-audio-btn" data-coach="xiaosi" title="Play Intro" aria-label="Play Intro">▶</button>
        </div>
        <div class="coach-info">
          <h4>{t['coach_xiaosi']}</h4>
          <p>{t['coach_xiaosi_sub']}</p>
        </div>
      </div>
      <div class="coach-card">
        <div class="coach-avatar-wrapper">
          <img class="coach-avatar" src="/images/avatar_xiaosu.png" alt="Coach XiaoSu" loading="lazy">
          <button class="play-audio-btn" data-coach="xiaosu" title="Play Intro" aria-label="Play Intro">▶</button>
        </div>
        <div class="coach-info">
          <h4>{t['coach_xiaosu']}</h4>
          <p>{t['coach_xiaosu_sub']}</p>
        </div>
      </div>
      <div class="coach-card">
        <div class="coach-avatar-wrapper">
          <img class="coach-avatar" src="/images/avatar_oliver.png" alt="Coach Oliver" loading="lazy">
          <button class="play-audio-btn" data-coach="oliver" title="Play Intro" aria-label="Play Intro">▶</button>
        </div>
        <div class="coach-info">
          <h4>{t['coach_oliver']}</h4>
          <p>{t['coach_oliver_sub']}</p>
        </div>
      </div>
      <div class="coach-card">
        <div class="coach-avatar-wrapper">
          <img class="coach-avatar" src="/images/avatar_sofia.png" alt="Coach Sofia" loading="lazy">
          <button class="play-audio-btn" data-coach="sofia" title="Play Intro" aria-label="Play Intro">▶</button>
        </div>
        <div class="coach-info">
          <h4>{t['coach_sofia']}</h4>
          <p>{t['coach_sofia_sub']}</p>
        </div>
      </div>
      <div class="coach-card">
        <div class="coach-avatar-wrapper">
          <img class="coach-avatar" src="/images/avatar_adam.png" alt="Coach Adam" loading="lazy">
          <button class="play-audio-btn" data-coach="adam" title="Play Intro" aria-label="Play Intro">▶</button>
        </div>
        <div class="coach-info">
          <h4>{t['coach_adam']}</h4>
          <p>{t['coach_adam_sub']}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Social Proof Section -->
  <section class="social-proof-section">
    <div class="review-card">
      <div class="stars">★★★★★</div>
      <p>"{t['review_1']}"</p>
      <div class="reviewer">- Apple TV & Gym User</div>
    </div>
    <div class="review-card">
      <div class="stars">★★★★★</div>
      <p>"{t['review_2']}"</p>
      <div class="reviewer">- HIIT & Fitness Coach</div>
    </div>
    <div class="review-card">
      <div class="stars">★★★★★</div>
      <p>"{t['review_3']}"</p>
      <div class="reviewer">- Core Workout Athlete</div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section" id="faq">
    <div class="section-title">
      <h2>{t['sec_faq_title']}</h2>
      <p>{t['sec_faq_sub']}</p>
    </div>
    {faqs_html}
  </section>

  <!-- Support Section -->
  <section class="support-section" id="support">
    <h2>{t['support_title']}</h2>
    <p>{t['support_sub']}</p>
    <a href="mailto:help@appengine.fun?subject=Workout%20Timer%20Feedback" class="support-email">
      {t['support_btn']}
    </a>
  </section>

  <!-- Sticky CTA -->
  <a href="https://apps.apple.com/app/id6811742209" id="stickyCta" class="sticky-cta" target="_blank" rel="noopener noreferrer">
    <span class="cta-apple-icon"></span>
    <span>{t['cta_app_store']}</span>
  </a>

  <!-- Footer -->
  <footer>
    <div class="footer-brand">
      <img class="footer-logo" src="/images/brand_logo.png?v=AppEngineInteractive" alt="AppEngine Interactive">
      <div class="footer-tagline">An AE Interactive Original Production</div>
    </div>
    <p>{t['footer_rights']}</p>
    <p style="margin-top: 14px;">
      <a href="/privacy?lang={lang_code}">{t['nav_privacy']}</a> • 
      <a href="#support">{t['nav_support']}</a> • 
      <a href="https://www.youtube.com/@appengine-a" target="_blank" rel="noopener noreferrer">YouTube</a> • 
      <a href="https://reviewcloud.net" target="_blank" rel="noopener noreferrer">ReviewCloud</a> • 
      <a href="https://appengine.fun" target="_blank" rel="noopener noreferrer">AE Interactive</a>
    </p>
    <p style="font-size: 11px; color: rgba(255, 255, 255, 0.3); margin-top: 24px; font-family: monospace; letter-spacing: 0.5px;">Build: {build_version_info}</p>
  </footer>

  <!-- Lightbox Video Modal -->
  <div id="videoModal" class="video-modal">
    <div class="video-modal-backdrop" id="modalBackdrop"></div>
    <div class="video-modal-dialog">
      <button class="video-modal-close" id="modalCloseBtn" aria-label="Close Video">✕</button>
      <div class="video-modal-player-wrap">
        <iframe id="modalIframe" src="" title="Workout Timer App Video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
    </div>
  </div>

  <!-- Client-side Interactive Scripts -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      // 1. Reveal Animations on Scroll
      const reveals = document.querySelectorAll(".feature-card, .coach-card, .review-card, .program-card, .eco-card, .section-title, .faq-item");
      reveals.forEach(el => el.classList.add("reveal"));
      
      const observer = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
          if(entry.isIntersecting) {{
            entry.target.classList.add("active");
            observer.unobserve(entry.target);
          }}
        }});
      }}, {{ threshold: 0.1 }});
      
      reveals.forEach(el => observer.observe(el));
      
      // 2. Apple TV Screenshot Tab Switcher
      const tvImg = document.getElementById("tvScreenImg");
      const tvButtons = document.querySelectorAll(".tv-tab-btn");
      tvButtons.forEach(btn => {{
        btn.addEventListener("click", function() {{
          tvButtons.forEach(b => b.classList.remove("active"));
          this.classList.add("active");
          const targetSrc = this.getAttribute("data-tv-src");
          if (tvImg && targetSrc) {{
            tvImg.style.opacity = "0.3";
            setTimeout(() => {{
              tvImg.src = targetSrc;
              tvImg.style.opacity = "1";
            }}, 150);
          }}
        }});
      }});

      // 3. Audio Playback Logic for Voice Coaches
      const coachAudio = {{
        "xiaosu": "data:audio/mp3;base64,{audio_dict['xiaosu.mp3']}",
        "xiaosi": "data:audio/mp3;base64,{audio_dict['xiaosi.mp3']}",
        "oliver": "data:audio/mp3;base64,{audio_dict['oliver.mp3']}",
        "sofia": "data:audio/mp3;base64,{audio_dict['sofia.mp3']}",
        "adam": "data:audio/mp3;base64,{audio_dict['adam.mp3']}"
      }};
      
      let currentAudio = null;
      let currentBtn = null;
      
      document.querySelectorAll('.play-audio-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
          const coach = this.getAttribute('data-coach');
          
          if (currentBtn === this && currentAudio && !currentAudio.paused) {{
            currentAudio.pause();
            currentAudio.currentTime = 0;
            this.classList.remove('playing');
            this.innerHTML = '▶';
            currentBtn = null;
            return;
          }}
          
          if (currentAudio) {{
            currentAudio.pause();
            currentAudio.currentTime = 0;
            if (currentBtn) {{
              currentBtn.classList.remove('playing');
              currentBtn.innerHTML = '▶';
            }}
          }}
          
          if (coachAudio[coach]) {{
            currentAudio = new Audio(coachAudio[coach]);
            currentBtn = this;
            this.classList.add('playing');
            this.innerHTML = '⏸';
            
            currentAudio.play().catch(e => console.log('Audio playback prevented:', e));
            
            currentAudio.onended = () => {{
              this.classList.remove('playing');
              this.innerHTML = '▶';
              currentBtn = null;
            }};
          }}
        }});
      }});

      // 4. Sticky CTA on scroll
      const stickyCta = document.getElementById('stickyCta');
      window.addEventListener('scroll', () => {{
        if (window.scrollY > 500) {{
          stickyCta.classList.add('visible');
        }} else {{
          stickyCta.classList.remove('visible');
        }}
      }});

      // 5. Video Lightbox Modal
      const modal = document.getElementById('videoModal');
      const modalIframe = document.getElementById('modalIframe');
      const backdrop = document.getElementById('modalBackdrop');
      const closeBtn = document.getElementById('modalCloseBtn');
      const videoTrigger = document.querySelector('[data-video-open="true"]');
      
      function openModal(e) {{
        if (e) e.preventDefault();
        modalIframe.src = "https://www.youtube-nocookie.com/embed/w05YC97VSYc?autoplay=1&rel=0";
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }}
      
      function closeModal() {{
        modal.classList.remove('active');
        modalIframe.src = "";
        document.body.style.overflow = '';
      }}
      
      if (videoTrigger) videoTrigger.addEventListener('click', openModal);
      if (backdrop) backdrop.addEventListener('click', closeModal);
      if (closeBtn) closeBtn.addEventListener('click', closeModal);
      window.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape' && modal.classList.contains('active')) {{
          closeModal();
        }}
      }});
    }});
  </script>
</body>
</html>
"""

def generate_privacy(lang_code):
    is_zh = "zh" in lang_code
    is_es = lang_code == "es"
    
    title = "隱私權政策 (Privacy Policy)" if "Hant" in lang_code else ("隐私政策 (Privacy Policy)" if is_zh else ("Política de Privacidad" if is_es else "Privacy Policy"))
    back_text = "返回首頁" if is_zh else ("Volver al inicio" if is_es else "Back to Workout Timer")
    updated_text = "最後更新日期：2026年10月28日" if is_zh else ("Última actualización: 28 de octubre de 2026" if is_es else "Last updated: October 28, 2026")
    
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{title} - Workout Timer</title>
  <meta name="description" content="Workout Timer Privacy Policy - 100% offline, zero data collection.">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/png" href="/images/app_icon.png">
  <style>
    body {{
      background: #000;
      color: #fff;
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
      line-height: 1.7;
      max-width: 800px;
      margin: 0 auto;
      padding: 40px 20px;
    }}
    h1 {{ font-size: 32px; margin-bottom: 12px; color: #30D158; }}
    h2 {{ font-size: 20px; margin-top: 32px; margin-bottom: 12px; }}
    p {{ color: #a1a1a6; margin-bottom: 16px; font-size: 15px; }}
    a {{ color: #30D158; text-decoration: none; }}
    .back-btn {{ display: inline-block; margin-bottom: 24px; font-weight: bold; }}
  </style>
</head>
<body>
  <a href="/?lang={lang_code}" class="back-btn">← {back_text}</a>
  <h1>{title}</h1>
  <p><em>{updated_text}</em></p>
  
  <h2>1. Zero Data Collection</h2>
  <p>Workout Timer is designed with privacy as a foundational principle. We do not collect, store, transmit, or sell any personal data, health data, device identifiers, or analytics. Your workout history and preferences remain strictly on your physical devices (iPhone, iPad, Apple Watch, Apple TV).</p>
  
  <h2>2. Apple Health & AirPods Integration</h2>
  <p>Workout Timer accesses Apple Health data (such as active heart rate and energy burned) exclusively on your local device with your explicit permission. This data is used solely to render real-time workout rings on your screen and Dynamic Island. It is never transmitted across the network.</p>

  <h2>3. Universal Purchase & In-App Purchases</h2>
  <p>All transactions are processed directly by Apple App Store via your Apple ID. We do not store or process payment or credit card credentials.</p>

  <h2>4. Contact</h2>
  <p>If you have any questions about this Privacy Policy, please contact us at <a href="mailto:help@appengine.fun">help@appengine.fun</a>.</p>
</body>
</html>
"""

# Compile pages
pages = {
    "en": generate_page("en"),
    "zh-Hant": generate_page("zh-Hant"),
    "zh-Hans": generate_page("zh-Hans"),
    "es": generate_page("es")
}

privacy_pages = {
    "en": generate_privacy("en"),
    "zh-Hant": generate_privacy("zh-Hant"),
    "zh-Hans": generate_privacy("zh-Hans"),
    "es": generate_privacy("es")
}

gtm_head = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W7N52ZML');</script>
<!-- End Google Tag Manager -->"""

gtm_body = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W7N52ZML"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

def inject_gtm(html_str):
    html_str = html_str.replace("<head>", f"<head>\n  {gtm_head}", 1)
    html_str = html_str.replace("<body>", f"<body>\n  {gtm_body}", 1)
    return html_str

pages = {k: inject_gtm(v) for k, v in pages.items()}
privacy_pages = {k: inject_gtm(v) for k, v in privacy_pages.items()}

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://workout.appengine.fun/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://workout.appengine.fun/?lang=en"/>
    <xhtml:link rel="alternate" hreflang="zh-Hant" href="https://workout.appengine.fun/?lang=zh-Hant"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://workout.appengine.fun/?lang=zh-Hans"/>
    <xhtml:link rel="alternate" hreflang="es" href="https://workout.appengine.fun/?lang=es"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://workout.appengine.fun/"/>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://workout.appengine.fun/privacy</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://workout.appengine.fun/privacy?lang=en"/>
    <xhtml:link rel="alternate" hreflang="zh-Hant" href="https://workout.appengine.fun/privacy?lang=zh-Hant"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://workout.appengine.fun/privacy?lang=zh-Hans"/>
    <xhtml:link rel="alternate" hreflang="es" href="https://workout.appengine.fun/privacy?lang=es"/>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
"""

robots_txt = """User-agent: *
Allow: /
Sitemap: https://workout.appengine.fun/sitemap.xml
"""

catalog_path = os.path.join(base_dir, "public", "api", "workouts_catalog.json")
if os.path.exists(catalog_path):
    with open(catalog_path, "r", encoding="utf-8") as f:
        workouts_catalog_raw = f.read()
else:
    workouts_catalog_raw = '{"version": 1, "items": []}'

worker_js = f"""
const PAGES = {json.dumps(pages)};
const PRIVACY_PAGES = {json.dumps(privacy_pages)};
const IMAGES = {json.dumps(images_dict)};
const SITEMAP_XML = {json.dumps(sitemap_xml)};
const ROBOTS_TXT = {json.dumps(robots_txt)};
const WORKOUTS_CATALOG_RAW = {json.dumps(workouts_catalog_raw)};

function base64ToUint8Array(base64) {{
  const binaryString = atob(base64);
  const len = binaryString.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {{
    bytes[i] = binaryString.charCodeAt(i);
  }}
  return bytes;
}}

function resolveLang(request) {{
  const url = new URL(request.url);
  const param = url.searchParams.get("lang");
  if (param && PAGES[param]) return param;
  if (param === "zh" || param === "tw" || param === "hk") return "zh-Hant";
  if (param === "cn") return "zh-Hans";

  const accept = (request.headers.get("accept-language") || "").toLowerCase();
  if (accept.includes("zh-tw") || accept.includes("zh-hk") || accept.includes("zh-hant")) return "zh-Hant";
  if (accept.includes("zh")) return "zh-Hans";
  if (accept.includes("es")) return "es";
  return "en";
}}

export default {{
  async fetch(request, env) {{
    const url = new URL(request.url);
    const pathname = url.pathname;

    // 0. Google Site Verification HTML
    if (pathname === "/google903e52d561cdf41c.html") {{
      return new Response("google-site-verification: google903e52d561cdf41c.html", {{
        headers: {{
          "content-type": "text/html;charset=UTF-8",
          "cache-control": "public, max-age=86400"
        }}
      }});
    }}

    // 1. Robots.txt
    if (pathname === "/robots.txt") {{
      return new Response(ROBOTS_TXT, {{
        headers: {{
          "content-type": "text/plain;charset=UTF-8",
          "cache-control": "public, max-age=86400"
        }}
      }});
    }}

    // 2. Sitemap.xml
    if (pathname === "/sitemap.xml") {{
      return new Response(SITEMAP_XML, {{
        headers: {{
          "content-type": "application/xml;charset=UTF-8",
          "cache-control": "public, max-age=86400"
        }}
      }});
    }}

    // 3. Image assets (/images/:filename)
    if (pathname.startsWith("/images/")) {{
      const filename = pathname.replace("/images/", "");
      if (IMAGES[filename]) {{
        const bytes = base64ToUint8Array(IMAGES[filename]);
        let mime = "image/png";
        if (filename.endsWith(".webp")) mime = "image/webp";
        else if (filename.endsWith(".jpg") || filename.endsWith(".jpeg")) mime = "image/jpeg";
        else if (filename.endsWith(".svg")) mime = "image/svg+xml";
        return new Response(bytes, {{
          headers: {{
            "content-type": mime,
            "cache-control": "public, max-age=31536000, immutable"
          }}
        }});
      }}
      return new Response("Image Not Found", {{ status: 404 }});
    }}

    // 3.5. Workouts Catalog API (Dynamic In-App Purchases & Programs)
    if (pathname === "/api/workouts_catalog.json" || pathname === "/workouts_catalog.json") {{
      if (env && env.ASSETS_BUCKET) {{
        const obj = await env.ASSETS_BUCKET.get("api/workouts_catalog.json");
        if (obj) {{
          return new Response(obj.body, {{
            headers: {{
              "content-type": "application/json;charset=UTF-8",
              "access-control-allow-origin": "*",
              "cache-control": "public, max-age=60, stale-while-revalidate=300"
            }}
          }});
        }}
      }}
      return new Response(WORKOUTS_CATALOG_RAW, {{
        headers: {{
          "content-type": "application/json;charset=UTF-8",
          "access-control-allow-origin": "*",
          "cache-control": "public, max-age=60, stale-while-revalidate=300"
        }}
      }});
    }}

    // 3.6. Cloudflare R2 Workout Video & Audio Assets (/assets/:slug/...)
    if (pathname.startsWith("/assets/") && env && env.ASSETS_BUCKET) {{
      const key = decodeURIComponent(pathname.slice(1));
      const obj = await env.ASSETS_BUCKET.get(key);
      if (!obj) {{
        return new Response("Asset Not Found", {{ status: 404 }});
      }}
      const headers = new Headers();
      obj.writeHttpMetadata(headers);
      headers.set("etag", obj.httpEtag);
      headers.set("access-control-allow-origin", "*");
      headers.set("accept-ranges", "bytes");
      headers.set("cache-control", "public, max-age=31536000, immutable");
      if (key.endsWith(".mp4")) headers.set("content-type", "video/mp4");
      else if (key.endsWith(".mp3")) headers.set("content-type", "audio/mpeg");
      else if (key.endsWith(".json")) headers.set("content-type", "application/json;charset=UTF-8");
      return new Response(obj.body, {{ status: 200, headers }});
    }}

    // 4. Privacy Policy
    const lang = resolveLang(request);
    if (pathname === "/privacy" || pathname === "/privacy.html") {{
      const html = PRIVACY_PAGES[lang] || PRIVACY_PAGES["en"];
      return new Response(html, {{
        headers: {{
          "content-type": "text/html;charset=UTF-8",
          "cache-control": "public, max-age=3600, stale-while-revalidate=86400"
        }}
      }});
    }}

    // 5. Main landing page
    const html = PAGES[lang] || PAGES["en"];
    return new Response(html, {{
      headers: {{
        "content-type": "text/html;charset=UTF-8",
        "cache-control": "public, max-age=3600, stale-while-revalidate=86400"
      }}
    }});
  }}
}};
"""

out_worker = os.path.join(base_dir, "worker.js")
with open(out_worker, "w") as f:
    f.write(worker_js)

print(f"Generated optimized worker.js, size: {len(worker_js)} bytes ({len(worker_js) / 1024 / 1024:.2f} MB)")

# Deploy to Cloudflare Worker
token = os.environ.get("CF_API_TOKEN", "")
if not token and os.path.exists(os.path.expanduser("~/.cf_token")):
    with open(os.path.expanduser("~/.cf_token"), "r") as f:
        token = f.read().strip()
account_id = "9fb3b494e6d4d659f2cf567efb94fc38"
script_name = "workouttimer-site"
url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{script_name}"

boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
body = []
body.append(f"--{boundary}".encode())
body.append(b'Content-Disposition: form-data; name="metadata"')
body.append(b'Content-Type: application/json')
body.append(b'')
body.append(json.dumps({
    "main_module": "index.js",
    "compatibility_date": "2024-03-03",
    "bindings": [
        {
            "type": "r2_bucket",
            "name": "ASSETS_BUCKET",
            "bucket_name": "workouttimer-assets"
        }
    ]
}).encode())

body.append(f"--{boundary}".encode())
body.append(b'Content-Disposition: form-data; name="index.js"; filename="index.js"')
body.append(b'Content-Type: application/javascript+module')
body.append(b'')
body.append(worker_js.encode())

body.append(f"--{boundary}--".encode())
body.append(b'')

payload = b"\r\n".join(body)

req = urllib.request.Request(url, data=payload, method="PUT", headers={
    "Authorization": f"Bearer {token}",
    "Content-Type": f"multipart/form-data; boundary={boundary}"
})

try:
    with urllib.request.urlopen(req) as resp:
        print("Worker deployed successfully to Cloudflare:", resp.read().decode())
except Exception as e:
    print("urllib upload failed, falling back to curl...", e)
    import subprocess
    curl_cmd = [
        "curl", "-s", "-X", "PUT", url,
        "-H", f"Authorization: Bearer {token}",
        "-F", 'metadata={"main_module": "index.js", "compatibility_date": "2024-03-03", "bindings": [{"type": "r2_bucket", "name": "ASSETS_BUCKET", "bucket_name": "workouttimer-assets"}]};type=application/json',
        "-F", f'index.js=@{out_worker};filename="index.js";type=application/javascript+module'
    ]
    res = subprocess.run(curl_cmd, capture_output=True, text=True)
    print("Curl deploy output:", res.stdout)
