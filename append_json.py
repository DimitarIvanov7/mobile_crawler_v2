import json
from email_sending import *

def append_data_json(link):
    with open('links.json') as f:
        data = json.load(f)
    data.append(link)
    # print(data)
    # print(link)
    with open('links.json', 'w') as f:
        json.dump(data, f)
        # f.write(list_items)

def check_data(link):
    with open('links.json') as fh:
        link_list = fh.read()
        if link in link_list:
            # print("yes")
            return True
        else:
            # print("no")
            send_message(link.replace('//www.', ''))
            append_data_json(link)
            return False
