from http.client import responses

import streamlit as st
import pickle
import requests

API_KEY = st.secrets["TMDB_API_KEY"]

def fetch_movie_details(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US")
    data = response.json()
    return {
        "id": data["id"],  # ✅ Keep TMDB movie ID
        "poster": "https://image.tmdb.org/t/p/w500" + data["poster_path"],
        "overview": data.get("overview", "No description available."),
        "release_date": data.get("release_date", "N/A"),
        "rating": data.get("vote_average", "N/A"),
        "genres": ", ".join([genre["name"] for genre in data.get("genres", [])])
    }

def recommend (movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1:21]

    recommmended_movies = []
    recommmended_movies_details = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        recommmended_movies.append(movies.iloc[i[0]].title)
        recommmended_movies_details.append(details)

    return recommmended_movies, recommmended_movies_details

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
# similarity = pickle.load(open('similarity_small.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select Movie",movies_list
)

movie_id = movies[movies['title'] == selected_movie_name].iloc[0].movie_id
details = fetch_movie_details(movie_id)

col1, col2 = st.columns([1, 2])
with col1:
    st.image(details["poster"], width=250)

with col2:
    st.markdown(f"### 🎥 {selected_movie_name}")
    st.markdown(f"**Release Date:** {details['release_date']}")
    st.markdown(f"**Genres:** {details['genres'] if details['genres'] else 'N/A'}")

    # IMDb rating with color-coded bar
    if details["rating"] != "N/A":
        rating_value = float(details["rating"])
        bar_width = min(rating_value * 10, 100)

        # Decide color based on rating
        if rating_value >= 7:
            bar_color = "#4CAF50"  # Green for good ratings
        elif rating_value >= 5:
            bar_color = "#FFC107"  # Yellow for average
        else:
            bar_color = "#F44336"  # Red for low ratings

        st.markdown(f"**⭐ IMDb Rating:** {rating_value}/10", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style='background-color: #ddd; border-radius: 10px; height: 15px; width: 100%;'>
                <div style='background-color: {bar_color}; width: {bar_width}%; 
                            height: 100%; border-radius: 10px;'>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("**⭐ IMDb Rating:** N/A")

    st.write(details["overview"])

if st.button("Recommend"):
    with st.spinner("🔍 Fetching recommendations..."):
        names, details_list = recommend(selected_movie_name)

    st.success("✅ Recommendations ready!")

    for i in range(0, len(names), 4):
        cols = st.columns(4)
        for idx, col in enumerate(cols):
            if i + idx < len(names):
                with col:
                    movie = details_list[i + idx]

                    # Make poster clickable & add hover tooltip for overview
                    tmdb_url = f"https://www.themoviedb.org/movie/{movie['id']}"

                    st.markdown(
                        f"""
                        <a href="{tmdb_url}" target="_blank" title="{movie['overview'].replace('"', '').replace("'", '')}">
                             <img src="{movie['poster']}" style="width:100%; border-radius:10px;">

                        </a>
                        """,
                        unsafe_allow_html=True
                    )

                    # Movie title
                    st.markdown(
                        f"<p style='text-align:center; font-size:14px; font-weight:bold;margin-bottom:1px;'>{names[i + idx]}</p>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<p style='text-align:center; font-size:12px; color:gray; margin-bottom:2px'>{movie['release_date'][:4]}</p>",
                        unsafe_allow_html=True
                    )

                    # Genres
                    if movie["genres"]:
                        st.markdown(
                            f"<p style='text-align:center; font-size:12px; color:gray; margin-bottom:2px;'>{movie['genres']}</p>",
                            unsafe_allow_html=True
                        )

                    # Rating bar
                    if movie["rating"] != "N/A":
                        rating_value = float(movie["rating"])
                        bar_width = min(rating_value * 10, 100)
                        bar_color = "#4CAF50" if rating_value >= 7 else "#FFC107" if rating_value >= 5 else "#F44336"

                        st.markdown(
                            f"""
                            <div style='background-color: #ddd; border-radius: 10px; height: 8px; width: 100%; margin-top:1px;'>
                                <div style='background-color: {bar_color}; width: {bar_width}%; height: 100%; border-radius: 10px;'></div>
                            </div>
                            <p style='text-align:center; font-size:12px;margin-top:1px;margin-bottom:2px;'>⭐ {rating_value}/10</p>
                            """,
                            unsafe_allow_html=True
                        )

                        # "More Info" button
                        st.markdown(
                            f"""
                            <a href="{tmdb_url}" target="_blank">
                                <button style='width:100%; margin-top:5px; background:#007BFF; color:white; border:none; padding:5px; border-radius:8px; cursor:pointer;'>
                                    More Info
                                </button>
                            </a>
                            <div style='margin-bottom:20px;'></div>  <!-- Add space below button -->
                            """,
                            unsafe_allow_html=True
                        )