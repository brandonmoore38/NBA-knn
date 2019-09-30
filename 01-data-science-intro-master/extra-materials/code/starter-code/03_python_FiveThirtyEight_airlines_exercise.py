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


""" PART 1 """
''' How many airlines are there '''

 
''' How many airlines start with the letter 'A' (only capital letters) '''

        
''' create a list that only includes airlines that start with the letter "A" '''


''' Create a list (of the same length) that contains 1 if there's a star and 0 if not.
Expected output: [0, 1, 0, ...] '''


""" PART 2 """
''' Create a list of airline names (include all airlines, but not the asterisk).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...] '''


''' number of available seat kilometers (ASKs), which is defined as the number
of seats multiplied by the number of kilometers the airline flies '''
   
   
ask = '320906734,1197672318,385803648,596871813,1865253802,3004002661,869253552,\
710174817,965346773,698012498,1841234177,5228357340,358239823,396922563,\
3179760952,2582459303,813216487,417982610,550491507,6525658894,557699891,\
335448023,488560643,506464950,613356665,301379762,493877795,1173203126,\
1574217531,277414794,1874561773,1734522605,1001965891,3426529504,1039171244,\
348563137,413007158,1917428984,295705339,682971852,859673901,2376857805,\
651502442,3276525770,325582976,792601299,259373346,1509195646,619130754,\
1702802250,1946098294,7139291291,2455687887,625084918,1005248585,430462962'
'

''' Create a dictionary in which the key is the airline name (without the star)
and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...} '''


""" PART 3 """
''' Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...] '''

import requests
import csv
r = requests.get(r'https://raw.githubusercontent.com/ga-students/DAT-DC-9/master/data/airlines.csv?token=AG8aPuuPFcxm-moE4jMHl4-xZXBKLnjAks5YDjDmwA%3D%3D')
data = [row for row in csv.reader(r.content.split('\n'))]

