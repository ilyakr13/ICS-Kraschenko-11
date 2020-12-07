"""модуль зчитує первинні файли для обробки
"""

def get_dovidnik():
    """повертає список клієнтів з файла 'dovidnik.txt` та фороматує значення

    from file = [
    "1;Універсам №1",
    "6;Галактон",
    "7;Поляниця"
    ] 

    return from file    

    Returns:
        dovidnik_list: список клієнтів
    """

    with open("./data/dovidnik.txt") as dovidnik_file:
        from_file = dovidnik_file.readlines() 

    # накопичувач клієнтів
    dovidnik_list = []

    # блок виділяє окремі реквізити з кожного рядка
    for line in from_file:
        line = line[:-2]
        line_list = line.split(';')
        dovidnik_list.append(line_list)

    return dovidnik_list

def get_orders():
    """повертає список накладних з файла 'orders.txt`

    Returns:
        from_file: список накладних
    """

    with open("./data/orders.txt") as orders_file:
        from_file = orders_file.readlines() 

    # список-накопичувач
    orders_list = []    
    
    # розбити строку на реквізити та перетворити формати (при потребі)
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list

def show_dovidnik(dovidnik):
    """ виводить список клітєнтів за деякою умовою

    Args:
        dovidnik ([list]): список клітєнтів
    """

    client_code_from = input("З якого коду клієнта? ")
    client_code_to   = input("По який код клієнта? ")
    
    kol_lines = 0

    for client in dovidnik:
        if  client_code_from  <= client[0] <= client_code_to:
            print("код: {:4} назва: {:16} адреса: {:20}".format(client[0], client[1], client[2]))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом {} не знайдено".format(client_code_from))



dovidnik = get_dovidnik()
show_dovidnik(dovidnik)

# orders = get_orders()
# print(orders)


   