from pathlib import Path
import configparser

config = configparser.ConfigParser()
config.read_file(open(f'{Path(__file__).parents[0]}/config.cfg'))

api_key = config['API']['api_key']
headers = {
    'Authorization' : 'bearer %s' % api_key
}


if __name__ == '__main__':
    print(headers)