# 🎬 Movie Recommender System (Beginner Project)

This is a **very basic movie recommender system** I built while learning about recommender systems. I followed a CampusX tutorial to understand how content-based filtering works using cosine similarity.

It's not fancy, it's not perfect — just a simple learning project to get my hands dirty.

---

## 🤖 What It Does

- Takes a movie name as input  
- Finds and recommends a few similar movies  
- Works by comparing movie "tags" using cosine similarity  
- That's it. No magic. No deep learning. Just plain logic and learning.

---

## 📦 Built With

- Python  
- Pandas  
- Scikit-learn  
- Pickle (for saving similarity matrix)  
- Streamlit *(optional, if running as a web app)*

---

## 📂 Files Included

- `app.py` and `Movie Recommender System.ipynb` – main code  
- `movie_dict.pkl` – movie data stored as a dictionary
- `README.md` – you're reading it  
- `requirements.txt` – dependencies

## 📂 Files *Not* Included

- `similarity.pkl` – Precomputed similarity scores  
  ⚠️ Not uploaded due to file size limit (25MB). You can either:
  - Recompute it at runtime (recommended for small datasets), or
  - Generate it locally using the script.

---

## 🚧 Disclaimer

This project is **just for learning purposes**.  
It doesn’t use any real user data, ratings, or advanced techniques.  
Better, smarter, more interesting projects are on the way — this was just step one.

---

## 🙏 Thanks

- Big thanks to [CampusX](https://www.youtube.com/c/CampusX) for the tutorial  
- Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
