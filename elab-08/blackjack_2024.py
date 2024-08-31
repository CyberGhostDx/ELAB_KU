import random


class Card:
    """Card(): create a card object. To create a deck, try \\Card.test_Card()\\!"""

    symbols = {"D": "♦", "C": "♣", "H": "♥", "S": "♠"}

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def get_name(self):
        return self.name

    def get_suit(self):
        return self.suit

    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"

    def test_Card(self):
        Names = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
        Suits = ["D", "C", "H", "S"]
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return " ".join(res)


class Deck:
    """Deck(): สร้างสำรับไพ่"""

    Names = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    Suits = ["D", "C", "H", "S"]

    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()

    def set_cards(self, cards):
        self.cards = cards

    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()

    def __repr__(self):
        res = [str(x) for x in self.cards]
        return " ".join(res)


def createVirtualDeck(s="K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠"):
    dd = s.split()
    res = []
    suit = {"♦": "D", "♣": "C", "♥": "H", "♠": "S"}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck


def cal_score(cards) -> int:
    score = 0
    for card in [x for x in cards if x.name != "A"] + [
        x for x in cards if x.name == "A"
    ]:
        if card.name in [str(x) for x in range(10)]:
            score += int(card.name)
        elif card.name == "A":
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += 10
    return score


def check_blackJack(cards) -> bool:
    if len(cards) < 2:
        return False
    if (cards[0].name in "TJKQ" and cards[1].name == "A") or (
        cards[1].name in "TJKQ" and cards[0].name == "A"
    ):
        return True
    if len(cards) == 5 and cal_score(cards) <= 21:
        return True
    return False


class Player:

    def __init__(self, name: str, cards=[], dealer=False):
        self.name = name
        self.cards = cards
        self.dealer = dealer
        self.score = cal_score(cards)
        self.isBlackJack = False

    def get_cards(self) -> str:
        if self.dealer:
            return f"O{Card.symbols[self.cards[0].get_suit()]} " + " ".join(
                map(str, self.cards[1:])
            )
        else:
            return " ".join(map(str, self.cards))

    def get_cards_list(self):
        return self.cards

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.score = cal_score(self.cards)
        self.isBlackJack = check_blackJack(self.cards)

    def get_score(self) -> int:
        return self.score

    def get_blackjack(self) -> bool:
        return self.isBlackJack

    def __str__(self):
        if self.dealer:
            cards = self.get_cards()
            self.dealer = False
            return f"{self.name:>9}: {cards:<16}-> {cal_score(self.cards[1:])}"
        else:
            return f"{self.name:>9}: {self.get_cards():<16}-> {self.get_score()}"


def play(player1="Computer", player2="Player", d=None, RENDER=False):
    print("Welcome to MikeLab BlackJack Casino.")
    # create a deck of cards
    if d == None:
        deck = Deck()
        deck.reset()
    else:
        # ----------------------------- virtual deck
        # d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    # ----------------------
    # print(deck)  # for DEBUG
    dealer = Player(player1, [], True)
    player = Player(player2, [])
    dealer.add_card(deck.get_card())
    player.add_card(deck.get_card())
    dealer.add_card(deck.get_card())
    player.add_card(deck.get_card())
    print(dealer)
    print(player)
    while len(player.get_cards_list()) < 5 and not player.get_blackjack():
        draw = input("Draw another card (y/n): ")
        if draw == "n" or draw == "N":
            break
        player.add_card(deck.get_card())
        print(player)
        if player.get_score() >= 21:
            break

    print("+++++++++++++++++++++++++++++++++")
    while (
        dealer.get_score() <= 16
        and len(dealer.get_cards_list()) < 5
        and not dealer.get_blackjack()
    ):
        dealer.add_card(deck.get_card())
    while (
        (
            dealer.get_score() < player.get_score()
            or player.get_blackjack()
            and not dealer.get_blackjack()
            and dealer.score < 21
        )
        and len(dealer.get_cards_list()) < 5
        and player.get_score() <= 21
    ):
        dealer.add_card(deck.get_card())
    print(dealer)
    print(player)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++ ")

    dealer_score = dealer.get_score()
    player_score = player.get_score()
    if (
        player_score == dealer_score
        or player.get_blackjack()
        and dealer.get_blackjack()
    ):
        print("Draw!")
    elif (
        (player_score > dealer_score and player_score <= 21 or player.get_blackjack())
        or dealer_score > 21
    ) and not dealer.get_blackjack():
        print(f"{player2} wins.")
    else:
        print(f"{player1} wins.")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    # ----------------------


###-------------- student code begins here --------------###


## main begins here
def testcase01():
    random.seed(2)
    play()


def testcase02():
    random.seed(16)
    play()


def testcase03():
    random.seed(30)
    play()


def testcase04():
    s = "K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠"
    play("Toto", "Tutu", d=s)


def testcase05():
    s = "A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠"
    play(d=s)


def testcase06():
    s = "4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠"
    play(d=s)


def testcase07():
    s = "4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠"
    play(d=s)


def testcase08():
    s = "4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠"
    play(d=s)


def testcase09():
    s = "5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠"
    play(d=s)


# ------------------------------------------
q = int(input("Select Test Case 1-9: "))
# q = 1
if q == 1:
    testcase01()
elif q == 2:
    testcase02()
elif q == 3:
    testcase03()
elif q == 4:
    testcase04()
elif q == 5:
    testcase05()
elif q == 6:
    testcase06()
elif q == 7:
    testcase07()
elif q == 8:
    testcase08()
elif q == 9:
    testcase09()
