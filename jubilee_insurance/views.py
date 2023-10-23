from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import render
from . import Jubilee_inpatient_pdf_form

import os
import requests


def get_sheet_data(employee_id):
    api_url = 'https://script.google.com/macros/s/AKfycbxD045hW1QEG7guajDL5JtwVC85VZa_srUX09V0tCsK_uvjNf6lNRXyCMt-46N4EPm78Q/exec'
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = response.json()

        if 'data' in json_data:
            data_list = json_data['data']

            employee_found = False
            employee_details = ""
            for item in data_list:
                emp_id = item.get('Emp Id')
                employee_details = item
                if emp_id is not None:
                    try:
                        if emp_id == int(employee_id) and len(str(item.get('Deleted On'))) < 1:
                            # print(item)
                            employee_found = True
                            break  # Exit the loop since we found the employee
                    except ValueError:
                        employee_found = True
                        employee_details = "Incorrect Value Entered"

            if employee_found:
                return employee_details
            else:
                return "Employee Not Found"
        else:
            return "The 'data' key is not present in the API."


def home(request):
    if request.method == "POST":
        post_data = request.POST

        if "company_name" in post_data:
            pdf_form = Jubilee_inpatient_pdf_form.generate_pdf_report(post_data)
            script_directory = os.path.dirname(os.path.abspath(__file__))
            response = HttpResponse(open(os.path.join(script_directory, pdf_form), 'rb'), content_type='application/pdf')
            return response

        try:
            employee_id = request.POST.get('employee_id')
            result = get_sheet_data(employee_id)
            jubilee_data = []
            if isinstance(result, dict):
                for value in result.values():
                    jubilee_data.append(value)
                return render(request, 'jubilee_health_insurance.html', {'jubilee_data': jubilee_data})
            elif result is None:
                return render(request, 'jubilee_health_insurance.html', {'result': "API Not Working"})
            else:
                return render(request, 'jubilee_health_insurance.html', {'result': result})
        except TypeError:
            pass
    else:
        return render(request, 'jubilee_health_insurance.html')


