import streamlit as st
import pandas as pd
import pickle

# ==============================
# 📂 Load data with cache
# ==============================
@st.cache_data
def load_data():
    books = pickle.load(open('books.pkl', 'rb'))
    similarity = pickle.load(open('similarity_books.pkl', 'rb'))

    return pd.DataFrame(books), similarity


books, similarity = load_data()


# ==============================
# 📚 Fetch book thumbnail (FIXED)
# ==============================
def fetch_thumbnail(index):
    url = books.iloc[index]['thumbnail']

    # Check for valid URL
    if pd.notna(url) and str(url).strip() != "" and str(url).startswith("http"):
        return url
    else:
        return "https://via.placeholder.com/150x220?text=No+Image"


# ==============================
# 🤖 Recommendation function
# ==============================
def recommend(book):
    if book not in books['title'].values:
        return [], []

    book_index = books[books['title'] == book].index[0]
    distances = similarity[book_index]

    books_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )

    recommended_books = []
    recommended_posters = []

    for i in books_list[1:6]:
        index = i[0]

        recommended_books.append(
            books.iloc[index]['title']
        )

        recommended_posters.append(
            fetch_thumbnail(index)
        )

    return recommended_books, recommended_posters


# ==============================
# 🎨 Streamlit UI
# ==============================
st.title("📚 Book Recommender System")

selected_book = st.selectbox(
    "Choose a book",
    books['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_book)

    if names:
        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i], use_container_width=True)

    else:
        st.warning("Book not found!")