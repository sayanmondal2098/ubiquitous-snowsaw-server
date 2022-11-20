import requests

SERVICENOW_URL = 'https://dev100406.service-now.com/'
SERVICENOW_USER = 'admin'
SERVICENOW_PWD = 'w96jcJmKM=B@'

DOWNLOAD_DIR = './downloads/'


REQUEST_HEADER = {"json": {"Content-Type": "application/xml", "Accept": "application/json"},
                  "png": {"Content-Type": "application/xml", "Accept": "application/png"},
                  "xml": {"Content-Type": "application/xml", "Accept": "application/xml"},
                  }

ATTACHMENT_API = '/api/now/attachment'
TABLE_API = '/api/now/table'
# TABLE_NAME = 'kb_knowledge'
TABLE_NAME = 'incident'


def get_table_data(table_name, param):
    url = SERVICENOW_URL + TABLE_API + '/' + table_name + '?' + param
    response = requests.get(url, auth=(SERVICENOW_USER, SERVICENOW_PWD), headers=REQUEST_HEADER.get('json'))
    if response.status_code != 200:  # if error, then exit
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    return response.json()


def get_attachment_info(sys_id):
    url = SERVICENOW_URL + ATTACHMENT_API + '/' + sys_id
    response = requests.get(url, auth=(SERVICENOW_USER, SERVICENOW_PWD), headers=REQUEST_HEADER.get('json'))
    if response.status_code != 200:  # if error, then exit
        print(f'Status:  {response.status_code}, Headers:{response.headers}')
        exit()
    return response.json()


def get_attachment(att_sys_id, file_type, download_dir):
    url = SERVICENOW_URL + '/' + ATTACHMENT_API + '/' + att_sys_id + '/file'
    response = requests.get(url, auth=(SERVICENOW_USER, SERVICENOW_PWD), headers=REQUEST_HEADER.get(file_type))
    if response.status_code != 200:  # if error, then exit
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    with open(download_dir, 'wb') as f:
        for chunk in response:
            f.write(chunk)


def get_file_attachment(record_number):
    param = 'sysparm_query=number=' + record_number + '&sysparam_limit=1'

    file_info = get_table_data(TABLE_NAME, param).get('result')
    if len(file_info) < 1:
        print(f'There is no attachment to sys_id:{record_number}')
        return
    attachment_sys_id = file_info[0].get('sys_id')

    param = 'sysparm_query=table_sys_id=' + attachment_sys_id + '&sysparam_limit=1'
    record = get_table_data('sys_attachment', param)
    result = record.get('result')
    for attach_file in result:
        attach_sys_id = attach_file.get('sys_id')
        content_type = attach_file.get('content_type').split('/')
        file_ext = content_type[1]
        file_name = attach_file.get('file_name')
        get_attachment(attach_sys_id, file_ext, DOWNLOAD_DIR + file_name)

