import requests
import matplotlib.pyplot as plt

# Ambil data dari API
url = 'https://api.open-meteo.com/v1/forecast?latitude=-0.46&longitude=117.14&hourly=temperature_2m,precipitation_probability,surface_pressure,cloudcover,vapor_pressure_deficit&forecast_days=3&timezone=Asia%2FSingapore'
response = requests.get(url)
data = response.json()

# Ambil data temperatur 2 meter
temperatures = []
for hourly in data['hourly']['temperature_2m']:
    temperatures.append(hourly)

# Buat grafik garis
hours = list(range(1, len(temperatures) + 1)) # Menggunakan jumlah jam sebagai sumbu x
plt.plot(hours, temperatures)
plt.xlabel('Jam')
plt.ylabel('Temperatur 2m (°C)')
plt.title('Grafik Temperatur 2m per Jam')
plt.show()

#%%

# Ambil data temperatur 2 meter
precipitation_probability = []
for hourly in data['hourly']['precipitation_probability']:
    precipitation_probability.append(hourly)
    
# Buat grafik garis
hours = list(range(1, len(temperatures) + 1)) # Menggunakan jumlah jam sebagai sumbu x
plt.plot(hours, temperatures)
plt.xlabel('Jam')
plt.ylabel('Probabilitas (%)')
plt.title('Grafik Probabilitas Presipitasi 2m per Jam')
plt.show()

#%%

# Ambil data temperatur 2 meter
surface_pressure = []
for hourly in data['hourly']['surface_pressure']:
    surface_pressure.append(hourly)
    
# Buat grafik garis
hours = list(range(1, len(temperatures) + 1)) # Menggunakan jumlah jam sebagai sumbu x
plt.plot(hours, temperatures)
plt.xlabel('Jam')
plt.ylabel('Surface Pressure (hPa)')
plt.title('Grafik Tekanan Udara per Jam')
plt.show()
