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

    # задаем масти и цены карт в будущей колоде
    suits = ("пики", "крести", "бубны", "черви")
    ranks = range(6, 15)

    # наполняем колоду и раздаем карты
    populate_deck(deck, suits, ranks)
    deal_cards(deck, user_hand, computer_hand)

    # играем раунды пока у игрока и компа есть карты
    while user_hand and computer_hand:
        new_round(user_hand, computer_hand)

    # печатаем результаты в конце игры
    os.system("cls")
    print("\n- результат игры:")
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


def deal_cards(deck: list, user_hand: list, computer_hand: list):
    """
        Первая половина колоды отправляется в руку игрока, вторая - компа.
        Сама колода остается нетронутой.
    """
    for card in deck[:len(deck) // 2]:
        user_hand.append(card)

    for card in deck[len(deck) // 2:]:
        computer_hand.append(card)


def print_cards(hand: list):
    for card in hand:
        print(*card.values(), end=", ")
    print("\n")


def take_cards(user_table: list, computer_table: list, hand: list):
    for card in user_table + computer_table:
        hand.insert(0, card)


def new_round(user_hand: list, computer_hand: list):
    user_table = []
    computer_table = []

    while True:
        os.system("cls")

        # заканчиваем раунд, если любому игроку нечем ходить
        if not user_hand or not computer_hand:
            break

        # забираем карту из руки и кладем ее на стол
        user_table.append(user_hand.pop())
        computer_table.append(computer_hand.pop())

        # печатаем руки и карты ходов
        print("- рука игрока:")
        print_cards(user_hand)
        print("- рука компьютера:")
        print_cards(computer_hand)
        print("- ход игрока:")
        print_cards(user_table)
        print("- ход компьютера:")
        print_cards(computer_table)

        if user_table[-1]["цена"] == computer_table[-1]["цена"]:
            input("Спор! Enter — сделать ход в споре")
        # заканчиваем раунд, если цены карт хода не равны
        else:
            break

    # печатаем результат хода и забираем карты со стола
    print("- результат раунда:")
    if user_table[-1]["цена"] > computer_table[-1]["цена"]:
        print("игрок победил и забирает карты")
        take_cards(user_table, computer_table, user_hand)
    else:
        print("компьютер победил и забирает карты")
        take_cards(user_table, computer_table, computer_hand)

    input("\nENTER - следующий ход")


if __name__ == '__main__':
    game()
