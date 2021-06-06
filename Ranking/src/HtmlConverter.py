import json


def json_to_html(json_object):
    html_table = "<table align=\"center\">\n"
    for player in json_object["players"]:
        html_table += "  <tr>\n"
        html_table += "      <td>" + str(player["rank"]) + "</td>\n"
        html_table += "      <td>" + str(player["name"]) + "</td>\n"
        html_table += "      <td>" + str(player["points"]) + "</td>\n"
        html_table += "  </tr>\n"
    html_table += "\n</table>"
    return html_table

