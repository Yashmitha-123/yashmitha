# ==========================================
# utils.py
# ==========================================

import pandas as pd
import pickle
import requests
import streamlit as st

# ==========================================
# TMDB API KEY
# ==========================================

API_KEY = "b7d3955b180a1d71a2dd6949cd41140a"

# ==========================================
# LOAD DATA
# ==========================================

@st.cache_resource
def load_data():

    movies_dict = pickle.load(
        open("movies_eve.pkl", "rb")
    )

    similarity = pickle.load(
        open("similarity_eve.pkl", "rb")
    )

    movies = pd.DataFrame(
        movies_dict
    )

    # ======================================
    # FIX MOVIE ID
    # ======================================

    if "movie_id" not in movies.columns:

        if "id" in movies.columns:

            movies.rename(
                columns={
                    "id":"movie_id"
                },
                inplace=True
            )

    return movies, similarity

movies, similarity = load_data()

# ==========================================
# FETCH MOVIE DETAILS
# ==========================================


def fetch_movie_details(movie_id):

    try:

        # ======================================
        # TMDB API URL
        # ======================================

        url = (
            f"https://api.themoviedb.org/3/movie/"
            f"{movie_id}?api_key={API_KEY}"
        )

        response = requests.get(
            url,
            timeout=10
        )

        # ======================================
        # CHECK RESPONSE
        # ======================================

        if response.status_code != 200:
            return None

        data = response.json()

        # ======================================
        # POSTER
        # ======================================

        poster_path = data.get(
            "poster_path"
        )

        poster = (

            f"https://image.tmdb.org/t/p/w500{poster_path}"

            if poster_path

            else "https://via.placeholder.com/500x750"
        )

        # ======================================
        # GENRES
        # ======================================

        genres = ", ".join([

            g["name"]

            for g in data.get(
                "genres",
                []
            )

        ])

        # ======================================
        # RETURN MOVIE DETAILS
        # ======================================

        return {

            "title": data.get(
                "title",
                "Unknown"
            ),

            "poster": poster,

            "rating": round(
                data.get(
                    "vote_average",
                    0
                ),
                1
            ),

            "overview": data.get(
                "overview",
                "No overview available"
            ),

            "genres": genres,

            # ==================================
            # RELEASE DATE
            # ==================================

            "release": data.get(
                "release_date",
                "N/A"
            ),

            # ==================================
            # LANGUAGE
            # ==================================

            "language": data.get(
                "original_language",
                "N/A"
            ).upper(),

            "movie_id": movie_id
        }

    except Exception as e:

        print("ERROR:", e)

        return None

        # ======================================
        # RETURN DATA
        # ======================================

        return {

            "title": data.get(
                "title",
                "Unknown"
            ),

            "poster": poster,

            "rating": round(
                data.get(
                    "vote_average",
                    0
                ),
                1
            ),

            "overview": data.get(
                "overview",
                "No overview available"
            ),

            "genres": genres,

            "movie_id": movie_id
        }

    except Exception as e:

        print("ERROR:", e)

        return None
# =====================================
# GENRE MOVIES
# =====================================

@st.cache_data(ttl=3600)

def get_movies_by_genre(selected_genre):

    genre_movies = []

    genre_map = {

        "Action": 28,
        "Comedy": 35,
        "Drama": 18,
        "Sci-Fi": 878,
        "Romance": 10749,
        "Thriller": 53,
        "Adventure": 12,
        "Animation": 16,
        "Fantasy": 14,
        "Horror": 27
    }

    genre_id = genre_map.get(
        selected_genre,
        28
    )

    url = (
        f"https://api.themoviedb.org/3/discover/movie"
        f"?api_key={API_KEY}"
        f"&with_genres={genre_id}"
        f"&sort_by=popularity.desc"
    )

    try:

        # ==========================
        # SAFE REQUEST
        # ==========================

        response = requests.get(

            url,

            timeout=20,

            headers={
                "accept": "application/json",
                "User-Agent": "Mozilla/5.0"
            }
        )

        # ==========================
        # STATUS CHECK
        # ==========================

        if response.status_code != 200:

            st.error(
                f"TMDB Error {response.status_code}"
            )

            return []

        data = response.json()

        # ==========================
        # FETCH 20 MOVIES
        # ==========================

        for movie in data.get(
            "results",
            []
        )[:20]:

            try:

                details = fetch_movie_details(
                    movie["id"]
                )

                if details:

                    genre_movies.append(
                        details
                    )

            except:

                pass

        return genre_movies

    # ==========================
    # INTERNET ERROR
    # ==========================

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Internet blocked TMDB API"
        )

        return []

    # ==========================
    # TIMEOUT
    # ==========================

    except requests.exceptions.Timeout:

        st.error(
            "❌ Request Timeout"
        )

        return []

    # ==========================
    # OTHER ERROR
    # ==========================

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

        return []
# ==========================================
# RECOMMEND MOVIES
# ==========================================

def recommend(movie):

    recommended_movies = []

    try:

        # ==================================
        # FIND MOVIE INDEX
        # ==================================

        movie_index = movies[
            movies["title"] == movie
        ].index[0]

        # ==================================
        # SIMILARITY SCORES
        # ==================================

        distances = similarity[
            movie_index
        ]

        # ==================================
        # TOP 10 MOVIES
        # ==================================

        movie_list = sorted(

            list(enumerate(distances)),

            reverse=True,

            key=lambda x:x[1]

        )[1:11]

        # ==================================
        # FETCH DETAILS
        # ==================================

        for i in movie_list:

            movie_id = movies.iloc[
                i[0]
            ].movie_id

            details = fetch_movie_details(
                movie_id
            )

            if details:

                recommended_movies.append(
                    details
                )

    except Exception as e:

        st.error(
            f"Recommendation Error: {e}"
        )

    return recommended_movies


# =====================================
# TRENDING MOVIES
# =====================================

@st.cache_data(ttl=3600)

def get_trending_movies():

    trending_movies = []

    url = (
        f"https://api.themoviedb.org/3/trending/movie/day"
        f"?api_key={API_KEY}"
    )

    try:

        response = requests.get(

            url,

            headers={
                "User-Agent":"Mozilla/5.0"
            },

            timeout=15
        )

        # ==========================
        # FAILED REQUEST
        # ==========================

        if response.status_code != 200:

            st.error(
                "Failed to fetch trending movies"
            )

            return []

        data = response.json()

        # ==========================
        # FETCH ONLY 10 MOVIES
        # ==========================

        for movie in data.get(
            "results",
            []
        )[:10]:

            details = fetch_movie_details(
                movie["id"]
            )

            if details:

                trending_movies.append(
                    details
                )

        return trending_movies

    # ==============================
    # INTERNET ERROR
    # ==============================

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Internet Connection Error"
        )

        return []

    # ==============================
    # TIMEOUT ERROR
    # ==============================

    except requests.exceptions.Timeout:

        st.error(
            "❌ Request Timeout"
        )

        return []

    # ==============================
    # OTHER ERRORS
    # ==============================

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

        return []
# =====================================
# TOP RATED MOVIES
# =====================================

@st.cache_data(ttl=3600)

def get_top_rated_movies():

    top_movies = []

    url = (
        f"https://api.themoviedb.org/3/movie/top_rated"
        f"?api_key={API_KEY}"
    )

    try:

        response = requests.get(

            url,

            timeout=15
        )

        # ==========================
        # STATUS CHECK
        # ==========================

        if response.status_code != 200:

            st.error(
                "Failed to fetch movies"
            )

            return []

        data = response.json()

        # ==========================
        # FETCH 10 MOVIES
        # ==========================

        for movie in data.get(
            "results",
            []
        )[:10]:

            details = fetch_movie_details(
                movie["id"]
            )

            if details:

                top_movies.append(
                    details
                )

        return top_movies

    # ==========================
    # INTERNET ERROR
    # ==========================

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Internet Connection Error"
        )

        return []

    # ==========================
    # TIMEOUT
    # ==========================

    except requests.exceptions.Timeout:

        st.error(
            "❌ Request Timeout"
        )

        return []

    # ==========================
    # OTHER ERRORS
    # ==========================

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

        return []