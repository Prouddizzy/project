import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Proud
# Part 1
songs_file = "songs-of-10s.csv"
genres_file = "genres-of-10s.csv"

songs_df = pd.read_csv(songs_file)
genres_df = pd.read_csv(genres_file)

# Part 2
print("Number of Rows and Columns:", songs_df.shape)

num_rows = input("Enter number of rows to display: ")
print(songs_df.head(int(num_rows)))

# Part 3
joined_df = songs_df.set_index('artist').join(genres_df.set_index('artist'))
grouped_data = joined_df.groupby('genre').agg(
    num_songs=('track', 'count'),
    mean_danceability=('danceability', 'mean'),
    mean_energy=('energy', 'mean'),
    mean_valence=('valence', 'mean'),
    mean_tempo=('tempo', 'mean')
)
print("Grouped Data:")
print(grouped_data.head())

#handling missing values
joined_df.dropna(inplace=True)

# Number of hits/flops 
num_hits = joined_df[joined_df['hit/flop'] == 'hit'].shape[0]
num_flops = joined_df[joined_df['hit/flop'] == 'flop'].shape[0]
print("Number of hits:", num_hits)
print("Number of flops:", num_flops)

# Top 5 artists 
top_artists = joined_df.groupby('artist').size().reset_index(name='count').sort_values('count', ascending=False).head(5)
print("Top 5 artists with most songs:")
print(top_artists)

# Part 4
grouped_hits_flops = joined_df.groupby('hit/flop').agg(
    mean_danceability=('danceability', 'mean'),
    mean_energy=('energy', 'mean'),
    mean_valence=('valence', 'mean'),
    mean_tempo=('tempo', 'mean'),
    std_danceability=('danceability', 'std'),
    std_energy=('energy', 'std'),
    std_valence=('valence', 'std'),
    std_tempo=('tempo', 'std')
)

print("Grouped Data by Hit/Flop:")
print(grouped_hits_flops)

# Hits/flops histogram
joined_df['hit/flop'].hist()
plt.title('Hits/Flops Histogram')
plt.xlabel('Hit/Flop')
plt.ylabel('Frequency')
plt.show()

#  Genre Bar Chart
genres_data = joined_df['genre'].value_counts()[:10]
genres_data.plot(kind='bar')
plt.title('Top 10 Genres')
plt.ylabel('Song Count')
plt.show()
