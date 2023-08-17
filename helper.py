from datetime import datetime
import pytz

def convert_to_12_hour_format(timestamp, target_timezone_str= 'Asia/Karachi'):
    datetime_obj = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
    target_timezone = pytz.timezone(target_timezone_str)
    datetime_obj_target_timezone = datetime_obj.astimezone(target_timezone)
    # Extract the time in 12-hour format (AM/PM)
    converted_time_12_hour = datetime_obj_target_timezone.strftime("%I:%M %p")
    return converted_time_12_hour


def convert_to_12_hour_format_for_zayaan(timestamp, target_timezone_str= 'Asia/Karachi'):
    datetime_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    target_timezone = pytz.timezone(target_timezone_str)
    datetime_obj_target_timezone = datetime_obj.astimezone(target_timezone)
    # Extract the time in 12-hour format (AM/PM)
    converted_time_12_hour = datetime_obj_target_timezone.strftime("%I:%M %p")
    return converted_time_12_hour

def req_data_for_sastaticket(origin,destination,date='2023-08-19'):
    req_json_data = {
    'route_type': 'ONEWAY',
    'cabin_class': {
        'code': 'Y',
        'label': 'Economy',
    },
    'traveler_count': {
        'num_adult': 1,
        'num_child': 0,
        'num_infant': 0,
    },
    'legs': [
        {
            'departure_date': f'{date}',
            'origin': f'{origin}',
            'destination': f'{destination}',
        },

    ],
    'analytics_data': {
        'device_id': '76e7c873-1c59-40f5-99c7-500921dfb3f8',
    },
    }

    # print('data:',req_json_data)
    return req_json_data


def req_data_for_gozayaan(origin,destination,date):
    req_json_data2 = {
    'adult': 1,
    'child': 0,
    'child_age': [],
    'infant': 0,
    'cabin_class': 'Economy',
    'trips': [
        {
            'origin': f'{origin}',
            'destination': f'{destination}',
            'preferred_time': f'{date}',
        },
    ],
    'currency': 'PKR',
    'region': 'PK',
    'segment_id': 'ef33e8dd-83c4-473e-84f1-bc01363fc82f',
    'platform_type': 'GZ_WEB',
    }

    return req_json_data2




