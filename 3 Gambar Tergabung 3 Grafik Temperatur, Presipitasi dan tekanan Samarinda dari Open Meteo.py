import requests
import matplotlib.pyplot as plt

import datetime
now = datetime.datetime.now()
skrg = now.hour

# Ambil data dari API
url = 'https://api.open-meteo.com/v1/forecast?latitude=-0.46&longitude=117.14&hourly=temperature_2m,precipitation_probability,surface_pressure,cloudcover,vapor_pressure_deficit&forecast_days=3&timezone=Asia%2FSingapore'
response = requests.get(url)
data = response.json()

hours = list(range(1, 73))  # Jam 1 hingga Jam 70

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
    
# Ambil data tekanan udara
cloudcover = []
for hourly in data['hourly']['cloudcover']:
    cloudcover.append(hourly)

# Buat subplot dengan 4 grafik dalam 1 baris
fig, axs = plt.subplots(4, 1, figsize=(10, 12))

# Grafik pertama: Temperatur 2m per Jam
axs[0].plot(hours, temperatures)
axs[0].set_xlabel('Jam')
axs[0].set_ylabel('Temperatur 2m (°C)')
axs[0].set_title('Grafik Temperatur 2m per Jam')
axs[0].axvline(x=skrg, color='red', linestyle=':', label='Waktu saat ini')

# Grafik kedua: Probabilitas Presipitasi per Jam
axs[1].plot(hours, precipitation_probabilities)
axs[1].set_xlabel('Jam')
axs[1].set_ylabel('Probabilitas (%)')
axs[1].set_title('Grafik Probabilitas Presipitasi per Jam')
axs[1].axvline(x=skrg, color='red', linestyle=':', label='Waktu saat ini')

# Grafik ketiga: Tekanan Udara per Jam
axs[2].plot(hours, surface_pressures)
axs[2].set_xlabel('Jam')
axs[2].set_ylabel('Surface Pressure (hPa)')
axs[2].set_title('Grafik Tekanan Udara per Jam')
axs[2].axvline(x=skrg, color='red', linestyle=':', label='Waktu saat ini')

# Grafik ketiga: Tekanan Udara per Jam
axs[3].plot(hours, cloudcover)
axs[3].set_xlabel('Jam')
axs[3].set_ylabel('Cloud Cover')
axs[3].set_title('Grafik Tutupan Awan per Jam')
axs[3].axvline(x=skrg, color='red', linestyle=':', label='Waktu saat ini')

# Set spacing antara subplot
plt.subplots_adjust(hspace=0.4)

# Tampilkan grafik
plt.show()
