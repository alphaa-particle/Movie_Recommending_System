# 🎬 Movie Recommending System

A simple content-based movie recommendation system that suggests similar movies using the **Bag of Words** model and **CountVectorization**. Enter a movie name into a clean **Streamlit web app**, and get five similar titles instantly!

---

## 📌 Features

- Recommends **5 similar movies** based on the selected title
- Uses **CountVectorizer (Bag of Words)** to analyze textual metadata
- Computes **cosine similarity** between movie vectors
- Built with an interactive **Streamlit interface** for ease of use

---

## 🧠 Techniques Used

- **Text Vectorization**: `CountVectorizer` from `sklearn` to convert text data into vectors
- **Similarity Calculation**: `cosine_similarity` from `sklearn.metrics.pairwise`
- **Web App**: Built using `Streamlit`
- **Data Handling**: `pandas` for data management and preprocessing

---

## 🗂️ Project Structure

```bash
├── Movie_Recommender_Model.ipynb   # Notebook with model development
├── app.py                          # Streamlit app for user interaction
├── movie_dict.pkl                  # Serialized movie dictionary
├── movies.pkl                      # Preprocessed DataFrame with movie data
├── README.md                       # Project documentation
🚀 How It Works
Load and preprocess movie metadata (title, genres, overview, etc.)

Convert metadata into vectors using CountVectorizer

Compute cosine similarity between all movie vectors

User selects a movie from the dropdown; top 5 similar movies are displayed

▶️ Running the Streamlit App
1. Clone the repository
git clone https://github.com/alphaa-particle/Movie_Recommending_System.git
cd Movie_Recommending_System
2. Install dependencies
pip install -r requirements.txt
If requirements.txt is missing:

pip install streamlit pandas scikit-learn
3. Run the Streamlit app
streamlit run app.py
This will open the app in your browser at http://localhost:8501

🧪 Sample Output
🎥 Selected Movie: Avatar

Top 5 Recommendations:
1. Guardians of the Galaxy
2. John Carter
3. Star Trek
4. Ender's Game
5. The Helix... Loaded
💡 Possible Enhancements
Use TF-IDF or Word2Vec for better recommendations

Incorporate movie posters, cast, or user ratings

Add genre filters or a search bar in the app

Merge with collaborative filtering for a hybrid system

🙌 Credits
Developed with ❤️ by alphaa-particle

📄 License
This project is licensed under the MIT License.

