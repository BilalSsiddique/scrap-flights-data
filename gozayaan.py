import requests
import request_data   #headers and urls stored here
import pprint  
import helper  ##helper functions
import json
import time


class RequestData():

    def __init__(self,url,headers):
        self.url = url
        self.headers = headers
        self.resp_data = []


    def specify_routes_for_request(self,origin,destination,date):
        
        res_data = helper.req_data_for_gozayaan(origin,destination,date)
        return res_data


    def make_request(self,origin,destination,date):
        
        if self.url and self.headers and origin and destination and date:
            try:
                if self.specify_routes_for_request(origin,destination,date):
                    res = requests.post(url=self.url,headers=self.headers,json= self.specify_routes_for_request(origin,destination,date))
                    if (res.ok):
                        try:
                            resp = res.json()
                            id_for_req = resp['result']['id']
                            if id_for_req:
                                next_req = requests.get(self.url+id_for_req,headers=self.headers)
                                if next_req.ok:
                                    print('request ok')
                                    next_req = next_req.json()
                                    
                                    
                                    while True:
                                        if len(next_req['result']['results'])>0:
                                            self.resp_data.append(next_req['result']['results'])
                                            print('Server:',next_req['result']['status'])
                                            if next_req['result']['status'] == 'DONE':
                                                print('DONE')
                                                
                                                return self.resp_data
                                            else:
                                                
                                                next_req = requests.get(self.url+id_for_req,headers=self.headers)
                                                next_req = next_req.json()
                                        else:
                                            next_req = requests.get(self.url+id_for_req,headers=self.headers)
                                            next_req = next_req.json()
                                    
                                        # return next_req['result']['results']       
    
                                else:
                                    print(f'Error : {next_req.status_code}')
                                    return False
                        except :
                            print('Something went Wrong')
                            return False
                    else:
                        print(f'Error : {res.status_code}')
                        return False
                else:
                    print('routes error, failed')
                    return False
            except (requests.ConnectionError,requests.Timeout) as e:
                print(f'Internet is Off \n {e}')
                return False
        else:
            print('url and headers not provided')
            return False




class ScrapData():

    def __init__(self,origin,destination,url,headers,date):
        self.res = RequestData(url,headers)
        self.origin  = origin
        self.destination = destination
        self.date = date
        self.res_data = self.res.make_request(self.origin,self.destination,self.date)
        # print(self.res_data)


    def flight_details_goZayaan(self):
        if (self.res_data and len(self.res_data)>0):
            result = self.res_data
            
            flight_details= [{'Website Name:','GoZayaan'}]
            total_flights = 0
            for i in range(len(result)):
                for j in range(len(result[i])):
                    total_flights+=1
                    flight_name = result[i][j]['flights'][0]['plating_carrier']['name']
                    flight_timing_d = result[i][j]['flights'][0]['options'][0]['departure_time']
                    flight_timing_a = result[i][j]['flights'][0]['options'][0]['arrival_time']
                    extract_time_d = helper.convert_to_12_hour_format_for_zayaan(flight_timing_d)
                    extract_time_a = helper.convert_to_12_hour_format_for_zayaan(flight_timing_a)
                    fare_actual = result[i][j]['total_price']
                    fare_discount = result[i][j]['discount']
                    if fare_discount:
                        fare_discount = fare_discount
                    else:
                        fare_discount= None
                    
                    flight_details.append({'flight_name':flight_name,'flight_timing':{'departure_timing':extract_time_d,'arrival_timing':extract_time_a,'fare':{'fare_actual':fare_actual,'fare_discounted':fare_discount}},})
            
            print('Total Flights:', total_flights)
            print(f'routes : {self.origin}-{self.destination} Date: {self.date}')
            return flight_details
            # else:
            #     return 'error something went wrong'
            
        else:
            return {'data not found'}



# KHI - ISB => date='2023-08-19') 
obj = ScrapData(url=request_data.url3,headers=request_data.headers3,origin='KHI',destination='ISB',date='2023-08-19')
print('\n')
pprint.pprint(obj.flight_details_goZayaan())

# KHI - ISB => date='2023-08-20') 
obj = ScrapData(url=request_data.url3,headers=request_data.headers3,origin='KHI',destination='ISB',date='2023-08-20')
print('\n')
pprint.pprint(obj.flight_details_goZayaan())

# KHI - ISB => date='2023-08-21') 
obj = ScrapData(url=request_data.url3,headers=request_data.headers3,origin='KHI',destination='ISB',date='2023-08-21')
print('\n')
pprint.pprint(obj.flight_details_goZayaan())



# KHI - LHE => date='2023-08-19') 
obj = ScrapData(url=request_data.url3,headers=request_data.headers3,origin='KHI',destination='LHE',date='2023-08-19')
print('\n')
pprint.pprint(obj.flight_details_goZayaan())

# KHI - LHE => date='2023-08-20') 
obj = ScrapData(url=request_data.url3,headers=request_data.headers3,origin='KHI',destination='LHE',date='2023-08-20')
print('\n')
pprint.pprint(obj.flight_details_goZayaan())

# KHI - LHE => date='2023-08-21') 
obj = ScrapData(url=request_data.url3,headers=request_data.headers3,origin='KHI',destination='LHE',date='2023-08-21')
print('\n')
pprint.pprint(obj.flight_details_goZayaan())