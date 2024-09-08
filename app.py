import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('spotify_data.csv')

# Convert 'modified_at' to datetime and extract the year
df['modified_at'] = pd.to_datetime(df['modified_at'], unit='s')
df['year'] = df['modified_at'].dt.year

# Set Seaborn style
sns.set(style="whitegrid")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", 
    ['Number of Followers Per Year', 
     'Top 10 Artists by Number of Followers in 2016', 
     'Top 10 Playlists by Number of Followers in 2016',
     'Top 10 Tracks by Number of Followers in 2016', 
     'Top 10 Artists in New York', 
     'Top 5 Tracks of Wiz Khalifa'])

# Number of Followers Per Year
if options == 'Number of Followers Per Year':
    st.title('Number of Followers Per Year')
    followers_per_year = df.groupby('year')['num_followers'].sum().reset_index()
    followers_per_year.columns = ['Year', 'Total_Followers']

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Year', y='Total_Followers', data=followers_per_year, marker='o', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Followers')
    ax.set_title('Followers Growth Over Years')
    
    st.pyplot(fig)

# Top 10 Artists by Number of Followers in 2016
elif options == 'Top 10 Artists by Number of Followers in 2016':
    st.title('Top 10 Artists by Number of Followers in 2016')
    df_2016 = df[df['year'] == 2016]
    top_10_artists_2016 = df_2016.groupby('artist_name')['num_followers'].sum().reset_index()
    top_10_artists_2016 = top_10_artists_2016.sort_values(by='num_followers', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='num_followers', y='artist_name', data=top_10_artists_2016, palette='coolwarm', ax=ax)
    ax.set_xlabel('Number of Followers')
    ax.set_ylabel('Artist Name')
    ax.set_title('Top 10 Artists in 2016')
    ax.invert_yaxis()

    st.pyplot(fig)

# Top 10 Playlists by Number of Followers in 2016
elif options == 'Top 10 Playlists by Number of Followers in 2016':
    st.title('Top 10 Playlists by Number of Followers in 2016')
    df_2016 = df[df['year'] == 2016]
    top_10_playlists_2016 = df_2016.groupby('playlist_name')['num_followers'].sum().reset_index()
    top_10_playlists_2016 = top_10_playlists_2016.sort_values(by='num_followers', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='num_followers', y='playlist_name', data=top_10_playlists_2016, palette='coolwarm', ax=ax)
    ax.set_xlabel('Number of Followers')
    ax.set_ylabel('Playlist Name')
    ax.set_title('Top 10 Playlists in 2016')

    st.pyplot(fig)

# Top 10 Tracks by Number of Followers in 2016
elif options == 'Top 10 Tracks by Number of Followers in 2016':
    st.title('Top 10 Tracks by Number of Followers in 2016')
    df_2016 = df[df['year'] == 2016]
    top_10_tracks_2016 = df_2016.groupby('track_name')['num_followers'].sum().reset_index()
    top_10_tracks_2016 = top_10_tracks_2016.sort_values(by='num_followers', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='num_followers', y='track_name', data=top_10_tracks_2016, palette='coolwarm', ax=ax)
    ax.set_xlabel('Number of Followers')
    ax.set_ylabel('Track Name')
    ax.set_title('Top 10 Tracks in 2016')

    st.pyplot(fig)

# Top 10 Artists in New York
elif options == 'Top 10 Artists in New York':
    st.title('Top 10 Artists by Number of Followers in New York')
    top_10_artists_ny = df[df['playlist_name'] == 'New York'].groupby('artist_name')['num_followers'].sum().reset_index()
    top_10_artists_ny = top_10_artists_ny.sort_values(by='num_followers', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='num_followers', y='artist_name', data=top_10_artists_ny, palette='plasma', ax=ax)
    ax.set_xlabel('Number of Followers')
    ax.set_ylabel('Artist Name')
    ax.set_title('Top 10 Artists in New York')

    st.pyplot(fig)

# Top 5 Tracks of Wiz Khalifa
elif options == 'Top 5 Tracks of Wiz Khalifa':
    st.title('Top 5 Tracks of Wiz Khalifa')
    top_5_tracks_wiz = df[df['artist_name'] == 'Wiz Khalifa'].sort_values(by='num_followers', ascending=False).head(5)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='num_followers', y='track_name', data=top_5_tracks_wiz, palette='viridis', ax=ax)
    ax.set_xlabel('Number of Followers')
    ax.set_ylabel('Track Name')
    ax.set_title('Top 5 Tracks of Wiz Khalifa')

    st.pyplot(fig)
