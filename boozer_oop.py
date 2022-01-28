from random import shuffle


class Deck:
    def __init__(self):
        ranks = range(6, 15)
        suits = ("пики", "крести", "черви", "бубны")
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        shuffle(self.cards)

    def deal(self, players):
        if self.cards:
            while self.cards:
                for player in players:
                    player.cards.append(self.cards.pop())
        else:
            print("В колоде нет карт!")


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def show_cards(self):
        print("--- Карты игрока", self.name, "---")
        for card in self.cards:
            print(card.rank, card.suit, end=", ")
        print("\n")

    def play_card(self):
        print(self.name, "положил карту на стол")

    def take_cards(self):
        print(self.name, "забрал карты со стола")


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Lap:
    def new_lap(self, players):
        cards_in_lap = []
        for player in players:
            player.play_card()


deck = Deck()

# может, без переменных, индексами списка?
p1 = Player("Юзер", [])
p2 = Player("Компьютер", [])
all_players = [p1, p2]  

deck.deal(all_players)

lap = Lap()
lap.new_lap(all_players)


