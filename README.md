# Tiemplo-y-Clima-
Este programa obtiene los datos de Temperatura, Humedad,  Fecha y Hora de las Apis TimeZonedDB y OpenWheatherMap, El programa es muy simple, ingresas tus Api Key de las 2 plataformas y cada 5 minutos se irán actualizando los valores, el tiempo de actualización es totalmente configurable, alas api-key se guardan asi que no es necesario ingresarlas siempre    
# Ejecucion
REQUISITOS PARA EJECUTAR EL PROGRAMA
====================================

1️⃣ TENER PYTHON INSTALADO
---------------------------
- En **Windows**: Descargar e instalar Python desde https://www.python.org/downloads/
- En **Linux**: Python ya viene instalado en la mayoría de distribuciones.

Para verificar si Python está instalado, ejecutar en la terminal:
```
python --version
```
Si no funciona, probar con:
```
python3 --version
```


2️⃣ INSTALAR DEPENDENCIAS
-------------------------
El programa usa la biblioteca `requests` para obtener datos de las APIs. Para instalarla:

🔹 **En Windows (CMD o PowerShell)**
```
pip install requests
```

🔹 **En Linux**
Si `pip` no está instalado, primero instalarlo:
```
sudo apt install python3-pip  # (Debian/Ubuntu)
sudo dnf install python3-pip  # (Fedora)
```
Luego instalar `requests`:
```
pip install requests
```
Para verificar la instalación:
```
python -c "import requests; print('Requests instalado correctamente')"
```


3️⃣ OBTENER CLAVES API
----------------------
El programa necesita dos claves API:
- **TimeZoneDB** (para obtener la hora actual). Registrarse en: https://timezonedb.com
- **OpenWeatherMap** (para obtener el clima). Registrarse en: https://openweathermap.org/api

💡 **Ambas claves deben ingresarse en la interfaz del programa o guardarse en `config.json`.**


4️⃣ EJECUTAR EL PROGRAMA
------------------------
Una vez instalado todo, abrir una terminal y ejecutar:
```
python weather_time_gui.py
```
Si estás en Linux:
```
python3 weather_time_gui.py
```

🚀 OPCIONAL: HACERLO PORTABLE
-----------------------------
Si deseas que el programa funcione sin necesidad de instalar Python en otras computadoras, convertirlo en un ejecutable con `PyInstaller`:

🔹 **En Windows**
```
pip install pyinstaller
pyinstaller --onefile --windowed weather_time_gui.py
```
Esto generará un archivo **weather_time_gui.exe** en la carpeta `dist/`.

🔹 **En Linux**
```
pip install pyinstaller
pyinstaller --onefile weather_time_gui.py
```
Esto generará un ejecutable en `dist/weather_time_gui`.

