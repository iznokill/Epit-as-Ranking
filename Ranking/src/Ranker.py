import json


def game_to_iterable(game_file):
    game_list = game_file.split("\n")
    assert not len(game_list) % 3, "Given game stats are not complete"
    return {game_list[i + 1]: game_list[i:i + 2] for i in range(0, len(game_list), 3)}


def game_stats(game):
    game_file = open(game, 'r').read()
    return game_to_iterable(game_file)


def add_player(file, player):
    json_file = open(file, "r")
    json_object = json.load(json_file)
    json_file.close()
    players_nb = len(json_object["players"])
    json_object["players"] += [{"name": player, "rank": players_nb, "points": 0}]
    json_file = open(file, "w")
    json.dump(json_object, json_file)
    json_file.close()
    return str(json_object)


def update_json(json_object, game_object):
    player_list = game_object.keys()
    points = len(player_list)
    players = json_object["players"]
    ind = 0
    for player in players:
        if player["name"] in player_list:
            points //= 2 if points > 1 else 1
            json_object["players"][ind]["points"] += points
        ind += 1

    players = sorted(players, key=lambda k: k.get('points', 0), reverse=True)
    rank = 0
    for _ in players:
        players[rank]["rank"] = rank + 1
        rank += 1

    json_object["players"] = players
    return json_object


def Ranker(file, game):
    try:
        json_file = open(file, "r")
        game_object = game_stats(game)
        json_object = json.load(json_file)
        json_file.close()
        json_object = update_json(json_object, game_object)
        json_file = open(file, "w")
        json.dump(json_object, json_file)
        json_file.close()
        return str(json_object)
    except:
        print("json file is not on point")
