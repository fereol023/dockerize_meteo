L'image est buildée en 2 étapes : 
- Etape 1: Transformation d'un fichier de data (module caché)
   * <b>input</b> : meteo_source.csv
   * <b>output</b> : meteo_transformee.csv
   * <b>Principe</b> : le programme de transformation (module 1) augmente les températures de 10%. <u>Cette couche sert d'image de base pour l'étape 2</u>.

- Etape 2 : Analyse et reporting.
  * <b>input</b> : meteo_transformee.csv
  * <b>output</b> : dossier images => plot évolution temperature + fichier txt contenant quelques statistiques descriptives.  

- Cette image embarque un volume (répertoire /app) donc il faudrait lancer le conteneur avec un volume par exemple : 
```
docker run -v /app -it fereol023/proj_img8
```
- Résultats / Utilisation : 

Le conteneur contient un dossier ``/app`` avec l'arborescence suivante : 
  * ``app/_data`` :  ``meteo_transformee.csv``
  * ``app/_images`` : ``sortie.txt``  ``evolution_temperature.png``
  * ``app/module2`` : ``analyse.py``   ``rapport.py``   ``pipeline.py``

On peut lister ou visualiser le contenu du répertoire ``/app`` et de ses sous-répertoires lorsqu'on lance le conteneur en mode interactif avec des commandes bash : 
  * `` ls _data`` ou ``ls _images`` ou encore ``ls _module2``
