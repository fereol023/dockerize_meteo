import pandas as pd

# Chargement des données transformées
weather_data = pd.read_csv("_data/meteo_transformee.csv")

# Conversion de la colonne 'date' en datetime
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Analyse des tendances météorologiques
hottest_months = weather_data.groupby(weather_data['Date'].dt.month)['Température'].mean().idxmax()
windiest_days = weather_data.groupby(weather_data['Date'].dt.day_name())['Vent'].mean().idxmax()

with open('_images/sortie.txt', 'w') as file:
    file.write(f"Mois le plus chaud : {hottest_months}\n")
    file.write(f"Jour le plus venteux : {windiest_days}\n")
