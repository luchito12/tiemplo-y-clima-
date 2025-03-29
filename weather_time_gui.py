import tkinter as tk
from tkinter import messagebox
import requests
import json
import os
import threading
import time

# Archivo de configuración para guardar claves API
CONFIG_FILE = "config.json"
UPDATE_INTERVAL = 300  # 5 minutos en segundos

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"timezone_api_key": "", "weather_api_key": ""}

def save_config(timezone_api_key, weather_api_key):
    config = {"timezone_api_key": timezone_api_key, "weather_api_key": weather_api_key}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def get_weather():
    config = load_config()
    weather_api_key = config.get("weather_api_key")
    timezone_api_key = config.get("timezone_api_key")
    
    if not weather_api_key or not timezone_api_key:
        messagebox.showwarning("Claves API", "Por favor, ingrese las claves API.")
        return
    
    try:
        # Obtener ubicación automática
        ip_response = requests.get("http://ip-api.com/json/")
        ip_data = ip_response.json()
        print("Datos de IP:", ip_data)  # DEPURACIÓN

        city = ip_data.get("city", "Desconocido")
        lat, lon = ip_data.get("lat"), ip_data.get("lon")

        if lat is None or lon is None:
            raise Exception("No se pudo obtener la ubicación.")

        # Obtener datos del clima
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        print("Respuesta de OpenWeatherMap:", weather_data)  #Imprime la respuesta completa

        if "main" not in weather_data:
            raise Exception("Error en la respuesta del clima: " + str(weather_data))

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        # Obtener datos de la zona horaria
        timezone_url = f"https://api.timezonedb.com/v2.1/get-time-zone?key={timezone_api_key}&format=json&by=position&lat={lat}&lng={lon}"
        timezone_response = requests.get(timezone_url)
        timezone_data = timezone_response.json()
        
        print("Respuesta de TimeZoneDB:", timezone_data)  # Ver la respuesta

        if "formatted" not in timezone_data:
            raise Exception("Error en la respuesta de la zona horaria: " + str(timezone_data))

        time_data = timezone_data['formatted']
        
        weather_label.config(text=f"Ubicación: {city}\nTemperatura: {temperature}°C\nHumedad: {humidity}%\nHora: {time_data}")
    except Exception as e:
        weather_label.config(text="Error al obtener datos")
        print("Error:", e)


def save_keys():
    timezone_api_key = timezone_entry.get()
    weather_api_key = weather_entry.get()
    save_config(timezone_api_key, weather_api_key)
    messagebox.showinfo("Guardado", "Claves API guardadas correctamente.")

def auto_update():
    while True:
        get_weather()
        time.sleep(UPDATE_INTERVAL)

# Crear ventana
root = tk.Tk()
root.title("Tiempo y Clima")
root.geometry("400x300")

tk.Label(root, text="Clave API TimeZoneDB:").pack()
timezone_entry = tk.Entry(root)
timezone_entry.pack()

tk.Label(root, text="Clave API OpenWeatherMap:").pack()
weather_entry = tk.Entry(root)
weather_entry.pack()

tk.Button(root, text="Guardar Claves", command=save_keys).pack()
tk.Button(root, text="Actualizar Datos", command=get_weather).pack()

weather_label = tk.Label(root, text="Esperando datos...")
weather_label.pack()

# Iniciar actualización automática en un hilo separado
thread = threading.Thread(target=auto_update, daemon=True)
thread.start()

root.mainloop()
