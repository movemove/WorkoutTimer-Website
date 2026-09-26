import os
import base64
import json
import urllib.request

import subprocess
from datetime import datetime

def get_git_info():
    try:
        # Get short hash of HEAD
        commit_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8').strip()
        # Get current time
        build_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        return f"v-{commit_hash} ({build_time})"
    except Exception as e:
        return "v-unknown"

build_version_info = get_git_info()


base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, "public", "images")

image_files = [
    "app_icon.png", "brand_logo.png", "og_preview.png",
    "shot_timer.png", "shot_complete.png", "shot_settings.png",
    "shot_zh_1.png", "shot_zh_coach.png",
    "avatar_adam.png", "avatar_oliver.png", "avatar_sofia.png",
    "avatar_xiaosi.png", "avatar_xiaosu.png"
]

images_dict = {}
for name in image_files:
    p = os.path.join(img_dir, name)
    if os.path.exists(p):
        with open(p, "rb") as f:
            images_dict[name] = base64.b64encode(f.read()).decode("utf-8")
    else:
        print(f"Warning: image not found: {p}")

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
        "title": "Workout Timer: Voice Coach - High Intensity Interval Training & Gym Clock",
        "desc": "Next-gen workout timer with studio voice coaches in 4 languages, 10-Min Abs video guidance, Apple Watch & AirPods heart rate sync, Dynamic Island Live Activity, and 100% offline privacy.",
        "keywords": "workout timer, interval timer, hiit timer, tabata timer, voice coach, apple watch workout, dynamic island timer, boxing timer, gym clock, 10 min abs, core workout, live activity",
        "brand_name": "Workout Timer",
        "nav_features": "Features",
        "nav_coaches": "Coaches",
        "nav_faq": "FAQ",
        "nav_support": "Support",
        "nav_privacy": "Privacy",
        "hero_badge": "NEXT-GEN INTERVAL & GYM CLOCK",
        "hero_title": "Push Your Limits with <span>Studio Voice Coaches</span>",
        "hero_sub": "The ultimate high-intensity interval timer featuring real studio-recorded voice trainers, 10-Min Abs video demonstrations, standalone Apple Watch & AirPods heart rate sync, and complete offline privacy.",
        "pills": [
            "⌚️ Apple Watch & AirPods Sync",
            "🏝️ Dynamic Island Live Activity",
            "🔥 10-Min Abs with Coach Hannah",
            "📺 50:50 Cinema Landscape Mode",
            "🔒 100% Offline Privacy"
        ],
        "cta_app_store": "Download for Free",
        "cta_watch_video": "Watch Video Demo",
        "cta_note": "iOS 17+ & watchOS 10+ • No Account Required",
        "gallery_hint": "👈 Swipe horizontally to preview app screens 👉",
        "sec_video_badge": "APP DEMO",
        "sec_video_title": "Experience Workout Timer in Action",
        "sec_video_sub": "Watch Coach Hannah guide the 10-Min Abs routine, explore the 50:50 Cinema Landscape Mode, and see Apple Watch & AirPods live sync in real-time.",
        "sec_features_title": "Engineered for Athletic Excellence",
        "sec_features_sub": "Everything you need for Tabata, HIIT, Boxing, AMRAP, and Core Workouts.",
        "features": [
            {
                "icon": "🎙️",
                "title": "Studio Human Coaches",
                "desc": "Real studio-recorded voice coaches in English (US & UK), Spanish (LatAm), and Chinese (Traditional & Simplified) guide every work, rest, and countdown."
            },
            {
                "icon": "🔥",
                "title": "10-Min Abs Curated Program",
                "desc": "12-round core workout with seamless video loops and 20s rest previews (UP NEXT), letting you prep your body smoothly for the next movement."
            },
            {
                "icon": "⌚️",
                "title": "Apple Watch & AirPods Live Sync",
                "desc": "Standalone watchOS app with wrist haptic cues, plus live streaming heart rate and active calories from Apple Watch and AirPods Pro."
            },
            {
                "icon": "🏝️",
                "title": "Dynamic Island & Live Activity",
                "desc": "Track your interval progression directly from your Lock Screen and Dynamic Island with hardware-accelerated GPU progress bars."
            },
            {
                "icon": "📺",
                "title": "50:50 Landscape Gym Clock",
                "desc": "Giant digits readable from 5 meters across the gym floor, paired with split-screen video form guidance on your workout mat."
            },
            {
                "icon": "🎬",
                "title": "Post-Workout Celebration Videos",
                "desc": "Celebrate every breakthrough! Your chosen coach congratulates you with a full-screen motivational video after each completed session."
            },
            {
                "icon": "⚙️",
                "title": "Built-in & Custom Presets",
                "desc": "Launch instantly into classic Tabata (20s/10s), HIIT (40s/20s), or 3-minute Boxing rounds, or customize your own sets and cycles."
            },
            {
                "icon": "🔒",
                "title": "100% Offline & Pure Privacy",
                "desc": "No account creation, no analytics tracking, no forced subscriptions, and zero advertising. Your training data stays strictly on your device."
            }
        ],
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
        "sec_faq_title": "Frequently Asked Questions",
        "sec_faq_sub": "Everything you need to know about Workout Timer.",
        "faqs": [
            {
                "q": "Does Workout Timer require a monthly subscription?",
                "a": "No. Workout Timer is a single, one-time purchase. There are no recurring subscriptions, no hidden fees, and absolutely no ads. Buy it once, and own all studio voice coaches forever."
            },
            {
                "q": "How does the Apple Watch & AirPods heart rate monitoring work?",
                "a": "The app includes a dedicated standalone Apple Watch app that delivers tactile haptic taps on your wrist. When paired with iPhone, it streams live heart rate and active calories to your circular timer ring and Dynamic Island."
            },
            {
                "q": "Can I listen to my own music while the timer is running?",
                "a": "Yes! The app features intelligent Audio Ducking: whenever your coach announces a countdown or interval transition, it automatically lowers background Spotify or Apple Music volume, then immediately restores it."
            },
            {
                "q": "What is the 10-Min Abs guided workout?",
                "a": "It is an official 12-round core curriculum (30s Work / 20s Rest). During Work, it displays standard looping video form; during Rest, it automatically previews the upcoming exercise with an UP NEXT badge so you can transition seamlessly."
            }
        ],
        "support_title": "Need Help or Have Feedback?",
        "support_sub": "We are dedicated to providing the cleanest, most athletic workout timer experience. For questions or feature suggestions:",
        "support_btn": "✉️ Contact Support: help@appengine.fun",
        "review_1": "The voice coaches make such a huge difference. I finally feel like I am in a real studio class!",
        "review_2": "The 50:50 landscape mode is genius. I can see the huge numbers from across my garage gym.",
        "review_3": "Love the 10-Min Abs preview feature! I never lose my form or get confused during transitions.",
        "footer_rights": "© 2026 Workout Timer: Voice Coach. An AE Interactive Original Production. All rights reserved."
    },
    "zh-Hant": {
        "title": "間歇計時器：真人語音教練 (Workout Timer) - Tabata / HIIT 健身房運動倒數鐘",
        "desc": "專為 Tabata、HIIT 與循環訓練打造的次世代運動計時器，搭載多國語言錄音室真人教練，全程語音激勵您的每次訓練。",
        "keywords": "間歇計時器, Tabata計時器, HIIT訓練計時, 語音教練, 健身房計時器, 動態島即時動態, Apple Watch健身計時, 核心腹肌課表, 10分鐘腹肌, 拳擊計時器, 離線運動計時, 無廣告計時器",
        "brand_name": "間歇計時器",
        "nav_features": "核心特色",
        "nav_coaches": "語音教練",
        "nav_faq": "常見問題",
        "nav_support": "技術支援",
        "nav_privacy": "隱私權政策",
        "hero_badge": "次世代間歇運動計時器",
        "hero_title": "專注極限突破，有 <span>錄音室真人教練</span> 全程陪伴",
        "hero_sub": "告別單調的嗶嗶聲！專業錄音室真人教練語音伴練、10分鐘核心腹肌示範影片、Apple Watch 雙向同步與 AirPods 即時心率，100% 離線無廣告守護您的隱私。",
        "pills": [
            "⌚️ Apple Watch & AirPods 心率同步",
            "🏝️ 動態島 & 鎖定畫面即時動態",
            "🔥 10-Min Abs 核心腹肌影音指導",
            "📺 50:50 橫向劇院巨幕模式",
            "🔒 100% 離線純淨無追蹤"
        ],
        "cta_app_store": "前往 App Store 免費下載",
        "cta_watch_video": "觀看實機影片",
        "cta_note": "支援 iOS 17+ 與 watchOS 10+ • 無需註冊帳號",
        "gallery_hint": "👈 左右滑動檢視實機操作畫面 👉",
        "sec_video_badge": "實機功能展示",
        "sec_video_title": "親身體驗 Workout Timer 的流暢實機操作",
        "sec_video_sub": "觀看 Hannah 教練 10 分鐘腹肌示範、50:50 橫向劇院巨幕模式，以及 Apple Watch 與 AirPods 即時心率串流。",
        "sec_features_title": "專為極致運動表現打造",
        "sec_features_sub": "滿足 Tabata、高強度間歇 (HIIT)、拳擊回合、AMRAP 與腹肌雕塑的所有需求。",
        "features": [
            {
                "icon": "🎙️",
                "title": "錄音室真人教練原聲",
                "desc": "提供台灣繁中（小司）、中文（小酥）、英式英語（Oliver）、美式英語（Adam）與西語（Sofia），全程語音陪伴每個訓練與休息倒數。"
            },
            {
                "icon": "🔥",
                "title": "10-Min Abs 核心腹肌課表",
                "desc": "12 輪科學循環動作，訓練時循環播放標準動作示範，20 秒休息時自動提前預習（UP NEXT）下一動，喝水調整從容就位。"
            },
            {
                "icon": "⌚️",
                "title": "Apple Watch & AirPods 同步",
                "desc": "具備專屬 watchOS 獨立手錶 App 提供手腕觸覺回饋，並可即時串流 Apple Watch 與 AirPods Pro 的即時心率與活動卡路里。"
            },
            {
                "icon": "🏝️",
                "title": "動態島與鎖定畫面即時動態",
                "desc": "無需解鎖 iPhone，鎖定畫面與動態島即能顯示高硬體加速進度環、當前階段與剩餘秒數，抬手即看超省電。"
            },
            {
                "icon": "📺",
                "title": "50:50 橫向健身房巨幕模式",
                "desc": "專為遠距設計！超大粗體數字在 5 公尺外清晰可辨，橫向分割畫面左側播放動作影片，右側大時鐘掌控全場。"
            },
            {
                "icon": "🎬",
                "title": "訓練完成真人慶祝影片",
                "desc": "為每一次全力以赴喝采！每次完成高強度訓練後，教練將親自以高畫質影片為您擊掌祝賀，點燃下一次挑戰的動力。"
            },
            {
                "icon": "⚙️",
                "title": "內建經典與自由自訂",
                "desc": "秒開 Tabata (20s/10s)、經典 HIIT (40s/20s)、拳擊 3 分鐘回合，亦可自由設定組數、大循環與休息間隔。"
            },
            {
                "icon": "🔒",
                "title": "100% 離線純淨與隱私守護",
                "desc": "無需註冊帳號、無任何第三方追蹤分析、無廣告干擾。您的個人運動數據完全只保存在您的設備本機。"
            }
        ],
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
        "sec_faq_title": "常見問題解答 (FAQ)",
        "sec_faq_sub": "關於間歇計時器的核心功能與常見疑問。",
        "faqs": [
            {
                "q": "這款計時器需要付費訂閱嗎？",
                "a": "不需要！Workout Timer 採一次性買斷制。沒有任何月費訂閱、沒有隱藏費用，也絕對沒有廣告干擾。一次付費，終身擁有所有錄音室真人教練。"
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
                "q": "什麼是「10-Min Abs 核心腹肌」引導課表？",
                "a": "這是由專業教練研發的 12 輪科學腹肌課表（30s 訓練 / 20s 休息）。訓練期間會持續循環播放標準動作示範，休息時會自動提前播放下一組動作並標示「UP NEXT」，讓您在喝水喘氣時做好預習。"
            }
        ],
        "support_title": "需要協助或提供寶貴建議？",
        "support_sub": "我們致力於打造地表最順手專業的運動計時器。如果您有任何使用問題或功能建議，歡迎聯絡：",
        "support_btn": "✉️ 聯繫技術支援：help@appengine.fun",
        "review_1": "教練語音真的差很多，比起單調的嗶嗶聲，現在終於有在健身房上課的激勵感了！",
        "review_2": "橫式的 50:50 大時鐘太棒了，手機放在遠處地上也能清楚看到剩幾秒。",
        "review_3": "10 分鐘腹肌課表的 UP NEXT 預習超級貼心，休息喝水時能提早知道下一個動作。",
        "footer_rights": "© 2026 間歇計時器：語音教練 (Workout Timer)。保留所有權利。"
    },
    "zh-Hans": {
        "title": "间歇计时器：真人语音教练 (Workout Timer) - Tabata / HIIT 健身房运动倒数钟",
        "desc": "专为 Tabata、HIIT 与循环训练打造的次世代运动计时器，搭载多国语言录音室真人教练，全程语音激励您的每次训练。",
        "keywords": "间歇计时器, Tabata倒计时, HIIT训练计时, 语音教练, 健身房计时器, 动态岛实时活动, Apple Watch运动计时, 核心腹肌课表, 10分钟腹肌, 拳击计时器, 离线运动计时, 无广告计时器",
        "brand_name": "间歇计时器",
        "nav_features": "核心功能",
        "nav_coaches": "语音教练",
        "nav_faq": "常见问题",
        "nav_support": "技术支持",
        "nav_privacy": "隐私政策",
        "hero_badge": "次世代间歇运动计时器",
        "hero_title": "全力突破体能极限，有 <span>录音室真人教练</span> 全程陪伴",
        "hero_sub": "告别单调的机械提示音！专业录音室真人教练原声播报、10分钟核心腹肌示范视频、Apple Watch 独立手表与 AirPods 实时心率，100% 离线无广告守护您的隐私。",
        "pills": [
            "⌚️ Apple Watch & AirPods 心率同步",
            "🏝️ 动态岛 & 锁屏实时活动",
            "🔥 10-Min Abs 核心腹肌影音指导",
            "📺 50:50 横向影院巨幕模式",
            "🔒 100% 离线纯净无追踪"
        ],
        "cta_app_store": "前往 App Store 免费下载",
        "cta_watch_video": "观看实机演示",
        "cta_note": "支持 iOS 17+ 与 watchOS 10+ • 无需注册账号",
        "gallery_hint": "👈 左右滑动查看实机操作画面 👉",
        "sec_video_badge": "实机功能展示",
        "sec_video_title": "亲身体验 Workout Timer 的流畅实机操作",
        "sec_video_sub": "观看 Hannah 教练 10 分钟腹肌示范、50:50 横向影院巨幕模式，以及 Apple Watch 与 AirPods 实时心率同步。",
        "sec_features_title": "专为巅峰运动表现而生",
        "sec_features_sub": "全面满足 Tabata、高强度间歇 (HIIT)、拳击实战与腹肌雕塑的所有需求。",
        "features": [
            {
                "icon": "🎙️",
                "title": "录音室真人教练原声",
                "desc": "提供小酥（普通话）、小司（台湾繁体）、Oliver（英式英语）、Adam（美式英语）与 Sofia（西班牙语），全流程语音伴随每个阶段。"
            },
            {
                "icon": "🔥",
                "title": "10-Min Abs 核心腹肌课表",
                "desc": "12 轮科学循环动作，训练时循环播放动作示范，20 秒休息时自动提前预习（UP NEXT）下一动，喝水喘气从容就位。"
            },
            {
                "icon": "⌚️",
                "title": "Apple Watch & AirPods 同步",
                "desc": "配备专属 watchOS 独立手表应用提供震动提醒，并可实时串流 Apple Watch 与 AirPods Pro 监测的心率与动态卡路里。"
            },
            {
                "icon": "🏝️",
                "title": "动态岛与锁屏实时活动",
                "desc": "无需点亮解锁手机，锁屏与动态岛即可呈现硬件加速进度环与倒数秒数，一瞥即知当前状态。"
            },
            {
                "icon": "📺",
                "title": "50:50 横向健身房巨幕模式",
                "desc": "专为健身房远距观察设计！超大数字在 5 米外清晰可见，横向左右分割同时呈现示范动作与巨幅时钟。"
            },
            {
                "icon": "🎬",
                "title": "训练完成真人庆祝视频",
                "desc": "为每一次拼搏喝彩！每次完成高强度训练，教练亲自以高清视频向您击掌祝贺，点燃下一次挑战动力。"
            },
            {
                "icon": "⚙️",
                "title": "内置经典与自由定制",
                "desc": "即刻开启 Tabata (20s/10s)、经典 HIIT (40s/20s)、拳击 3 分钟实战，自由设置工作时长与循环间歇。"
            },
            {
                "icon": "🔒",
                "title": "100% 离线纯净与隐私保护",
                "desc": "无需注册账号、无第三方跟踪代码、无广告干扰。您的运动数据完全保留在设备本地。"
            }
        ],
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
        "sec_faq_title": "常见问题解答 (FAQ)",
        "sec_faq_sub": "关于间歇计时器的核心功能与常见疑问。",
        "faqs": [
            {
                "q": "这款计时器需要付费订阅吗？",
                "a": "不需要！Workout Timer 采用一次性买断制。没有任何月费订阅、没有隐藏费用，也绝对没有广告干扰。一次付费，终身拥有所有录音室真人教练。"
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
                "q": "什么是「10-Min Abs 核心腹肌」引导课表？",
                "a": "这是由专业教练设计的 12 轮核心课表（30s 训练 / 20s 休息）。训练时循环播放标准动作示范，休息时自动提前播放下一动并标注「UP NEXT」，助您从容做好就位准备。"
            }
        ],
        "support_title": "需要帮助或反馈建议？",
        "support_sub": "我们致力于提供极致畅快专业的运动计时体验。如有任何问题或需求建议，请随时联系：",
        "support_btn": "✉️ 联系支持团队：help@appengine.fun",
        "review_1": "语音教练真的非常赞，比以前听无聊的嘟嘟声有动力多了，感觉就像在上私教课！",
        "review_2": "横屏的 50:50 大时钟设计很棒，手机放地上也能看清倒数。",
        "review_3": "10分钟腹肌课表在休息时会提前预览下一个动作，这个细节做得太好了！",
        "footer_rights": "© 2026 间歇计时器：语音教练 (Workout Timer)。保留所有权利。"
    },
    "es": {
        "title": "Workout Timer: Entrenador de Voz - Temporizador HIIT, Tabata y Cronómetro de Gimnasio",
        "desc": "Temporizador de intervalos de última generación con entrenadores de voz reales de estudio para guiarte y motivarte en cada repetición.",
        "keywords": "temporizador de intervalos, temporizador tabata, cronometro hiit, entrenador de voz, reloj gimnasio, pantalla gigante gym, apple watch temporizador, entrenamiento abdomen 10 min, dynamic island timer, cronometro boxeo",
        "brand_name": "Workout Timer",
        "nav_features": "Funciones",
        "nav_coaches": "Entrenadores",
        "nav_faq": "Preguntas",
        "nav_support": "Soporte",
        "nav_privacy": "Privacidad",
        "hero_badge": "TEMPORIZADOR HIIT & RELOJ DE GIMNASIO",
        "hero_title": "Supera tus límites con <span>Entrenadores de Voz</span>",
        "hero_sub": "El temporizador definitivo con entrenadores grabados en estudio en varios idiomas, videos de guía para Abdomen en 10 Minutos, sincronización de pulso con Apple Watch y máxima privacidad offline.",
        "pills": [
            "⌚️ Apple Watch & AirPods Sync",
            "🏝️ Dynamic Island Live Activity",
            "🔥 Guía en Video Abdomen 10 Min",
            "📺 Modo Cine Panorámico 50:50",
            "🔒 100% Privacidad Offline"
        ],
        "cta_app_store": "Descargar Gratis en el App Store",
        "cta_watch_video": "Ver Video Demo",
        "cta_note": "Compatible con iOS 17+ y watchOS 10+ • Sin cuentas ni registro",
        "gallery_hint": "👈 Desliza horizontalmente para explorar las pantallas 👉",
        "sec_video_badge": "DEMO EN ACCIÓN",
        "sec_video_title": "Descubre Workout Timer en Acción",
        "sec_video_sub": "Mira la rutina de abdomen con la entrenadora Hannah, el Modo Cine 50:50 y la sincronización con Apple Watch y AirPods.",
        "sec_features_title": "Diseñado para el Máximo Rendimiento",
        "sec_features_sub": "Todo lo que necesitas para entrenamientos Tabata, HIIT, Boxeo, AMRAP y Core.",
        "features": [
            {
                "icon": "🎙️",
                "title": "Entrenadores de Voz Reales",
                "desc": "Voces profesionales grabadas en estudio en Español latinoamericano, Inglés (EE.UU. y Reino Unido) y Chino que te guían en cada serie y descanso."
            },
            {
                "icon": "🔥",
                "title": "Programa Abdomen en 10 Minutos",
                "desc": "12 rondas con bucles de video de técnica estándar y vista previa en el descanso (UP NEXT) para prepararte sin prisas."
            },
            {
                "icon": "⌚️",
                "title": "Apple Watch & AirPods Sync",
                "desc": "App independiente para watchOS con alertas hápticas en la muñeca, y transmisión de pulso y calorías en tiempo real desde Apple Watch y AirPods Pro."
            },
            {
                "icon": "🏝️",
                "title": "Dynamic Island & Live Activity",
                "desc": "Sigue la cuenta atrás directamente desde tu pantalla de bloqueo y Dynamic Island con barras aceleradas por GPU sin gastar batería."
            },
            {
                "icon": "📺",
                "title": "Reloj de Gimnasio 50:50 Horizontal",
                "desc": "Dígitos gigantes legibles a 5 metros de distancia a través del gimnasio, junto a la demostración en video en tu colchoneta."
            },
            {
                "icon": "🎬",
                "title": "Video de Celebración al Terminar",
                "desc": "¡Celebra tu esfuerzo! Tu entrenador personal te felicita con un video motivacional real a pantalla completa tras cada sesión."
            },
            {
                "icon": "⚙️",
                "title": "Rutinas Integradas y Personalizadas",
                "desc": "Comienza al instante con Tabata (20s/10s), HIIT clásico (40s/20s), Boxeo (3m/1m) o diseña tus propias series y descansos."
            },
            {
                "icon": "🔒",
                "title": "100% Offline y Máxima Privacidad",
                "desc": "Sin registro de cuentas, sin rastreadores ni suscripciones forzosas. Tus datos de entrenamiento permanecen siempre en tu dispositivo."
            }
        ],
        "sec_coaches_title": "Conoce a tus Entrenadores de Voz",
        "sec_coaches_sub": "Cinco entrenadores profesionales listos para motivarte en cada repetición.",
        "coach_xiaosu": "Coach XiaoSu",
        "coach_xiaosu_sub": "Chino Mandarín • Cálida y Motivadora",
        "coach_xiaosi": "Coach XiaoSi",
        "coach_xiaosi_sub": "Chino Mandarín (Taiwán) • Profesional y Enérgica",
        "coach_oliver": "Coach Oliver",
        "coach_oliver_sub": "Inglés Británico • Enérgico y Dinámico",
        "coach_sofia": "Coach Sofia",
        "coach_sofia_sub": "Español (LatAm) • Firme, Enérgica e Inspiradora",
        "coach_adam": "Coach Adam",
        "coach_adam_sub": "Inglés Estadounidense • Claro, Potente y Motivador",
        "sec_faq_title": "Preguntas Frecuentes (FAQ)",
        "sec_faq_sub": "Todo lo que necesitas saber sobre Workout Timer.",
        "faqs": [
            {
                "q": "¿La aplicación es gratuita?",
                "a": "¡Sí! Workout Timer es completamente gratis para descargar y usar. Sin suscripciones, sin anuncios y sin cargos ocultos."
            },
            {
                "q": "¿Cómo funciona la medición con Apple Watch y AirPods?",
                "a": "La app incluye una app independiente para Apple Watch con toques hápticos en la muñeca. Al vincularse con el iPhone, transmite el pulso cardíaco y las calorías a la esfera del temporizador y a Dynamic Island."
            },
            {
                "q": "¿Puedo escuchar música mientras uso el temporizador?",
                "a": "¡Por supuesto! Cuenta con Atenuación de Audio inteligente (Audio Ducking): cuando el entrenador habla, baja automáticamente el volumen de Spotify o Apple Music y lo restablece al terminar."
            },
            {
                "q": "¿En qué consiste el entrenamiento guiado de Abdomen 10 Min?",
                "a": "Es una rutina científica de 12 rondas (30s trabajo / 20s descanso). Durante el trabajo muestra videos de técnica en bucle, y durante el descanso previsualiza el siguiente ejercicio con una etiqueta «UP NEXT»."
            }
        ],
        "support_title": "¿Necesitas Ayuda o Tienes Preguntas?",
        "support_sub": "Estamos dedicados a ofrecerte el mejor temporizador de entrenamiento. Contáctanos:",
        "support_btn": "✉️ Contactar Soporte: help@appengine.fun",
        "review_1": "¡Los entrenadores de voz hacen una gran diferencia! Siento que estoy en una clase real.",
        "review_2": "El modo horizontal 50:50 es genial. Puedo ver los números gigantes desde lejos.",
        "review_3": "¡Me encanta la vista previa de Abdomen 10 Min! Nunca pierdo la forma en las transiciones.",
        "footer_rights": "© 2026 Workout Timer: Entrenador de Voz. Todos los derechos reservados."
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
                "alternateName": ["間歇計時器", "Gym Clock", "Tabata Timer"],
                "url": "https://workout.appengine.fun/",
                "image": "https://workout.appengine.fun/images/app_icon.png",
                "screenshot": [
                    "https://workout.appengine.fun/images/shot_timer.png",
                    "https://workout.appengine.fun/images/shot_complete.png",
                    "https://workout.appengine.fun/images/shot_settings.png"
                ],
                "description": t["desc"],
                "applicationCategory": "HealthApplication, SportsApplication",
                "operatingSystem": "iOS 17.0+, watchOS 10.0+",
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
                    "ratingCount": "128",
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
    
    # Feature cards HTML
    features_html = ""
    for f in t["features"]:
        features_html += f"""
        <div class="feature-card">
          <div class="feature-icon">{f['icon']}</div>
          <h3>{f['title']}</h3>
          <p>{f['desc']}</p>
        </div>"""

    # FAQ accordion HTML
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

    # Hero pills HTML
    pills_html = "".join([f'<div class="pill">{p}</div>' for p in t["pills"]])

    # Gallery images
    shot1 = "/images/shot_zh_1.png" if "zh" in lang_code else "/images/shot_timer.png"
    shot2 = "/images/shot_zh_coach.png" if "zh" in lang_code else "/images/shot_complete.png"

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
  <meta property="og:image:alt" content="Workout Timer: Voice Coach app preview banner">

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
      --bg-dark: #000000;
      --card-bg: #121216;
      --card-border: rgba(255, 255, 255, 0.08);
      --text-main: #FFFFFF;
      --text-muted: #8E8E93;
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
    }}
    /* Header / Nav */
    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(0, 0, 0, 0.85);
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
      width: 38px;
      height: 38px;
      border-radius: 9px;
      box-shadow: 0 4px 12px rgba(48, 209, 88, 0.3);
    }}
    .brand-title {{
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }}
    .nav-right {{
      display: flex;
      align-items: center;
      gap: 16px;
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
      border-radius: 99px;
      padding: 4px 10px;
      font-size: 13px;
      font-weight: 700;
      gap: 6px;
    }}
    .lang-picker a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .lang-picker a.active {{
      color: var(--primary-green);
    }}
    @media (max-width: 768px) {{
      .nav-links {{
        display: none;
      }}
    }}

    /* Hero */
    .hero {{
      text-align: center;
      padding: 60px 20px 40px;
      max-width: 900px;
      margin: 0 auto;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(48, 209, 88, 0.12);
      color: var(--primary-green);
      padding: 6px 16px;
      border-radius: 99px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 24px;
      border: 1px solid rgba(48, 209, 88, 0.28);
    }}
    h1 {{
      font-size: clamp(34px, 5.5vw, 62px);
      font-weight: 900;
      letter-spacing: -1.5px;
      line-height: 1.12;
      margin-bottom: 20px;
    }}
    h1 span {{
      background: linear-gradient(135deg, #30D158 0%, #FF9F0A 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      font-size: clamp(16px, 2.2vw, 20px);
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 28px;
    }}
    .pills-container {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 36px;
    }}
    .pill {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 99px;
      padding: 8px 16px;
      font-size: 13px;
      font-weight: 700;
      color: #fff;
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
      box-shadow: 0 10px 30px rgba(48, 209, 88, 0.45);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .cta-btn:hover, .cta-btn:active {{
      transform: scale(0.98);
      box-shadow: 0 14px 40px rgba(48, 209, 88, 0.65);
    }}
    .cta-apple-icon {{
      font-size: 22px;
    }}
    .cta-group {{
      display: inline-flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin-bottom: 4px;
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
      border: 1px solid rgba(255, 255, 255, 0.16);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: background 0.2s, transform 0.2s, border-color 0.2s;
    }}
    .cta-video-btn:hover, .cta-video-btn:active {{
      background: rgba(255, 255, 255, 0.16);
      border-color: rgba(255, 255, 255, 0.35);
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
      margin-top: 12px;
    }}

    /* Gallery Showcase */
    .gallery-container {{
      position: relative;
      width: 100%;
      margin: 30px auto 60px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .gallery {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 20px;
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
      flex: 0 0 220px;
      width: 220px;
      max-width: 220px;
      scroll-snap-align: center;
      background: #111;
      border-radius: 32px;
      padding: 8px;
      border: 3px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
      transition: transform 0.3s;
    }}
    .device-frame:hover {{
      transform: translateY(-6px);
    }}
    .device-frame img {{
      width: 100%;
      height: auto;
      border-radius: 26px;
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
      margin: 20px auto 60px;
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
      border-radius: 20px;
      overflow: hidden;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
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
      max-width: 920px;
      z-index: 2;
      transform: scale(0.95);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .video-modal.active .video-modal-dialog {{
      transform: scale(1);
    }}
    .video-modal-close {{
      position: absolute;
      top: -46px;
      right: 0;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      width: 36px;
      height: 36px;
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
      padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
      height: 0;
      border-radius: 18px;
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

    /* Features Grid (Bento Style) */
    .features {{
      max-width: 1160px;
      margin: 0 auto;
      padding: 40px 20px;
    }}
    .section-title {{
      text-align: center;
      margin-bottom: 48px;
    }}
    .section-title h2 {{
      font-size: clamp(28px, 4vw, 42px);
      font-weight: 900;
      letter-spacing: -1px;
      margin-bottom: 12px;
    }}
    .section-title p {{
      color: var(--text-muted);
      font-size: 17px;
    }}
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
    }}
    .feature-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 28px 24px;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .feature-card:hover {{
      border-color: rgba(48, 209, 88, 0.4);
      transform: translateY(-3px);
    }}
    .feature-icon {{
      font-size: 32px;
      margin-bottom: 16px;
    }}
    .feature-card h3 {{
      font-size: 19px;
      font-weight: 800;
      margin-bottom: 10px;
      letter-spacing: -0.3px;
    }}
    .feature-card p {{
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.55;
    }}

    /* Coaches Section */
    .coaches-section {{
      max-width: 1160px;
      margin: 40px auto;
      padding: 40px 20px;
    }}
    .coaches-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
    }}
    .coach-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 24px;
      text-align: center;
      transition: transform 0.2s, border-color 0.2s;
    }}
    .coach-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(255, 159, 10, 0.4);
    }}
    .coach-avatar {{
      width: 255px;
      height: auto;
      aspect-ratio: 1 / 1;
      max-width: 100%;
      border-radius: 50%;
      object-fit: cover;
      display: block;
      margin: 0 auto 16px;
      border: 2px solid rgba(255, 255, 255, 0.15);
    }}
    .coach-info h4 {{
      font-size: 17px;
      font-weight: 800;
      margin-bottom: 6px;
    }}
    .coach-info p {{
      font-size: 13px;
      color: var(--text-muted);
    }}

    /* FAQ Section */
    .faq-section {{
      max-width: 800px;
      margin: 40px auto;
      padding: 40px 20px;
    }}
    .faq-item {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      margin-bottom: 14px;
      overflow: hidden;
      transition: border-color 0.2s;
    }}
    .faq-item:hover, .faq-item[open] {{
      border-color: rgba(48, 209, 88, 0.4);
    }}
    .faq-question {{
      padding: 20px 24px;
      font-size: 17px;
      font-weight: 700;
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
      color: var(--primary-green);
      font-size: 12px;
      transition: transform 0.2s;
    }}
    .faq-item[open] .faq-arrow {{
      transform: rotate(180deg);
    }}
    .faq-answer {{
      padding: 0 24px 20px;
      color: var(--text-muted);
      font-size: 15px;
      line-height: 1.6;
    }}

    /* Support Section */
    .support-section {{
      text-align: center;
      max-width: 680px;
      margin: 60px auto;
      padding: 0 20px;
    }}
    .support-section h2 {{
      font-size: 28px;
      font-weight: 800;
      margin-bottom: 12px;
    }}
    .support-section p {{
      color: var(--text-muted);
      font-size: 16px;
      margin-bottom: 24px;
    }}
    .support-email {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--primary-green);
      padding: 14px 28px;
      border-radius: 99px;
      font-size: 16px;
      font-weight: 700;
      text-decoration: none;
      transition: background 0.2s, border-color 0.2s;
    }}
    .support-email:hover {{
      background: rgba(48, 209, 88, 0.15);
      border-color: var(--primary-green);
    }}

    /* Footer */
    footer {{
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 40px 20px 140px;
      text-align: center;
      color: var(--text-muted);
      font-size: 14px;
    }}
    .footer-brand {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      margin-bottom: 16px;
    }}
    .footer-logo {{
      height: 85px;
      opacity: 0.85;
    }}
    .footer-tagline {{
      font-size: 13px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: rgba(255, 255, 255, 0.4);
    }}
    footer a {{
      color: var(--primary-green);
      text-decoration: none;
      font-weight: 600;
    }}
    footer a:hover {{
      text-decoration: underline;
    }}

    /* Reveal Animation */
    .reveal {{
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .reveal.active {{
      opacity: 1;
      transform: translateY(0);
    }}
    
    /* Social Proof */
    .social-proof-section {{
      max-width: 1000px;
      margin: 0 auto 80px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
    }}
    .review-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 24px;
      border-radius: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .review-card .stars {{
      color: var(--primary-orange);
      font-size: 20px;
      letter-spacing: 2px;
    }}
    .review-card p {{
      font-size: 16px;
      font-style: italic;
      color: #FFF;
      flex-grow: 1;
    }}
    .review-card .reviewer {{
      font-size: 14px;
      color: var(--text-muted);
      font-weight: 500;
    }}
    
    /* Sticky CTA */
    .sticky-cta {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translate(-50%, 150px);
      background: var(--primary-green);
      color: #000;
      padding: 14px 32px;
      border-radius: 40px;
      font-weight: 700;
      font-size: 16px;
      text-decoration: none;
      box-shadow: 0 10px 30px rgba(48, 209, 88, 0.4);
      opacity: 0;
      transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 10px;
      white-space: nowrap;
      pointer-events: none;
    }}
    .sticky-cta.visible {{
      transform: translate(-50%, 0);
      opacity: 1;
      pointer-events: auto;
    }}
    .sticky-cta:hover {{
      transform: translate(-50%, -3px) scale(1.02);
      box-shadow: 0 12px 36px rgba(48, 209, 88, 0.5);
    }}


    .coach-info {{
      position: relative;
    }}
    .coach-avatar-wrapper {{
      position: relative;
      display: inline-block;
      margin-bottom: 16px;
    }}
    .play-audio-btn {{
      position: absolute;
      bottom: 0px;
      right: 0px;
      background: var(--primary-green);
      color: #000;
      border: 2px solid #1c1c1e;
      border-radius: 50%;
      width: 34px;
      height: 34px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 14px;
      padding-left: 2px;
      transition: transform 0.2s, background 0.3s;
      z-index: 2;
    }}
    .play-audio-btn:hover {{
      transform: scale(1.1);
    }}
    .play-audio-btn.playing {{
      background: var(--primary-orange);
      animation: pulse 1s infinite;
    }}


    /* Horizontal Carousel for Coaches on Mobile */
    @media (max-width: 768px) {{
      .coaches-grid {{
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
        gap: 16px;
        padding-bottom: 24px;
        scrollbar-width: none; /* Firefox */
      }}
      .coaches-grid::-webkit-scrollbar {{
        display: none; /* Safari and Chrome */
      }}
      .coach-card {{
        flex: 0 0 70%;
        max-width: 280px;
        padding: 20px; /* Slightly reduced padding to maximize photo space */
        scroll-snap-align: center;
      }}
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
          <!-- <a href="#features">{t['nav_features']}</a> -->
          <a href="#coaches">{t['nav_coaches']}</a>
          <a href="#faq">{t['nav_faq']}</a>
          <a href="#support">{t['nav_support']}</a>
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

  <!-- App Showcase Gallery -->
  <div class="gallery-container">
    <div class="gallery">
      <div class="device-frame">
        <img src="{shot1}" alt="Workout Timer Countdown Display" loading="eager">
      </div>
      <div class="device-frame">
        <img src="{shot2}" alt="Workout Complete Coach Celebration Video" loading="lazy">
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

  <!-- Features Bento Grid (Temporarily Removed) -->
  <!--
  <section class="features" id="features">
    <div class="section-title">
      <h2>{t['sec_features_title']}</h2>
      <p>{t['sec_features_sub']}</p>
    </div>
    <div class="features-grid">
      {features_html}
    </div>
  </section>
  -->

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
      <div class="reviewer">- App Store User</div>
    </div>
    <div class="review-card" style="transition-delay: 0.1s;">
      <div class="stars">★★★★★</div>
      <p>"{t['review_2']}"</p>
      <div class="reviewer">- Fitness Pro</div>
    </div>
    <div class="review-card" style="transition-delay: 0.2s;">
      <div class="stars">★★★★★</div>
      <p>"{t['review_3']}"</p>
      <div class="reviewer">- HIIT Lover</div>
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
    <p style="margin-top: 12px;">
      <a href="/privacy?lang={lang_code}">{t['nav_privacy']}</a> • 
      <a href="#support">{t['nav_support']}</a> • 
      <a href="https://www.youtube.com/@appengine-a" target="_blank" rel="noopener noreferrer">YouTube</a> • 
      <a href="https://reviewcloud.net" target="_blank" rel="noopener noreferrer">ReviewCloud</a> • 
      <a href="https://appengine.fun" target="_blank" rel="noopener noreferrer">AE Interactive</a>
    </p>
    <p style="font-size: 11px; color: rgba(255, 255, 255, 0.3); margin-top: 24px; font-family: monospace; letter-spacing: 0.5px;">Build: {build_version_info}</p>
  </footer>


  <!-- Scripts -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      // Reveal Animations
      const reveals = document.querySelectorAll(".feature-card, .coach-card, .review-card, .section-title, .faq-item");
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
      

      // Audio Playback Logic
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
          
          if (currentAudio) {{
            currentAudio.pause();
            currentAudio.currentTime = 0;
            if (currentBtn) currentBtn.classList.remove('playing');
            if (currentBtn === this) {{
              // Pause if clicking the same button
              currentAudio = null;
              currentBtn = null;
              this.innerHTML = '▶';
              return;
            }} else {{
              currentBtn.innerHTML = '▶';
            }}
          }}
          
          currentAudio = new Audio(coachAudio[coach]);
          currentBtn = this;
          
          this.classList.add('playing');
          this.innerHTML = '⏸';
          
          currentAudio.play();
          
          currentAudio.onended = () => {{
            this.classList.remove('playing');
            this.innerHTML = '▶';
            currentAudio = null;
            currentBtn = null;
          }};
        }});
      }});

      // Sticky CTA Logic
      const stickyCta = document.getElementById('stickyCta');
      const hero = document.querySelector('.hero');
      window.addEventListener('scroll', () => {{
        if (window.scrollY > hero.offsetHeight) {{
          stickyCta.classList.add('visible');
        }} else {{
          stickyCta.classList.remove('visible');
        }}
      }});

      // Video Cinema Lightbox Modal Logic
      const videoModal = document.getElementById('videoModal');
      const videoModalBackdrop = document.getElementById('videoModalBackdrop');
      const videoModalClose = document.getElementById('videoModalClose');
      const videoModalIframe = document.getElementById('videoModalIframe');
      const youtubeEmbedUrl = "https://www.youtube-nocookie.com/embed/w05YC97VSYc?autoplay=1&rel=0";

      function openVideoModal(e) {{
        if (e) e.preventDefault();
        if (videoModal && videoModalIframe) {{
          videoModalIframe.src = youtubeEmbedUrl;
          videoModal.classList.add('active');
          videoModal.setAttribute('aria-hidden', 'false');
          document.body.style.overflow = 'hidden';
          if (currentAudio) {{
            currentAudio.pause();
            if (currentBtn) {{
              currentBtn.classList.remove('playing');
              currentBtn.innerHTML = '▶';
            }}
          }}
        }}
      }}

      function closeVideoModal() {{
        if (videoModal && videoModalIframe) {{
          videoModal.classList.remove('active');
          videoModal.setAttribute('aria-hidden', 'true');
          videoModalIframe.src = '';
          document.body.style.overflow = '';
        }}
      }}

      document.querySelectorAll('.cta-video-btn, [data-video-open]').forEach(btn => {{
        btn.addEventListener('click', openVideoModal);
      }});

      if (videoModalClose) {{
        videoModalClose.addEventListener('click', closeVideoModal);
      }}
      if (videoModalBackdrop) {{
        videoModalBackdrop.addEventListener('click', closeVideoModal);
      }}
      document.addEventListener('keydown', function(e) {{
        if (e.key === 'Escape' && videoModal && videoModal.classList.contains('active')) {{
          closeVideoModal();
        }}
      }});
    }});
  </script>

  <!-- Video Cinema Modal -->
  <div id="videoModal" class="video-modal" aria-hidden="true" role="dialog">
    <div class="video-modal-backdrop" id="videoModalBackdrop"></div>
    <div class="video-modal-dialog">
      <button class="video-modal-close" id="videoModalClose" aria-label="Close Video">✕</button>
      <div class="video-modal-player-wrap">
        <iframe id="videoModalIframe" src="" title="Workout Timer App Showcase" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</body>
</html>
"""

def generate_privacy(lang_code):
    is_zh = "zh" in lang_code
    is_es = lang_code == "es"
    
    title = "隱私權政策 (Privacy Policy)" if "Hant" in lang_code else ("隐私政策 (Privacy Policy)" if is_zh else ("Política de Privacidad" if is_es else "Privacy Policy"))
    back_text = "返回首頁" if is_zh else ("Volver al inicio" if is_es else "Back to Workout Timer")
    updated_text = "最後更新日期：2026年9月17日" if is_zh else ("Última actualización: 17 de septiembre de 2026" if is_es else "Last updated: September 17, 2026")
    
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

    /* Reveal Animation */
    .reveal {{
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .reveal.active {{
      opacity: 1;
      transform: translateY(0);
    }}
    
    /* Social Proof */
    .social-proof-section {{
      max-width: 1000px;
      margin: 0 auto 80px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
    }}
    .review-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 24px;
      border-radius: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .review-card .stars {{
      color: var(--primary-orange);
      font-size: 20px;
      letter-spacing: 2px;
    }}
    .review-card p {{
      font-size: 16px;
      font-style: italic;
      color: #FFF;
      flex-grow: 1;
    }}
    .review-card .reviewer {{
      font-size: 14px;
      color: var(--text-muted);
      font-weight: 500;
    }}
    
    /* Sticky CTA */
    .sticky-cta {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translate(-50%, 150px);
      background: var(--primary-green);
      color: #000;
      padding: 14px 32px;
      border-radius: 40px;
      font-weight: 700;
      font-size: 16px;
      text-decoration: none;
      box-shadow: 0 10px 30px rgba(48, 209, 88, 0.4);
      opacity: 0;
      transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 10px;
      white-space: nowrap;
      pointer-events: none;
    }}
    .sticky-cta.visible {{
      transform: translate(-50%, 0);
      opacity: 1;
      pointer-events: auto;
    }}
    .sticky-cta:hover {{
      transform: translate(-50%, -3px) scale(1.02);
      box-shadow: 0 12px 36px rgba(48, 209, 88, 0.5);
    }}


    .coach-info {{
      position: relative;
    }}
    .coach-avatar-wrapper {{
      position: relative;
      display: inline-block;
      margin-bottom: 16px;
    }}
    .play-audio-btn {{
      position: absolute;
      bottom: 0px;
      right: 0px;
      background: var(--primary-green);
      color: #000;
      border: 2px solid #1c1c1e;
      border-radius: 50%;
      width: 34px;
      height: 34px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 14px;
      padding-left: 2px;
      transition: transform 0.2s, background 0.3s;
      z-index: 2;
    }}
    .play-audio-btn:hover {{
      transform: scale(1.1);
    }}
    .play-audio-btn.playing {{
      background: var(--primary-orange);
      animation: pulse 1s infinite;
    }}


    /* Horizontal Carousel for Coaches on Mobile */
    @media (max-width: 768px) {{
      .coaches-grid {{
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
        gap: 16px;
        padding-bottom: 24px;
        scrollbar-width: none; /* Firefox */
      }}
      .coaches-grid::-webkit-scrollbar {{
        display: none; /* Safari and Chrome */
      }}
      .coach-card {{
        flex: 0 0 70%;
        max-width: 280px;
        padding: 20px; /* Slightly reduced padding to maximize photo space */
        scroll-snap-align: center;
      }}
    }}

  </style>
</head>
<body>
  <a href="/?lang={lang_code}" class="back-btn">&larr; {back_text}</a>
  <h1>{title}</h1>
  <p>{updated_text}</p>

  <h2>1. Overview / 概述</h2>
  <p>Workout Timer ("we", "our", or "the app") values your personal privacy. Our core philosophy is simple: your workout routines, personal health timing, and usage habits are strictly your own business.</p>

  <h2>2. Data Collection & HealthKit / 數據收集與健康隱私</h2>
  <p>Workout Timer does NOT collect, transmit, store on remote servers, or sell any personally identifiable information (PII) or health data. Apple HealthKit and Apple Watch heart rate / calorie data are read locally on-device in real-time solely to display on your workout screen, and are never transmitted over the network.</p>

  <h2>3. Network Communication / 網絡傳輸</h2>
  <p>The app operates 100% offline. No telemetry, third-party advertising SDKs, crash analytics, or user tracking libraries are bundled within the app.</p>

  <h2>4. Audio & Media Permissions / 音頻權限</h2>
  <p>The app utilizes local audio playback capabilities to deliver studio voice coach announcements and sound effects. It does not record audio, access your microphone, or inspect your private media libraries.</p>

  <h2>5. Contact Us / 聯繫我們</h2>
  <p>If you have any questions about this Privacy Policy, you may contact us at: <a href="mailto:help@appengine.fun">help@appengine.fun</a></p>

  <!-- Scripts -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      // Reveal Animations
      const reveals = document.querySelectorAll(".feature-card, .coach-card, .review-card, .section-title, .faq-item");
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
      

      // Audio Playback Logic
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
          
          if (currentAudio) {{
            currentAudio.pause();
            currentAudio.currentTime = 0;
            if (currentBtn) currentBtn.classList.remove('playing');
            if (currentBtn === this) {{
              // Pause if clicking the same button
              currentAudio = null;
              currentBtn = null;
              this.innerHTML = '▶';
              return;
            }} else {{
              currentBtn.innerHTML = '▶';
            }}
          }}
          
          currentAudio = new Audio(coachAudio[coach]);
          currentBtn = this;
          
          this.classList.add('playing');
          this.innerHTML = '⏸';
          
          currentAudio.play();
          
          currentAudio.onended = () => {{
            this.classList.remove('playing');
            this.innerHTML = '▶';
            currentAudio = null;
            currentBtn = null;
          }};
        }});
      }});

      // Sticky CTA Logic
      const stickyCta = document.getElementById('stickyCta');
      const hero = document.querySelector('.hero');
      window.addEventListener('scroll', () => {{
        if (window.scrollY > hero.offsetHeight) {{
          stickyCta.classList.add('visible');
        }} else {{
          stickyCta.classList.remove('visible');
        }}
      }});
    }});
  </script>
</body>
</html>
"""

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
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1JL7EP8YTN"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-1JL7EP8YTN');
</script>"""

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

worker_js = f"""
const PAGES = {json.dumps(pages)};
const PRIVACY_PAGES = {json.dumps(privacy_pages)};
const IMAGES = {json.dumps(images_dict)};
const SITEMAP_XML = {json.dumps(sitemap_xml)};
const ROBOTS_TXT = {json.dumps(robots_txt)};

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
        return new Response(bytes, {{
          headers: {{
            "content-type": "image/png",
            "cache-control": "public, max-age=31536000, immutable"
          }}
        }});
      }}
      return new Response("Image Not Found", {{ status: 404 }});
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
    "compatibility_date": "2024-03-03"
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
        "-F", 'metadata={"main_module": "index.js", "compatibility_date": "2024-03-03"};type=application/json',
        "-F", f'index.js=@{out_worker};filename="index.js";type=application/javascript+module'
    ]
    res = subprocess.run(curl_cmd, capture_output=True, text=True)
    print("Curl deploy output:", res.stdout)

