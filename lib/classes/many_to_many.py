class Game:
    def __init__(self, title):
        self._title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 1 <= len(title) <= 15:
            self._title = title

    def results(self, new_result = None):
        if new_result is not None and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def players(self, new_player = None):
        if new_player is not None and isinstance(new_player, Player):
            if new_player not in self._players:
                self._players.append(new_player)
        return self._players

    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        return sum(player_scores) / len(player_scores) if player_scores else 0


class Player:
    def __init__(self, username):
        self._username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self, new_result=None):
        if new_result is not None and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        if new_game is not None and isinstance(new_game, Game):
            if new_game not in self._games_played:
                self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        return game in self._games_played

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)

        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score

            
    @property
    def player(self): 
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
       