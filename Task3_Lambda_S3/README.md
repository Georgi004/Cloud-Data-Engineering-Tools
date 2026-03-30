Proiect Analiza Muzicala Serverless - Task 3
Autor: Georgiana Mutascu

Descriere:
Acest proiect implementeaza un pipeline de date complet serverless in AWS. Functia Lambda proceseaza automat un volum de 90 de fisiere CSV (topuri muzicale) stocate intr-un bucket S3, realizeaza o analiza de agregare si genereaza un raport final cu Top 20 artisti.

Resurse Implementate:
AWS Lambda: Functia `MusicArtistRanker`
AWS S3: Bucket-ul `my-music-toplist-georgiana` pentru stocare `raw/` si `final/`.
IAM Role: Configurat cu politici specifice pentru acces S3 si permisiuni `PutObjectAcl`.
Lambda Layers: Utilizarea `AWSSDKPandas` pentru procesarea eficienta a datelor.

Identificatori si Acces:
ARN Functie: `arn:aws:lambda:us-east-1:797795454518:function:MusicArtistRanker`
Link Public Rezultat: [Top 20 Artists CSV](https://my-music-toplist-georgiana.s3.us-east-1.amazonaws.com/final/top20_artists_serverless.csv)

Reflectie Tehnica:
Cea mai mare provocare a acestui proiect a fost gestionarea granulara a permisiunilor de securitate. Am invatat ca in AWS, "Least Privilege" inseamna ca fiecare acțiune (cum ar fi scrierea unui fisier public prin ACL) trebuie autorizata explicit in rolul IAM.

De asemenea, am optimizat resursele functiei (Memory: 512MB, Timeout: 2min) pentru a asigura stabilitatea procesarii volumului mare de date. Aceasta experienta mi-a demonstrat cat de scalabila si eficienta este o arhitectura serverless fata de procesarea locala.