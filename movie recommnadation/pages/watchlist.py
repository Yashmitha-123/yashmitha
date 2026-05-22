import streamlit as st
import pandas as pd
from utils import fetch_movie_details

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="My Watchlist",
    page_icon="❤️",
    layout="wide"
)

# ==========================================
# BACKGROUND CSS
# ==========================================

st.markdown("""
<style>

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

font-size:65px;

font-weight:bold;

background:linear-gradient(
90deg,
#ff4d6d,
#ff758f,
#ffd6e0
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

margin-bottom:15px;
}

/* SUBTITLE */

.subtitle{

text-align:center;

font-size:22px;

color:white;

margin-bottom:40px;
}

/* CARD */

.movie-card{

background:rgba(255,255,255,0.08);

padding:18px;

border-radius:20px;

backdrop-filter:blur(12px);

box-shadow:0px 8px 25px rgba(0,0,0,0.4);

margin-bottom:25px;

text-align:center;
}

/* TEXT */

.movie-title{

font-size:20px;

font-weight:bold;

color:white;

margin-top:10px;
}

.rating{

color:#FFD700;

font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

# ==========================================
# TITLE
# ==========================================

st.markdown("""
<div class="title">
❤️ My Watchlist
</div>

<div class="subtitle">
Save your favorite movies and watch later
</div>
""", unsafe_allow_html=True)

# ==========================================
# WATCHLIST EMPTY
# ==========================================

if len(st.session_state.watchlist) == 0:

    st.info("No movies added to watchlist yet.")

# ==========================================
# DISPLAY WATCHLIST
# ==========================================

else:

    cols = st.columns(4)

    for index, movie in enumerate(
        st.session_state.watchlist
    ):

        with cols[index % 4]:

            st.markdown(
                "<div class='movie-card'>",
                unsafe_allow_html=True
            )

            st.image(
                movie["poster"],
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class='movie-title'>
                {movie['title']}
                </div>

                <div class='rating'>
                ⭐ {movie['rating']}
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "❌ Remove",
                key=f"remove_{index}"
            ):

                st.session_state.watchlist.pop(index)

                st.rerun()

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

# ==========================================
# CLEAR WATCHLIST
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

if len(st.session_state.watchlist) > 0:

    if st.button("🗑 Clear Watchlist"):

        st.session_state.watchlist = []

        st.rerun()