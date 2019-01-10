from test_functions import is_date, xls_output
from config import chat_name
import re

from datetime import datetime
from dateutil import parser
import pandas as pd

# clean data
with open('./txt/' + chat_name + '_last_messages.txt', 'r') as myfile:
    raw_data = myfile.readlines()
    clean_data = [x.strip() for x in raw_data] # clean strings
    clean_data = [x for x in clean_data if x != 'ߋ' and x != ''] # clean array

# parse data
messages_by_date = {}
message_time = ''
for line in clean_data:
    if re.match("\d+\-\d+\-\d+ \d+:\d+:\d+\+\d+:\d+", line):
        print(line)
        message_time = line
        messages_by_date[line] = []
    else:
        print(message_time)
        messages_by_date[message_time].append(line)
# print('pandas: ', int(pd.to_datetime(list(messages_by_date.keys())[0]).strftime('%Y%m%d%H%M%S')))

messages_by_date = sorted(messages_by_date.items(), key = lambda x:int(pd.to_datetime(x[0]).strftime('%Y%m%d%H%M%S')), reverse=True)
xls_output('./xls/' + chat_name + '_test_xls_output.xls', 'crypto_data', messages_by_date)
