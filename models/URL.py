import random

from db_config import init

class URL():
    all = []

    def __init__(self, data):
        self._short = data['short']
        self._long = data['long']
        URL.all.append(self)
    
    @property
    def short(self):
        return self._short
    
    @property
    def long(self):
        return self._long

    @classmethod
    def find_by_short(cls, short):
        return next((url for url in cls.all if url.short == short), None)
    
    @classmethod
    def find_by_long(cls, long):
        return next((url for url in cls.all if url.long == long), None)
    
    @classmethod
    def create(cls, long):
        short = cls.generate_short()
        url_data = { 'long': long, 'short': short }
        with init() as client:
            client.shortlify.url_data.insert_one(url_data)
        url = cls(url_data)
        return url
    
    @classmethod
    def generate_short(cls):
        possible_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        short_url = None

        # check for collisions
        while not short_url or next((url for url in cls.all if url.short == short_url), None):
            short_url = ''.join([random.choice(possible_chars) for _ in range(5)])
        
        return short_url
    
    @classmethod
    def load_from_db(cls):
        cls.all = []
        with init() as client:
            urls = list(client.shortlify.url_data.find())
            for url in urls:
                cls(url)

URL.load_from_db()
