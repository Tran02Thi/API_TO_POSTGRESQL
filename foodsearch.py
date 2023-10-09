from request import Request
import requests


class FoodSearch:
    def __init__(self, term, location,  categories, price=None):
        self._param = {'term': term, 'location': location, 'categories': categories}
        if price:
            self._param['price'] = price
        self._base_url= f"https://api.yelp.com/v3/transactions/delivery/search"
        self._food_list = self._search_food()
    def _search_food(self):
        food_search_request = Request.get_content(self._base_url, self._param)
        return food_search_request['businesses'] if food_search_request is not None else []

    def _parse_result(self, data):
       # Categories data : 'categories: [{'alias': 'empanadas', 'title': 'Empanadas'}]
        categories = ' '.join([category['title'] for category in data['categories']])

        # Longitude and latitude data :  'coordinates': {'latitude': 45.5232, 'longitude': -73.583459}
        longitude = data['coordinates']['longitude']
        latitude  = data['coordinates']['latitude']

        # Location example : 'location': { 'display_address': ['316 Avenue du Mont-Royal E', 'Montreal, QC H2T 1P7', 'Canada']}
        location = ','.join(data['location']['display_address'])

        return {
            'id': data['id'], 'name': self._add_escape_character(data['name']), 'image_url': data['image_url'], 'url': data['url'],
            'review_count': data['review_count'], 'categories': categories, 'rating': data['rating'], 'latitude': latitude,
            'longitude': longitude, 'price': data['price'], 'location': location, 'display_phone': data['display_phone']
        }
    def _add_escape_character(self, data):
        return data.replace("'", "''")

    def get_result(self):
        return [ self._parse_result(business) for business in self._food_list]