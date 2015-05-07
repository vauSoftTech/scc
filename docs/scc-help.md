# Simple Choghadiya Calculator
## Core Script (scc.py)

This is the core script that actually does the calculation and serves to the CLI version, and the GUI version. If you want to use this calculator in your Python scripts, then you must import this script and only this script in your python script.

Following is an example of the two kinds of script usage that you can do:

```python
import scc
choghadiyas = calculate(sunrise, sunset, nextsunrise)
```
It will return a python dictionary object.


If you want to calculate Choghadiya for a specific time of the day, you should do as follows:
```python
import scc
choghadiya = calculate_for_specific_time(sunrise, sunset, nextsunrise, given_time)
```
In the last parameter, given_time, you must specify a python datetime value for which the Choghaiya is needed.
This function call will return a Python Tuple having the following values:
1. Python Short name of the weekday indicating effective weekday name. It is important to note that the Gregorian Calender's weekday changes at mid-night but Sanatan Panchang's weekday remains effective until a moment before the next sunrise. 
2. "D" or "N" indicating whether it is a Day part choghadiya or night part choghadiya.
3. An integer in the range 1 to 8 indicate sequence number of that Choghadiya within day part or night part
4. Name of that particular Choghadiya
5. python datetime indicating exact time when this particular choghadiya started.
6. python datetime reflecting give_time - just for verification purpose that calculation has been done for this time.
7. python datetime indicating the exact time when that particular choghadiya is going to end.