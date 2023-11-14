
def find_common_participants(participants_first_group, participants_second_group, sep=','):
    participants_first_group = set(participants_first_group.split(sep)) #Преобразуем в слова, разделяем слова
    participants_second_group = set(participants_second_group.split(sep))
    common_participants = participants_first_group.intersection(participants_second_group) #Ищем пересечения
    common_participants = sorted(list(common_participants)) #сортируем слова в алфавитном порядке
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))


