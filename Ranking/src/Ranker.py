import json


def game_stats(game):
    game_file = open(game, 'r').read()
    return game_file


def Ranker(file, game):
    json_file = open(file, "r")
    json_object = json.load(json_file)
    json_file.close()
    return str(json_object)
