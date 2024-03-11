import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données transformées
weather_data = pd.read_csv("_data/meteo_transformee.csv")

# Génération de graphiques
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Température'], label='Température')
plt.title('Évolution de la Température')
plt.xlabel('Date')
plt.ylabel('Température (°C)')
plt.xticks(rotation=45)

# Spécifiez l'intervalle de ticks pour afficher uniquement chaque 30ème jour
ticks = ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01','2022-06-01',
         '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-31']
plt.xticks(ticks)
plt.legend()
plt.savefig("_images/evolution_temperature.png")
