import pprint

# Task 01 request_data => crowdmap

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


url = 'https://bindup.crowdmap.com/reports/fetch_reports?page=1&from=2023-06-01&to=2023-08-11'

# https://bindup.crowdmap.com/reports/fetch_reports?page=3&from=2023-06-01&to=2023-08-11


# TASKS 02 DATA part01 => sastaticket

headers2 = {
    'authority': 'www.sastaticket.pk',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://flights.sastaticket.pk',
    'referer': 'https://flights.sastaticket.pk/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}



url2=  'https://www.sastaticket.pk/api/v4/flights/'



# TASKS 02 DATA part02 => Gozayaan






url3 = 'https://production.gozayaan.com/api/flight/v2.0/search/'


headers3 = {
    'authority': 'production.gozayaan.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.gozayaan.com',
    'referer': 'https://www.gozayaan.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data2 = {
    'adult': 1,
    'child': 0,
    'child_age': [],
    'infant': 0,
    'cabin_class': 'Economy',
    'trips': [
        {
            'origin': 'KHI',
            'destination': 'ISB',
            'preferred_time': '2023-08-20',
        },
    ],
    'currency': 'PKR',
    'region': 'PK',
    'segment_id': 'ef33e8dd-83c4-473e-84f1-bc01363fc82f',
    'platform_type': 'GZ_WEB',
}

# response = requests.post('https://production.gozayaan.com/api/flight/v2.0/search/', headers=headers3, json=json_data2)
# response_json = response.json()
# id_for_request = response_json['result']['id']
# print(id_for_request)

