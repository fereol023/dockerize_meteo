FROM python:3.8-slim AS data_processing
# fichier de data processing uniquement
COPY _data/ /app/_data
COPY _module1/ /app/module1
# associer un volume pour la permanance des data
VOLUME /app
WORKDIR /app
RUN ["pip", "install", "pandas"]
RUN ["python", "module1/transformation.py"]
# CMD ["/bin/bash"]
# en output un fichier meteo_transformee.csv s'ajoute au repo _data

FROM python:3.8-slim
# copier la data resultant du processing à l'étape precedente
COPY --from=data_processing /app/_data/ /app/_data
# dossier target pour les sorties
COPY _images/ /app/_images
# dossier pour les scripts
COPY _module2/ /app/module2
VOLUME /app
WORKDIR /app
RUN ["pip", "install", "pandas"]
RUN ["pip", "install", "matplotlib"]
RUN ["python", "module2/pipeline.py"]
CMD ["/bin/bash"]



