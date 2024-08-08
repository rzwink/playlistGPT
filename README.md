# PlaylistGPT

PlaylistGPT is a Python script that automatically generates Spotify playlists based on band names mentioned in any given text. It uses OpenAI's GPT model to extract band names from text and the Spotipy library to fetch their most popular tracks on Spotify.

## Features

- **Band Name Extraction:** PlaylistGPT identifies band names from generalized text input using OpenAI's API.
- **Caching Mechanism:** The script caches band names, song names, and track IDs to enhance performance and minimize redundant API calls.
- **Spotify Playlist Generation:** It retrieves the most popular tracks for the identified bands from Spotify and compiles them into a playlist.

## Requirements

- Python 3.x
- OpenAI Python client
- Spotipy library
- dotenv library

## Setup

1. Clone this repository.
2. Install the required Python packages: `pip install openai spotipy python-dotenv`.
3. Create a `.env` file with your OpenAI API key and Spotify API credentials:
   ```
   OPENAI_KEY=your_openai_key
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
   ```
4. Run the script: `python playlist_gpt.py`.

## How It Works

1. **Input Text:** Provide any generalized text input that may include mentions of band names.
2. **Band Name Extraction:** PlaylistGPT utilizes OpenAI's API to parse the text and extract band names.
3. **Popular Track Retrieval:** The script then queries Spotify to get the most popular track for each identified band.
4. **Playlist Creation:** It creates a Spotify playlist with the retrieved tracks and provides the playlist URL.

## Usage

Simply run the script with a text input containing potential band names, and PlaylistGPT will handle the rest, delivering a Spotify playlist tailored to the mentioned bands.

## Notes

- Make sure your Spotify API credentials are set up correctly to authenticate and create playlists.
- The script is designed to be robust, skipping over bands or tracks that cannot be found on Spotify.

Enhance your music discovery and create unique playlists effortlessly with PlaylistGPT!