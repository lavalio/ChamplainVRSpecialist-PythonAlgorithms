#8-8. User Albums: Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.


def make_album(artist_name,album_title):
    album = {"artist name":artist_name, "album title":album_title}
    return album


while True:

    artist_name = input("1. Enter the artist name > ")
    album_title = input("2. Enter the album title > ")
    a_album = make_album(artist_name,album_title)
    print(a_album)
    print()
    print(a_album["artist name"],a_album["album title"])

    message = input("Continu? (y/n) >")
    print(message)

    if message == "n":
        break
    else:
        continue
