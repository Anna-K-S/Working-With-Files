# modul pickle
import pickle
import shelve

honda = ('civic',
         'grey',
         '2009',
         (
             (1, 'James B'),
             (2, 'Jane W'),
             (3, 'Jack S')
         )
         )
with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
# dump метод записывает объект в бинарный файл

with open('honda.pickle', 'rb') as honda_read:
    honda_from_file = pickle.load(honda_read)
print(honda_from_file)
# 'load' метод для извлечения/считывания из бинарного файла
model, color, year, owner_list = honda_from_file
print(model)
print(color)
print(year)
for owner in owner_list:
    owner_number, owner_name = owner
    print((owner_number, owner_name))

# Modul Shelve
# ключи должны быть только строками(str)


with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'
    print(cars['ford'])
    print(cars['renault'])
    for key in cars:
        print(key)
    cars = cars.get('jac', 'China')
    print(cars)

    while True:
        key = input('enter cat name')
        if key == 'quit':
            break


# Первый параметр метода - ключ, по которому следует получить значение,
# а второй - значение по умолчанию, которое возвращается, если ключ не найден
# обращение к объекту по ключу только в модуле shelve
# print(cars['mazda'])

# data update with shelve
with shelve.open('states') as states:
    states['Tokio'] = 'Japan'
    states['London'] = 'UK'
    states['Berlin'] = 'Germany'

    states['London'] = 'GB'
    for key in states:
        print(key, ' - ', states[key])

    # deleting data
    # for deleting use function 'pop()', operator 'del', method ' clear()'.

    print(states.pop('Tokio'))

# Conversion dictionaries into shelve
university = shelve.open('university_file')
university['schedules'] = {'monday_schedule': ['Math', 'English', 'English literature'],
                           'tuesday_schedule': ['Physics', 'English', 'Swimming'],
                           'wednesday_schedule': ['Running', 'Math', 'Drawing']}
university['tutors'] = {'Math': ['J.Brown', 'J.Smith'],
                        'English': ['M.W', 'K.Black']}
print(university['schedules'], ['tuesday_schedule'])
print(university['tutors'], ['English'])
university.close()
# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English', 'English literature'],
#         'tuesday_schedule': ['Physics', 'English', 'Swimming'],
#         'wednesday_schedule': ['Running', 'Math', 'Drawing']
#
#     },
#     'tutors': {
#         'Math': ['J.Brown', 'J.Smith'],
#         'English': ['M.W', 'K.Black']
#     }
# }
# print(university['schedules']['tuesday_schedule'])
# print(university['tutors']['English'])