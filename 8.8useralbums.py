def build_album(album, artist, songs=0):
    """Print album and artist and simply store song number."""
    album_info = {'album':album, 'artist':artist}
    if songs:
       album_info['songs'] = songs
    return album_info

album_prompt = "What album are you thinking of?"
artist_prompt = "Who is the artist?"

print("Enter q at any time to stop.")

while True:
    album = input(album_prompt)
    if album == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = build_album(artist, album)
    print(album)

print("\nThanks for responding!")
