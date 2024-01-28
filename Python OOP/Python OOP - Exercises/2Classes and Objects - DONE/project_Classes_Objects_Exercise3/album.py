from project.song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [song for song in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        elif song in self.songs:
            return f"Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        else:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                    return f"Removed song {song.name} from album {self.name}."
            return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        album_info = [f"Album {self.name}"]
        for song in self.songs:
            album_info.append(f" == {song.name}")
        return '\n'.join(album_info) + "\n"

























