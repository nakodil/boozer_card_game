from random import shuffle
import os


def game():
    """
        Создает колоду, карты пользователя, карты компа и стол - пустые списки.
        Вызывает функцию заполнения колоды картами - словарями цена:int и масть:str.
        Вызывает функцию раздачи карт поровну игроку и компу.
        Вызывает функцию нового раунда, пока у игрока и компа есть карты.
        Печатает результат когда закончатся все раунды.
    """

    # создаем и наполняем игровые объекты
    deck = []
    user_hand = []
    computer_hand = []
    table = []
    populate_deck(deck)
    deal_cards(deck, user_hand, computer_hand)
    
    # играем раунды пока у игрока и компа есть карты
    while user_hand and computer_hand:
        new_round(table, user_hand, computer_hand)

    # печатаем результаты в конце игры
    os.system("cls")
    print("\n---------- результат игры: ----------")
    if user_hand:
        print("игрок победил")
    else:
        print("компьютер победил")


def populate_deck(deck: list):
    """
        Наполняет колоду картами - словарями цена:int и масть:str.
        Перемешивает колоду.
        4 масти по 9 карт каждой = 36 карт в колоде
    """
    suits = ("пики", "крести", "бубны", "червы")
    for suit in suits:
        for i in range(6, 15):  # хардкод, взять количество карт в колоде из аргумента функции
            card = {}
            card["масть"] = suit
            card["цена"] = i
            deck.append(card)
    shuffle(deck)


def deal_cards(deck: list, user_hand: list, computer_hand: list):
    """
        Первая половина колоды отправляется в руку игрока, вторая - компа.
    """
    for card in deck[:18]:  # хардкод, взять длину колоды
        user_hand.append(card)
    for card in deck[18:]:
        computer_hand.append(card)


def new_round(table, user_hand, computer_hand):
    # очищаем экран и печатаем руки игрока и компа
    os.system("cls")
    print("---------- карты игрока: ----------")
    for card in user_hand:
        print(f'{card["цена"]} {card["масть"]}, ', end="")
    print("\n\n---------- карты компьютера: ----------")
    for card in computer_hand:
        print(f'{card["цена"]} {card["масть"]}, ', end="")
    print("")

    # делаем первый ход: выбираем последнюю карту в руке игрока и компа
    user_card = user_hand[-1]
    computer_card = computer_hand[-1]

    # добавляем выбранные карты на стол и удаляем их из рук игрока и компа
    table.append(user_hand.pop())
    table.append(computer_hand.pop())

    # печатаем карты этого хода 
    print("\n---------- ход игрока: ----------")
    print(user_card["цена"], user_card["масть"])
    print("\n---------- ход компьютера: ----------")
    print(computer_card["цена"], computer_card["масть"])

    # спор, когда цена карты игрока == цене карты компа
    while user_card["цена"] == computer_card["цена"]:
        user_card = user_hand[-1]
        computer_card = computer_hand[-1]

        table.append(user_hand.pop())
        table.append(computer_hand.pop())

        print("\n---------- ход игрока в споре: ----------")
        print(user_card["цена"], user_card["масть"])
        print("\n---------- ход компьютера в споре: ----------")
        print(computer_card["цена"], computer_card["масть"])

    # печатаем результат хода и забираем карты со стола
    print("\n---------- результат раунда: ----------")
    if user_card["цена"] > computer_card["цена"] :
        print("игрок победил и забирает карты")
        for card in table:
            user_hand.insert(0, card)
            print(f'{card["цена"]} {card["масть"]}')
    else:
        print("компьютер победил и забирает карты")
        for card in table:
            computer_hand.insert(0, card)
            print(f'{card["цена"]} {card["масть"]}')

    table.clear()
    input("\nENTER - следующий ход")


game()
