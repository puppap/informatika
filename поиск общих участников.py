#TODO Напишите функцию find_common_participants

def find_common_participants(groupone, grouptwo, sep=','): #возвращаем общий список участников из двух строк и sep (separator - разделитель)
    list1 = groupone.split(sep) #разбиваем первую строку на первый список участников
    list2 = grouptwo.split(sep) #разбиваем вторую строку на второй список участников
    common = [] #создаем пустой список, в котором будут общие фамилии участников
    #Находим общих участников
    for participant in list1: #проходим по первому списку
        if participant in list2: #если фамилия повторяется во втором списке
            common.append(participant) #добавляем фамилию участника в новый список common
    common.sort() #сортируем новый список по алфавиту
    return common #возвращаем результат

participants_first_group = "Иванов|Петров|Сидоров" #первый список участников
participants_second_group = "Петров|Сидоров|Смирнов" #второй список участников

#TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|')) #выводим общий список участников из двух групп с разделителем |