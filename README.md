## Dependencies
Please install python 3.8 or higher, no aditional library is required

## Description
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

```
Example 1:
INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```

## Architecture
Program was based in two general parts, one decoding part and one computing part

### Decoding part
This part intents to convert input intring into a dictionary in the following way
```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

{
    "RENE":[
        {
            "day":"MO",
            "start":"10:00",
            "end":"12:00"
        },
        {
            "day":"TU",
            "start":"10:00",
            "end":"12:00"
        },
        {
            "day":"TH",
            "start":"01:00",
            "end":"03:00"
        },
        {
            "day":"SA",
            "start":"14:00",
            "end":"18:00"
        },
        {
            "day":"SU",
            "start":"20:00",
            "end":"21:00"
        }
    ]
}
```

For this program started dividing string in "=" for getting the name, after that dividing by "," for getting days and finally "-" for getting hours, this having into account that day name is always a 2 character string

### Computing part

First combinate fuction throws all possible permutations for all users having as input names list using `combinate` function.

With all combinations program started to compare pairs of names traversing days list. 
Once day name matches times were compared, first time is converted to int value that express minutes of the day for a given hour (for example 10:00 == 600) using `get_intervals` fuction.

After that time intervals were compared for determine if them overlaps, choiced criteria was if end time of first intervals is higher than start time of second interval and start time of first interval is lower than end time of second interval the overlap.

Also is needed to include the opposite conditcion having that if end time of second interval is higher than start time of first interval and start time of second interval is lower than end time of first intervals the overlap.

## Quick start
Make sure that inputs.txt is a non empty file in root folder, here you can place you inputs according to convection given before. Afer that run following command in root folder

```bash
# for windows
python main.py

# for linux/mac
python3 main.py
```

## Tests
For running any test make sure that tests.txt exists in root folder and is non empty, here you can place as many test as you wish using convections given in following example (it's important ending each example with `End` command):

```
Example 1
INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
OUTPUT
RENE-ASTRID: 2
RENE-ANDRES: 2
ASTRID-ANDRES: 3
End
```
 Run `pytest` command in root folder