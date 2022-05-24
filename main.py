# import spotipy as spotify
# import applemusicpy as apple
# import setup
# song = input()

# def checkProvider(link):
#     if "spotify" in link:
#         provider = "spotify"
#     if "apple" in link:
#         provider = "apple_music"
#     if "amazon" in link:
#         provider = "amazon_music"
#     if "youtube" in link:
#         provider = "youtube_music"
#     if "deezer" in link:
#         provider = "deezer"
#     elif "https" in link:
#         provider = None
#         print("Invalid Link")


# def getSpotifyURI(link):
#     uri = link[32:len(link)]
#     # https://open.spotify.com/artist/09KZU0NsS7jRa5p0SflmGY
#     return uri

# if checkProvider(song) == "spotify":
#     uri = getSpotifyURI(song)
#     spotify.search(uri)
#     song_name = spotify.getname(uri)
#     song_album = spotify.getalbum(uri)
#     song_artist = spotify.getartist(uri)

# elif checkProvider(song) == "apple_music":
#     None



from js import console

def test_func(*args, **kwargs):

    # print('args:', args)
    # print('kwargs:', kwargs)

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')
    
    text = Element("input-box").element.value

    #print('text:', text)
    console.log(f'text: {text}')

    Element("general-link").element.innerText = text

    Element("general-link").element.innerText = text[0:3]