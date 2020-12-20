from tkinter import *
from PIL import ImageTk, Image
from six.moves import urllib
from addressFinder import FindToAddress
from weatherControl import WeatherControl
import io

FONT = ("Arial", 16, "normal")


def find_address():
    address_finder = FindToAddress(ip_entry.get())
    control_weather(address_finder.find_address())


def control_weather(parameters):
    weather_checker = WeatherControl()
    weather_params = weather_checker.find_weather_info(parameters)
    celcius_value.config(text=weather_params[0])
    weather_value.config(text=weather_params[2])
    visualize_weather()


def visualize_weather():
    raw_data = urllib.request.urlopen("http://openweathermap.org/img/wn/09d@2x.png").read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    weather_img = Label(image=image, bg="#F4976C")
    weather_img.grid(row=4, column=2, padx=2, pady=2)


window = Tk()
window.config(padx=50, pady=20, width=500, height=800, bg="#F4976C")
window.title("Weather Watcher")

ip_entry = Entry()
send_button = Button(text="Try", command=find_address, highlightthickness=0, bd=2, width=19)
celcius_label = Label(text="Celcius:", width=19, bg="#CCCCFF", bd=5)
celcius_value = Label(width=19, bd=5)
weather_label = Label(text="Weather:", width=19, bg="#CCCCFF", bd=5)
weather_value = Label(width=19, bd=5)
# img = PhotoImage(file="http://openweathermap.org/img/wn/10d@2x.png")

ip_entry.grid(row=1, column=1, padx=2, pady=2)
send_button.grid(row=1, column=2, padx=2, pady=2)
celcius_label.grid(row=2, column=1, padx=2, pady=2)
celcius_value.grid(row=2, column=2, padx=2, pady=2)
weather_label.grid(row=3, column=1, padx=2, pady=2)
weather_value.grid(row=3, column=2, padx=2, pady=2)
# comment end

print(ip_entry.get())

window.mainloop()
