
# 14-m
class Game:
    def __init__(self, title, genre, size):
        self.title = title
        self.genre = genre
        self.size = size

    def play(self):
        print(f"{self.title} boshlandi")


class OnlineGame(Game):
    def __init__(self, title, genre, size, server, players):
        super().__init__(title, genre, size)
        self.server = server
        self.players = players

    def play(self):
        super().play()
        print(f"Server: {self.server}, O‘yinchilar: {self.players}")

    def connect(self):
        print("Serverga ulanmoqda...")


g = OnlineGame("PUBG", "Battle", "2GB", "EU", 100)
g.play()
g.connect()
