from foodsearch import *
from databasedriver import DatabaseDriver
from foodsearch import FoodSearch
from queries import insert_business_table, create_business_table, create_business_schema



def to_string(data):
    return [str(value) for value in data.values()]


if __name__ == '__main__':

    paramester = {
        'term': 'food',
        'location': 'United States',
        'price': 2
    }

    search = FoodSearch(**paramester)
    db = DatabaseDriver()
    db.setup()

    queries = [insert_business_table.format(*to_string(result)) for result in search.get_results()]
    query_to_execute = "BEGIN; \n" + '\n'.join(queries) + "\nCOMMIT;"
    db.execute_query(query_to_execute)
