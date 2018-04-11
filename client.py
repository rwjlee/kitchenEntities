from DCK import DCK
from ck_entities import Company, Club, Person, League, City, Department, State, Exchange


dck = DCK()

entity_tuple = [(Company, "http://data.coding.kitchen/api/companies/1"), 
    (Club, "http://data.coding.kitchen/api/clubs/1"),
    (Person, "http://data.coding.kitchen/api/people/1"),
    (League, "http://data.coding.kitchen/api/leagues/"),
    (City, "http://data.coding.kitchen/api/cities/1"),
    (Department, "http://data.coding.kitchen/api/departments/1"),
    (State,"http://data.coding.kitchen/api/states/"),
    (Exchange, "http://data.coding.kitchen/api/exchanges/")]

for value in entity_tuple:
    obj, next_url = value
    dck.populate_table(obj, next_url)