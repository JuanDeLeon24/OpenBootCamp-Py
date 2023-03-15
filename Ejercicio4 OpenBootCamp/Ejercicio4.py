# pylint: disable=import-error
import requests

# Pedimos al usuario que introduzca el nombre de la ciudad
city = input("Introduce el nombre de la ciudad: ")

# Hacemos la petición a la API de OpenWeatherMap
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY"
response = requests.get(url)

# Comprobamos si la petición fue exitosa
if response.status_code == 200:
    # Obtenemos los datos del clima en formato JSON
    data = response.json()

    # Obtenemos la temperatura máxima y mínima
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]

    # Imprimimos los resultados
    print(f"La temperatura máxima en {city} es {temp_max} grados Kelvin.")
    print(f"La temperatura mínima en {city} es {temp_min} grados Kelvin.")
else:
    print(f"No se pudo obtener la información del clima para la ciudad {city}.")
