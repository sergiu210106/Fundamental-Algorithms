from datetime import datetime

def ex15(birthdate_str : str, currentdate_str: str):
    '''
    function that returns the number of days between two dates

    :param birthdate_str: str
    :param currentdate_str: str

    :return: int
    '''
    date_format = "%d.%m.%Y"
    birthdate = datetime.strptime(birthdate_str, date_format)
    currentdate = datetime.strptime(currentdate_str, date_format)

    diff = currentdate - birthdate

    return diff.days

if __name__ == "__main__":
    birthdate_str = input("Enter birthdate: ")
    currentdate_str = input("Enter current date: ")

    print(ex15(birthdate_str, currentdate_str))
