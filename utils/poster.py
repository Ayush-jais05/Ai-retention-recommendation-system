import requests
import streamlit as st
import re

# =========================
# LOAD API KEY 🔐
# =========================
API_KEY = st.secrets.get("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


# =========================
# CLEAN MOVIE NAME 🔥
# =========================
def clean_movie_name(name):
    return re.sub(r"\(\d{4}\)", "", name).strip()


def extract_year(name):
    match = re.search(r"\((\d{4})\)", name)
    return match.group(1) if match else None


# =========================
# SEARCH MOVIE (SMART 🔥)
# =========================
def search_movie(movie_name):
    if not API_KEY:
        return None

    try:
        year = extract_year(movie_name)
        movie_name = clean_movie_name(movie_name)

        url = f"{BASE_URL}/search/movie"

        params = {
            "api_key": API_KEY,
            "query": movie_name,
            "include_adult": False,
            "language": "en-US"
        }

        if year:
            params["year"] = year

        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()
        results = data.get("results", [])

        if not results:
            return None

        # 🎯 sort by popularity (better match)
        results = sorted(results, key=lambda x: x.get("popularity", 0), reverse=True)

        return results[0]

    except Exception:
        return None


# =========================
# FETCH POSTER 🎬
# =========================
@st.cache_data(show_spinner=False)
def fetch_poster(movie_name):
    movie = search_movie(movie_name)

    if movie and movie.get("poster_path"):
        return f"{IMAGE_BASE}{movie['poster_path']}"

    return None


# =========================
# FETCH TRAILER 🎥
# =========================
@st.cache_data(show_spinner=False)
def fetch_trailer(movie_name):
    if not API_KEY:
        return None

    try:
        movie = search_movie(movie_name)

        if not movie:
            return None

        movie_id = movie["id"]

        url = f"{BASE_URL}/movie/{movie_id}/videos"
        params = {"api_key": API_KEY}

        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()
        results = data.get("results", [])

        if not results:
            return None

        # 🎯 prefer trailer
        for vid in results:
            if vid["type"] == "Trailer" and vid["site"] == "YouTube":
                return f"https://www.youtube.com/watch?v={vid['key']}"

        # fallback
        for vid in results:
            if vid["site"] == "YouTube":
                return f"https://www.youtube.com/watch?v={vid['key']}"

    except Exception:
        return None

    return None


# =========================
# FETCH TRENDING 🔥
# =========================
@st.cache_data(show_spinner=False)
def fetch_trending_movies():
    if not API_KEY:
        return []

    try:
        url = f"{BASE_URL}/trending/movie/day"
        params = {"api_key": API_KEY, "language": "en-US"}

        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            return []

        data = response.json()

        return [m["title"] for m in data.get("results", [])[:10]]

    except Exception:
        return []


# =========================
# GENRE MAP 🎬 (FIXED ✅)
# =========================
GENRE_MAP = {
    "action": 28,
    "drama": 18,
    "romance": 10749,
    "horror": 27,
    "comedy": 35,
    "scifi": 878
}


# =========================
# FETCH MOVIES BY GENRE 🎬
# =========================
@st.cache_data(show_spinner=False)
def fetch_movies_by_genre(genre_name):
    if not API_KEY:
        return []

    try:
        genre_id = GENRE_MAP.get(genre_name.lower())

        # ❌ important fix
        if not genre_id:
            return []

        url = f"{BASE_URL}/discover/movie"

        params = {
            "api_key": API_KEY,
            "with_genres": genre_id,
            "sort_by": "popularity.desc",
            "language": "en-US",
            "include_adult": False
        }

        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            return []

        data = response.json()

        return [m["title"] for m in data.get("results", [])[:10]]

    except Exception:
        return []
