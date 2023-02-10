from requests import get
from sys import argv, exit
from dewiki import from_string

def main():
    try:   
        term = get_args().replace(" ", "_")
        
        page_id = get_page_id(term)
        page_content = get_page_content(page_id)
     
        wiki = open(f'{term}.wiki', "w")
        wiki.write(page_content)
        wiki.close()
        
    except Exception as ex:
        print("An error ocurred!")
        exit()

def get_page_id(term_to_search):
    try:         
        url = 'https://en.wikipedia.org/w/api.php'
        params = {
                'action': 'query',
                'format': 'json',
                'titles': term_to_search,
                'prop': 'extracts',
                'redirects': True,
            }

        response = get(url, params=params).json()
        page_id = next(iter(response['query']['pages'].values())).get('pageid')
                
        if page_id == "" or page_id == None:
            raise NotFoundInAPI()
        
        return page_id

    except NotFoundInAPI as ex:
        print(ex)
        exit()
    except Exception as ex:
        print("An error ocurred!")
        exit()

def get_page_content(page_id):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'parse',
        'pageid': page_id,
        'prop': 'wikitext',
        'format': 'json'
    }
    try:
        response = get(url, params=params).json()
        data = response['parse']['wikitext']['*']
        return from_string(data).strip()
    except Exception as ex:
        print("An error occurred!")
        exit()


def get_args():
    try:
        if len(argv) != 2:
            raise Exception() 
        return argv[1].strip()
    except Exception:
        print("Wrong arguments!") 
        exit()

class NotFoundInAPI(Exception):
    def __init__(self) -> None:
        self.message = "Term not found on wikipedia."
        super().__init__(self.message)

if __name__ == "__main__":
    main()
    