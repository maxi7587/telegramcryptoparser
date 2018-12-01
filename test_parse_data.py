from test_functions import is_date, xls_output

# clean data
with open('test_messages.txt', 'r') as myfile:
    raw_data = myfile.readlines()
    # raw_data = myfile.read().replace('\n', '')
    clean_data = [x.strip() for x in raw_data] # clean strings
    clean_data = [x for x in clean_data if x != 'ߋ' and x != ''] # clean array

# parse data
messages_by_date = {}
message_time = ''
for line in clean_data:
    if is_date(line):
        message_time = line
        messages_by_date[line] = []
    else:
        messages_by_date[message_time].append(line)


xls_output('test_xls_output.xls', 'crypto_data', messages_by_date)
