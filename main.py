import requests
import json
from pprint import pprint
from urllib.parse import urlparse
from urllib.parse import parse_qs


def get_query_params():
    """ parse query parameters from a URL for later usages """
    url = "http://nb.ncha.gov.cn/je/api/load?tableCode=QldHX05CTE4%3D&whereSql=QU5EIE5CX05EID0gMjAyMSBBTkQgTkJfU19OQU1FID0gJ%2BWMl%2BS6rOW4gic%3D&orderSql=&page=1&start=0&limit=15"
    parsed_url  = urlparse(url)
    params = parse_qs(parsed_url.query)
    new_params = {}
    # By default, params store values as an array, in our scenario ,there is only one item in each array
    # so we convert the `params` dict to a more concise one
    for k, v in params.items():
        new_params[k] = v[0]  
    pprint(new_params)


def main():
    # such url can be retrieve from chrome (or other explorer)
    url = 'http://nb.ncha.gov.cn/je/api/load'

    # These values are directly copy from the website url
    # You can try new values of the following params to test if more data can be fetched at a time
    # Sometimes you may have to modify both `page` and `start` to check whether more data can be fetched.
    # You can also use `for` loop to perform multiple requests and join all the data
    params = {
        'limit': '15',

        # data are organized into pages in order to make the server response more quickly.
        'page': '1', 

        # Some implementation of a server may use such param to mark the data offset. 
        # By common practice, you can change it to 15 to check whether more data can be loaeded
        'start': '0',  

        # Need more investigation on these two, I guess this is related to museums from diffent zones, cities, etc.
        'tableCode': 'QldHX05CTE4=',
        'whereSql': 'QU5EIE5CX05EID0gMjAyMSBBTkQgTkJfU19OQU1FID0gJ+WMl+S6rOW4gic='
    }

    payload={}

    # seems like `Cookie` maybe not a required item
    headers = {
        'Cookie': 'JSESSIONID=C41D0197789C067D62C09012DC62AF61'
    }
    response = requests.request("GET", url, headers=headers, data=payload, params=params)
    resp = json.loads(response.text)
    # rows = resp['']
    pprint(resp)


if __name__ == '__main__':
    main()