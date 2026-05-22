import streamlit as st

st.set_page_config(
    page_title="CineVerse AI",
    page_icon="🎬",
    layout="wide"
)

# =========================================
# BACKGROUND
# =========================================
st.markdown("""
<style>

.stApp{
background:
linear-gradient(rgba(0,0,0,0.75),
rgba(0,0,0,0.85)),
url("https://pngtree.com/free-backgrounds-photos/movie");

background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;
}

.main-box{

margin-top:120px;
padding:60px;
border-radius:30px;

background:rgba(255,255,255,0.08);

backdrop-filter:blur(15px);

text-align:center;

box-shadow:0px 10px 40px rgba(0,0,0,0.5);
}

.title{

font-size:85px;
font-weight:bold;

background:linear-gradient(
90deg,
#ff4d4d,
#ffd93d,
#4D96FF
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{

font-size:28px;
color:white;
margin-top:20px;
}

.info{

font-size:18px;
color:#d1d5db;
margin-top:30px;
line-height:1.8;
}

.stButton>button{

background:linear-gradient(
90deg,
#00F5FF,
#8B5CF6
);

color:white;
font-size:22px;
padding:15px 40px;
border:none;
border-radius:15px;

margin-top:40px;

transition:0.4s;
}

.stButton>button:hover{

transform:scale(1.05);
box-shadow:0px 0px 25px #00F5FF;
}
[data-testid="stSidebar"]{
            display:none;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-box">

<div class="title">
🎬 CineVerse AI
</div>

<div class="subtitle">
AI Powered Movie Recommendation Platform
</div>

<div class="info">

Discover movies intelligently using Artificial Intelligence.<br><br>

✔ Personalized Recommendations <br>
✔ Trending & Top Rated Movies <br>
✔ Genre Based Search <br>
✔ Movie Analytics Dashboard <br>
✔ Save Movies to Watchlist <br>

</div>

</div>
""", unsafe_allow_html=True)

col1,col2,col3=st.columns([2,1,2])

with col2:
    if st.button("🚀 Get Started"):
        st.switch_page("pages/main.py")