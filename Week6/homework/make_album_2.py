# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album

def make_album(artist_name,album_title, no_tracks = 0):
    album = {"artist name":artist_name, "album title":album_title, "number of tracks":no_tracks}
    return album

a_album = make_album("bob", "fly with the wind", 12)
b_album = make_album("zoe", "gone with the wind")

print(a_album)
print(b_album)