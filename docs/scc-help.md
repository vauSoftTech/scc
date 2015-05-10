# Simple Choghadiya Calculator
## Core Script (Choghadiya.py)

This is the core script that actually does the calculation and serves to the CLI version, and the GUI version. If you want to use this calculator in your Python scripts, then you must import this script and only this script in your python script.

Following is an example of the two kinds of script usage that you can do:

```python
import choghadiya
c = Choghadiya(date, sunrise_time, sunset_time [, next_sunrise_time])
```
Now you have a python class readily available in variable c.


If you want to calculate Choghadiya for a specific time of the day, you should do as follows:
```python
import choghadiya
c = Choghadiya(date, sunrise_time, sunset_time [, next_sunrise_time]) \
               .current_choghadiyu()
```
See the source-code of choghadiya.py for the documentation of what is available in that class. 