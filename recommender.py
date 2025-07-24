import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load the dataset
data_path = "data/ml-100k/"
ratings = pd.read_csv(os.path.join(data_path, "u.data"), sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])
movies = pd.read_csv(os.path.join(data_path, "u.item"), sep="|", encoding="latin-1", usecols=[0, 1], names=["movie_id", "title"])

# Merge datasets
df = pd.merge(ratings, movies, on="movie_id")

# Create pivot table
pivot_table = df.pivot_table(index="user_id", columns="title", values="rating")

# Fill NaN with 0
pivot_table_filled = pivot_table.fillna(0)

# Compute cosine similarity
similarity = cosine_similarity(pivot_table_filled.T)
similarity_df = pd.DataFrame(similarity, index=pivot_table.columns, columns=pivot_table.columns)

# --- ADD THIS FUNCTION ---
def recommend(movie_title, num_recommendations=5, save_to_file=False):
    if movie_title not in similarity_df.columns:
        print(f"'{movie_title}' not found in the movie list.")
        return

    similar_movies = similarity_df[movie_title].sort_values(ascending=False)[1:num_recommendations + 1]

    output_lines = [f"\nTop {num_recommendations} recommendations for '{movie_title}':\n"]

    for i, (title, score) in enumerate(similar_movies.items(), start=1):
        line = f"{i}. {title:<40} [Similarity Score: {score:.2f}]"
        output_lines.append(line)

    output_text = "\n".join(output_lines)
    print(output_text)

    if save_to_file:
        os.makedirs("output", exist_ok=True)
        with open("output/recommendations.txt", "a", encoding="utf-8") as f:
            f.write(output_text + "\n\n")

# --- CALL THE FUNCTION HERE ---
recommend("Star Wars (1977)", num_recommendations=5, save_to_file=True)
