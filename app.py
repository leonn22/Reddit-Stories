import streamlit as st
from utils.reddit_scraper import get_reddit_story
from utils.tts import text_to_speech
from utils.video_maker import make_video
import os

st.set_page_config(page_title="Reddit Story Generator", layout="centered")
st.title("🎤 Reddit Story Video Generator")

story_input_method = st.radio("How do you want to input the story?", ["Paste Reddit URLs (batch)", "Paste Text Manually"])

voice_option = st.selectbox("Choose a voice engine", ["gTTS", "pyttsx3"])

# Use a static background image
DEFAULT_BG_PATH = "assets/backgrounds/default_bg.jpg"

if story_input_method == "Paste Reddit URLs (batch)":
    urls_input = st.text_area("Enter multiple Reddit post URLs (one per line)")
    if st.button("Generate Videos"):
        if not urls_input.strip():
            st.error("Please provide at least one Reddit URL.")
        else:
            urls = [u.strip() for u in urls_input.splitlines() if u.strip()]
            for i, reddit_url in enumerate(urls):
                with st.spinner(f"Processing video {i+1}/{len(urls)}..."):
                    story_text = get_reddit_story(reddit_url)
                    audio_path = text_to_speech(story_text, engine=voice_option)
                    output_path = make_video(story_text, audio_path, DEFAULT_BG_PATH)

                    st.success(f"Video {i+1} created!")
                    st.video(output_path)
                    with open(output_path, "rb") as file:
                        st.download_button(f"📥 Download Video {i+1}", file, file_name=f"reddit_story_{i+1}.mp4")
else:
    story_text = st.text_area("Paste your Reddit story text here", height=300)
    if st.button("Generate Video"):
        if not story_text:
            st.error("Please provide a story text.")
        else:
            with st.spinner("Generating voiceover..."):
                audio_path = text_to_speech(story_text, engine=voice_option)

            with st.spinner("Creating video..."):
                output_path = make_video(story_text, audio_path, DEFAULT_BG_PATH)

            st.success("Video created successfully!")
            st.video(output_path)
            with open(output_path, "rb") as file:
                st.download_button("📥 Download Video", file, file_name="reddit_story_video.mp4")
