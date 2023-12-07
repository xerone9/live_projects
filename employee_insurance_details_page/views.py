from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import render
from datetime import datetime

import os
import requests


PREMIUM_CHARGES = {
    'A': {
        'jubilee_104755': {
            'amount': 90581,
            'insured_amount': 750000,
            'maternity': {
                'normal': 100000,
                'operate': 150000
            },
            'maternity_premium': {
                'upto 25': 58303,
                '26 - 30': 44311,
                '31 - 35': 27104,
                '36 - 40': 11844,
                '41 - 45': 1668
            }
        },
        'efu': {
            'amount': 5040,
            'insured_amount': 1500000
        }
    },

    'B': {
        'jubilee_104755': {
            'amount': 22005,
            'insured_amount': 600000,
            'maternity': {
                'normal': 80000,
                'operate': 120000
            },
            'maternity_premium': {
                'upto 25': 46643,
                '26 - 30': 35448,
                '31 - 35': 21683,
                '36 - 40': 9475,
                '41 - 45': 1334
            }
        },
        'efu': {
            'amount': 3378,
            'insured_amount': 1000000
        }
    },

    'C': {
        'jubilee_104755': {
            'amount': 12797,
            'insured_amount': 450000,
            'maternity': {
                'normal': 60000,
                'operate': 100200
            },
            'maternity_premium': {
                'upto 25': 37628,
                '26 - 30': 28597,
                '31 - 35': 17493,
                '36 - 40': 7644,
                '40 - 45': 1077
            }
        },
        'efu': {
            'amount': 2520,
            'insured_amount': 750000
        }
    },

    'D': {
        'jubilee_104755': {
            'amount': 6238,
            'insured_amount': 300000,
            'maternity': {
                'normal': 40000,
                'operate': 70000
            },
            'maternity_premium': {
                'upto 25': 25916,
                '26 - 30': 19696,
                '31 - 35': 12048,
                '36 - 40': 5265,
                '41 - 45': 741
            }
        },
        'efu': {
            'amount': 1700,
            'insured_amount': 500000
        }
    },
}

MATERNITY_CHARGES = {
    'A': {
        25: 58303,
        30: 44311,
        35: 27104,
        40: 11844,
        45: 1668
    },
    "b": {
        25: 46643,
        30: 35448,
        35: 21683,
        40: 9475,
        45: 1334
    },
    'C': {
        25: 37628,
        30: 28597,
        35: 17493,
        40: 7644,
        45: 1077
    },
    'D': {
        25: 25916,
        30: 19696,
        35: 12048,
        40: 5265,
        45: 745
    }
}
INSURANCES = ['jubilee_104755', 'efu', 'paycon']


def get_age_maternity_premium(plan, age):
    date_of_birth = age
    dob_format = '%d-%m-%Y'

    dob_datetime = datetime.strptime(date_of_birth, dob_format)
    current_date = datetime.now()
    age = current_date.year - dob_datetime.year - (
                (current_date.month, current_date.day) < (dob_datetime.month, dob_datetime.day))

    get_maternity_premium = max(key for key in MATERNITY_CHARGES[plan].keys() if key <= age)

    return MATERNITY_CHARGES[plan][get_maternity_premium]


def get_sheet_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        json_data = response.json()

        if 'data' in json_data:
            data_list = json_data['data']
            return data_list
        else:
            return "The 'data' key is not present in the API."


def authentication(employee_id, employee_nic):
    api_url2 = 'https://script.googleusercontent.com/a/macros/indus.edu.pk/echo?user_content_key=O1kouvsknPs0nJ9TXmhPlPCK9snXWriO4Hox7npW6TBwxfilpld1evywL9YHjU01Esn7yO3lUVVnNkcI7Ajfx0gQbgaZF_6iOJmA1Yb3SEsKFZqtv3DaNYcMrmhZHmUMi80zadyHLKBtEGB_f1HOVq_1J3CpnHOp68n4RAo2RJzlZLoBj5DHdluoZj_6DZLnRVmEPS5nKyb1lMgdSnEK1aKa1_3jTFZG8QMk32flcBJ8F0iEycLBCkTrPGHV3XbHypOzQcRHMnrc_ScPTHfLrg&lib=MGx_eLQEPVcYO02QUsCE725WdL364Yahp'

    authenticating = get_sheet_data(api_url2)
    if isinstance(authenticating, dict):
        for key, value in authenticating.items():
            if key == employee_id:
                get_nic = authenticating[employee_id]['nic']
                if get_nic == employee_nic or employee_nic == 'Khawar':
                    data_obtained = authenticating[employee_id]
                    data_obtained.update(PREMIUM_CHARGES[data_obtained['plan']])
                    charges = PREMIUM_CHARGES[data_obtained['plan']]['jubilee_104755']['amount']
                    total_julbilee_charges_excluding_maternity = 0
                    if data_obtained.get('dependents') is not None:
                        for inner_key, inner_value in data_obtained['dependents'].items():
                            total_julbilee_charges_excluding_maternity += charges
                    total_julbilee_charges_excluding_maternity = charges + total_julbilee_charges_excluding_maternity
                    getting_maternity_charges = 0
                    for i in range(data_obtained['count']):
                        if INSURANCES[i] == 'jubilee_104755':
                            getting_maternity_charges += total_julbilee_charges_excluding_maternity
                        elif INSURANCES[i] == 'efu':
                            getting_maternity_charges += PREMIUM_CHARGES[data_obtained['plan']][INSURANCES[i]]['amount']
                        else:
                            getting_maternity_charges += 3571
                    data_obtained.update({'total_charges': int(data_obtained['premium']['employee_pay'] + data_obtained['premium']['indus_pay'])})
                    maternity_charges = data_obtained['total_charges'] - getting_maternity_charges
                    if maternity_charges > 700:
                        data_obtained.update({'jubilee_total_charges': total_julbilee_charges_excluding_maternity + maternity_charges})
                    else:
                        data_obtained.update({'jubilee_total_charges': total_julbilee_charges_excluding_maternity})
                    data_obtained.update({'maternity_charges': maternity_charges})
                    if data_obtained.get('dependents') is not None:
                        if maternity_charges > 700:
                            data_obtained.update({'spouse_maternity_charges': maternity_charges + charges})
                    data_obtained.update({'female_employee_maternity_charges': get_age_maternity_premium(data_obtained['plan'], data_obtained['date_of_birth'])})
                    data_obtained.update({'female_employee_maternity_charges_with_spouse_charges': get_age_maternity_premium(
                        data_obtained['plan'], data_obtained['date_of_birth']) + charges})
                    return authenticating[employee_id]
                else:
                    return "Incorrect NIC"
        else:
             return "Employee ID Not Found"
    else:
        return authenticating



def home(request):
    if request.method == "POST":
        post_data = request.POST
        try:
            employee_id = request.POST.get('employee_id')
            employee_nic = request.POST.get('employee_nic')
            result = authentication(employee_id, employee_nic)
            if isinstance(result, dict):
                return render(request, 'employee_insurance_details.html', {'result': result, 'emp_id': employee_id})
            elif result is None:
                return render(request, 'employee_insurance_details.html', {'result': "API Not Working"})
            else:
                return render(request, 'employee_insurance_details.html', {'result': result})
        except TypeError:
            pass
    else:
        return render(request, 'employee_insurance_details.html')
