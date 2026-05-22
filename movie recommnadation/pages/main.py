import streamlit as st

st.set_page_config(
    page_title="CineVerse AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# CSS
# =========================================

st.markdown("""
<style>

/* HIDE SIDEBAR */

[data-testid="stSidebar"]{
display:none;
}

/* BACKGROUND */

.stApp{

background:
linear-gradient(
rgba(0,0,0,0.78),
rgba(0,0,0,0.88)
),

url("https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=2070");

background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;
}

/* TITLE */

.title{

text-align:center;

font-size:70px;

font-weight:bold;

background:linear-gradient(
90deg,
#00F5FF,
#8B5CF6,
#EC4899
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

margin-top:20px;
}

/* SUBTITLE */

.subtitle{

text-align:center;

font-size:24px;

color:white;

margin-bottom:50px;
}

/* CARD */

.card{

height:320px;

background:rgba(255,255,255,0.08);

padding:55px 35px;

border-radius:32px;

backdrop-filter:blur(15px);

text-align:center;

transition:0.5s;

box-shadow:0px 10px 35px rgba(0,0,0,0.45);

margin-bottom:45px;

cursor:pointer;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;
}

/* HOVER */

.card:hover{

transform:translateY(-15px) scale(1.03);

box-shadow:0px 20px 40px rgba(0,245,255,0.45);
}

/* CARD TITLE */

.card-title{

font-size:42px;

font-weight:bold;

color:white;

margin-bottom:18px;
}

/* CARD TEXT */

.card-text{

font-size:22px;

color:#e5e7eb;

line-height:1.7;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================

st.markdown("""
<div class="title">
🎬 CineVerse AI
</div>

<div class="subtitle">
Explore Movies with Artificial Intelligence
</div>
""", unsafe_allow_html=True)

# =========================================
# FIRST ROW
# =========================================

col1,col2,col3 = st.columns(3,gap="large")

with col1:

    st.markdown("""
    <a href="/recommendation" target="_self" class="card-link">

    <div class="card">

    <div class="card-title">
    🎬 Recommendation
    </div>

    <div class="card-text">
    AI personalized movie suggestions
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <a href="/trending" target="_self" class="card-link">

    <div class="card">

    <div class="card-title">
    🔥 Trending
    </div>

    <div class="card-text">
    Explore today's viral movies
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <a href="/top_rated" target="_self" class="card-link">

    <div class="card">

    <div class="card-title">
    ⭐ Top Rated
    </div>

    <div class="card-text">
    Highest rated movies
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

# =========================================
# ROW 2
# =========================================

col4,col5,col6 = st.columns(3,gap="large")

with col4:

    st.markdown("""
    <a href="/genres" target="_self" class="card-link">

    <div class="card">

    <div class="card-title">
    🎭 Genres
    </div>

    <div class="card-text">
    Browse movies by category
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <a href="/watchlist" target="_self" class="card-link">

    <div class="card">

    <div class="card-title">
    ❤️ Watchlist
    </div>

    <div class="card-text">
    Save favorite movies
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <a href="/dashboard" target="_self" class="card-link">

    <div class="card">

    <div class="card-title">
    📊 Dashboard
    </div>

    <div class="card-text">
    Movie analytics & insights
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)