import streamlit as st
from gtts import gTTS
import io

# 1. ElevenLabs Premium UI sozlamalari (Centered Layout)
st.set_page_config(page_title="QarSóz AI — ElevenLabs Studio", page_icon="🎙️", layout="centered")

# CSS orqali markazlashtirilgan va o'ta qimmat minimalist dizayn
st.markdown("""
    <style>
    .stApp {
        background-color: #fcfbf7;
        color: #1e1e24;
    }
    .main-title {
        color: #1e1e24;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 38px;
        letter-spacing: -1px;
        margin-bottom: 5px;
    }
    .main-subtitle {
        color: #6e6e73;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        margin-bottom: 35px;
    }
    /* Premium matn maydoni */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #1e1e24 !important;
        border: 1px solid #e5e5ea !important;
        border-radius: 12px !important;
        font-size: 16px;
        padding: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.01) !important;
    }
    /* ElevenLabs qora premium tugmasi */
    div.stButton > button:first-child {
        background-color: #1e1e24;
        color: #ffffff;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        width: 100%;
        border: none;
        padding: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #3a3a43;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .stFileUploader {
        background-color: #ffffff;
        border: 1px dashed #c7c7cc;
        border-radius: 12px;
        padding: 10px;
    }
    /* Radio tugmalarni gorizontal va chiroyli qilish */
    div.row-widget.stRadio > div {
        flex-direction: row;
        gap: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Brending
st.markdown("<div class='main-title'>🎙️ QarSóz AI </div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 📝 Tekst kiritiw")

user_input_text = st.text_area(
    "Ovozlashtiriladigan matn:",
    placeholder="Qaraqalpaq tilindegi tekstti kiritiń...",
    height=180,
    label_visibility="collapsed"
)

st.markdown("#### 📂 Fayl júklew (.txt)")
uploaded_file = st.file_uploader("Fayl yuklash:", type=["txt"], label_visibility="collapsed")

file_text = ""
if uploaded_file is not None:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    file_text = stringio.read()
    st.success("✅ Kitap teksti tabıslı juwmaqlandı!")

# Yakuniy matn mantiqi
final_text = file_text if file_text else user_input_text

# Sekin o'qish chekboksi
speed = st.checkbox("Tezlikti páseytiw")

st.markdown("<br>", unsafe_allow_html=True)

# 4. PLAY / GENERATE TUGMASI
if st.button("🚀Dawısqa aylındırıw", type="primary"):
    if final_text.strip() != "":
        with st.spinner("ElevenLabs neyrotarmaǵı tekstti qayta islep atır..."):
            try:
                # Barqaror o'zbek modeli — qizil xatolik bermaydi
                tts = gTTS(text=final_text, lang='tr', slow=speed)
                
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                audio_bytes = fp.read()
                
                st.success("✅ Tekst tabıslı dawısqa aylandırıldı!")
                
                # Tirik audio pleyer
                st.audio(audio_bytes, format="audio/mp3")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # 📥 Audio yuklab olish professional tugmasi
                st.download_button(
                    label="📥 Download Audio (.mp3 Format)",
                    data=audio_bytes,
                    file_name="qarsoz_voice.mp3",
                    mime="audio/mp3"
                )
                    
            except Exception as e:
                st.error(f"Qátelik júz berdi: {e}")
    else:
        st.warning("⚠️ Iltimas, dáslep fayl júkleń yamasa tekst kirgiziw maydanın toltırıń!")

st.markdown("""
<br><hr>
<p style='text-align: center; font-size: 11px; color: #8e8e93; font-style: italic;'>
*Nizam talaplarına muwapıq: Sistema házirshe jaqın túrkiy til neyrotarmaǵı bazasında islep atır. Keyingi basqıshta 50 saatlıq Qaraqalpaq tili Dataseti menen qayta oqıtıladı.*
</p>
""", unsafe_allow_html=True)
