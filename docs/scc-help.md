# Simple Choghadiya Calculator
## Core Script (scc.py)

This is core script that actually does the calculation and serves to CLI version and GUI version. If you want to use this calculator in your Python scripts that you must import this script and only this script in your python script.

Following is an example of two kinds of usage that you can do:

```python
import scc
choghadiyas = calculate(sunrise, sunset, nextsunrise)
```
It will return a python dictionary object.


If you want to calculate Choghadiya for the specific time of the day, you should do as follows:
```python
import scc
choghadiya = calculate_for_specific_time(sunrise, sunset, nextsunrise, given_time)
```
In that last parameter, given_time, you must specify a python datetime value for which the Choghaiya is needed.
This function call will return a Python Tuple having following values:
1. Python Short name of the weekday indicating effective weekday name. It is important to note that Gregorian Calender's weekday changes at mid-night but Sanatan Panchang' weekday remains effective till just a moment before the next sunrise. 
2. "D" or "N" indicating whether it is a Day part choghadiya or night part choghadiya.
3. An integer in the range 1 to 8 indicate sequence number of that Choghadiya within day part or night part
4. Name of that particular Choghadiya
5. python datetime indicating exact time when this particular choghadiya started.
6. python datetime reflecting give_time - just for verification purpose that calculation has been done for this time.
7. python datetime indicating exact time when this particular choghadiya is going to end.