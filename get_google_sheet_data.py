import requests

api_url = 'https://script.googleusercontent.com/macros/echo?user_content_key=9lqFBZi2A22CUqSKwQOi7n7m0KEkN87kwpzsPRsqC8heE9an5zsCBhJkssffHxJyJd0DeLVn3_zlRXjMJxbS5VZjRk80CfCKm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnNBDo7FyGVyfLyBFzUa2VmZXehupzsKB1C00WiIvGh4ywzixjekGD7hqNeBGxn1eug5FYLDp9NIKf-xX-1qEzQhlBLShXJG4bw&lib=MGx_eLQEPVcYO02QUsCE725WdL364Yahp'
response = requests.get(api_url)

if response.status_code == 200:
    json_data = response.json()

    # Accessing specific keys in the JSON object
    if 'data' in json_data:
        data_list = json_data['data']

        # Flag to check if employee with Emp Id 1372 exists
        employee_found = False

        # Loop through the list of dictionaries
        for item in data_list:
            emp_id = item.get('Emp Id')
            if emp_id is not None:
                if emp_id == 8057:
                    print("Employee Found:")
                    print(item)
                    employee_found = True
                    break  # Exit the loop since we found the employee

        if not employee_found:
            print("Not Found")
    else:
        print("The 'data' key is not present in the JSON response.")