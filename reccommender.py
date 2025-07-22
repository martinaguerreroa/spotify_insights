from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
import pandas as pd

def build_artist_similarity_matrix(df):
    pivot = df.pivot_table(index="artistName", columns="date", values="minPlayed", aggfunc="sum").fillna(0)
    norm = normalize(pivot)
    sim = cosine_similarity(norm)
    return pd.DataFrame(sim, index=pivot.index, columns=pivot.index)

def recommend_artists(artist_name, sim_df, top_n=5):
    if artist_name not in sim_df.index:
        return f"Artist '{artist_name}' not found."
    return sim_df[artist_name].sort_values(ascending=False).iloc[1:top_n+1]
