from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load Environment Variables
ENVIORNMENT_PATH = "C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/"
load_dotenv(f"{ENVIORNMENT_PATH}.env.txt")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")
scope = "playlist-modify-private"

# Define Functions
def authenticate_spotify():
    """
    Will use SpotifyOAuth to Authenticate Spotify after a developer's account has been created.
    Returns username and creates a token.txt file with Spotify access token
    """
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri="http://example.com",
            show_dialog=True,
            cache_path=f"{ENVIORNMENT_PATH}token.txt",
            username=SPOTIFY_USERNAME,
        )
    )
    # return authentication object
    return sp
def return_spotify_URI(song_title):
    """Returns a song URI based on an input song title"""
    query = f"track: {song_title} year: {year}"
    try:
        search_object = sp.search(q=query, limit=1, type="track")
        song_uri = search_object['tracks']['items'][0]['uri']
        print(f"Found song: {song_title}")
        return song_uri
    except IndexError:
        print(f"Couldn't Find the song {song_title}. Skipped")
        missing_songs.append(song_title)
        return


def get_input_date() -> str:
    """Get a valid YYYY-MM-DD Date. Returns a Date YYYY-MM-DD"""
    # Loop until a valid date is entered
    while True:
        input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
        try:
            datetime.strptime(input_date, "%Y-%m-%d")
        except ValueError:
            print("This is not a valid date")
        else:
            # Date is valid, break loop
            break
    return input_date

def make_soup(input_date):
    """Takes an input date and returns an html parsed webpage for web scraping"""
    billboard_top_100_url = f"https://www.billboard.com/charts/hot-100/{input_date}/"

    # make HTTP GET request
    response = requests.get(url=billboard_top_100_url)
    # extract text
    billboard_page_text = response.text

    # Create Soup
    soup = BeautifulSoup(billboard_page_text, "html.parser")
    return soup

def return_songs(soup: object) -> list:
    """Returns the top 100 Billboard song titles based on an input date"""
    # First extract all the chart rows to filter out unneeded elements
    chart_rows = soup.find_all(name="ul", class_="o-chart-results-list-row")
    # extract song times by grabbing h3 tags, finding c-title class and the id "title-of-a-story"
    # get text and strip white space for reach song title
    songs = [row.find("h3", class_='c-title', id="title-of-a-story").getText().strip() for row in chart_rows]
    return songs

def create_new_playlist(playlist_name: str) -> str:
    """Take input time travel date and creates a playlist. Will return the playlist id"""
    playlist_object = sp.user_playlist_create(
        user=userid,
        name=playlist_name,
        public=False
                    )
    return playlist_object['id']

def add_songs_to_Spotify_Playlist(playlist_id: str):
    """Will take a list of Spotify URIs and add them to a playlist."""
    try:
        sp.user_playlist_add_tracks(user=userid, playlist_id=playlist_id, tracks=found_songs)
        print(f"Songs added to {Playlist_Name}  Successfully!")
    except ValueError:
        print("That didn't work!")


# Create Time Travel Playlist Script!

# get the input date for time travel
time_travel_date = get_input_date()
# make an GET request using the time travel date
webpage_soup = make_soup(time_travel_date)
# return list of top 100 songs from time travel date
song_list = return_songs(webpage_soup)

# Authenticate Spotify
sp = authenticate_spotify()
# return user id
userid = sp.current_user()['id']

# Extract year to get the right version of the songs
year = datetime.strptime(time_travel_date, "%Y-%m-%d").year

# Create lists to hold missing and found songs
missing_songs = []
found_songs = [return_spotify_URI(song) for song in song_list]

# Create new playlist
Playlist_Name = f"{time_travel_date} Billboard 100"
playlist_id = create_new_playlist(Playlist_Name)

# Add the songs to the Spotify Playlist
add_songs_to_Spotify_Playlist(playlist_id)

print(f"The following song's were not added to the playlist: {missing_songs}")




