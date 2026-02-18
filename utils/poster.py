import requests
import streamlit as st

# =========================
# LOAD API KEY (SAFE 🔐)
# =========================
API_KEY = st.secrets.get("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


# =========================
# HELPER: SEARCH MOVIE
# =========================
def search_movie(movie_name):
    """
    Search movie in TMDB and return first result
    """
    if not API_KEY:
        return None  # prevents crash if key missing

    try:
        url = f"{BASE_URL}/search/movie"
        params = {
            "api_key": API_KEY,
            "query": movie_name
        }

        response = requests.get(url, params=params, timeout=5)

        # check valid response
        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("results"):
            return data["results"][0]

    except Exception:
        pass

    return None


# =========================
# FETCH POSTER 🎬
# =========================
@st.cache_data(show_spinner=False)
def fetch_poster(movie_name):
    """
    Get movie poster URL
    """
    movie = search_movie(movie_name)

    if movie and movie.get("poster_path"):
        return f"{IMAGE_BASE}{movie['poster_path']}"

    return None


# =========================
# FETCH TRAILER 🎥
# =========================
@st.cache_data(show_spinner=False)
def fetch_trailer(movie_name):
    """
    Get YouTube trailer URL
    """
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

        if data.get("results"):
            # first try trailer
            for vid in data["results"]:
                if vid["type"] == "Trailer" and vid["site"] == "YouTube":
                    return f"https://www.youtube.com/watch?v={vid['key']}"

            # fallback: teaser (nice touch 🔥)
            for vid in data["results"]:
                if vid["site"] == "YouTube":
                    return f"https://www.youtube.com/watch?v={vid['key']}"

    except Exception:
        pass

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
        params = {"api_key": API_KEY}

        data = requests.get(url, params=params, timeout=5).json()

        return [m["title"] for m in data.get("results", [])[:10]]

    except Exception:
        return []


# =========================
# FETCH MOVIES BY GENRE 🎬
# =========================
# TMDB Genre IDs
GENRE_MAP = {
    "action": 28,
    "drama": 18,
    "romance": 10749
}

@st.cache_data(show_spinner=False)
def fetch_movies_by_genre(genre_name):
    if not API_KEY:
        return []

    try:
        genre_id = GENRE_MAP.get(genre_name.lower())

        url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": API_KEY,
            "with_genres": genre_id,
            "sort_by": "popularity.desc"
        }

        data = requests.get(url, params=params, timeout=5).json()

        return [m["title"] for m in data.get("results", [])[:10]]

    except Exception:
        return []