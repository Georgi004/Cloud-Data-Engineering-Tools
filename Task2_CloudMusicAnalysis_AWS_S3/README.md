ANALIZA SCENEI MUZICALE (AWS S3 & Python)

Acest proiect face parte din cursul Cloud Data Engineering Tools. Sarcina a presupus procesarea si agregarea datelor muzicale din 90 de fisiere CSV stocate itr-un bucket real AWS S3, provenite de la trei platforme diferite: Spotify, Deezer si iTunes.

Arhitectura si Tehnologii
- Cloud Storage: AWS S3 (Bucket: my-music-toplist-georgiana)
- Procesare Date: Python cu biblioteca Pandas
- Integrare Cloud: Boto3 pentru comunicare cu serviciile AWS
- Securitate:
    - utilizator IAM cu permisiuni de citire/scriere
    - Google Colab Secrets pentru protejarea cheilor de acces (Access Key & Secret Key)
    - Bucket Policy (JSON) pentru a permite accesul public strict la rezultatele finale.

Etapele Procesului
1. Conectare Securizata: Initializarea sesiunii Boto3 folosind credentiale IAM stocate in variabile de mediu.

2. Ingestia Datelor: Citirea automata a celor 90 de fisiere din folderul "raw/" direct in memorie folosind io.BytesIO pentru eficienta.

3. Curatare si Transformare: Extragerea platformei (Spotify/Deezer/iTunes) din numele fisierului si concatenarea datelor intr-un singur set de date unitar.

4. Agregare si Clasificare: Calcularea metricilor de performanta pentru artisti:
    - numar de aparitii
    - numar de piese unice
    - pozitia medie si cea mai buna pozitie ocupata
    - numarul de platforme pe care este prezent artistul.

5. Livrare: Salvarea unui "Top 20 Artisti" intr-un fisier CSV si incarcarea acestuia in folderul "final/" din S3 cu acces public.

Rezultatul Final
Proiectul genereaza un clasament agregat care ajuta echipa sa identifice rapid cei mai populari artisti ai lunii pe toate platformele analizate.

Resurse
- Notebook Colab: https://colab.research.google.com/drive/1nmXonpwN8zqCIR7PrJwa2wWsbBymIrXs?usp=sharing
Fisier CSV din S3: https://my-music-toplist-georgiana.s3.us-east-1.amazonaws.com/final/top20_artists.csv
