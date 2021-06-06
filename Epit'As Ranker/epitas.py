from Ranking.src.Ranker import add_player, Ranker
from  Ranking.src.HtmlConverter import file_to_html


def get_player_name(confirm=False):
    if confirm:
        return input("write player name again: ")
    return input("write player name: ")


def get_game_file_name(confirm=False):
    if confirm:
        return input("write game file name again: ")
    return input("write game file name: ")


def adding_player():
    try:
        name = get_player_name()
        if name != get_player_name(True):
            return adding_player()
        add_player("Database/database.json", name)
    except:
        print("Unable to add player to database")


def update_database():
    try:
        game = get_game_file_name()
        if game != get_game_file_name(True):
            return update_database()
        Ranker("Database/database.json", "GameHistory/" + game)
    except:
        print("Unable to update database")
def convert_to_html():
    try:
        res = file_to_html("Database/database.json")
        print(res)
    except:
        print("Unable to Convert database")



def options(again):
    if again:
        return int(input(
            "----<Do you want to update again?:>----\n\n        choose from the options below:\n[1]: add player     "
            "[2]: "
            "update database\n[3]: convert to html table     [4]: exit\n"))

    return int(input(
        "----<Weclcome to Epit'As Ranking System:>----\n\n        choose from the options below:\n[1]: add player     "
        "[2]: "
        "update database\n[3]: convert to html table     [4]: exit\n"))


if __name__ == "__main__":
    again = False
    while (option := options(again)) != 4:
        again = True
        if option == 1:
            adding_player()
        elif option == 2:
            update_database()
        elif option == 3:
            convert_to_html()
        else:
            continue
    print("---<Thanks for using this Script by: Izno(Youssef Kadaoui Abbassi)>---")
