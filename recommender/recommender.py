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
    """
    Remove year (1999), lowercase, strip spaces
    """
    return re.sub(r"\(\d{4}\)", "", title).strip().lower()


# =========================
# PREPROCESS MOVIES (ONE TIME)
# =========================
if "clean_title" not in movies.columns:
    movies["clean_title"] = movies["title"].apply(clean_title)


# =========================
# GET MOVIE INDEX (NOT ID ⚠️)
# =========================
def get_movie_index(movie_name):
    """
    Return index position (used by KNN model)
    """

    movie_name_clean = clean_title(movie_name)

    # exact match
    exact_match = movies[movies["clean_title"] == movie_name_clean]
    if not exact_match.empty:
        movie_id = exact_match.iloc[0]["movieId"]

        if movie_id in movie_ids:
            return movie_ids.index(movie_id)

    # partial match
    partial_match = movies[movies["clean_title"].str.contains(movie_name_clean)]
    if not partial_match.empty:
        movie_id = partial_match.iloc[0]["movieId"]

        if movie_id in movie_ids:
            return movie_ids.index(movie_id)

    return None


# =========================
# MAIN RECOMMENDER 🔥
# =========================
def recommend_movies(movie_name, top_n=10):
    try:
        idx = get_movie_index(movie_name)

        # ❌ movie not found
        if idx is None:
            return get_popular_movies(top_n)

        # 🔥 KNN search
        distances, indices = model.kneighbors(
            [model._fit_X[idx]],
            n_neighbors=top_n + 1
        )

        # remove itself
        indices = indices[0][1:]

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
    """
    fallback if movie not found
    """
    return movies["title"].head(top_n).tolist()
