# r/YourBaroness Inspired Playlist Generator

A Python-based application inspired by a Reddit post on r/YourBaroness. I asked for music recommendations similar to Baroness, which led to a rich thread of responses from the community. This application takes those recommendations, processes them, and creates a Spotify playlist featuring popular tracks from the mentioned bands.

## Features

- **Text Analysis:** Utilizes OpenAI's API to extract band names from a given text input.
- **Caching:** Implements caching for band names, song names, and track IDs to minimize redundant API calls and enhance performance.
- **Spotify Integration:** Interacts with the Spotify API to fetch the most popular songs for each band and compiles them into a playlist.

## How to Run

### Prerequisites

- Python 3.x
- Spotify Developer Account for API credentials
- OpenAI API key
- Flask (for web server functionality)
- Required Python libraries:
  - `spotipy`
  - `python-dotenv`
  - `openai`

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/PlaylistGPT.git
   cd PlaylistGPT
   ```

2. **Install the Dependencies:**

   ```bash
   pip install spotipy python-dotenv openai Flask
   ```

3. **Set Up Environment Variables:**

   Create a `.env` file in the project root directory and add your Spotify and OpenAI API credentials:

   ```
   OPENAI_KEY=your_openai_api_key
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

### Running the Application

1. **Start the Flask Server:**

   The `app.py` script initializes a Flask web server for Spotify authentication.

   ```bash
   python app.py
   ```

   - Navigate to `http://localhost:8888` in your browser and complete the Spotify authentication process.

2. **Generate a Spotify Playlist:**

   Once authenticated, you can run the `make_playlist.py` script to generate the playlist based on the extracted band names.

   ```bash
   python make_playlist.py
   ```

   - This script will read the input text, extract band names, retrieve their most popular songs, and create a playlist on your Spotify account.

### Maintaining the Application

- **Caching:** The application uses JSON files for caching band names, songs, and track IDs. These files (`band_name_cache.json`, `song_cache.json`, `track_cache.json`) are automatically updated with each execution. To refresh the cache, simply delete these files.

- **API Key Management:** Ensure your API keys in the `.env` file are kept secure and are regularly rotated as per best security practices.

- **Dependencies:** Periodically check for updates to the `spotipy`, `openai`, and `Flask` libraries to ensure compatibility with Spotify and OpenAI API changes.

- **Custom Input:** Modify the `input_text` variable in `make_playlist.py` with different text to generate playlists based on other Reddit threads or text sources.

## Contributions

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are always welcome!

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

Enjoy creating personalized playlists inspired by your favorite bands and the r/YourBaroness community! 🎸🎶
---

