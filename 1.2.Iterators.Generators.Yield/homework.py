import json
import hashlib


FILE = 'countries.json'
BASE_URL = 'https://en.wikipedia.org/wiki'
FILE_TO_WRITE = 'link_country.txt'


class LinkIterator:


    def __init__(self, file, base_url, file_to_write):
        
        self.file = file
        self.base_url = base_url
        self.file_to_write = file_to_write

        with open(self.file) as file_json:
            self.data = file_json.read()
            self.countries = json.loads(self.data)


    def get_pairs(self):

        self.pairs = {}
        for country in self.countries:
            self.link = '/'.join((self.base_url, country['name']['common']))
            self.pairs[country['name']['common']] = self.link

        return self.pairs


    def write_to_file(self):
        
        pairs = self.get_pairs()
        with open(self.file_to_write, 'w') as file:
            json_obj = json.dump(pairs, file, indent=1)


iterator = LinkIterator(FILE, BASE_URL, FILE_TO_WRITE)
iterator.write_to_file()


def generate_hash(file_path):
    
    with open(FILE_TO_WRITE, 'rb') as f:
        for line in f:
            line = line.strip()
            hash_line = hashlib.md5()
            hash_line.update(line)
            yield hash_line.digest()


for item in generate_hash(FILE_TO_WRITE):
    print(item)