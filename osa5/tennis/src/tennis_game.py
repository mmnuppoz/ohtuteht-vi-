class TennisGame:
    SCORE_NAME = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        if player_name in self.scores:
            self.scores[player_name] += 1

    def get_score(self):
        p1_score = self.scores[self.player1_name]
        p2_score = self.scores[self.player2_name]

        if p1_score == p2_score:
            return self.even_score(p1_score)
        if self.is_advantage_or_win(p1_score, p2_score):
            return self.advantage_or_win(p1_score, p2_score)
        return self.find_score(p1_score, p2_score)
    
    def even_score(self, score):
        return f"{self.SCORE_NAME[score]}-All" if score <3 else "Deuce"
    
    def is_advantage_or_win(self, score1, score2):
        return True if max(score1, score2) >= 4 else False

    def advantage_or_win(self, score1, score2):
        diff = abs(score1 - score2)
        if diff == 1:
            return f"Advantage {self.leading_player(score1, score2)}"
        return f"Win for {self.leading_player(score1, score2)}"

    def leading_player(self, score1, score2):
        return self.player1_name if score1 > score2 else self.player2_name

    def find_score(self, score1, score2):
        return f"{self.SCORE_NAME[score1]}-{self.SCORE_NAME[score2]}"

    # def get_score(self):
    #     score = ""
    #     temp_score = 0

    #     if self.m_score1 == self.m_score2:
    #         if self.m_score1 == 0:
    #             score = self.SCORE_NAME[0]
    #         elif self.m_score1 == 1:
    #             score = self.SCORE_NAME[1]
    #         elif self.m_score1 == 2:
    #             score = self.SCORE_NAME[2]
    #         else:
    #             score = "Deuce"
    #     elif self.m_score1 >= 4 or self.m_score2 >= 4:
    #         minus_result = self.m_score1 - self. m_score2

    #         if minus_result == 1:
    #             score = "Advantage player1"
    #         elif minus_result == -1:
    #             score = "Advantage player2"
    #         elif minus_result >= 2:
    #             score = "Win for player1"
    #         else:
    #             score = "Win for player2"
    #     else:
    #         for i in range(1, 3):
    #             if i == 1:
    #                 temp_score = self.m_score1
    #             else:
    #                 score = score + "-"
    #                 temp_score = self.m_score2

    #             if temp_score == 0:
    #                 score = score + "Love"
    #             elif temp_score == 1:
    #                 score = score + "Fifteen"
    #             elif temp_score == 2:
    #                 score = score + "Thirty"
    #             elif temp_score == 3:
    #                 score = score + "Forty"

    #     return score
