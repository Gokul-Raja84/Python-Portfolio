'''

Weather forecast using Python

'''

#import the necessary Library

import requests

#input the city name

city = input('input the city name : ')

print('Displaying Weather report for: ' + city)

#To fetch the weather details

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#resulting weather report

print(res.text)
