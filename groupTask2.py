"""Usage: mac_conversion.py (-T|-D) [-f <filename> | -x <hexvalue>] 
        
 
Arguments:
    -T  time conversion
    -D  date conversion

Options:
    -x <hexvalue>  get hexvalue
    -f <filename>  get filename
"""

from docopt import docopt
import datetime
import os

if __name__ == '__main__':
   
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__)
    #print(arguments)
    temp = 0
    #Perform little endian swap
    if arguments['-x']:
        temp = arguments['-x']
    else:
        #filename = "input.txt"
        #dir = os.path.dirname(filename)
        #if not os.path.exists(dir):
        #    os.makedirs(dir)
        # 
        with open(arguments['-f'], 'r+') as fin:
            for line in fin:
                #print(line)
                temp = line
        
    first_two = temp[2:4]
    last_two = temp[4:]
    little_e = last_two+first_two

    #print(little_e)
    #Hex to decimal conversion
    decimal_num = int(little_e, 16)
    #print(decimal_num)
    
    #Dec to bin conversion
    bin_num = decimal_num
    #print(bin_num)
    
    #Time conversion - hour(5 bits) minute(6 bits) second(5 bits)
    if arguments['-T'] == True:
        
        bit_mask = 31
        mask_hour = bin_num >> 11
        hour = mask_hour & bit_mask

        bit_mask = 63
        mask_minute = bin_num >> 5
        minute = mask_minute & bit_mask

        bit_mask = 31
        second = bin_num & bit_mask

        second = second * 2

        am_pm = "am"
        
        if hour > 12:
            am_pm = "pm"

        hour = hour % 12
        
        print("Time: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + am_pm)

    
    #Date conversion - year(7 bits) month(4 bits) day(5 bits)
    else:
        
        #print("else")

        bit_mask = 127
        mask_year = bin_num >> 9
        year = mask_year & bit_mask
        year = year + 1980
        #print("Year = " + str(year))

        bit_mask = 15
        mask_month = bin_num >> 5
        month = mask_month & bit_mask

        #print("Month = " + str(month))

        bit_mask = 31
        day = bin_num & bit_mask

        #print("Day = " + str(day))

        input = str(day)+'/'+str(month)+'/'+str(year)
        my_date = datetime.datetime.strptime(input, "%d/%m/%Y")

        print ("Date: " + my_date.strftime("%d %b, %Y"))


