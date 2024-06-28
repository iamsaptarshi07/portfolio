from projects import PROJECTS
from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd

if not isinstance(current_dir, Path):
    current_dir = Path(current_dir)

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
# profile_pic = current_dir / "assets" / "profile-pic.png"
profile_pic = current_dir / "assets" / "image.jpg"


# ---- GENERAL SETTINGS ----

PAGE_TITLE = "Digital CV | Saptarshi Mandal"
PAGE_ICON = ":wave:"
NAME = "Saptarshi Mandal"
DESCRIPTION = """
I was born and brought up in Kolkata. I'm very passionate about learning new technologies, 
particularly machine learning, and I'm also interested in the stock market.
"""
EMAIL = "iamsaptarshi07@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/saptarshi-mandal-92916b257/",
    "Github": "https://github.com/iamsaptarshi07",
    "Twitter": "https://twitter.com/saptarshi_twts",
}


st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)

# --- CODE FOR LOADING CSS, PDF & PROFILE PIC ---

with open(css_file, "r") as css:
    st.markdown("<style>{}</style>".format(css.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as cv_pdf:
    CVbyte = cv_pdf.read()

Profile_pic = Image.open(profile_pic)


# --- CODE FOR LOADING PROFILE PIC & DOWNLOADING PDF ---

col1, col2 = st.columns([0.40, 0.60])
# col1, col2 = st.columns([0.55, 0.45])
with col1:
    st.image(Profile_pic, width=260)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=CVbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)


# ---- SOCIAL MEDIA LINKS ----

st.write("&nbsp;")  # This is puts a non breaking space between two sections

cols = st.columns(len(SOCIAL_MEDIA))
for _, (platform, url) in enumerate(SOCIAL_MEDIA.items()):
    cols[_].write(f"[{platform}]({url})")


# ---- SKILLS ----

st.write("&nbsp;")  # This is puts a non breaking space between two sections
st.title("Skills")
st.write("---")
st.write(
    """
- 👨‍💻 Programming: Python (Pandas,Scikit-learn,Numpy)
- 💻 Linux
- 🗄️ Git
- 🫙 Docker
- 📊 Data Visualization
- ☁️ Cloud: Render
"""
)
# - 📚


# ---- PROJECTS ----

st.write("&nbsp;")  # This is puts a non breaking space between two sections
st.title("Projects")
st.write("---")
for name, link in PROJECTS.items():
    st.write(f"[{name}]({link})")
