class Musica:
    musicas = []

    def __init__(self, name: str, artist: str, lenght: int):
        self.name = name
        self.artist = artist
        self.lenght = lenght
        Musica.musicas.append(self)

    def __str__(self):
        return f"{self.name} | {self.artist} | {self.lenght}"

    def list_artist():
        for artist in Musica.musicas:
            print(f"{artist.name} | {artist.artist} | {artist.lenght}")

musica1 = Musica("Cold Play", "The Kid Laroi", 2)

print(musica1)