list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

number = len(list_players)

middle_index = number // 2
left_team = list_players[:middle_index]
right_team = list_players[middle_index:]

print(left_team)
print(right_team)
