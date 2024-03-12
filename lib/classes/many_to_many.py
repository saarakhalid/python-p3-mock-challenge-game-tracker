class Game:
    def __init__(self, title):
        self._title = None
        self.title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if self._title is None and isinstance(title, str) and len(title) > 0:
            self._title = title

    def results(self):
        # Return the list of results for the game
        return self._results

    def players(self):
        # Return a list of unique players who participated in the game
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        # Calculate the average score for a given player in the game
        player_scores = [result.score for result in self._results if result.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0


class Player:
    all = []

    def __init__(self, username):
        self._username = None
        self.username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return self._results

    def games_played(self):
        # Return a list of unique games the player participated in
        return list(set(result.game for result in self._results))

    def played_game(self, game):
        # Check if the player played a specific game
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        # Count the number of times the player played a specific game
        return sum(result.game == game for result in self._results)


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        player.results().append(self)
        game.results().append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score

    @classmethod
    def all(cls):
        return cls.all


def played_game(self, game):
    # Check if the player played a specific game
    return any(result.game == game for result in self._results)


def num_times_played(self, game):
    # Count the number of times the player played a specific game
    return sum(result.game == game for result in self._results)


# Add played_game and num_times_played methods to Player class dynamically
Player.played_game = played_game
Player.num_times_played = num_times_played


def average_score(self, player):
    player_scores = [result.score for result in self._results if result.player == player]
    if player_scores:
        return sum(player_scores) / len(player_scores)
    return 0


# Add average_score method to Game class
Game.average_score = average_score
