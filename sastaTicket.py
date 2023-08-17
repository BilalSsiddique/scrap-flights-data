import requests
import request_data   #headers and urls stored here
import pprint  
import helper  ##helper functions


class RequestData():

    def __init__(self,url,headers):
        self.url = url
        self.headers = headers


    def specify_routes_for_request(self,origin,destination,date):
        
        res_data = helper.req_data_for_sastaticket(origin,destination,date)
        return res_data


    def make_request(self,origin,destination,date):
        
        if self.url and self.headers and origin and destination and date:
            try:
                if self.specify_routes_for_request(origin,destination,date):
                    res = requests.post(url=self.url,headers=self.headers,json=self.specify_routes_for_request(origin,destination,date))
                    if (res.ok):
                        try:
                            return res.json()
                        except :
                            print('Something went Wrong')
                            return False
                    else:
                        print(f'Error : {res.status_code}')
                        return False
                else:
                    print('routes error, routes not privovided')
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
        self.date= date
        self.res_data = self.res.make_request(self.origin,self.destination,date)


    def flight_data(self):
        # print(len(flights))
        flight_details= [{'Website Name:','SastaTicket'}]
        # print(self.res_data,self.res_data['success'])
        # print(self.res_data)
        if (self.res_data and self.res_data['success'] and len(self.res_data['data']['flights'][0])>0):
            # print(self.res_data)
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
                    print(f'routes : {self.origin}-{self.destination} Date: {self.date}')
                    return flight_details
                else:
                    return 'error something went wrong'
            else:
                return {'error:data not found'}
        else:
            return {'flight details empty, Try again'}



# KHI-ISB => date='2023-08-19'
obj = ScrapData(url=request_data.url2,headers=request_data.headers2,origin='KHI',destination='ISB',date='2023-08-19')
print('\n')
pprint.pprint(obj.flight_data())

# date='2023-08-20'
obj = ScrapData(url=request_data.url2,headers=request_data.headers2,origin='KHI',destination='ISB',date='2023-08-20')
print('\n')
pprint.pprint(obj.flight_data())

# date='2023-08-21'
obj = ScrapData(url=request_data.url2,headers=request_data.headers2,origin='KHI',destination='ISB',date='2023-08-21')
print('\n')
pprint.pprint(obj.flight_data())


# for KHI-LHE   => date='2023-08-19'
print('\n')
obj2 = ScrapData(url=request_data.url2,headers= request_data.headers2,origin='KHI',destination='LHE',date='2023-08-19')
print('\n')
pprint.pprint(obj2.flight_data())

# => date='2023-08-20'
print('\n')
obj2 = ScrapData(url=request_data.url2,headers= request_data.headers2,origin='KHI',destination='LHE',date='2023-08-20')
print('\n')
pprint.pprint(obj2.flight_data())

# => date='2023-08-21'
print('\n')
obj2 = ScrapData(url=request_data.url2,headers= request_data.headers2,origin='KHI',destination='LHE',date='2023-08-21')
print('\n')
pprint.pprint(obj2.flight_data())