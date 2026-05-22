import streamlit as st
import pandas as pd
import plotly.express as px
from utils import movies

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide"
)

# =====================================
# LOAD HTML
# =====================================
with open(
    "templates/dashboard.html",
    "r",
    encoding="utf-8"
) as f:

    st.markdown(
        f.read(),
        unsafe_allow_html=True
    )

# =====================================
# METRICS
# =====================================
total_movies = len(movies)

avg_rating = 8.5

top_genre = "Sci-Fi"

# =====================================
# METRIC CARDS
# =====================================
c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "🎬 Total Movies",
        total_movies
    )

with c2:

    st.metric(
        "⭐ Average Rating",
        avg_rating
    )

with c3:

    st.metric(
        "🔥 Trending Genre",
        top_genre
    )

st.markdown("---")

# =====================================
# BAR CHART
# =====================================
genre_data = pd.DataFrame({

    "Genre": [

        "Action",
        "Comedy",
        "Sci-Fi",
        "Romance",
        "Thriller",
        "Drama",
        "Adventure"

    ],

    "Popularity": [

        95,
        80,
        99,
        70,
        88,
        85,
        90

    ]
})

fig = px.bar(

    genre_data,
    x="Genre",
    y="Popularity",
    title="🔥 Genre Popularity"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# PIE CHART
# =====================================
pie_data = pd.DataFrame({

    "Category": [

        "Trending",
        "Top Rated",
        "Recommended",
        "Watchlist"

    ],

    "Users": [

        40,
        25,
        20,
        15

    ]
})

fig2 = px.pie(

    pie_data,
    names="Category",
    values="Users",
    title="🎬 User Interests"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# MOVIE TABLE
# =====================================
st.markdown(
    "## 🎥 Movie Dataset Preview"
)

st.dataframe(
    movies.head(20),
    use_container_width=True
)