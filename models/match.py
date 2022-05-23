from tinydb import TinyDB


db = TinyDB("db.json")
matches_table = db.table("matches")


class Match:
    def __init__(self, player_one, player_two, m_id):
        """_summary_

        Args:
            player_one (_type_):instance of Player
            player_two (_type_):instance of Player
        """
        self.player_one = player_one
        self.player_two = player_two
        self.m_id = m_id

        self.player_one_score = 0.0
        self.player_two_score = 0.0

        self.match = (
            [self.player_one, self.player_one_score],
            [self.player_two, self.player_two_score],
        )

    def display_match_result(self):
        return {
            "Matchs": f"{self.player_one} contre {self.player_two}",
            "Résultats": f"{self.player_one_score} - {self.player_two_score}",
        }

    def save(self):
        serialized_match = {
            "player_one": self.player_one,
            "player_two": self.player_two,
            "player_one_score": self.player_one_score,
            "player_two_score": self.player_two_score,
        }

        matches_table.insert(serialized_match)

    def __str__(self):
        return f"{self.player_one} contre {self.player_two}"


def load_matches():
    serialized_matches = []
    for matches in matches_table:
        serialized_matches.append(matches)

    return serialized_matches
