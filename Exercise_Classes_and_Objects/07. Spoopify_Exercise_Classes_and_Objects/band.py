from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for new_album in self.albums:
            if new_album.name == album.name:
                return f"Band {self.name} already has {new_album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(album)
                    return f"Album {album.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"

        for album in self.albums:
            result += '\n'
            result += album.details()

        return result

