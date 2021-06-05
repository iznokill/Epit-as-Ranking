from Ranking.src.Ranker import Ranker


def test_update(file, update_text, result):
    res = Ranker(file, update_text)
    assert res == result, "Update failed\ngot:\n" + res + "\nexpected:\n" + result


if __name__ == "__main__":
    test_update("test_files/empty.json", "test_files/simple_game.txt", "{}")
