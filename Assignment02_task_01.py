from bs4 import BeautifulSoup
import requests
import request_data
from datetime import date
import pprint
import re
from csv import DictWriter
import os

class RequestData():

    def __init__(self,url):
        self.soup = None
        self.url = url



    def make_request(self,):
        
        if self.url:
            try:
                res = requests.get(url=self.url,headers=request_data.headers)
                self.url = ''    # clear url
                if (res.ok):
                    try:
                        soup = BeautifulSoup(res.text, "html.parser")
                        for script in soup.find_all('script'):
                            script.extract()
                        self.soup = soup
                        return self.soup
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

    def update_url(self,up_path,fromm = '2023-06-01',to= '2023-08-11'):
        try:
            self.url = f'https://bindup.crowdmap.com/reports/fetch_reports?page={up_path}&from={fromm}&to={to}'
            
            return self.make_request()
        except AttributeError as ae:
            print(f'end of Pages {ae}')



class ScrapData():

    def __init__(self):
        self.data = []
        self.soup_obj = RequestData(request_data.url)
        self.soup = self.soup_obj.make_request()
        self.next_page = '1'
        self.field_names = ['TITLE', 'DATE', 'LOCATION',
               'URL', 'TEXT','CAPTURE_DATE']

    def scrape_next(self):
            if len(self.next_page.strip()) > 0:
                self.soup = self.soup_obj.update_url(self.next_page)
                self.scrap_required_data()

    def scrap_required_data(self):
        if self.soup:
            all_posts = self.soup.select('.r_details')
            check_page = self.soup.select('li a.next')[0].attrs['href']
            for data in all_posts:
                post_title =  data.select('h3 a.r_title')[0].text.strip()
                post_url = data.select('h3 a.r_title')[0].get('href')
                post_date = data.select('p.r_date')[0].text.strip()
                post_location = data.select('p.r_location a' )[0].text.strip()
                post_text= data.select('div.r_description')[0].text.strip()
                post_text = post_text.replace('\t','').replace('\n','').replace('More Information', '').replace('Less Information','')
                # soup_obj2 = RequestData(post_url)
                # soup2=soup_obj2.make_request()
                # # print(soup2,'tet')
                # desc= soup2.select('div.report-description-text')[0]
                # desc = desc.find_next('br').next_sibling.strip()
                # if desc:
                #     if 'Published' in desc:
                #         find_index = desc.index('Published')
                #         published = desc[find_index:]
                #     else:
                #         published= None
                # else:
                #     published= None
                
                dic={
                    'TITLE': post_title,
                    'DATE': post_date,
                    'LOCATION':post_location,
                    'URL': f'{post_url}',
                    'TEXT': post_text,
                    'CAPTURE_DATE': f'{date.today().isoformat()}',
                }
                self.data.append(dic)  ## just for showing data 
                
            with open('data.csv', 'a',encoding='utf-8') as f:
                dict_object = DictWriter(f, fieldnames=self.field_names)
                dict_object.writeheader()
                dict_object.writerows(self.data)
                f.close()

            pprint.pprint(f' - Last Post Of  Page No {self.next_page} : {self.data[-1]}')
            validate_for_number = re.search(r'\d+',check_page)
            if validate_for_number:
                number = validate_for_number.group()
                self.next_page = number
                print('Nextpage:',self.next_page)
                self.scrape_next()
            else:
                pprint.pprint(self.get_extracted_data())
                return

    def get_extracted_data(self):
        return {'Data':self.data,'Length':len(self.data)}



obj = ScrapData()
obj.scrap_required_data()
