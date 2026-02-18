import joblib
import pandas as pd
import re

# =========================
# LOAD MODELS (OPTIMIZED 🔥)
# =========================
model = joblib.load("models/movie_model.pkl")     # KNN model
movie_ids = joblib.load("models/movie_ids.pkl")   # index → movieId mapping
movies = joblib.load("models/movies.pkl")         # movie metadata


# =========================
# CLEAN TITLE 🔥
# =========================
def clean_title(title):
    return re.sub(r"\(\d{4}\)", "", title).strip().lower()


# =========================
# PREPROCESS MOVIES (ONE TIME)
# =========================
if "clean_title" not in movies.columns:
    movies["clean_title"] = movies["title"].apply(clean_title)

# 🔥 FAST lookup dictionary (BIG performance boost 🚀)
movieid_to_index = {mid: i for i, mid in enumerate(movie_ids)}


# =========================
# GET MOVIE INDEX
# =========================
def get_movie_index(movie_name):

    movie_name_clean = clean_title(movie_name)

    # exact match
    exact_match = movies[movies["clean_title"] == movie_name_clean]
    if not exact_match.empty:
        movie_id = exact_match.iloc[0]["movieId"]
        return movieid_to_index.get(movie_id)

    # partial match (safe regex OFF ⚠️)
    partial_match = movies[
        movies["clean_title"].str.contains(movie_name_clean, regex=False)
    ]

    if not partial_match.empty:
        movie_id = partial_match.iloc[0]["movieId"]
        return movieid_to_index.get(movie_id)

    return None


# =========================
# MAIN RECOMMENDER 🔥
# =========================
def recommend_movies(movie_name, top_n=10):
    try:
        idx = get_movie_index(movie_name)

        # ❌ fallback
        if idx is None:
            return get_popular_movies(top_n)

        # 🔥 GET VECTOR
        query = model._fit_X[idx]

        # 🔥 FIX: ensure 2D array (VERY IMPORTANT)
        if hasattr(query, "toarray"):
            query = query.toarray()

        if len(query.shape) == 1:
            query = query.reshape(1, -1)

        # 🔥 KNN SEARCH
        distances, indices = model.kneighbors(
            query,
            n_neighbors=top_n + 1
        )

        indices = indices[0][1:]  # remove itself

        recommended = []

        for i in indices:
            movie_id = movie_ids[i]

            title_row = movies[movies["movieId"] == movie_id]

            if not title_row.empty:
                recommended.append(title_row.iloc[0]["title"])

        return recommended

    except Exception as e:
        return [f"Error: {str(e)}"]


# =========================
# POPULAR MOVIES (FALLBACK)
# =========================
def get_popular_movies(top_n=10):
    return movies["title"].head(top_n).tolist()
