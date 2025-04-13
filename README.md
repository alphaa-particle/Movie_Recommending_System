# 🎬 Movie Recommending System

A content-based movie recommendation system that suggests similar movies using **Bag of Words** (CountVectorizer) and **cosine similarity**. The entire application is built in **Streamlit**, allowing users to interactively select a movie and instantly get five similar movie recommendations.

---

## 🚀 Demo

> ⚡ Launch the app locally using Streamlit — it's fast, lightweight, and easy to use.

---

## 📌 Features

- 🔍 Recommend **5 similar movies** based on content metadata
- 🧠 Uses **CountVectorizer** to implement the **Bag of Words** model
- 📐 Calculates similarity using **cosine similarity**
- 💻 Fully built in **Streamlit** — no separate backend required
- 🧾 Easy to run locally or deploy online (Streamlit Cloud / Hugging Face Spaces)

---

## 🧠 Technologies Used

| Purpose              | Library           |
|----------------------|-------------------|
| Web Framework        | Streamlit         |
| Data Handling        | Pandas            |
| Text Vectorization   | CountVectorizer   |
| Similarity Measure   | cosine_similarity |
| Serialization        | pickle            |

---

## 🗂️ Project Structure

├── app.py # Full Streamlit application (UI + logic) ├── movie_dict.pkl # Dictionary containing movie data ├── movies.pkl # DataFrame with movie metadata ├── README.md # Project documentation


---

📸 App Preview

![image](https://github.com/user-attachments/assets/12dddfa8-58ce-4fb9-855f-b5c7fb35ac01)

Home Screen	Recommendations
💡 How It Works
Load a movie metadata dataset using pandas

Process the textual data and vectorize using CountVectorizer

Compute pairwise cosine similarity scores between movies

User selects a movie → Top 5 similar movies are displayed

🎯 Sample Output
Selected Movie: Avatar

Top 5 Recommendations:
1. Guardians of the Galaxy
2. John Carter
3. Star Trek
4. Ender's Game
5. The Helix... Loaded
🚧 Future Enhancements
🎞️ Add movie posters and links via TMDb API

📊 Use TF-IDF or embedding-based NLP models

🎭 Include genre, cast, and user ratings

🔄 Deploy live on Streamlit Cloud or Hugging Face

🙌 Author
Made with ❤️ by alphaa-particle

📄 License
This project is licensed under the MIT License. Feel free to use and modify it.
