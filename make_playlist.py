import os
import openai
import spotipy
import json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
openai.api_key = os.environ.get('OPENAI_KEY')

# Spotify API credentials
SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

# Spotify scope for playlist modification
scope = "playlist-modify-public"

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

input_text = """
If you like heavy and melodic: Devin Townsend, The Armed, Myrkur, Torche, ASG. Lots more but those are some favorites. Oh also check out the Conjurer/Pijn collab which should definitely appeal to Baroness fans.



Upvote
16

Downvote
Reply
reply

Award

Share
Share

theironzach
•
2d ago
It’s crazy how much that Conjurer and Pijn collab sounds like the EPs. It’s so dead on that I wonder if it was intentional


Upvote
5

Downvote
Reply
reply

Award

Share
Share

u/lolwut19 avatar
lolwut19
•
1d ago
fucking love ASG. crazy underrated band


Upvote
3

Downvote
Reply
reply

Award

Share
Share

ReliableChicken
•
2d ago
This week - Mastodon, Gojira, Mutoid Man, Sound Garden, Alice in Chains, Tool, Queens of the Stone Age to name but a few



Upvote
16

Downvote
Reply
reply

Award

Share
Share

Relevant_Debt_4331
•
1d ago
Bruh, that’s the exact same bands I listen to except swap mutoid man for red fang lol



Upvote
6

Downvote
Reply
reply

Award

Share
Share

u/tombstone1200 avatar
tombstone1200
•
1d ago
Why not both



Upvote
3

Downvote
Reply
reply

Award

Share
Share

ReliableChicken
•
1d ago
Very true


Upvote
1

Downvote
Reply
reply

Award

Share
Share

ReliableChicken
•
1d ago
lol it was a mutoid man or red fang, mutoid won out due to Baroness appearing on 2 minutes to midnight covering purple rain, YouTube clip


Upvote
2

Downvote
Reply
reply

Award

Share
Share

fucjin
•
1d ago
These are all very correct.


Upvote
2

Downvote
Reply
reply

Award

Share
Share

eduardopinto
•
2d ago
Viagra boys and idles



Upvote
19

Downvote
Reply
reply

Award

Share
Share

chaosarcadeV2
•
2d ago
Oft if you love those bands I recommend checking out Amyl and the Sniffers


Upvote
5

Downvote
Reply
reply

Award

Share
Share

u/donny_chang avatar
donny_chang
•
2d ago
Alcest, Jeff Buckley, old CKY. Wide variety


Upvote
7

Downvote
Reply
reply

Award

Share
Share

u/Lakai1983 avatar
Lakai1983
•
2d ago
David Bowie Bruno Mars Tyler Childers Run the Jewels MF Doom. I’m kinda all over the place. I don’t like any one genre. I like specific artists and sometimes only specific songs or albums. I mean there are several of the usual bands a Baroness fan would probably be into that I am heavily into myself but these seem to fit the non obvious category.


Upvote
6

Downvote
Reply
reply

Award

Share
Share

juanprada
•
2d ago
I discovered Cloud Rat last week and I've been listening to them non-stop.


Upvote
5

Downvote
Reply
reply

Award

Share
Share

jdc3000
•
2d ago
Today I listened to Rakim, Cannonball Adderly, YOB, and Gojira


Upvote
5

Downvote
Reply
reply

Award

Share
Share

u/Chernobog3 avatar
Chernobog3
•
2d ago
Devin Townsend, Alcest, The Gathering, Clutch, Grateful Dead, Florence and the Machine


Upvote
5

Downvote
Reply
reply

Award

Share
Share

u/bad_actor avatar
bad_actor
•
2d ago
Callous Daoboys, Aesop Rock, HEALTH, and Dillinger are my next-most frequent listens


Upvote
4

Downvote
Reply
reply

Award

Share
Share

wewontstaydead
•
2d ago
Amigo the Devil, Danzig, Blood Command, Pup, Fit for An Autopsy



Upvote
4

Downvote
Reply
reply

Award

Share
Share

u/doomtoflesh avatar
doomtoflesh
•
2d ago
I always think it's a shame Blood Command didnt catch on more (at least in America). Great band



Upvote
2

Downvote
Reply
reply

Award

Share
Share

wewontstaydead
•
2d ago
I live in the US and yeah they don't have much of a fan base here


Upvote
1

Downvote
Reply
reply

Award

Share
Share

Whistler45
•
2d ago
Old gojira, old mastadon, old Metallica, old kylesa, old lamb of god, old ISIS, old tool. old baroness



Upvote
4

Downvote
Reply
reply

Award

Share
Share

theironzach
•
2d ago
Old



Upvote
1

Downvote
Reply
reply

Award

Share
Share

Whistler45
•
2d ago
You know it’s old when two of the bands I listed broke up almost a decade ago and still think there’s a difference in old and new for them. All isis is old all kylesa is old, but not to me… so old



Upvote
3

Downvote
Reply
reply

Award

Share
Share

u/BonerJamz98 avatar
BonerJamz98
•
1d ago
Fan of Black Tusk?



Upvote
1

Downvote
Reply
reply

Award

Share
Share

Whistler45
•
1d ago
Old Black Tusk, before Jonathan Athon died. They kinda fell off for me after that. I’ve seen em a few times. I remember seeing them at 25 watt in RVA, they played right after the Slayer show ended at the national, we went from slayer to downtown for Black Tusk. There was probably 12 people there because everyone went to slayer. They played like 3 songs and then said “fuck this we’re done” because of the terrible turn out. They got heckled a bunch for quitting on the set, stuff like “you’d never make it in RVA!” It was funny but kinda the breaking point of when I stopped listening to them.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/EffectiveAmbitious53 avatar
EffectiveAmbitious53
•
2d ago
Hall and Oates

Sneaker Pimps

Babybird

Depeche Mode

Fiona Apple.


Upvote
4

Downvote
Reply
reply

Award

Share
Share

Jefftaint
•
2d ago
Lankum. Dark Irish folk that inspired some of the vocals on Stone.



Upvote
3

Downvote
Reply
reply

Award

Share
Share

originalface1
•
2d ago
Minor flex, their singer (the real punk looking guy) was at a gig I played a few weeks back lol.


Upvote
2

Downvote
Reply
reply

Award

Share
Share

cantankerosaurus
•
2d ago
Since a few weeks I have listened a lot to Fontaines D.C. and Idles. Only discovered them this year... Besides that: Zeal & Ardor, Queens of the Stone Age, Brutus, All Them Witches, Mogwai, Clutch,...


Upvote
3

Downvote
Reply
reply

Award

Share
Share

u/porkchopexpress76 avatar
porkchopexpress76
•
1d ago
Devin Townsend has been my favorite artist since the mid 90’s.

Dillinger, Converge, Cave In, Botch I’m sure aren’t controversial. But I love grindcore. Nasum, Rotten Sound, Wormrot, Insect Warfare. PV like Nails, Weekend Nachos, Iron Lung, Spazz, The Locust etc.

As far as non obvious, love Springsteen, Tom Waits, Dylan, Nick Cave, PJ Harvey, Sonic Youth, Sigur Ros, Amon Tobin, Autechre, Boards of Canada.

I can’t think of too much that’s a total 180 from Baroness except Elvis I guess. An ex got me into his music and against my will it stuck. Johnny Cash and Willie Nelson too.


Upvote
3

Downvote
Reply
reply

Award

Share
Share

Gullible-Box7637
•
2d ago
Recently i have really gotten into Electric Masada



Upvote
2

Downvote
Reply
reply

Award

Share
Share

weinerzz
•
2d ago
Yesss, I've been getting into John Zorn a lot and his collabs with Yamataka Eye


Upvote
4

Downvote
Reply
reply

Award

Share
Share

SunOfInti_92
•
2d ago
Northlane


Upvote
2

Downvote
Reply
reply

Award

Share
Share

u/cbseip13 avatar
cbseip13
•
2d ago
Frank Turner, Kishi Bashi, and Josh Ritter are three of my favorite artists. I listen to them as much as Baroness.


Upvote
2

Downvote
Reply
reply

Award

Share
Share

chaosarcadeV2
•
2d ago
All them witches is another great band. Very unique sound and they touch on a range of high energy and a lot of quiet relaxing songs. Definitely worth looking up their KEXP performances.


Upvote
2

Downvote
Reply
reply

Award

Share
Share

macoily
•
1d ago
Been getting into coheed and Cambria recently, really groovy stuff


Upvote
2

Downvote
Reply
reply

Award

Share
Share

traumsturm
•
1d ago
Hecc, I listen to so many of the brands listed already. Dreamwell, Destroy Boys, Faetooth, Worriers, Emma Ruth Rundle, Thou, Blood Incantation, Big|Brave, Mannequin Pussy, King Woman



Upvote
2

Downvote
Reply
reply

Award

Share
Share

originalmetathought
•
21h ago
I loooooooove ERR!


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/rufusness avatar
rufusness
•
21h ago
Fugazi. And I think there are some similarities. Not many, but some.


Upvote
2

Downvote
Reply
reply

Award

Share
Share

u/mebetiffbeme avatar
mebetiffbeme
•
15h ago
Thank you for organizing them!


Upvote
2

Downvote
Reply
reply

Award

Share
Share

cameronrichardson77
•
2d ago
Coheed, Tool, Mastodon


Upvote
2

Downvote
Reply
reply

Award

Share
Share

Rubes27
•
2d ago
I’m a huge Avett Brothers fan.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/No-Breakfast4481 avatar
No-Breakfast4481
•
2d ago
Opeth


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/ddeeny avatar
ddeeny
•
2d ago
Zeal and Ardor, Glass Animals, Childish Gambino, Cults the last couple of weeks


Upvote
1

Downvote
Reply
reply

Award

Share
Share

psychedelicdevilry
•
2d ago
Tauk, Dopapod, Machine Head, Blackbraid, John Scofield, Gojira


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/FacelessLord1 avatar
FacelessLord1
•
2d ago
Grateful Dead is my favourite band of all time. I also would say John Cale fits into non obvious, Parquet Courts too.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

_Doos
•
2d ago
Some of the Yellow/Green era Baroness reminds me of Beck's early era. Check out the Mellow Gold album. Skip 'Loser' if you're over it but the rest of it is pretty fun.



Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/arashikagedropout avatar
arashikagedropout
•
2d ago
I respect your opinion, but I just don't see (hear) it.


Upvote
2

Downvote
Reply
reply

Award

Share
Share

u/arashikagedropout avatar
arashikagedropout
•
2d ago
Lately - Viagra Boys (live Shrimp Sessions actually sound better than their albums), Plague Vendor, lcd soundsystem, and Careless Whisper by George Michael when I want to sing something at the top of my lungs while driving. Lol


Upvote
1

Downvote
Reply
reply

Award

Share
Share

Sat147Li197
•
2d ago
Anekdoten, King Crimson, Rory Gallagher, Cult of Luna, AmenRa... Too many to write them all... And so various...


Upvote
1

Downvote
Reply
reply

Award

Share
Share

Frydog42
•
2d ago
RISHLOO - One of my absolute favorites. I love the growth of their sound and musicianship each album brings.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

SenhorPopoto
•
1d ago
King Gizzard and The Lizard Wizard (new record out tomorrow btw)


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/Chromaticon11 avatar
Chromaticon11
•
1d ago
I'm more of a proghead, actually. So Dream Theater, Pain of Salvation, Fates Warning... And some stuff out of the line: woods of Ypres, Rammstein, Shores of Null, Megadeth, Metallica, UneXpect.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

CoffeeToDeath
•
1d ago
Been listening to a lot of Sub Rosa, Khanate and Nadja lately.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

w0nga7
•
1d ago
Recently I've been obsessed with Cory Wong, Esperanza Spalding, and Alan Parsons Project


Upvote
1

Downvote
Reply
reply

Award

Share
Share

too_old_4_this_crap
•
1d ago
Ethel Cain


Upvote
1

Downvote
Reply
reply

Award

Share
Share

BeNiceMudd
•
1d ago
Kurt Vile, The Velvet Underground, Idles, Dr. Dog are all in rotation. I like some Miles Davis thrown in too.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

MemphisFoo
•
1d ago
Foo Fighters. Almost every band I hear has some connection back to Dave Grohl. Queens for obvious reasons, but Josh Homme intro’d me to Mastodon, Mastodon intro’d me to Baroness, Kvelertak, Zeal and Ardor, Gojira, Kylesa, Dillinger Escape Plan.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

eriniva
•
1d ago
Silverstien has been a favorite of mine for the better part of the last 20 years


Upvote
1

Downvote
Reply
reply

Award

Share
Share

JomLofty
•
1d ago
Kylesa


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/JGL_302 avatar
JGL_302
•
1d ago
311


Upvote
1

Downvote
Reply
reply

Award

Share
Share

RedditAwesome2
•
1d ago
I think they’re within the same realm as Clutch~


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/ohno_raptors avatar
ohno_raptors
•
23h ago
Love Baroness and love Trampled by Turtles too! I will add a few of my favorite bands that I didn't see on the list: Gunship, Haken, Russian Circles, and Dinosaur Jr.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

originalmetathought
•
21h ago
You just named a ton of shit I listen to


Upvote
1

Downvote
Reply
reply

Award

Share
Share

Local_Outcome_4835
•
17h ago
Add Sasquatch on there while you’re at it! I was listening to Clutch and started looking through Spotify’s recommendations, came across “Rational Woman” by them and my god have I become a fan.


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/de1m0nte avatar
de1m0nte
•
14h ago
The Disco Biscuits


Upvote
1

Downvote
Reply
reply

Award

Share
Share

u/Bendaario avatar
Bendaario
•
5h ago
This will shock people, but I've been very into Chapelle Roan and A Perfect Circle lately

Most names on here I already listen to as well


"""

# Cache file paths
BAND_NAME_CACHE_FILE = 'band_name_cache.json'
SONG_CACHE_FILE = 'song_cache.json'
TRACK_CACHE_FILE = 'track_cache.json'

# Load caches from files
if os.path.exists(BAND_NAME_CACHE_FILE):
    with open(BAND_NAME_CACHE_FILE, 'r') as f:
        band_name_cache = json.load(f)
else:
    band_name_cache = {}

if os.path.exists(SONG_CACHE_FILE):
    with open(SONG_CACHE_FILE, 'r') as f:
        song_cache = json.load(f)
else:
    song_cache = {}

if os.path.exists(TRACK_CACHE_FILE):
    with open(TRACK_CACHE_FILE, 'r') as f:
        track_cache = json.load(f)
else:
    track_cache = {}

def extract_band_names(text):
    # Check if result is already in the cache
    if text in band_name_cache:
        print("Using cached band names.")
        return band_name_cache[text]

    # Send the conversation to OpenAI API using the chat completion format
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant that extracts band names from text in json array format."},
            {"role": "user", "content": f"Extract a list of band names from the following text:\n{text}\n\nBand names:"}
        ],
        response_format={"type": "json_object"}
    )

    # Parse the JSON response
    band_names = json.loads(response.choices[0].message['content'])

    # Store the result in the cache and save to file
    band_name_cache[text] = band_names
    with open(BAND_NAME_CACHE_FILE, 'w') as f:
        json.dump(band_name_cache, f)

    return band_names

def get_most_popular_song(artist_name):
    # Check if result is already in the cache
    if artist_name in song_cache:
        print(f"Using cached song for {artist_name}.")
        return song_cache[artist_name]

    # Search for the artist on Spotify and get their most popular song
    results = sp.search(q=artist_name, type='artist')
    if results['artists']['items']:
        artist_id = results['artists']['items'][0]['id']
        top_tracks = sp.artist_top_tracks(artist_id)
        if top_tracks['tracks']:
            most_popular_song = top_tracks['tracks'][0]['name']
            song_cache[artist_name] = most_popular_song
            # Save to cache file
            with open(SONG_CACHE_FILE, 'w') as f:
                json.dump(song_cache, f)
            return most_popular_song

    # Cache None if no song is found
    song_cache[artist_name] = None
    with open(SONG_CACHE_FILE, 'w') as f:
        json.dump(song_cache, f)
    return None

def get_track_id(song, artist):
    # Check if track is already in the cache
    track_key = f"{song}_{artist}"
    if track_key in track_cache:
        print(f"Using cached track ID for {song} by {artist}.")
        return track_cache[track_key]

    # Search for the track on Spotify
    track_results = sp.search(q=f'track:{song} artist:{artist}', type='track')
    if track_results['tracks']['items']:
        track_id = track_results['tracks']['items'][0]['id']
        track_cache[track_key] = track_id
        # Save to cache file
        with open(TRACK_CACHE_FILE, 'w') as f:
            json.dump(track_cache, f)
        return track_id

    # Cache None if no track ID is found
    track_cache[track_key] = None
    with open(TRACK_CACHE_FILE, 'w') as f:
        json.dump(track_cache, f)
    return None


def create_spotify_playlist(user_id, playlist_name, track_ids):
    # Create a new playlist on Spotify
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    playlist_id = playlist['id']

    # Spotify limits the number of tracks you can add at once to 100
    chunk_size = 100
    for i in range(0, len(track_ids), chunk_size):
        chunk = track_ids[i:i + chunk_size]
        try:
            sp.playlist_add_items(playlist_id=playlist_id, items=chunk)
        except spotipy.exceptions.SpotifyException as e:
            print(f"An error occurred while adding tracks: {e}")
            continue  # Skip to the next chunk if there's an error

    return playlist['external_urls']['spotify']


def main():
    # Extract band names
    band_names = extract_band_names(input_text)
    print(f"Extracted band names: {band_names}")

    # Get the most popular songs and their track IDs
    track_ids = []
    for band in band_names['bands']:
        song = get_most_popular_song(band)
        if song:
            track_id = get_track_id(song, band)
            if track_id:
                track_ids.append(track_id)

    if track_ids:
        # Create the Spotify playlist
        user_id = sp.current_user()['id']
        playlist_name = "YourBaroness - Non obvious bands you like"
        playlist_url = create_spotify_playlist(user_id, playlist_name, track_ids)
        print(f"Playlist created: {playlist_url}")
    else:
        print("No songs found to add to the playlist.")

if __name__ == "__main__":
    main()
