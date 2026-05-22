import streamlit as st
from utils import movies, recommend

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Recommendation",
    layout="wide"
)

# =====================================
# CSS
# =====================================

st.markdown("""

<style>

/* ================================
BACKGROUND
================================ */

.stApp{

background-image:

linear-gradient(
rgba(0,0,0,0.82),
rgba(0,0,0,0.88)
),

url("https://images.unsplash.com/photo-1440404653325-ab127d49abc1?q=80&w=2070");

background-size:cover;

background-position:center;

background-repeat:no-repeat;

background-attachment:fixed;
}

/* ================================
REMOVE WHITE SPACE
================================ */

.block-container{

padding-top:2rem;
}

/* ================================
TITLE
================================ */

.main-title{

text-align:center;

font-size:65px;

font-weight:bold;

background:linear-gradient(
90deg,
#00F5FF,
#8B5CF6,
#EC4899
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

margin-bottom:15px;
}

/* ================================
SUBTITLE
================================ */

.sub-title{

text-align:center;

font-size:22px;

color:white;

margin-bottom:40px;
}

/* ================================
SELECT BOX
================================ */

.stSelectbox label{

color:white !important;

font-size:20px;
}

.stSelectbox > div > div{

background:rgba(255,255,255,0.12);

color:white;

border-radius:15px;
}

/* ================================
BUTTON
================================ */

.stButton > button{

width:100%;

background:linear-gradient(
90deg,
#00F5FF,
#8B5CF6
);

color:white;

font-size:20px;

font-weight:bold;

border:none;

padding:14px;

border-radius:15px;

margin-top:15px;

transition:0.3s;
}

.stButton > button:hover{

transform:scale(1.03);

box-shadow:0 0 20px rgba(0,245,255,0.5);
}

/* ================================
MOVIE CARD
================================ */

.movie-card{

background:rgba(255,255,255,0.08);

padding:18px;

border-radius:24px;

backdrop-filter:blur(12px);

box-shadow:0 0 20px rgba(0,0,0,0.5);

margin-bottom:30px;

transition:0.4s;
}

/* ================================
HOVER
================================ */

.movie-card:hover{

transform:translateY(-10px);

box-shadow:0 0 25px rgba(0,245,255,0.45);
}

/* ================================
MOVIE TITLE
================================ */

.movie-title{

font-size:24px;

font-weight:bold;

color:white;

margin-top:12px;

margin-bottom:10px;
}

/* ================================
MOVIE INFO
================================ */

.movie-info{

font-size:16px;

color:#f3f4f6;

line-height:1.8;
}

/* ================================
EXPANDER
================================ */

.streamlit-expanderHeader{

color:white !important;

font-size:17px;
}

</style>

""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.markdown("""

<div class="main-title">
🎬 AI Movie Recommendation
</div>

<div class="sub-title">
Discover Similar Movies with AI Powered Suggestions
</div>

""", unsafe_allow_html=True)

# =====================================
# SELECT MOVIE
# =====================================

selected_movie = st.selectbox(
    "🎥 Choose Movie",
    movies["title"].values
)

# =====================================
# BUTTON
# =====================================

if st.button("🚀 Recommend Movies"):

    recommendations = recommend(
        selected_movie
    )

    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(5)

    # =================================
    # DISPLAY MOVIES
    # =================================

    for idx, movie in enumerate(
        recommendations
    ):

        with cols[idx % 5]:

            st.markdown(
                "<div class='movie-card'>",
                unsafe_allow_html=True
            )

            # ==========================
            # POSTER
            # ==========================

            st.image(
                movie["poster"],
                use_container_width=True
            )

            # ==========================
            # DETAILS
            # ==========================

            st.markdown(
                f"""

                <div class="movie-title">
                🎬 {movie['title']}
                </div>

                <div class="movie-info">

                ⭐ Rating: {movie['rating']} <br>

                🎭 Genres: {movie['genres']} <br>

                📅 Release: {movie['release']} <br>

                🌍 Language: {movie['language']}

                </div>

                """,
                unsafe_allow_html=True
            )

            # ==========================
            # OVERVIEW
            # ==========================

            with st.expander(
                "📝 Overview"
            ):

                st.write(
                    movie["overview"]
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )