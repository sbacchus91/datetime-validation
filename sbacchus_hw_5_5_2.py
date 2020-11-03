"""
Shane Bacchus
Class: CS 521 - Fall 1
Date:10/10
Homework Problem # 2
Description of Problem (just a 1-2 line summary!):
Validate Datetime
"""


def is_valid_datetime (date):
    """Dateime Validation"""
    print (is_valid_datetime.__doc__)
    #  Variable creation for validation

    date_correct = False
    error_message = ""
    


    #  Validation
    if len(date) != 19:
        date_correct = False
        error_message = "Invalid: Not Exact # of Characters expected in date"
        return date_correct, error_message

    #  If the above validation is passed, continue on to parse out the below
    day = date[3:5]
    month = date[0:2]
    year = date[6:10]
    hour = date[11:13]
    minute = date[14:16]
    second = date[17:19]
    first_slash = date[2]
    second_slash = date[5]
    first_colon = date[13]
    second_colon = date[16]

    if day.isdigit() == False or month.isdigit() == False or year.isdigit() == False or hour.isdigit() == False or minute.isdigit() == False or second.isdigit() == False:
        date_correct = False
        error_message = "Invalid: Components of date not found (Non Digits found when not expected)"
        return date_correct, error_message
    elif first_slash != '/' or second_slash !='/' or first_colon != ':' or second_colon !=':':
        date_correct = False
        error_message = "Invalid: Components of date not found (Forward slashes and colons are not found they should be)"
        return date_correct, error_message
    elif int(day) > 31:
        date_correct = False
        error_message = "Invalid: There are not more than 31 days in a month"
        return date_correct, error_message
    elif int(month) > 12:
        date_correct = False
        error_message = "Invalid: There are not more than 12 months in a year"
        return date_correct, error_message
    elif int(hour) > 24:
        date_correct = False
        error_message = "Invalid: There are not more than 24 hours in a day"
        return date_correct, error_message
    elif len(year) != 4:
        date_correct = False
        error_message = "Invalid: The year was not correctly entered"
        return date_correct, error_message
    elif int(minute) > 59:
        date_correct = False
        error_message = "Invalid: There are not more than 60 minutes in an hour"
        return date_correct, error_message
    elif int(second) > 59:
        date_correct = False
        error_message = "Invalid: There are not more than 60 seconds in a minute"
        return date_correct, error_message
    else: #  Return valid
        date_correct = True
        return date_correct, None
    
  
    

if __name__ == "__main__":
    date = input("Enter a date time including leading zeros on a 24 hour scale (MM/DD/YYYY HR:MIN:SEC): ") 
    returned_tuple = is_valid_datetime(date)

    if returned_tuple[0] == False: #  Invalid string prints
        print(returned_tuple[1])
        

    else: #  Valid string variable creations for print
        day = date[3:5]
        month = date[0:2]
        year = date[6:10]
        hour = date[11:13]
        minute = date[14:16]
        second = date[17:19]
        
        if int(hour) < 12:
            am_or_pm = 'AM'
        else:
            am_or_pm = 'PM'
        
        #  Print statements
        print("DD/MM/YYYY is " + day + '/' + month + '/' + year)
        print("HR:MIN:SEC is " + hour + ':' + minute + ':' + second)
        print("MM/YYYY is " + month + '/' + year)
        print("The time is " + am_or_pm)
    
    
	


