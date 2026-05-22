import streamlit as st
from utils import get_trending_movies

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Trending Movies",
    layout="wide"
)

# =====================================
# WATCHLIST SESSION
# =====================================

if "watchlist" not in st.session_state:

    st.session_state.watchlist = []

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
REMOVE TOP SPACE
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

font-size:17px;

font-weight:bold;

border:none;

padding:12px;

border-radius:14px;

margin-top:12px;
}

/* ================================
EXPANDER
================================ */

.streamlit-expanderHeader{

color:white !important;
}

</style>

""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.markdown("""

<div class="main-title">
🔥 Trending Movies
</div>

<div class="sub-title">
Explore Today's Most Popular Movies
</div>

""", unsafe_allow_html=True)

# =====================================
# GET MOVIES
# =====================================

movies = get_trending_movies()

# =====================================
# DISPLAY MOVIES
# =====================================

cols = st.columns(5)

for idx, movie in enumerate(movies):

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

        # ==========================
        # WATCHLIST BUTTON
        # ==========================

        if st.button(
            "❤️ Add to Watchlist",
            key=movie["movie_id"]
        ):

            already_exists = any(

                m["movie_id"] == movie["movie_id"]

                for m in st.session_state.watchlist
            )

            if not already_exists:

                st.session_state.watchlist.append(
                    movie
                )

                st.success(
                    "Added to Watchlist ❤️"
                )

            else:

                st.warning(
                    "Movie already exists!"
                )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )