import configparser
from pathlib import Path
from foodsearch import FoodSearch
from queries import insert_business_table
from databasedriver import DatabaseDriver
import argparse

config = configparser.ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))

def getArgparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
    description="A Example yelp business finder based on parameters such as term, location, price, ")

    return parser


def to_string(data):
    return [str(value) for value in data.values()]

def main(parser: argparse.ArgumentParser) -> None:

    # Define parser argument
    args = parser.parse_args()

    # Pricing levels to filter the search result with: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$.
    # Pricing levels to filter the search result with
    search = FoodSearch(term=args.term, location=args.location, price=args.price)

    # Connecting to Postgresql
    db = DatabaseDriver()
    db.setup()

    queries = [insert_business_table.format(*to_string(result)) for result in search.get_results()]
    query_to_execute = "BEGIN; \n" + '\n'.join(queries) + "\nCOMMIT;"
    db.execute_query(query_to_execute)

if __name__ == "__main__":
    
    parser = getArgparse()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    test = parser.add_argument_group('test')
    required.add_argument("-t", "--term",  metavar='', required=True,
                          help="Search term, for example \"food\" or \"restaurants\". The term may also be business names, such as \"Starbucks.\".")
    required.add_argument("-l", "--location",  metavar='', required=True,
                          help="This string indicates the geographic area to be used when searching for businesses. ")
    optional.add_argument("-p", "--price", type=int, metavar='', required=False, default=1,
                          help="Pricing levels to filter the search result with: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$.")
    
    
    main(parser)

    