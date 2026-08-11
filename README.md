# 🎬 Movie Recommendation System

A content-based **Movie Recommendation System** built with **Python, Streamlit, and the TMDB API**.
The application recommends movies similar to a selected movie and displays relevant movie information and posters.

## 🚀 Live Demo

👉 **[Try the Movie Recommendation System](https://movie-recommendation-system124.streamlit.app/)**


## ✨ Features

* 🎥 Select a movie and get similar movie recommendations
* 🔍 Movie search/selection interface
* 🖼️ Fetches movie posters using the TMDB API
* 🤖 Content-based recommendation system
* ⚡ Interactive Streamlit web interface
* 📱 Simple and user-friendly design

## 🛠️ Technologies Used

* **Python**
* **Pandas** — Data manipulation
* **NumPy** — Numerical operations
* **Streamlit** — Web application framework
* **Requests** — API requests
* **TMDB API** — Movie information and posters
* **Pickle** — Loading pre-trained recommendation data
* **Git & Git LFS** — Version control and large file management

## 🧠 How It Works

The recommendation system uses a **content-based filtering approach**.

1. Movie data is processed to create feature representations.
2. Similarity between movies is calculated.
3. The resulting similarity matrix is stored in `similarity.pkl`.
4. When a user selects a movie, the system finds movies with the highest similarity scores.
5. The TMDB API is used to retrieve movie posters and additional information.
6. The recommended movies are displayed through the Streamlit interface.

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py                  # Main Streamlit application
├── movies.pkl              # Processed movie data
├── similarity.pkl          # Movie similarity matrix
├── requirements.txt        # Python dependencies
├── .gitattributes          # Git LFS configuration
├── .gitignore              # Ignored files and secrets
└── README.md               # Project documentation
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ItsMaryamAsad/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your TMDB API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

**Never commit your API key to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔐 API Key & Security

This project uses the **TMDB API** to retrieve movie information and posters.

The API key is stored using Streamlit secrets and is intentionally excluded from the GitHub repository.

If you run the project locally, create your own `secrets.toml` file and add your TMDB API key.

## 📦 Large Files

The `similarity.pkl` file is a large machine-learning data file and is managed using **Git Large File Storage (Git LFS)**.

To work with the repository, make sure Git LFS is installed:

```bash
git lfs install
```

Then clone the repository normally.

## 🎯 Future Improvements

* ⭐ Add movie ratings and genres
* 🎭 Add genre-based filtering
* 🔥 Display trending movies
* 📊 Improve recommendation accuracy
* 📱 Improve mobile responsiveness
* 🌙 Add dark/light theme options
* ❤️ Allow users to create a favorites list

## 👩‍💻 Author

**Maryam Asad**

Software Engineering Student

---

⭐ If you found this project interesting, consider giving the repository a star!
