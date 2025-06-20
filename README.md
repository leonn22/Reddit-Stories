# Reddit Story Video Generator

Turn Reddit stories into vertical, Instagram- or TikTok-ready videos with AI-generated voiceovers and stylish backgrounds.

## 🚀 Features
- Paste a Reddit URL (batch or single)
- Scrapes the post's text
- Text-to-Speech conversion (gTTS or pyttsx3)
- Auto video creation with animated text and a blurred background
- Downloadable .mp4 output

## 🛠 Tech Stack
- Streamlit — UI framework
- gTTS — Google Text-to-Speech
- moviepy — Video generation
- Pillow — Image editing
- BeautifulSoup — Reddit HTML scraping

## 📁 Project Structure
```
reddit_story_app/
├── app.py
├── requirements.txt
├── utils/
│   ├── reddit_scraper.py
│   ├── tts.py
│   └── video_maker.py
└── assets/
    └── backgrounds/
        └── default_bg.jpg
```

## ✅ Setup Instructions
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Deployment
Deploy easily on Streamlit Cloud.

---

Made with ❤️ for the Reddit stories niche.