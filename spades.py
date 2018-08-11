from random import shuffle

card_values = {
	1: "Two",
	2: "Three",
	3: "Four",
	4: "Five",
	5: "Six",
	6: "Seven",
	7: "Eight",
	8: "Nine",
	9: "Ten",
	10: "Jack",
	11: "Queen",
	12: "King",
	13: "Ace"
}

class Player(object):
	def __init__(self, name, score, hand):
		self.name = name
		self.score = score
		self.hand = hand

	def __str__(self):
		return "Player: %s, (%s), score %s" % (self.name, len(self.hand), self.score)

class Card(object):
	def __init__(self, suit, value):
		super(Card, self).__init__()
		self.suit = suit
   		self.value = value

  	def __str__(self):
		return "Card: (suit: %s, value: %s)" % (self.suit, card_values[self.value])

	def get_player_id_of_card(self):
		return self.player_id

def populate_deck(deck):
	for x in xrange(1,14):
		deck.append(Card('Hearts', x))
	for x in xrange(1,14):
		deck.append(Card('Diamonds', x))
	for x in xrange(1,14):
		deck.append(Card('Clubs', x))
	for x in xrange(1,14):
		deck.append(Card('Spades', x))

def print_deck(deck):
	for x in deck:
		print(x)

def print_hand(player):
	print(player)
	for card in player.hand:
		print(card)
		print(card.get_player_id_of_card())

def print_cards(_cards):
	for card in _cards:
		print(card)

def shuffle_deck(deck):
	shuffle(deck)

def distribute_hand(_player, _deck, _amount):
	for x in xrange(0, _amount):
		tmp = _deck.pop(0)
		tmp.player_id = id(_player)
		_player.hand.append(tmp)

def play_round(_player_one, _player_two, _current_cards):
	_current_cards.append(_player_one.hand.pop(0))
	_current_cards.append(_player_two.hand.pop(0))
	find_highest_card(_current_cards)

def find_the_highest_value_card(_cards):
	highest_card = None
	for card in _cards:
		if not highest_card:
			highest_card = card
			continue
		if (card_values[card.value] > card_values[highest_card.value]):
			highest_card = card
			continue
	print(highest_card)
	return highest_card

def find_highest_card(_cards):
	highest_card = None
	spade_cards = []
	spade_cards = find_spades(_cards)
	if (spade_cards):
		print('Find the Highest Spade')
		highest_card = find_the_highest_value_card(spade_cards)
	else:
		current_suit = _cards[0].suit
		print('Find the highest card with a suit of %s' % current_suit)
		_cards = filter(lambda x : x.suit != current_suit, _cards)
		highest_card = find_the_highest_value_card(_cards)

def find_spades(_cards):
	spade_cards = []
	for card in _cards:
		if (card.suit == 'Spades'):
			spade_cards.append(card)
	return spade_cards

deck = []
current_cards = []
players = []

populate_deck(deck)
shuffle_deck(deck)

player_1 = Player("player_1", 0, [])
player_2 = Player("player_2", 0, [])

players.append(player_1)
players.append(player_2)

distribute_hand(player_1, deck, 5)
distribute_hand(player_2, deck, 5)

play_round(player_1, player_2, current_cards)
