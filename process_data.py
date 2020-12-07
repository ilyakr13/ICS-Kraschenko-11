""" розрахунок заявок на товари по магазину
"""

from data_service import get_orders, get_dovidnik

zajavka = {
    'oborud' : "",
    'client' : "",
    'zakaz'  : "",
    'kol'    : 0,
    'price'  : 0.0,
    'total'  : 0.0  
     }


def create_zajavka():
   """формування сріску заявок по магазину на основі вхідних файлів
   """
   orders = get_orders()
   dovidnik = get_dovidnik()


   zajavka_list = []

   for order in orders:
       zajavka_copy = zajavka.copy()
       zajavka_copy['oborud'] = order[2]
       zajavka_copy['zakaz']  = order[1]
       zajavka_copy['kol']    = order[3]
       zajavka_copy['price']  = order[4]
       zajavka_copy['total']  =zajavka_copy['kol'] * zajavka_copy['price']


       zajavka_copy['client'] = get_client_name(order[0])


def get_client_name(client_code):
    """повертає назву клієнта по його коду"""
    for client in dovidnik:
        if client[0] = client_code:
          return client[1]
 
    
         



   return zajavka_list

create_zajavka
