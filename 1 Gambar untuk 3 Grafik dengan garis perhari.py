import requests
import matplotlib.pyplot as plt

import datetime
now = datetime.datetime.now()
skrg = now.hour

# Ambil data dari API
url = 'https://api.open-meteo.com/v1/forecast?latitude=-0.46&longitude=117.14&hourly=temperature_2m,precipitation_probability,surface_pressure,cloudcover,vapor_pressure_deficit&forecast_days=3&timezone=Asia%2FSingapore'
response = requests.get(url)
data = response.json()

# Ambil data temperatur 2 meter
temperatures = []
for hourly in data['hourly']['temperature_2m']:
    temperatures.append(hourly)

# Ambil data probabilitas presipitasi
precipitation_probabilities = []
for hourly in data['hourly']['precipitation_probability']:
    precipitation_probabilities.append(hourly)

# Ambil data tekanan udara
surface_pressures = []
for hourly in data['hourly']['surface_pressure']:
    surface_pressures.append(hourly)
    
# Ambil data tutupan aan
cloud_cover = []
for hourly in data['hourly']['cloudcover']:
    cloud_cover.append(hourly)

# Mengatur sumbu x dengan jam
hours = list(range(1, 71))  # Jam 1 hingga Jam 70

# Plot grafik dengan 3 garis
plt.figure(figsize=(10, 6))

# Plot grafik temperatur 2m
plt.plot(hours, [temp/55 for temp in temperatures[:70]], label='Temperatur (°C)', color='orange')

# Plot grafik probabilitas presipitasi
plt.plot(hours, [prob/100 for prob in precipitation_probabilities[:70]], label='Probabilitas Presipitasi (%)', color='blue')

# Plot grafik tekanan udara
plt.plot(hours, [pressure/2000 for pressure in surface_pressures[:70]], label='Tekanan Udara (hPa)', color='black')

# Plot grafik tutupan awan
plt.plot(hours, [pressure/172.5 for pressure in cloud_cover[:70]], label='Tutupan Awan', color='green')

# Tambahkan garis vertikal pada waktu 24 jam dan 48 jam
plt.axvline(x=skrg, color='red', linestyle=':', label='Waktu saat ini')
plt.axvline(x=24, color='gray', linestyle='--', label='Besok')
plt.axvline(x=48, color='gray', linestyle='-.', label='Lusa')

plt.xlabel('Jam')
plt.ylabel('Nilai')
plt.title('Grafik Temperatur, Probabilitas Presipitasi, Tekanan Udara dan Tutupan Awan Samarinda')
plt.legend()

# Set rasio (ylim) yang sama untuk tiap garis
plt.ylim(0, 1)

plt.show()
