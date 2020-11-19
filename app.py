from tkinter import *

import requests
root = Tk()
root.geometry('400x400')
root.config(bg="orange")
def test_function(entry):
    print("Entry:", entry)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        clouds = weather['clouds']['all']





        if show_weather:
            final_str = 'Place: %s \nWeather: %s \nTemperature: %s \nHumidity: %s \nWindspeed: %s \nClouds: %s \n' % (name, desc, temp,humidity,wind,clouds)

    except:
       final_str = 'There was a problem'

    return final_str

frame1 =Frame(root,bg="black", bd=25)
frame1.pack(side=BOTTOM)

entrybox = Entry(frame1)
entrybox.pack(side=BOTTOM)

show_weather = Button(frame1,text="Weather",command=lambda: get_weatherM(entrybox.get()))
show_weather.pack(side=BOTTOM)

frame2 = Frame(root, bd=10)
frame2.pack(side=TOP)

label = Label(frame2)
label.pack(side=TOP)


def get_weatherM(city):
    weather_key = '181489a8df6dc65ef7036a5a8dfb60e5'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=parameters)
    weather = response.json()

    label['text'] = format_response(weather)


mainloop()
