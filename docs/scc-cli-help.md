# SCC Command Line Interface
**scc-cli.py** provides *command line interface* for **scc.py**. Following is documentation for Command Line Arguments that needs to be provided to this script in order to get the result.

**--date**
Date for which Choghadiya needs to be calculated. This Argument is not compulsory. If date needs to be provided, it has to be in **YYYY-MM-DD** format. If the date is provided in correct format, it will be used as date for which Choghadiya will be calculated. 

**--sunrise**
Time of Sunrise in **HH:MM** format for the date provided in **date** argument. This is mandatory argument. Without knowing the time of Sunrise, it is not possible to come-p with Choghadiya table for that day.

**--sunset**
Time of Sunset in **HH:MM** format for the date provided in **date** argument. This is mandatory argument. Without knowing the time of Sunrise, it is not possible to come-p with Choghadiya table for that day.

**--next-sunrise**
Time of next Sunrise that is going to happen immediately after the time mentioned in **sunset** argument, in **HH:MM** format for the date provided in **date** argument. If you do not provide this argument, next sunrise will be assumed to be happening at the same time provided in **sunrise** argument.

**--calc-at**
This is an optional argument. if you do not provide it, current system time will be taken into account for reporting the Choghadiya running at that specific time.

**RESULT**
Result will have Five fields and can easily **pipe** into **awk command**. Following is the explanation of each of the five fields.

**First Field** - Name of Vedic day effective at the time of --calc-at argument.

**Second Field** - Will have either **D** or **N** indicating Whether this Choghadiya belongs of Day part of the Vedic Day or Night Part of the Vedic day.

**Third Field** - Indicates sequence number of the Choghadiya that was running at **calc-at**

**Fourth Field** - Indicates the name of the Choghadiya that was running at **calc-at**

**Fifth Field** - Indicates the beginning time of the currently running choghadiya.

**Sixth Field** - Just reproduces **calc-at**

**Seventh Field** - Indicates the ending time of the currently running choghadiya.

**EXAMPLE USAGE**
Following assumes that ....
1. the required version of Python is installed
2. *either* the terminal is open, and the folder containing the script is pwd *OR* the script is reachable via PATH variable.
3. *either* the script is invoked using Python or the *executable bit* is set on the script.
 
```bash
>>> scc-cli.py --sunrise=06:03 --sunset=19:10
>>> Thu D 1 Shubh 201505070603 07:00 201505070741
```
The result tells us that when the script was run at 7 in the morning on 7th May 2015, it was Vedic day of Thursday, and the ver first Choghadiyu for that day was in effect at that point of time. It was going to end at 07:41.
Now suppose at the same time you want to check which Choghadiyu will be running at noon exactly at 12:30 on the same day, you can find it out in following way.
```bash
>>> scc-cli.py --sunrise=06:03 --sunset=19:10 --calc-at=12:30
>>> Thu D 4 Chal 201505071058 07:00 201505071236
```
That tells us that *Chal* Choghadiyu will be running at 12:30 on that day, and it was going to last only for next 6 minutes.

Now let us say, we just need Current Choghadiya for today at current time we just need Index number of it, name of it and ending time of it. That can be achieved in following manner.

```bash
>>> scc-cli.py --sunrise=06:03 --sunset=19:10 | awk '{ print $3, $4, $7 }'
>>> 1 Shubh 201505070741
```
