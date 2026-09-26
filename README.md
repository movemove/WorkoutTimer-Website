# Workout Timer — Marketing & Showcase Website

Official marketing, product showcase, and documentation website for **Workout Timer: Voice Coach**.

🌐 **Live URL**: [https://workout.appengine.fun](https://workout.appengine.fun)

---

## 🌟 Features

- **4 Languages Supported**: English (`/`), Traditional Chinese (`/?lang=zh-Hant`), Simplified Chinese (`/?lang=zh-Hans`), and Spanish (`/?lang=es`).
- **Interactive Audio Previews**: Play studio-recorded sample audio for all 5 coaches (XiaoSu, XiaoSi, Oliver, Adam, Sofia).
- **Embedded Showcase Video & Cinema Lightbox Modal**: Embedded YouTube player with custom frosted-glass dark theater modal.
- **Privacy Policy**: Fully localized zero-data-collection policy.
- **Google Analytics 4 & GTM**: Integrated with `G-1JL7EP8YTN` and `GTM-W7N52ZML`.
- **Cloudflare Worker**: Edge-served single-file worker bundling high-resolution device assets and optimized audio samples.

---

## 🚀 Build & Deployment

To compile the multi-lingual pages and deploy directly to Cloudflare Worker `workouttimer-site`:

```bash
python3 build_multilingual_site.py
```
