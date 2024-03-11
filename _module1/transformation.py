import pandas as pd

# Chargement des données extraites
weather_data = pd.read_csv("_data/meteo_source.csv")
# Simulation de changements climatiques (augmentation de la température)
weather_data["Température"] += 0.1 * weather_data["Température"]

# Sauvegarde des données transformées
weather_data.to_csv("_data/meteo_transformee.csv", index=False)