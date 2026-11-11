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

# Load all images dynamically for /images/* route
images_dict = {}
if os.path.exists(img_dir):
    for fname in sorted(os.listdir(img_dir)):
        if fname.startswith('.') or not (fname.endswith('.png') or fname.endswith('.webp') or fname.endswith('.jpg') or fname.endswith('.jpeg')):
            continue
        p = os.path.join(img_dir, fname)
        with open(p, "rb") as f:
            images_dict[fname] = base64.b64encode(f.read()).decode("utf-8")

print(f"Loaded {len(images_dict)} images for Worker bundle.")

# Load official 7 programs from workouts_catalog.json
catalog_path = os.path.join(base_dir, "public", "api", "workouts_catalog.json")
if os.path.exists(catalog_path):
    with open(catalog_path, "r", encoding="utf-8") as f:
        workouts_catalog_raw = f.read()
        catalog_data = json.loads(workouts_catalog_raw)
else:
    workouts_catalog_raw = '{"version": 1, "items": []}'
    catalog_data = {"items": []}

coach_images = [
    "/images/coach_01_sofia.webp",
    "/images/coach_02_hannah.webp",
    "/images/coach_03_chloe.webp",
    "/images/coach_04_elena.webp",
    "/images/coach_05_marcus.webp",
    "/images/coach_06_ryan.webp",
    "/images/coach_07_rossi.webp"
]

PROMIES_URL = "https://www.promies.net/promotion/7b5a2e4b-ced3-4f45-8519-4fa5e98c0c13"
APP_STORE_URL = "https://apps.apple.com/app/id6811742209"

translations = {
    "en": {
        "title": "Workout Timer: Zero-Ad HIIT Interval Timer & Studio Voice Coach",
        "desc": "Zero-ad interval timer with studio voice coaches in 4 languages, 7 guided HD coach programs, Apple Watch & Apple TV sync, and 100% offline privacy.",
        "keywords": "workout timer, interval timer, hiit timer, tabata timer, voice coach, apple watch workout, apple tv workout, boxing timer, gym clock",
        "brand_name": "Workout Timer",
        "nav_privacy": "Privacy",
        "nav_support": "Support",
        "hero_badge": "ZERO ADS • 7 HD COACH PROGRAMS • UNIVERSAL APP",
        "hero_title": "Zero-Clutter Interval Timer & <span>AI Voice Coach</span>",
        "hero_sub": "Instant Tabata, HIIT, and Boxing timers paired with 7 studio-guided video programs across iPhone, iPad, Apple Watch, and Apple TV.",
        "cta_app_store": "Download on the App Store",
        "promo_badge": "🎁 FREE UNLOCK",
        "promo_text": "Claim a free promo code for guided coach classes",
        "promo_cta": "Claim on Promies →",
        "vid_tab_1": "🎬 Official Demo",
        "vid_tab_2": "🔥 Coach Hannah",
        "vid_tab_3": "🩺 Dr. Elena",
        "sec_programs_badge": "7 GUIDED VIDEO PROGRAMS",
        "sec_programs_title": "Train with 7 Studio Coaches",
        "sec_programs_sub": "Swipe through all 7 HD video programs with automatic UP NEXT rest previews.",
        "swipe_hint": "Swipe to explore all 7 programs →",
        "footer_rights": "© 2026 Workout Timer. An AE Interactive Production."
    },
    "zh-Hant": {
        "title": "間歇計時器 (Workout Timer) - 零廣告 HIIT / Tabata 語音教練",
        "desc": "零廣告高強度間歇計時器！內建 4 國語言真人語音教練、7 大高清帶練課表，支援 iPhone、iPad、Apple Watch 與 Apple TV。",
        "keywords": "間歇計時器, Tabata計時器, HIIT訓練計時, 語音教練, 健身房計時器, Apple Watch健身, Apple TV健身",
        "brand_name": "間歇計時器",
        "nav_privacy": "隱私權政策",
        "nav_support": "聯繫支援",
        "hero_badge": "零廣告干擾 • 7 大高清教練課表 • 全平台通用",
        "hero_title": "極簡專業間歇計時 & <span>真人語音教練</span>",
        "hero_sub": "秒開 Tabata、HIIT 與拳擊回合，搭配 7 大專業教練高清循環動作示範，完整支援 iPhone、Apple Watch 與 Apple TV。",
        "cta_app_store": "App Store 免費下載",
        "promo_badge": "🎁 限時免費解鎖",
        "promo_text": "領取免費教練課程兌換碼",
        "promo_cta": "前往領取 →",
        "vid_tab_1": "🎬 官方實機展示",
        "vid_tab_2": "🔥 Hannah 教練",
        "vid_tab_3": "🩺 Dr. Elena 博士",
        "sec_programs_badge": "7 大高清帶練課表",
        "sec_programs_title": "7 位專業教練全程帶練",
        "sec_programs_sub": "左右滑動瀏覽 7 大高清動作課表，休息期間自動預覽下一動。",
        "swipe_hint": "左右滑動瀏覽 7 大課表 →",
        "footer_rights": "© 2026 Workout Timer. AE Interactive 原創出品。"
    },
    "zh-Hans": {
        "title": "间歇计时器 (Workout Timer) - 零广告 HIIT / Tabata 语音教练",
        "desc": "零广告高强度间歇计时器！内置 4 国语言真人语音教练、7 大高清跟练课表，支持 iPhone、iPad、Apple Watch 与 Apple TV。",
        "keywords": "间歇计时器, Tabata计时器, HIIT训练计时, 语音教练, 健身房计时器, Apple Watch健身, Apple TV健身",
        "brand_name": "间歇计时器",
        "nav_privacy": "隐私政策",
        "nav_support": "联系支持",
        "hero_badge": "零广告干扰 • 7 大高清教练课表 • 全平台通用",
        "hero_title": "极简专业间歇计时 & <span>真人语音教练</span>",
        "hero_sub": "秒开 Tabata、HIIT 与拳击回合，搭配 7 大专业教练高清循环动作示范，完整支持 iPhone、Apple Watch 与 Apple TV。",
        "cta_app_store": "App Store 免费下载",
        "promo_badge": "🎁 限时免费解锁",
        "promo_text": "领取免费教练课程兑换码",
        "promo_cta": "前往领取 →",
        "vid_tab_1": "🎬 官方实机展示",
        "vid_tab_2": "🔥 Hannah 教练",
        "vid_tab_3": "🩺 Dr. Elena 博士",
        "sec_programs_badge": "7 大高清跟练课表",
        "sec_programs_title": "7 位专业教练全程跟练",
        "sec_programs_sub": "左右滑动浏览 7 大高清动作课表，休息期间自动预览下一动。",
        "swipe_hint": "左右滑动浏览 7 大课表 →",
        "footer_rights": "© 2026 Workout Timer. AE Interactive 原创出品。"
    },
    "es": {
        "title": "Workout Timer: Cronómetro HIIT Sin Anuncios y Entrenador de Voz",
        "desc": "Cronómetro de intervalos sin anuncios con entrenadores de voz en 4 idiomas, 7 programas guiados en video HD y sincronización con Apple Watch y Apple TV.",
        "keywords": "workout timer, cronometro hiit, tabata timer, entrenador de voz, apple watch fitness, apple tv workout",
        "brand_name": "Workout Timer",
        "nav_privacy": "Privacidad",
        "nav_support": "Soporte",
        "hero_badge": "SIN ANUNCIOS • 7 PROGRAMAS HD • COMPRA UNIVERSAL",
        "hero_title": "Cronómetro HIIT Minimalista y <span>Entrenador de Voz</span>",
        "hero_sub": "Temporizadores instantáneos para Tabata, HIIT y Boxeo con 7 programas guiados en video HD para iPhone, iPad, Apple Watch y Apple TV.",
        "cta_app_store": "Descargar en App Store",
        "promo_badge": "🎁 CÓDIGO GRATIS",
        "promo_text": "Obtén un código promocional gratis para las clases",
        "promo_cta": "Reclamar código →",
        "vid_tab_1": "🎬 Demo Oficial",
        "vid_tab_2": "🔥 Coach Hannah",
        "vid_tab_3": "🩺 Dra. Elena",
        "sec_programs_badge": "7 PROGRAMAS GUIADOS EN HD",
        "sec_programs_title": "Entrena con 7 Coaches de Estudio",
        "sec_programs_sub": "Desliza para explorar los 7 programas con vista previa automática del siguiente ejercicio.",
        "swipe_hint": "Desliza para ver los 7 programas →",
        "footer_rights": "© 2026 Workout Timer. Una producción de AE Interactive."
    }
}

def generate_schema_json(lang_code):
    t = translations[lang_code]
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
                "description": t["desc"],
                "applicationCategory": "HealthApplication, SportsApplication",
                "operatingSystem": "iOS 17.0+, iPadOS 17.0+, watchOS 10.0+, tvOS 17.0+",
                "downloadUrl": APP_STORE_URL,
                "installUrl": APP_STORE_URL,
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock"
                }
            }
        ]
    }
    return json.dumps(schema_graph, ensure_ascii=False)

def generate_page(lang_code):
    t = translations[lang_code]
    schema_json = generate_schema_json(lang_code)

    # Build 7 Coach Program Cards from official catalog
    programs_html = ""
    items = catalog_data.get("items", [])
    for idx, item in enumerate(items):
        badge_num = f"#{idx+1:02d}"
        coach_img = coach_images[idx] if idx < len(coach_images) else "/images/app_icon.png"
        prog_title = item.get("localizedNames", {}).get(lang_code) or item.get("localizedNames", {}).get("en", "")
        prog_sub = item.get("localizedSubtitles", {}).get(lang_code) or item.get("localizedSubtitles", {}).get("en", "")
        coach_name = item.get("coachName", "")
        coach_role = item.get("coachTitle", {}).get(lang_code) or item.get("coachTitle", {}).get("en", "")
        coach_bio = item.get("coachBio", {}).get(lang_code) or item.get("coachBio", {}).get("en", "")

        programs_html += f"""
        <article class="program-card">
          <div class="program-card-top">
            <img src="{coach_img}" alt="{coach_name}" class="coach-portrait" width="64" height="64" loading="lazy">
            <div class="program-head-info">
              <span class="program-num">{badge_num} • {coach_name}</span>
              <h3 class="program-title">{prog_title}</h3>
              <div class="coach-role">{coach_role}</div>
            </div>
          </div>
          <div class="program-interval-pill">⏱️ {prog_sub}</div>
          <p class="program-bio">{coach_bio}</p>
        </article>"""

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
  <meta name="theme-color" content="#05060A">
  <meta name="apple-itunes-app" content="app-id=6811742209">

  <link rel="canonical" href="https://workout.appengine.fun/?lang={lang_code}">
  <link rel="alternate" hreflang="en" href="https://workout.appengine.fun/?lang=en">
  <link rel="alternate" hreflang="zh-Hant" href="https://workout.appengine.fun/?lang=zh-Hant">
  <link rel="alternate" hreflang="zh-Hans" href="https://workout.appengine.fun/?lang=zh-Hans">
  <link rel="alternate" hreflang="es" href="https://workout.appengine.fun/?lang=es">
  <link rel="alternate" hreflang="x-default" href="https://workout.appengine.fun/">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{t['brand_name']}">
  <meta property="og:url" content="https://workout.appengine.fun/?lang={lang_code}">
  <meta property="og:title" content="{t['title']}">
  <meta property="og:description" content="{t['desc']}">
  <meta property="og:image" content="https://workout.appengine.fun/images/og_preview.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t['title']}">
  <meta name="twitter:description" content="{t['desc']}">
  <meta name="twitter:image" content="https://workout.appengine.fun/images/og_preview.png">

  <link rel="icon" type="image/png" href="/images/app_icon.png">
  <link rel="apple-touch-icon" href="/images/app_icon.png">

  <script type="application/ld+json">
  {schema_json}
  </script>

  <style>
    :root {{
      --green: #30D158;
      --orange: #FF9F0A;
      --cyan: #64D2FF;
      --bg: #05060A;
      --card: rgba(20, 22, 30, 0.88);
      --border: rgba(255, 255, 255, 0.1);
      --text: #F5F7FA;
      --muted: #9498A6;
    }}
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, sans-serif;
    }}
    body {{
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      overflow-x: hidden;
      background-image:
        radial-gradient(ellipse 85% 40% at 50% 0%, rgba(48, 209, 88, 0.16) 0%, transparent 70%),
        radial-gradient(circle at 85% 20%, rgba(100, 210, 255, 0.1) 0%, transparent 45%);
      background-repeat: no-repeat;
    }}

    /* 1. Compact Header */
    header {{
      position: sticky;
      top: 10px;
      z-index: 100;
      padding: 0 14px;
    }}
    nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 9px 14px;
      max-width: 920px;
      margin: 0 auto;
      background: rgba(12, 14, 20, 0.82);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border);
      border-radius: 999px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #fff;
    }}
    .brand img {{
      width: 32px;
      height: 32px;
      border-radius: 8px;
      border: 1px solid rgba(48, 209, 88, 0.4);
    }}
    .brand-title {{
      font-size: 16px;
      font-weight: 800;
      letter-spacing: -0.3px;
    }}
    .lang-picker {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      padding: 5px 11px;
      border-radius: 99px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .lang-picker a {{
      color: var(--muted);
      text-decoration: none;
      padding: 2px 3px;
    }}
    .lang-picker a.active {{
      color: var(--green);
    }}
    .lang-sep {{
      color: rgba(255, 255, 255, 0.2);
      font-size: 10px;
    }}

    /* 2. Section 1: Hero + Single Video Player */
    .hero {{
      max-width: 860px;
      margin: 0 auto;
      padding: 28px 16px 36px;
      text-align: center;
    }}
    .hero-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.7px;
      color: var(--green);
      background: rgba(48, 209, 88, 0.12);
      border: 1px solid rgba(48, 209, 88, 0.35);
      padding: 5px 14px;
      border-radius: 99px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: clamp(28px, 6vw, 52px);
      font-weight: 900;
      letter-spacing: -1.2px;
      line-height: 1.1;
      margin-bottom: 12px;
      text-wrap: balance;
    }}
    h1 span {{
      background: linear-gradient(135deg, #30D158 0%, #64D2FF 60%, #FF9F0A 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-sub {{
      font-size: clamp(14.5px, 2vw, 17.5px);
      color: var(--muted);
      max-width: 620px;
      margin: 0 auto 20px;
      text-wrap: balance;
    }}
    .hero-actions {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
    }}
    .cta-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, #30D158 0%, #22B345 100%);
      color: #000;
      padding: 14px 32px;
      border-radius: 99px;
      font-size: 16px;
      font-weight: 900;
      text-decoration: none;
      box-shadow: 0 10px 28px rgba(48, 209, 88, 0.4);
      transition: transform 0.2s;
      width: 100%;
      max-width: 320px;
    }}
    .cta-btn:active, .cta-btn:hover {{
      transform: translateY(-1px);
    }}
    .promo-pill {{
      display: inline-flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 99px;
      background: rgba(255, 159, 10, 0.12);
      border: 1px solid rgba(255, 159, 10, 0.4);
      text-decoration: none;
      color: #fff;
      font-size: 13px;
      transition: border-color 0.2s;
    }}
    .promo-pill:hover {{
      border-color: var(--orange);
    }}
    .promo-tag {{
      background: var(--orange);
      color: #000;
      font-size: 10.5px;
      font-weight: 900;
      padding: 2px 8px;
      border-radius: 99px;
    }}
    .promo-cta {{
      color: var(--green);
      font-weight: 800;
    }}

    /* Hero Video Box */
    .video-stage {{
      background: var(--card);
      border: 1px solid rgba(48, 209, 88, 0.28);
      border-radius: 22px;
      padding: 14px;
      box-shadow: 0 20px 55px rgba(0, 0, 0, 0.75);
    }}
    .video-tabs {{
      display: flex;
      justify-content: center;
      gap: 8px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .vid-tab {{
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: var(--text);
      padding: 7px 14px;
      border-radius: 99px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .vid-tab.active {{
      background: var(--green);
      color: #000;
      border-color: var(--green);
      box-shadow: 0 4px 14px rgba(48, 209, 88, 0.35);
    }}
    .video-frame {{
      position: relative;
      width: 100%;
      padding-bottom: 56.25%;
      height: 0;
      border-radius: 14px;
      overflow: hidden;
      background: #000;
    }}
    .video-frame iframe {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }}

    /* 3. Section 2: 7 Coach Programs Carousel */
    .programs-section {{
      max-width: 1060px;
      margin: 12px auto 44px;
      padding: 0 16px;
    }}
    .sec-head {{
      text-align: center;
      margin-bottom: 18px;
    }}
    .sec-head h2 {{
      font-size: clamp(22px, 4vw, 34px);
      font-weight: 900;
      letter-spacing: -0.6px;
      margin-bottom: 6px;
    }}
    .sec-head p {{
      font-size: 14px;
      color: var(--muted);
    }}
    .programs-carousel {{
      display: flex;
      gap: 14px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      padding: 6px 4px 16px;
    }}
    .programs-carousel::-webkit-scrollbar {{
      display: none;
    }}
    .program-card {{
      flex: 0 0 84%;
      max-width: 310px;
      scroll-snap-align: center;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
    }}
    @media (min-width: 680px) {{
      .program-card {{
        flex: 0 0 290px;
        scroll-snap-align: start;
      }}
    }}
    .program-card-top {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .coach-portrait {{
      width: 60px;
      height: 60px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid rgba(48, 209, 88, 0.5);
      flex-shrink: 0;
    }}
    .program-head-info {{
      min-width: 0;
    }}
    .program-num {{
      display: block;
      font-size: 11px;
      font-weight: 800;
      color: var(--green);
      letter-spacing: 0.3px;
    }}
    .program-title {{
      font-size: 17px;
      font-weight: 800;
      line-height: 1.25;
      margin: 2px 0;
    }}
    .coach-role {{
      font-size: 11.5px;
      color: var(--muted);
      line-height: 1.3;
    }}
    .program-interval-pill {{
      font-size: 12px;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(100, 210, 255, 0.1);
      border: 1px solid rgba(100, 210, 255, 0.25);
      padding: 6px 11px;
      border-radius: 10px;
    }}
    .program-bio {{
      font-size: 13px;
      color: var(--muted);
      line-height: 1.45;
    }}
    .swipe-hint {{
      text-align: center;
      font-size: 12px;
      color: var(--muted);
      margin-top: 2px;
    }}

    /* 4. Section 3: Minimal Footer & Sticky Bar */
    footer {{
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 28px 16px 90px;
      text-align: center;
      font-size: 13px;
      color: var(--muted);
    }}
    .footer-links {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 12px;
      font-weight: 600;
    }}
    .footer-links a {{
      color: var(--text);
      text-decoration: none;
    }}
    .footer-links a:hover {{
      color: var(--green);
    }}
    .sticky-cta {{
      position: fixed;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%) translateY(90px);
      opacity: 0;
      pointer-events: none;
      z-index: 99;
      background: var(--green);
      color: #000;
      padding: 12px 26px;
      border-radius: 99px;
      font-size: 14.5px;
      font-weight: 900;
      text-decoration: none;
      box-shadow: 0 10px 28px rgba(48, 209, 88, 0.5);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.25s ease, opacity 0.25s ease;
      white-space: nowrap;
    }}
    .sticky-cta.visible {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
      pointer-events: auto;
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <nav>
      <a href="/?lang={lang_code}" class="brand">
        <img src="/images/app_icon.png" alt="{t['brand_name']}" width="32" height="32">
        <span class="brand-title">{t['brand_name']}</span>
      </a>
      <div class="lang-picker">
        <a href="/?lang=en" class="{'active' if lang_code == 'en' else ''}">EN</a>
        <span class="lang-sep">•</span>
        <a href="/?lang=zh-Hant" class="{'active' if lang_code == 'zh-Hant' else ''}">繁</a>
        <span class="lang-sep">•</span>
        <a href="/?lang=zh-Hans" class="{'active' if lang_code == 'zh-Hans' else ''}">简</a>
        <span class="lang-sep">•</span>
        <a href="/?lang=es" class="{'active' if lang_code == 'es' else ''}">ES</a>
      </div>
    </nav>
  </header>

  <!-- Section 1: Hero + Official Video Player -->
  <main>
    <section class="hero">
      <div class="hero-badge">{t['hero_badge']}</div>
      <h1>{t['hero_title']}</h1>
      <p class="hero-sub">{t['hero_sub']}</p>

      <div class="hero-actions">
        <a href="{APP_STORE_URL}" class="cta-btn" target="_blank" rel="noopener noreferrer">
          <span></span>
          <span>{t['cta_app_store']}</span>
        </a>
        <a href="{PROMIES_URL}" class="promo-pill" target="_blank" rel="noopener noreferrer">
          <span class="promo-tag">{t['promo_badge']}</span>
          <span>{t['promo_text']}</span>
          <span class="promo-cta">{t['promo_cta']}</span>
        </a>
      </div>

      <div class="video-stage">
        <div class="video-tabs" role="tablist">
          <button type="button" class="vid-tab active" data-vid="8v_mNiGaJ1Q">{t['vid_tab_1']}</button>
          <button type="button" class="vid-tab" data-vid="Lr17qfFtyIk">{t['vid_tab_2']}</button>
          <button type="button" class="vid-tab" data-vid="l3AbmjBSlKc">{t['vid_tab_3']}</button>
        </div>
        <div class="video-frame">
          <iframe id="heroVideoIframe"
                  src="https://www.youtube-nocookie.com/embed/8v_mNiGaJ1Q?rel=0&playsinline=1"
                  title="{t['title']}"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  referrerpolicy="strict-origin-when-cross-origin"
                  allowfullscreen></iframe>
        </div>
      </div>
    </section>

    <!-- Section 2: 7 Coach Programs Carousel -->
    <section class="programs-section" id="programs">
      <div class="sec-head">
        <div class="hero-badge">{t['sec_programs_badge']}</div>
        <h2>{t['sec_programs_title']}</h2>
        <p>{t['sec_programs_sub']}</p>
      </div>
      <div class="programs-carousel">
        {programs_html}
      </div>
      <div class="swipe-hint">{t['swipe_hint']}</div>
    </section>
  </main>

  <!-- Section 3: Minimal Footer -->
  <footer>
    <div class="footer-links">
      <a href="mailto:help@appengine.fun?subject=Workout%20Timer%20Support">✉️ {t['nav_support']}: help@appengine.fun</a>
      <a href="/privacy?lang={lang_code}">🔒 {t['nav_privacy']}</a>
      <a href="https://www.youtube.com/watch?v=8v_mNiGaJ1Q" target="_blank" rel="noopener noreferrer">▶ YouTube</a>
    </div>
    <p>{t['footer_rights']}</p>
    <p style="font-size: 11px; opacity: 0.35; margin-top: 8px; font-family: monospace;">Build: {build_version_info}</p>
  </footer>

  <!-- Sticky Bottom Download CTA -->
  <a href="{APP_STORE_URL}" id="stickyCta" class="sticky-cta" target="_blank" rel="noopener noreferrer">
    <span></span>
    <span>{t['cta_app_store']}</span>
  </a>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      // 1. Video Tab Switcher
      const iframe = document.getElementById("heroVideoIframe");
      const tabs = document.querySelectorAll(".vid-tab");
      tabs.forEach(tab => {{
        tab.addEventListener("click", function() {{
          tabs.forEach(t => t.classList.remove("active"));
          this.classList.add("active");
          const vid = this.getAttribute("data-vid");
          if (iframe && vid) {{
            iframe.src = "https://www.youtube-nocookie.com/embed/" + vid + "?rel=0&playsinline=1&autoplay=1";
          }}
        }});
      }});

      // 2. Sticky CTA on Scroll
      const stickyCta = document.getElementById("stickyCta");
      window.addEventListener("scroll", () => {{
        if (window.scrollY > 360) {{
          stickyCta.classList.add("visible");
        }} else {{
          stickyCta.classList.remove("visible");
        }}
      }}, {{ passive: true }});
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
        "cache-control": "public, max-age=0, must-revalidate"
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
    curl_cmd = [
        "curl", "-s", "-X", "PUT", url,
        "-H", f"Authorization: Bearer {token}",
        "-F", 'metadata={"main_module": "index.js", "compatibility_date": "2024-03-03", "bindings": [{"type": "r2_bucket", "name": "ASSETS_BUCKET", "bucket_name": "workouttimer-assets"}]};type=application/json',
        "-F", f'index.js=@{out_worker};filename="index.js";type=application/javascript+module'
    ]
    res = subprocess.run(curl_cmd, capture_output=True, text=True)
    print("Curl deploy output:", res.stdout)
