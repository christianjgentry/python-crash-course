#this is not at all how i consume music so this is a research project for me.
def build_album(album, artist, songs=0):
    """Print album and artist and simply store song number."""
    album_info = {'album':album, 'artist':artist}
    if songs:
       album_info['songs'] = songs
    return album_info

album= build_album('Pretty.Odd', 'Panic at the Disco')
print(album)

album= build_album('Death of a Bachelor', 'Panic at the Disco')
print(album)

album= build_album("A Fever you Can't Sweat Out", 'Panic at the Disco')
print(album)

album= build_album("A Fever you Can't Sweat Out", 'Panic at the Disco', songs=14)
print(album)