import sys

def get_credentials():
    api_name = input('Please tell me your API name: ')
    api_id = input('Now tell me your API ID: ')
    api_hash = input('Now I need your API hash: ')
    chat_name = input('Finally, tell me the user/chat/channel you want to log: ')
    user_data = {
        'api_name': api_name,
        'api_id': api_id,
        'api_hash': api_hash,
        'chat_name': chat_name
    }
    return user_data

def create_config(user_data):
    verbose = 'verbose = True\r\n'
    api_name = 'api_name = \'' + user_data['api_name'] + '\'\r\n'
    api_id = 'api_id = ' + user_data['api_id'] + '\r\n'
    api_hash = 'api_hash = \'' + user_data['api_hash'] + '\'\r\n'
    chat_name = 'chat_name = \'' + user_data['chat_name'] + '\'\r\n'
    f = open('config.py', 'w+')
    f.writelines([verbose, api_name, api_id, api_hash, chat_name])
    f.write('\r\n')
    f.close()

def save_message(message):
    f = open('telegram_messages.txt', 'a+')
    f.write(message + '\r\n')
    f.write('\r\n')
    f.close()

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
