import requests
import os
import logging
import re

# Specify the folder path
FOLDERPATH = 'C:/Users/chidu/Downloads/projects/music_player/Songs'

# Logging configuration
logging.basicConfig(level=logging.DEBUG)

# Search for a song
def search_song(name):
    url = "https://spotify-scraper.p.rapidapi.com/v1/track/download"
    querystring = {"track": name}
    headers = {
        "X-RapidAPI-Key": "1ae4654528msh82cf9d56f299a41p175eb1jsnebd34a46be13",
        "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'youtubeVideo' in data and 'title' in data['youtubeVideo'] and 'audio' in data['youtubeVideo']:
            song_title = data['youtubeVideo']['title']
            song_title = extract_words(song_title)
            song_audio = data['youtubeVideo']['audio'][0]['url']
            try:
                download_song(song_title, song_audio)
                return True
            except Exception as e:
                logging.error(f"Error downloading song: {e}")
                return False
        else:
            return False
    else:
        logging.error(f"Error {response.status_code}")
        return False


def extract_words(song_name):
    # Define the regex pattern to match words outside parentheses and brackets
    pattern = r'\b(?:\w+(?:\'\w+)?)(?![^\(]*\))(?![^\[]*\])\b'
    # Find all matches of the pattern in the song_name
    matches = re.findall(pattern, song_name)
    # Join the matches into a single string with underscores replacing spaces
    joined_string = '_'.join(matches)
    # Append ".mp3" to the joined string and return
    return f"{joined_string}.mp3"

# Function to download song to a file
def download_song(song_name, song_audio):
    # Make a get request
    response = requests.get(song_audio)
    # Check if the request was successful
    if response.status_code == 200:
        # Join the songname to the folder
        with open(os.path.join(FOLDERPATH, song_name), 'wb') as song:
            song.write(response.content)
        logging.debug("Audio saved")
        return True
    else:
        logging.error(f"Error downloading audio: {response.status_code}")
        return False

# Display the downloaded songs
def list_downloaded_songs():
    filepath = os.listdir(FOLDERPATH)
    songs = [song.split(".")[0] for song in filepath]
    return songs
