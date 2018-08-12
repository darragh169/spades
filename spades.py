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

def play_round(_current_cards):
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

def get_card_from_hand(_index, _cards):
	return _cards.pop(_index)

def game_loop():
	populate_deck(deck)
	shuffle_deck(deck)
	for x in xrange(0, NUMBER_OF_PLAYERS):
		players.append(Player("player_"+`x+1`, 0, []))
		distribute_hand(players[x], deck, NUMBER_OF_ROUNDS)
		print_hand(players[x])
		player_choice_index = (int(raw_input("player one choose your card..... \n"))-1)
		current_cards.append(get_card_from_hand(player_choice_index, players[x].hand))
		print(current_cards[len(current_cards)-1])
	play_round(current_cards)

NUMBER_OF_PLAYERS = 2
NUMBER_OF_ROUNDS = 2

deck = []
current_cards = []
players = []

game_loop()
