from dateutil.parser import parse

# functions
def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False
