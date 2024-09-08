# Spotify-Analysis

# Spotify Wrapped for New York City 🎵📊🎧

## Overview
This project is an interactive data dashboard built with [Streamlit](https://streamlit.io/) to explore Spotify music trends in New York City. It uses data from the Spotify Million Playlist Dataset, and allows users to analyze song listening habits, discover top artists and tracks, and visualize various trends related to playlists and follower counts.

The dashboard includes the following sections:
1. **Followers Growth Over Years**: A line chart showing the growth in Spotify followers over the years.
2. **Top 10 Artists in 2016**: A bar chart displaying the top 10 artists by number of followers in 2016.
3. **Top 10 Playlists in 2016**: A bar chart highlighting the top 10 Spotify playlists by number of followers in 2016.
4. **Top 10 Tracks in 2016**: A bar chart showing the top 10 tracks by number of followers in 2016.
5. **Top 10 Artists in New York**: A bar chart displaying the top 10 artists in the "New York" playlist by number of followers.
6. **Top 5 Tracks of Wiz Khalifa**: A bar chart visualizing the top 5 tracks of Wiz Khalifa by number of followers.

## Features
- **Interactive Visualization**: The dashboard includes multiple data visualizations using Seaborn and Matplotlib for easy interpretation.
- **Navigation**: A sidebar allows users to switch between different views of the data, from general trends to artist-specific insights.
- **Data Analysis**: The dashboard showcases aggregated data analysis by year, artist, playlist, and song.

## Data
The project uses the following columns from the [Spotify Million Playlist Dataset](https://www.kaggle.com/datasets/spotify/spotify-million-playlist-dataset):
- `playlist_name`: The name of the playlist.
- `collaborative`: Whether the playlist is collaborative.
- `modified_at`: The timestamp when the playlist was last modified.
- `num_tracks`: The number of tracks in the playlist.
- `num_albums`: The number of albums in the playlist.
- `num_followers`: The number of followers for the playlist.
- `artist_name`: The name of the artist.
- `track_name`: The name of the track.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MariamYasser9/Spotify-Analysis.git
   cd spotify-wrapped-nyc
