#Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.


def make_album(artist_name,album_title):
    album = {"artist name":artist_name, "album title":album_title}
    return album

a_album = make_album("bob", "fly with the wind")
b_album = make_album("zoe", "gone with the wind")
c_album = make_album("Ali", "fly with the rain")

print(a_album)
print(b_album)
print(c_album)
