import json, requests
from pprint import pprint

from base import Base, DbManager

class DCK():
    def __init__(self):
        self.db_Manager = DbManager()

    def get_json(self, url):
        resp = requests.get(url)
        if resp.status_code!=200:
            return None
        return json.loads(resp.text)

    def get_entity(self, obj, url):
        results = self.db_Manager.open().query(obj).filter(obj.api == url).all()
        
        json_data= self.get_json(url)
        entity = obj()
        entity.parse_json(json_data)
        
        if len(results)==0:
            self.db_Manager.save(entity)
        
        return entity

    def find_end(self, endChar, url):
        for index, c in enumerate(url[::-1]):
            if c==endChar:
                return len(url)-index-1
        
        return None

    def find_base_url(self, url):
        index=self.find_end('/', url)

        if index:
            return url[: index+1]
        else:
            return None

    def populate_table(self, obj, next_url):
        base_url=self.find_base_url(next_url)

        if base_url:
            group_data=self.get_json(next_url)
            page_id=1
            
            while group_data:
                print(next_url)
                for result in group_data:
                    single_url = result['api']
                    print(single_url)

                    self.get_entity(obj, single_url)
                
                page_id=page_id+1
                next_url=base_url+str(page_id)
                group_data=self.get_json(next_url)

                # group_data=None