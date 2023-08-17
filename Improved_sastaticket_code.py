import requests
import request_data   #headers and urls stored here
import pprint  
import helper  ##helper functions
from time import sleep

class RequestData():

    def __init__(self,url,headers):
        self.url = url
        self.headers= headers
        self.req_data = None

    def specify_routes_for_request(self,origin,destination,req_data_func):
        print('function',req_data_func)
        if origin and destination:
            self.req_data = req_data_func(origin,destination)
        else:
            print('routes not provided')
            return False

    def make_request(self):
        
        if self.url and self.req_data:
            try:
                
                res = requests.post(url=self.url,headers=self.headers,json=self.req_data)
                if (res.ok):
                    try:
                        return res.json()
                    except :
                        print('Something went Wrong')
                        return False
                else:
                    print(f'Error : {res.status_code}')
                    return False
                
            except (requests.ConnectionError,requests.Timeout) as e:
                print(f'Internet is Off \n {e}')
                return False
        else:
            print('url and headers not provided')
            return False


class ScrapData():

    def __init__(self,req_obj):
        self.res = req_obj
        self.res_data = self.res.make_request()



    def flight_data_sasta_ticket(self):
        # print(len(flights))
        flight_details = ['sastaticket.pk']
        # print(self.res_data,self.res_data['success'])
        if (self.res_data and self.res_data['success']):
            flights = self.res_data['data']['flights'][0]
            if (len(flights)>0):
                for i in range(len(flights)):

                    flight_name=flights[i]['provider']
                    flight_timing_d = flights[i]['legs'][0]['segments'][0]["departure_datetime"]
                    flight_timing_a  = flights[i]['legs'][0]['segments'][0]["arrival_datetime"]
                    extract_time_d = helper.convert_to_12_hour_format(flight_timing_d)
                    extract_time_a = helper.convert_to_12_hour_format(flight_timing_a)
                    fare_actual =  flights[i]['fare_options'][0]['price']["gross_fare"]
                    fare_discounted =  flights[i]['fare_options'][0]['price']['breakdown']['adult']["total_fare"]
                    if fare_discounted > fare_actual:
                        fare_actual = fare_discounted
                        fare_discounted= None
                    else: 
                        fare_discounted= fare_discounted

                    flight_details.append({'flight_name':flight_name,'flight_timing':{'departure_timing':extract_time_d,'arrival_timing':extract_time_a,'fare':{'fare_actual':fare_actual,'fare_discounted':fare_discounted}},})
                
                if len(flight_details)>1:
                    
                    return flight_details
                else:
                    return 'error something went wrong'
            else:
                return {'error:data not found'}
        else:
            return {'something went wrong'}





# GO ZOYAAN




# #####################################


# SASTATICKET

# req_data query 1 => KHI TO ISB
url = request_data.url2
headers = request_data.headers2
origin = 'KHI'
destination = 'ISB'
sastaticket_func = helper.req_data_for_sastaticket

# object
res = RequestData(url,headers)
res.specify_routes_for_request(origin,destination,req_data_func=sastaticket_func)

# object
obj = ScrapData(req_obj=res)
print(f'routes : {origin}-{destination}')
print('\n')
pprint.pprint(obj.flight_data_sasta_ticket())


sleep(20)



# req_data query 2 => KHI TO LHE
origin = 'KHI'
destination = 'LHE'

# object 
res = RequestData(url,headers)  #url and headers same
# with origin and destination
res.specify_routes_for_request(origin,destination,sastaticket_func)

print('\n')
obj2 = ScrapData(req_obj=res)
print('\n')
print(f'routes : {origin}-{destination}')
print('\n')
pprint.pprint(obj2.flight_data_sasta_ticket())
