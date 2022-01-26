"""
пока пара карт на столе равна
"""

from random import shuffle
import os


def game():
    """
        Создает колоду, карты пользователя, карты компа и стол - пустые списки.
        Вызывает функцию заполнения колоды картами - словарями цена:int и масть:str.
        Вызывает функцию раздачи карт поровну игроку и компу.
        Вызывает функцию нового раунда в цикле, пока у игрока и компа есть карты.
        Печатает результат когда закончатся все раунды.
    """

    # создаем игровые объекты
    deck = []
    user_hand = []
    computer_hand = []
    table = []

    # задаем масти и цены карт в будущей колоде
    suits = ("пики", "крести", "бубны", "червы")
    ranks = range(6, 15)

    # наполняем колоду и раздаем карты
    populate_deck(deck, suits, ranks)
    deal_cards(deck, user_hand, computer_hand)

    # руки для теста спора
    user_hand = [{"цена": 10, "масть": "юзеров"}, {"цена": 7, "масть": "юзеров"}, {"цена": 6, "масть": "юзеров"}]
    computer_hand = [{"цена": 9, "масть": "компов"}, {"цена": 7, "масть": "компов"}, {"цена": 6, "масть": "компов"},]
    
    # играем раунды пока у игрока и компа есть карты
    while user_hand and computer_hand:
        new_round(table, user_hand, computer_hand)

    # печатаем результаты в конце игры
    print("\n---------- результат игры: ----------")
    if user_hand:
        print("игрок победил")
    else:
        print("компьютер победил")


def populate_deck(deck: list, suits: tuple, ranks: range):
    """
        Наполняет колоду картами - словарями цена:int и масть:str.
        Перемешивает колоду.
        4 масти по 9 карт каждой = 36 карт в колоде
    """
    for suit in suits:
        for rank in ranks: 
            deck.append({"масть": suit, "цена": rank})
    shuffle(deck)


def deal_cards(deck: list, user_hand:list, computer_hand:list):
    """
        Первая половина колоды отправляется в руку игрока, вторая - компа.
        Сама колода остается нетронутой.
    """
    for card in deck[:len(deck) // 2]:
        user_hand.append(card)

    for card in deck[len(deck) // 2:]:
        computer_hand.append(card)


def print_hand(hand: list):
    for card in hand:
        print(card["цена"], card["масть"], end=", ")
    print("\n")


def take_cards(table, hand):
    for card in table:
            hand.insert(0, card)
            print(*card.values(), end=", ")


def new_round(table, user_hand, computer_hand):
    """
        Юзер ходит первым.
        Игроки выкладывают карты по очереди, пока пары карт равны по значению

        Разделить на функции Бросить карту на стол и Сравнить последние выброшенные карты

    """

    # ленивое OR
    while not table or table[-2]["цена"] == table[-1]["цена"]:
        os.system("cls")

        print("---------- карты игрока: ----------")
        print_hand(user_hand)
        print("---------- карты компьютера: ----------")
        print_hand(computer_hand)
        
        print("---------- ход игрока: ----------")
        print(*user_hand[-1].values(), end="")
        table.append(user_hand.pop())

        print("\n\n---------- ход компьютера: ----------")
        print(*computer_hand[-1].values(), end="")
        table.append(computer_hand.pop())

        print("\n\n---------- карты на столе: ---------")
        print(*table, end=", ")
        print("\n")

        input("Следующий ход")


    input("Вышел из спора")

    """
    # печатаем результат хода и забираем карты со стола
    print("\n---------- результат раунда: ----------")
    if user_card["цена"] > computer_card["цена"] :
        print("игрок победил и забирает карты:", end=" ")
        take_cards(table, user_hand)
    else:
        print("компьютер победил и забирает карты:", end=" ")
        take_cards(table, computer_hand)

    table.clear()
    input("\n\nENTER - следующий ход")
    """

game()
