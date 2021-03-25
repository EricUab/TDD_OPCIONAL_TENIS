class Player:
  def __init__(self, name:str):
    self._name = name
    self._points = 0

  def get_score(self):
    return self._points

  def won(self):
    self._points += 1

  def set_score(self, score):
    self._points = score

class Game:
  def __init__(self, player1: Player, player2: Player):
    self._player1 = player1
    self._player2 = player2

  def won_point(self, player: Player):
    player.won()
  
  def get_score(self):
    if self._player1.get_score() == self._player2.get_score():
      return self._empats()
    else:
      return self._altres()

  def _altres(self):
    if self._player1.get_score() == 0:
      if self._player2.get_score() == 1:
        return "Love-Fifteen"
      elif self._player2.get_score() == 2:
        return "Love-Thirty"
      elif self._player2.get_score() == 3:
        return "Love-Forty"
    if self._player1.get_score() == 1:
      if self._player2.get_score() == 0:
        return "Fifteen-Love"
      elif self._player2.get_score() == 2:
        return "Fifteen-Thirty"
      elif self._player2.get_score() == 3:
        return "Fifteen-Forty"
    elif self._player1.get_score() == 2:
      if self._player2.get_score() == 0:
        return "Thirty-Love"
      elif self._player2.get_score() == 1:
        return "Thirty-Fifteen"
      elif self._player2.get_score() == 3:
        return "Thirty-Forty"
    elif self._player1.get_score() == 3:
      if self._player2.get_score() == 0:
        return "Forty-Love"
      elif self._player2.get_score() == 1:
        return "Forty-Fifteen"
      elif self._player2.get_score() == 2:
        return "Forty-Thirty"
    
    return self._guanyador()

  def _guanyador(self):
    if self._player1.get_score() - self._player2.get_score() >= 2:
      return "Win for player1"
    elif self._player2.get_score() - self._player1.get_score() >= 2:
      return "Win for player2"
    else:
      return self._advantagePlayerN()

  def _advantagePlayerN(self):
      return "Advantage player1" if self._player1.get_score() > self._player2.get_score() else "Advantage player2"

  def _empats(self):
    if self._player1.get_score() == 0:
      return "Love-All"
    elif self._player1.get_score() == 1:
      return "Fifteen-All"
    elif self._player1.get_score() == 2:
      return "Thirty-All"
    elif self._player1.get_score() == 3 or self._player1.get_score() == 4:
      return "Deuce"
