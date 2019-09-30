# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:57:34 2016

@author: alsherman

Data Source: https://github.com/fivethirtyeight/data/tree/master/airline-safety
"""

airlines = """Aer Lingus,Aeroflot*,Aerolineas Argentinas,Aeromexico*,Air Canada,Air France,
Air India*,Air New Zealand*,Alaska Airlines*,Alitalia,All Nippon Airways,American*,
Austrian Airlines,Avianca,British Airways*,Cathay Pacific*,China Airlines,Condor,
COPA,Delta / Northwest*,Egyptair,El Al,Ethiopian Airlines,Finnair,Garuda Indonesia,
Gulf Air,Hawaiian Airlines,Iberia,Japan Airlines,Kenya Airways,KLM*,Korean Air,LAN Airlines,
Lufthansa*,Malaysia Airlines,Pakistan International,Philippine Airlines,Qantas*,
Royal Air Maroc,SAS*,Saudi Arabian,Singapore Airlines,South African,Southwest Airlines,
Sri Lankan / AirLanka,SWISS*,TACA,TAM,TAP - Air Portugal,Thai Airways,Turkish Airlines,
United / Continental*,US Airways / America West*,Vietnam Airlines,Virgin Atlantic,
Xiamen Airlines"""


''' How many airlines are there '''

#  formula = # of commans + 1
airlines_num = 1
for character in airlines:
    if character == ',':
        airlines_num += 1

# is there a more pythonic way?

# what is the type of airlines
type(airlines)

# what operations can we conduct on a string?
dir(airlines) 

'airline1,airline2'.split(',') # bring up documentation for split

# now we have a list
dir([]) == dir(list) # assignment versus equivalence / python does not have variables

?list.count
['a','a'].count('a')

len(airlines.split(','))

# two questions: where does len comes from and what is it used at the 
# start rather than the end of the list (e.g. len(list) vs. list.len())


# side note .. special methods
5 + 5
'a' + 'a'
(5).__add__(5)
'a'.__add__('a')


 
''' How many airlines start with the letter 'A' (only capital letters) '''

a_airlines_count = 0
for airline in airlines.split(','):
    if airline[0] == 'A':
        a_airlines_count += 1

### slicing
# slicing is inclusive of the first number and exclusive of the last number
airlines[0]
airlines[0:1]
airlines[-1]

# option 2 - improved syntax and structure
airlines_list = airlines.split(',') # discuss lists versus dicts

airline_count = 0
for airline in airlines_list:
    if airline.startswith('A'): # show starts with
        airline_count += 1


# option 3 - list comprehensions
l1 = []
for airline in airlines_list:
    l1.append(airline)

# return value   for loop 
[airline         for airline in airlines_list]


l2 = []
for airline in airlines_list:
    l2.append(airline.startswith('A'))

sum([airline.startswith('A') for airline in airlines_list])
sum([airline[0] == 'A' for airline in airlines_list])

        
''' create a list that only includes airlines that start with the letter "A" '''

l3 = []
for airline in airlines_list:
    if airline.startswith('A'):
        l3.append(airline)
#sum(l2) versus len(l3) - explain why we cannot do sum(l3)
    
# return value     for loop                      conditional
[airline           for airline in airlines_list  if airline.startswith('A')]


'''
Create a list (of the same length) that contains 1 if there's a star and 0 if not.
Expected output: [0, 1, 0, ...]
'''

#True value   conditional           else value    for loop
[1            if airline[-1] == '*'  else 0        for airline in airlines_list]

[1 if '*' in airline else 0 for airline in airlines_list]


# 'set' data structure is useful for gathering unique elements
my_list = [1, 2, 1]

# 'in' statement is useful for lists
1 in my_list            # True
3 in my_list            # False

# 'in' is useful for strings (checks for substrings)
my_string = 'hello there'
'the' in my_string      # True
'then' in my_string     # False

# 'in' is useful for dictionaries (checks keys but not values)
my_dict = {'name':'Alex', 'title':'Hey You!'}
'name' in my_dict       # True
'Alex' in my_dict      # False


'''
1. Create a list of airline names (include all airlines, but not the asterisk).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...] 
'''

airlines_wo_asterisk = airlines.replace('*','').replace('\n','').split(',')


"""number of available seat kilometers (ASKs), which is defined as the number
   of seats multiplied by the number of kilometers the airline flies
"""
   
ask = '320906734,1197672318,385803648,596871813,1865253802,3004002661,869253552,\
710174817,965346773,698012498,1841234177,5228357340,358239823,396922563,\
3179760952,2582459303,813216487,417982610,550491507,6525658894,557699891,\
335448023,488560643,506464950,613356665,301379762,493877795,1173203126,\
1574217531,277414794,1874561773,1734522605,1001965891,3426529504,1039171244,\
348563137,413007158,1917428984,295705339,682971852,859673901,2376857805,\
651502442,3276525770,325582976,792601299,259373346,1509195646,619130754,\
1702802250,1946098294,7139291291,2455687887,625084918,1005248585,430462962'
'

'''
Create a dictionary in which the key is the airline name (without the star)
and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...}
'''
ask_list = ask.replace('\n','').split(',')

airlines_ask = {}
for i in range(len(airlines_wo_asterisk)):
    airlines_ask[airlines_wo_asterisk[i]] = ask_list[i]

# approach 2 - using zip
dict(zip(airlines_wo_asterisk, ask_list))


'''
1. Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...]
'''

import requests
import csv
r = requests.get(r'https://raw.githubusercontent.com/ga-students/DAT-DC-9/master/data/airlines.csv?token=AG8aPuuPFcxm-moE4jMHl4-xZXBKLnjAks5YDjDmwA%3D%3D')
r.content
data = [row for row in csv.reader(r.content.split('\n'))]
data = data[1:-1]

num_years = 30
incidents_list = []

for row in data:
    incidents = float(row[2]) + float(row[5])
    average_incidents = round(incidents / num_years, 2)
    incidents_list.append(average_incidents)