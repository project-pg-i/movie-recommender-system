# 🎬 Movie Recommendation System

This is a simple movie recommendation system I built using **collaborative filtering** and **cosine similarity**. It’s based on the popular [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/).

This was one of my first AI/ML projects where I explored how to recommend movies based on user ratings — a great way to get hands-on with real data and basic ML concepts.

---

## 📌 What It Does

- Recommends similar movies using item-based collaborative filtering
- Calculates similarity between movies using cosine similarity
- You can input any movie title and get a list of similar recommendations
- Built using Python libraries like `pandas`, `numpy`, and `scikit-learn`

---

## 📁 Dataset Used

- MovieLens 100k (official site: [GroupLens](https://grouplens.org/datasets/movielens/100k/))
- Main files used:
  - `u.data` – user ratings
  - `u.item` – movie titles

---

## 🗂️ Folder Structure

movie-recommender-system/
├── recommender.py # Main Python file with the recommendation logic
├── README.md # Project overview (this file)
├── requirements.txt # Dependencies list
└── data/
└── ml-100k/
├── u.data # Ratings data
└── u.item # Movie titles

---

## ✅ Requirements

Install dependencies:

```bash
pip install -r requirements.txt


🚀 How to Run It
In your terminal, run:

python recommender.py

You can modify the movie title and number of recommendations at the bottom of recommender.py:

recommend("Star Wars (1977)", num_recommendations=5)

💡 Sample Output

Top 5 recommendations for 'Star Wars (1977)':

1. Return of the Jedi (1983) (Similarity Score: 0.88)
2. Raiders of the Lost Ark (1981) (Similarity Score: 0.76)
3. Empire Strikes Back, The (1980) (Similarity Score: 0.75)
4. Toy Story (1995) (Similarity Score: 0.73)
5. Godfather, The (1972) (Similarity Score: 0.70)

📚 What I Learned

How to work with real-world datasets
Creating pivot tables to structure data
Using cosine similarity for recommendations
Building a basic ML-powered system without deep algorithms

🔄 Future Improvements

If I continue building this, I’d like to:
Add a web UI (maybe with Streamlit)
Try user-based filtering as well
Improve the recommendation quality with more features