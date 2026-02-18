import streamlit as st
import joblib

# recommender logic
from recommender.recommender import recommend_movies

# poster + trailer + categories
from utils.poster import (
    fetch_poster,
    fetch_trailer,
    fetch_trending_movies,
    fetch_movies_by_genre
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Recommendation Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# HEADER
# =========================
st.markdown("## 🎬 Recommendation Engine")
st.markdown("Explore movies like Netflix with AI recommendations 🚀")
st.markdown("---")

# =========================
# LOAD MOVIES (CACHE 🔥)
# =========================
@st.cache_data
def load_movies():
    movies = joblib.load("models/movies.pkl")
    movies["clean"] = movies["title"].str.lower().str.strip()
    return movies

movies_df = load_movies()

# 🔥 LIMIT BASE LIST TO 3000 (IMPORTANT)
movies_df = movies_df.head(3000)

movie_list = movies_df["title"].tolist()

# =========================
# SEARCH SYSTEM 🔍
# =========================
st.markdown("### 🔍 Search Movie")

search_query = st.text_input("Type movie name...")

def normalize(text):
    return text.lower().strip()

# 🔥 SMART FILTERING
if search_query:
    filtered_df = movies_df[
        movies_df["clean"].str.contains(normalize(search_query), regex=False)
    ]

    # 🔥 LIMIT DISPLAY (UI SAFE)
    filtered_df = filtered_df.head(200)

else:
    # 🔥 SHOW POPULAR / FIRST 200
    filtered_df = movies_df.head(200)

filtered_movies = filtered_df["title"].tolist()

# show count (REAL COUNT, not limited one)
if search_query:
    total_matches = movies_df[
        movies_df["clean"].str.contains(normalize(search_query), regex=False)
    ].shape[0]

    st.caption(f"{total_matches} results found (showing top {len(filtered_movies)})")

# dropdown
if filtered_movies:
    selected_movie = st.selectbox("🎬 Select Movie", filtered_movies)
else:
    st.warning("No matching movies found 😕")
    selected_movie = None

# =========================
# RECOMMENDATION BUTTON
# =========================
if st.button("🎯 Get Recommendations"):

    if not selected_movie:
        st.warning("Please select a movie first 🎬")

    else:
        with st.spinner("Finding best recommendations... 🎬"):

            try:
                recommendations = recommend_movies(selected_movie, top_n=10)

                st.markdown("## 🎬 Recommended Movies")

                # 🔥 GRID (2 rows)
                for row in range(2):
                    cols = st.columns(5)

                    for i in range(5):
                        idx = row * 5 + i
                        if idx >= len(recommendations):
                            break

                        movie = recommendations[idx]

                        with cols[i]:
                            poster = fetch_poster(movie)

                            if poster:
                                st.image(poster, use_container_width=True)

                            st.caption(movie)

                            trailer = fetch_trailer(movie)
                            if trailer:
                                st.link_button("▶ Trailer", trailer)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# =========================
# NETFLIX STYLE ROWS
# =========================
def show_row(title, movies):
    st.markdown(f"## {title}")

    cols = st.columns(5)

    for i, movie in enumerate(movies[:5]):
        with cols[i]:
            poster = fetch_poster(movie)
            if poster:
                st.image(poster, use_container_width=True)

            st.caption(movie)

            trailer = fetch_trailer(movie)
            if trailer:
                st.link_button("▶", trailer)

# =========================
# REAL-TIME SECTIONS
# =========================
st.markdown("---")

show_row("🔥 Trending Now (Real-Time)", fetch_trending_movies())
show_row("💥 Action Movies (Real-Time)", fetch_movies_by_genre("action"))
show_row("🎭 Drama Movies (Real-Time)", fetch_movies_by_genre("drama"))
show_row("❤️ Romance Movies (Real-Time)", fetch_movies_by_genre("romance"))

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
    "<p style='text-align:center; font-size:12px;'>This product uses the TMDB API but is not endorsed or certified by TMDB.</p>",
    unsafe_allow_html=True
)

st.markdown("<p style='text-align:center;'>Built with ❤️ by Ayush Raj</p>", unsafe_allow_html=True)
