class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo

    def update_elo(self, new_elo):
        self.elo = new_elo

    def __str__(self):
        return f"{self.name}: {self.elo}"

# Return the expected score of the match
def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

# Return a score factor depending how close was the match
def score_factor(winner_score, loser_score):
    margin_of_victory = winner_score - loser_score
    total_games = winner_score + loser_score
    return 1 + (margin_of_victory / total_games)

def update_elo(winner_1, winner_2, loser_1, loser_2, winner_score, loser_score, k=32):
    # Calculate combined ratings
    combined_winner_rating = (winner_1.elo + winner_2.elo) / 2
    combined_loser_rating = (loser_1.elo + loser_2.elo) / 2

    # Calculate expected scores
    expected_winner = expected_score(combined_winner_rating, combined_loser_rating)
    expected_loser = expected_score(combined_loser_rating, combined_winner_rating)

    # Calculate scre factor depending how close the match was
    factor = score_factor(winner_score, loser_score)

    # Update ELO ratings
    winner_1.update_elo(winner_1.elo + k * factor * (1 - expected_winner))
    winner_2.update_elo(winner_2.elo + k * factor * (1 - expected_winner))
    loser_1.update_elo(loser_1.elo + k * factor * (0 - expected_loser))
    loser_2.update_elo(loser_2.elo + k * factor * (0 - expected_loser))

# Print rankings of a player
def print_rankings(players):
    sorted_players = sorted(players, key=lambda x: x.elo, reverse=True)
    for i, player in enumerate(sorted_players):
        print(f"{i + 1}. {player}")

# Predit who will win a match
def predict_result(player1, player2, player3, player4):
    # Calculate combined ratings
    combined_winner_rating = (player1.elo + player2.elo) / 2
    combined_loser_rating = (player3.elo + player4.elo) / 2

    # Calculate expected scores
    expected_winner = expected_score(combined_winner_rating, combined_loser_rating)
    expected_loser = expected_score(combined_loser_rating, combined_winner_rating)

    if expected_winner > expected_loser:
        print(f"{player1.name} and {player2.name} will win with a probability of {expected_winner:.2f}")
    else:
        print(f"{player3.name} and {player4.name} will win with a probability of {expected_loser:.2f}")

# Simulate a match
def play_match(player1, player2, player3, player4, score1, score2):
    # Determine winners and losers based on scores
    if score1 > score2:
        winner_1, winner_2, loser_1, loser_2 = player1, player2, player3, player4
    else:
        winner_1, winner_2, loser_1, loser_2 = player3, player4, player1, player2

    print("----------------")
    print("Match Results:", winner_1.name, "and", winner_2.name, "vs.", loser_1.name, "and", loser_2.name)
    print("Score:", score1 if score1 > score2 else score2, "-", score2 if score1 > score2 else score1)

    update_elo(winner_1, winner_2, loser_1, loser_2, score1 if score1 > score2 else score2, score2 if score1 > score2 else score1)
    print_rankings([player1, player2, player3, player4])


# Main

sebastian = Player("Sebastian", 1500)
chimes = Player("Chimes", 1500)
omar = Player("Omar", 1500)
joma = Player("Joma", 1500)
franco = Player("Franco", 1500)

print("----Ranking Inicial-------")
print_rankings([sebastian, chimes, omar, joma, franco])

# Partida Padel Club Sabado
play_match(joma, chimes, franco, omar, 4, 6)
play_match(joma, chimes, franco, omar, 6, 0)
play_match(joma, chimes, franco, omar, 6, 7)

# Partida Jueves amigo
play_match(sebastian, chimes, franco, omar, 6, 2)
play_match(sebastian, chimes, franco, omar, 6, 0)

play_match(sebastian, franco, chimes, omar, 6, 3)
play_match(sebastian, franco, chimes, omar, 6, 1)
play_match(sebastian, franco, chimes, omar, 2, 6)
play_match(sebastian, franco, chimes, omar, 5, 1)

# Partida Sabado
play_match(omar, franco, chimes, joma, 6, 2)
play_match(omar, franco, chimes, joma, 6, 7)
play_match(omar, franco, chimes, joma, 7, 6)
play_match(omar, franco, chimes, joma, 6, 1)

# Partidos Miercoles
play_match(omar, chimes, franco, joma, 6, 3)
play_match(omar, chimes, franco, joma, 6, 0)
play_match(franco, chimes, omar, joma, 6, 1)
play_match(franco, chimes, omar, joma, 3, 6)
play_match(franco, chimes, omar, joma, 6, 3)
play_match(franco, omar, chimes, joma, 3, 4)

print("----Ranking Actual-------")
print_rankings([sebastian, chimes, omar, joma, franco])
