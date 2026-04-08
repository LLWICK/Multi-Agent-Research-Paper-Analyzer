import streamlit as st
import requests

st.set_page_config(page_title="Research Paper Analyzer", layout="wide")

st.title("📄 Research Paper Analyzer")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ File uploaded")

    if st.button("Analyze Paper"):
        with st.spinner("🚀 Sending to backend..."):

            files = {
                "file": (uploaded_file.name, uploaded_file, "application/pdf")
            }

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    files=files
                )

                if response.status_code == 200:
                    result = response.json()['results']

                    st.success("✅ Analysis Complete!")

                    col1, col2 = st.columns(2)

                    with col1:
                        with st.expander("📘 Teach", expanded=True):
                            st.markdown(result.get("teach", "Not found"))

                        with st.expander("🧪 Experiment"):
                            st.markdown(result.get("experiment", "Not found"))

                    with col2:
                        with st.expander("📐 Math", expanded=True):
                            st.markdown(result.get("math", "Not found"))

                        with st.expander("📺 YouTube Videos", expanded=True):
                            youtube_links  = result.get("youtube")

                            if not youtube_links:
                                st.info("No videos available")
                            else:
                                def get_video_id(url):
                                    if "v=" in url:
                                        return url.split("v=")[1].split("&")[0]
                                    elif "youtu.be/" in url:
                                        return url.split("youtu.be/")[1].split("?")[0]
                                    return None

                                for idx, link in enumerate(youtube_links):
                                    video_id = get_video_id(link)

                                    if video_id:
                                        thumb_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

                                        st.markdown(f"""
                                            <a href="{link}" target="_blank">
                                                <img src="{thumb_url}" style="width:100%; border-radius:10px;">
                                            </a>
                                        """, unsafe_allow_html=True)

                                        st.caption(f"▶ Watch Video {idx + 1}")
                                        st.write("---")

                else:
                    st.error(f"❌ Backend Error: {response.status_code}")

            except Exception as e:
                st.error(f"❌ Connection Error: {str(e)}")