#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : scc.py
    License      : GNU General Public License v3.0


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

# All import statements for Gujarati પંચાંગ - ચોઘડિયા
import platform
import sys
from datetime import datetime as dt

# Constants for the names of the Gujarati પંચાંગ - ચોઘડિયા
CHOGHADIYU_AM: str = 'Amrut'
CHOGHADIYU_CH: str = 'Chal'
CHOGHADIYU_KA: str = 'Kaal'
CHOGHADIYU_LA: str = 'Laabh'
CHOGHADIYU_RO: str = 'Rog'
CHOGHADIYU_SH: str = 'Shubh'
CHOGHADIYU_UD: str = 'Udveg'

#
# Dictionary holding names of all the choghadiya for all the days of a week
# Structure of this nested dictionary is as follows:
# Out most dictionary holds key-value pair of weekday number and respective
# Choghadiya names for day and night as inner dictionary.
# Weekday number corresponds to weekday number returned by Python's Weekday
# method of the datetime class.
#
CHOGHADIYA_DICT = {
    0:  # MONDAY
        {'D': {1: CHOGHADIYU_AM,
               2: CHOGHADIYU_KA,
               3: CHOGHADIYU_SH,
               4: CHOGHADIYU_RO,
               5: CHOGHADIYU_UD,
               6: CHOGHADIYU_CH,
               7: CHOGHADIYU_LA,
               8: CHOGHADIYU_AM},
         'N': {1: CHOGHADIYU_CH,
               2: CHOGHADIYU_RO,
               3: CHOGHADIYU_KA,
               4: CHOGHADIYU_LA,
               5: CHOGHADIYU_UD,
               6: CHOGHADIYU_SH,
               7: CHOGHADIYU_AM,
               8: CHOGHADIYU_CH}
         },
    1:  # TUESDAY
        {'D': {1: CHOGHADIYU_RO,
               2: CHOGHADIYU_UD,
               3: CHOGHADIYU_CH,
               4: CHOGHADIYU_LA,
               5: CHOGHADIYU_AM,
               6: CHOGHADIYU_KA,
               7: CHOGHADIYU_SH,
               8: CHOGHADIYU_RO},
         'N': {1: CHOGHADIYU_KA,
               2: CHOGHADIYU_LA,
               3: CHOGHADIYU_UD,
               4: CHOGHADIYU_SH,
               5: CHOGHADIYU_AM,
               6: CHOGHADIYU_CH,
               7: CHOGHADIYU_RO,
               8: CHOGHADIYU_KA}
         },
    2:  # WEDNESDAY
        {'D': {1: CHOGHADIYU_LA,
               2: CHOGHADIYU_AM,
               3: CHOGHADIYU_KA,
               4: CHOGHADIYU_SH,
               5: CHOGHADIYU_RO,
               6: CHOGHADIYU_UD,
               7: CHOGHADIYU_CH,
               8: CHOGHADIYU_LA},
         'N': {1: CHOGHADIYU_UD,
               2: CHOGHADIYU_SH,
               3: CHOGHADIYU_AM,
               4: CHOGHADIYU_CH,
               5: CHOGHADIYU_RO,
               6: CHOGHADIYU_KA,
               7: CHOGHADIYU_LA,
               8: CHOGHADIYU_UD}
         },
    3:  # THURSDAY
        {'D': {1: CHOGHADIYU_SH,
               2: CHOGHADIYU_RO,
               3: CHOGHADIYU_UD,
               4: CHOGHADIYU_CH,
               5: CHOGHADIYU_LA,
               6: CHOGHADIYU_AM,
               7: CHOGHADIYU_KA,
               8: CHOGHADIYU_SH},
         'N': {1: CHOGHADIYU_AM,
               2: CHOGHADIYU_CH,
               3: CHOGHADIYU_RO,
               4: CHOGHADIYU_KA,
               5: CHOGHADIYU_LA,
               6: CHOGHADIYU_UD,
               7: CHOGHADIYU_SH,
               8: CHOGHADIYU_AM}
         },
    4:  # FRIDAY
        {'D': {1: CHOGHADIYU_CH,
               2: CHOGHADIYU_LA,
               3: CHOGHADIYU_AM,
               4: CHOGHADIYU_KA,
               5: CHOGHADIYU_SH,
               6: CHOGHADIYU_RO,
               7: CHOGHADIYU_UD,
               8: CHOGHADIYU_CH},
         'N': {1: CHOGHADIYU_RO,
               2: CHOGHADIYU_KA,
               3: CHOGHADIYU_LA,
               4: CHOGHADIYU_UD,
               5: CHOGHADIYU_SH,
               6: CHOGHADIYU_AM,
               7: CHOGHADIYU_CH,
               8: CHOGHADIYU_RO}
         },
    5:  # SATURDAY
        {'D': {1: CHOGHADIYU_KA,
               2: CHOGHADIYU_SH,
               3: CHOGHADIYU_RO,
               4: CHOGHADIYU_UD,
               5: CHOGHADIYU_CH,
               6: CHOGHADIYU_LA,
               7: CHOGHADIYU_AM,
               8: CHOGHADIYU_KA},
         'N': {1: CHOGHADIYU_LA,
               2: CHOGHADIYU_UD,
               3: CHOGHADIYU_SH,
               4: CHOGHADIYU_AM,
               5: CHOGHADIYU_CH,
               6: CHOGHADIYU_RO,
               7: CHOGHADIYU_KA,
               8: CHOGHADIYU_LA}
         },
    6:  # SUNDAY
        {'D': {1: CHOGHADIYU_UD,
               2: CHOGHADIYU_CH,
               3: CHOGHADIYU_LA,
               4: CHOGHADIYU_AM,
               5: CHOGHADIYU_KA,
               6: CHOGHADIYU_SH,
               7: CHOGHADIYU_RO,
               8: CHOGHADIYU_UD},
         'N': {1: CHOGHADIYU_SH,
               2: CHOGHADIYU_AM,
               3: CHOGHADIYU_CH,
               4: CHOGHADIYU_RO,
               5: CHOGHADIYU_KA,
               6: CHOGHADIYU_LA,
               7: CHOGHADIYU_UD,
               8: CHOGHADIYU_SH}
         }
}


def calculate(sunrise_datetime, sunset_datetime, next_sunrise_datetime):
    """
        This routine fills Choghadiya slots of CHOGHADIYA_SLOTS dictionary by
        first arriving at length of day and nigh choghadiya and then calculates
        all the choghadiya slots.
    """
    if not isinstance(sunrise_datetime, dt):
        print("Invalid data received as sunrise datetime.", file=sys.stderr)
        sys.exit(1)

    if not isinstance(sunset_datetime, dt):
        print("Invalid data received as sunset datetime.", file=sys.stderr)
        sys.exit(1)

    if not isinstance(next_sunrise_datetime, dt):
        print("Invalid data received as next sunrise datetime.",
              file=sys.stderr)
        sys.exit(1)

    if not sunrise_datetime < sunset_datetime < next_sunrise_datetime:
        sys.exit(1)

    total_day_len = next_sunrise_datetime - sunrise_datetime
    if total_day_len.days > 1:
        print("Can not calculate when next sunrise datetime is more "
              "than one day apart.",
              file=sys.stderr)

    day_choghadiya_len = (sunset_datetime - sunrise_datetime) / 8
    night_choghadiya_len = (next_sunrise_datetime - sunset_datetime) / 8
    week_day_no = sunrise_datetime.weekday()

    #
    # This dictionary holds Choghadiya for a given day with their respective
    # start and end time.
    #
    slots = {
        'D':
            {
                1: {"N": "", "S": 0.0, "E": 0.0},
                2: {"N": "", "S": 0.0, "E": 0.0},
                3: {"N": "", "S": 0.0, "E": 0.0},
                4: {"N": "", "S": 0.0, "E": 0.0},
                5: {"N": "", "S": 0.0, "E": 0.0},
                6: {"N": "", "S": 0.0, "E": 0.0},
                7: {"N": "", "S": 0.0, "E": 0.0},
                8: {"N": "", "S": 0.0, "E": 0.0}
            },
        'N':
            {
                1: {"N": "", "S": 0.0, "E": 0.0},
                2: {"N": "", "S": 0.0, "E": 0.0},
                3: {"N": "", "S": 0.0, "E": 0.0},
                4: {"N": "", "S": 0.0, "E": 0.0},
                5: {"N": "", "S": 0.0, "E": 0.0},
                6: {"N": "", "S": 0.0, "E": 0.0},
                7: {"N": "", "S": 0.0, "E": 0.0},
                8: {"N": "", "S": 0.0, "E": 0.0}
            }
    }

    dst = sunrise_datetime
    den = dst + day_choghadiya_len
    nst = sunset_datetime
    nen = nst + night_choghadiya_len

    for i in range(1, 9):
        slots['D'][i]["N"] = CHOGHADIYA_DICT[week_day_no]['D'][i]
        slots['N'][i]["N"] = CHOGHADIYA_DICT[week_day_no]['N'][i]
        slots['D'][i]["S"] = dst
        slots['N'][i]["S"] = nst
        slots['D'][i]["E"] = den
        slots['N'][i]["E"] = nen
        dst, den = den, den + day_choghadiya_len
        nst, nen = nen, nen + night_choghadiya_len
    return slots


def calculate_for_specific_time(sunrise_datetime, sunset_datetime, next_sunrise_datetime, given_time):
    x = calculate(sunrise_datetime, sunset_datetime, next_sunrise_datetime)
    for key, val in x.items():
        for subkey, subval in val.items():
            if subval['S'] <= given_time <= subval['E']:
                result = key, subkey, subval['N'], subval['S'], subval['E']
                return result
    return None


def main():
    message = """
    SIMPLE CHOGHADIYA CALCULATOR:-
    ============================
    Correct way to use this script is to import this script in your python 
    script and then call it as follows, passing three required arguments  
    
    >>> import scc
    >>> scc.calculate( d1, d2, d3)
    This will return entire dictionary of the all the choghadiya for given time.
    
    Where d1, d2 and d3 must be valid instances of python datetime class and 
    they must contain following values:
    
        d1 - must have value for Sunrise's date & time
        d2 - must have value for Sunset's date & time
        d3 - must have value for next day's Sunrise's date & time
        
    or
    if you need choghadiya information for just a point of time use following 
    method.
    
    >>> import scc
    >>> d1 = dttm.now().replace( hour=6, minute=30)
    >>> d2 = dttm.now().replace( hour=18, minute=30)
    >>> d3 = dttm.now().replace( day=17, hour=6, minute=30)
    >>> d4 = dttm.now()
    >>> scc.calculate_for_specific_time(d1, d2, d3, d4)
    
    This will give one single choghadiya for given time provided d1 <= d4 <= d3.
    """

    print(message)


if __name__ == '__main__':
    main()