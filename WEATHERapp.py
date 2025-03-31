import tkinter as tk
from PIL import Image, ImageTk
import requests
import time
from io import BytesIO

def getWeather(event=None):
    city = textField.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5957815eee4291d552a4c93a4396db85"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    icon_code = json_data['weather'][0]['icon']  # Extract icon code
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = f"{condition}\n{temp}°C"
    final_data = f"\nMin Temp: {min_temp}°C\nMax Temp: {max_temp}°C\nPressure: {pressure}\nHumidity: {humidity}\nWind Speed: {wind}\nSunrise: {sunrise}\nSunset: {sunset}"
    
    label1.config(text=final_info)
    label2.config(text=final_data)

    # Fetch and display weather icon
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_response = requests.get(icon_url)
    icon_image = Image.open(BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)

    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo  # Keep reference to avoid garbage collection

# GUI Setup
canvas = tk.Tk()
canvas.geometry("600x550")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

icon_label = tk.Label(canvas)  # Label for weather icon
icon_label.pack()

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
