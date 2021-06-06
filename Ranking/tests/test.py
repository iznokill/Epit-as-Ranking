from Ranking.src.Ranker import Ranker, add_player


def test_update(file, update_text, expected):
    res = Ranker(file, update_text)
    assert res == expected, "Update failed\ngot:\n" + str(res) + "\nexpected:\n" + expected


def test_add(file, player, expected):
    res = add_player(file, player)
    assert res == expected, "Update failed\ngot:\n" + str(res) + "\nexpected:\n" + expected


if __name__ == "__main__":
    test_add("test_files/empty.json","youssef","{'players': [{'name': 'youssef', 'rank': 0, 'points': 0}]}")
