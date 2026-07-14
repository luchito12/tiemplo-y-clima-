# Tiempo y Clima 🌤️

Programa simple que muestra tu ubicación, temperatura, humedad y hora local, actualizándose solo cada tanto (intervalo configurable).

## ⚡ Versión portable (recomendada)

¿Solo querés usarlo? No necesitás instalar Python ni nada. Descargá `TiempoYClima.exe` y hacé doble clic.

**No hace falta registrarse en ningún lado ni conseguir API keys.** Abrís el programa, y automáticamente detecta tu ubicación por IP y trae el clima. Eso es todo.

> 🌐 Necesita conexión a internet para funcionar (usa APIs públicas gratuitas).

## ✨ Qué hace

- Detecta tu ubicación aproximada por IP (ciudad, coordenadas).
- Trae temperatura y humedad actuales de esa ubicación.
- Calcula la hora local correcta según tu zona horaria.
- Se actualiza solo cada 5 minutos por defecto (podés cambiar el intervalo desde la interfaz, con el botón "Guardar").
- Botón "Actualizar ahora" para forzar una actualización manual en cualquier momento.
- **Selector de país**: elegís cualquier país de una lista y consultás su clima y hora local, sin perder de vista tu propia ubicación.
- **Mapa mundial de husos horarios en estilo ASCII**: un mapa de texto monoespaciado (como los mapas de terminal clásicos), con las 24 franjas UTC marcadas arriba, donde se ubican dos marcadores — el tuyo y el del país que consultaste. La ventana es redimensionable: al agrandarla, el mapa recalcula el tamaño de fuente para verse más grande y detallado.

## 🖱️ Uso rápido

| Acción | Cómo |
|---|---|
| Ver datos actuales | Se cargan solos al abrir |
| Forzar actualización | Botón "Actualizar ahora" |
| Cambiar frecuencia de actualización | Escribí los minutos y clic en "Guardar" |
| Consultar otro país | Elegilo en el desplegable y clic en "Consultar" |
| Ver dónde cae en el mapa | Se marca solo, con un punto de color, al consultar |

---

## 🔧 Sobre las APIs (por qué no hace falta configurar nada)

Esta versión reemplaza el esquema anterior (que pedía claves de TimeZoneDB y OpenWeatherMap) por dos servicios públicos gratuitos que **no requieren API key ni registro**:

- **[ip-api.com](https://ip-api.com)** — geolocalización por IP (ciudad, coordenadas y zona horaria).
- **[Open-Meteo](https://open-meteo.com)** — datos de clima (temperatura, humedad).

La hora local se calcula con la librería estándar de Python (`zoneinfo`) usando la zona horaria que ya viene en la respuesta de ip-api, así que tampoco hace falta una tercera API solo para la hora.

> ⚠️ La precisión de la ubicación por IP es aproximada (a nivel ciudad), no exacta como un GPS.

El mapa mundial es dibujado a mano en el propio programa (sin librerías de mapas externas): continentes aproximados como polígonos simples, rasterizados a una grilla y pintados de un solo color, más las líneas de husos horarios cada 15°. Es intencionalmente sencillo, pensado para ubicar posiciones relativas, no para uso cartográfico preciso.

---

## 🛠️ Para desarrolladores: compilar el portable vos mismo

### Requisitos (solo para compilar, no para usar el programa)
- Python 3.x instalado (con la opción "tcl/tk and IDLE" tildada en el instalador — viene tildada por defecto).

### Pasos
1. Descargá/cloná esta carpeta completa (necesita `weather_time_gui.py` y `build.bat` juntos).
2. Doble clic en `build.bat`.
3. Esperá a que termine — instala `pyinstaller` y `requests` automáticamente y compila.
4. Tu portable queda en `dist\TiempoYClima.exe`. Es un único archivo, autocontenido.

### Ejecutar directo desde el código fuente (sin compilar)
```bash
pip install -r requirements.txt
python weather_time_gui.py
```

## 🐛 Errores comunes

- **"Error de certificado SSL"**: bug conocido al empaquetar `requests` con PyInstaller — si recompilás vos mismo, asegurate de usar `build.bat` tal cual (incluye `--collect-all certifi`, que lo soluciona).
- **`ZoneInfoNotFoundError` / no encuentra el huso horario**: Windows no trae la base de datos de zonas horarias del sistema como Linux/Mac, así que Python depende del paquete `tzdata`. `build.bat` ya incluye `--collect-all tzdata` para embeberla en el `.exe`.
- **"Error de conexión a internet"**: chequeá tu conexión; el programa depende de las APIs públicas mencionadas arriba.
- **Cualquier otro error**: se genera automáticamente un archivo `error.log` en la misma carpeta que el `.exe`, con el detalle técnico completo. Si algo falla, abrilo y ahí vas a ver la causa exacta (útil para reportar el problema).
- **`ModuleNotFoundError: No module named 'requests'`** (corriendo desde código fuente): `pip install requests tzdata`.
