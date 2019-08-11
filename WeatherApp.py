import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

def format_response(weather):
   try:
      name = weather['name']
      desc = weather['weather'][0]['description']
      temp = weather['main']['temp']
      final_str = 'City: %s \nConditions: %s \nTemperature(F): %s' %(name, desc, temp)
   except:
      final_str = 'There was an error retrieving the information!'

   return final_str

def get_weather(city):
   weather_key = '56b4abce473b2dd644d6d8f5415292ab'
   url = 'https://api.openweathermap.org/data/2.5/weather'
   params = {'APPID': weather_key, 'q': city, 'units': 'imperial' }
   response = requests.get(url, params=params)
   weather = response.json()
   label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(
   root,
   height=HEIGHT,
   width=WIDTH
)
canvas.pack()

background_image = tk.PhotoImage(file='gui_bg.png')
background_label = tk.Label(
   root,
   image=background_image
)
background_label.place(
   relwidth=1,
   relheight=1
)

frame = tk.Frame(
   root,
   bg='black',
   bd=5
)
frame.place(
   anchor='n',
   relx=0.5, 
   rely=0.1,
   relwidth=0.75,
   relheight=0.1
)

entry = tk.Entry(
   frame,
   font=40
)
entry.place(
   relwidth=0.65,
   relheight=1
)

button = tk.Button(
   frame,
   font=40,
   text="Get Weather",
   command=lambda: get_weather(entry.get())
) 
button.place(
   relx=0.7,
   relheight=1,
   relwidth=0.3
)

lower_frame = tk.Frame(
   root,
   bg='black',
   bd=10
)
lower_frame.place(
   anchor='n',
   relx=0.5,
   rely=0.25,
   relwidth=0.75,
   relheight=0.6
)

label = tk.Label(
   lower_frame,
   font=('Modern', 25),
   justify='left',
   bd=4,
   bg='white'
)
label.place(
   relwidth=1,
   relheight=1
)

root.mainloop()