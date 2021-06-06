from Ranking.src.Ranker import Ranker


def test_update(file, update_text, expected):
    res = Ranker(file, update_text)
    assert res == expected, "Update failed\ngot:\n" + str(res) + "\nexpected:\n" + expected


if __name__ == "__main__":
    test_update("test_files/empty.json", "test_files/simple_game.txt", None)
    test_update("test_files/simple.json", "test_files/simple_game.txt",
                "{'players': [{'name': 'turbo-ice', 'rank': 1, 'points': 10}, {'name': 'ScottPosey', 'rank': 2, "
                "'points': 10}]}")
