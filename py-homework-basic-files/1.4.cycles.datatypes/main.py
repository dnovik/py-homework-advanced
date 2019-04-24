import csv

flats_list = list()

#можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
#print (flats_list)

with open('output.csv', newline='', encoding='utf-8') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

#TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
#и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
# 2) добавьте в код подсчет количества новостроек

new_buildings = 0
flat_description = list()
for flat in flats_list[1:]:
    if 'новостройка' in flat:
        new_buildings += 1
    print("{}".format(flat[0]))
print(f'Кол-во новостроек равно: {new_buildings}')

#TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. 
# Используйте следующие поля из файла output.csv: 
# ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:

flat_info = dict()
for flat in flats_list[1:]:
    flat_id = flat[0] 
    rooms = flat[1]
    types = flat[2]
    price = flat[11]
    
    if flat_id not in flat_info:
        flat_info[flat_id] = list()
        flat_info[flat_id].append({
            'rooms' : flat[1], 
            'type' : flat[2],
            'price' : flat[11]})
    
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, 
# а список описаний квартир в виде словаря, который вы сделали в п.1 

flat_info = dict()
for flat in flats_list[1:]:
    flat_id = flat[0] 
    rooms = flat[1]
    types = flat[2]
    metro = flat[3].replace('м.', '')
    price = flat[11]
    description = flat[12]
    
    if description not in flat_info:
        flat_info[description] = list()
        flat_info[description].append({
            'id' : flat[0],
            'metro' : flat[3],
            'rooms' : flat[1], 
            'type' : flat[2],
            'price' : flat[11]})

        
# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
flat_info = dict()
for flat in flats_list[1:]:
    flat_id = flat[0] 
    metro = flat[3].replace('м.', '')
    
    if metro not in flat_info:
        flat_info[metro] = list()
        flat_info[metro] = 1
    else:
        flat_info[metro] += 1

