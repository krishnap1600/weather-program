# weather.py - Launches a select site of the user's choice to
# display the weather forecast of the zipcode inputted

import webbrowser, pyperclip, sys

GOOGLEWEATHER = 1
WEATHERCHANNEL = 2
WEATHERBUG = 3

# Asks user what website they would prefer to get weather info
print("Which site would you like to use to get your weather forecast?\n")
print("1. Google")
print("2. Weather Channel")
print("3. Weatherbug")

preferred_site = int(input())

# reprompts until user enters an existing option
while (preferred_site < GOOGLEWEATHER or preferred_site > WEATHERBUG):
    print("Please enter an existing number option:")
    preferred_site = int(input())

# asks for user's zipcode
print("Please enter your zipcode:")
zipcode = input()

# determines which site to open up
if(preferred_site == GOOGLEWEATHER):
    webbrowser.open('https://www.google.com/search?q=' + zipcode + '+weather')
elif(preferred_site == WEATHERCHANNEL):
    webbrowser.open('https://weather.com/weather/today/l/' + zipcode)
else:
    webbrowser.open('https://www.weatherbug.com/weather-forecast/now/' + zipcode)
