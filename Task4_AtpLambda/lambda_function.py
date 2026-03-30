import pandas as pd
import boto3
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'atp-analysis-georgiana'
    file_key = 'raw/atp_tennis.csv' 
    output_key = 'results/atp_summary.csv'
    
    # 1. Citire date
    obj = s3.get_object(Bucket=bucket, Key=file_key)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()), low_memory=False)
    
    # 2. Curatare date
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    
    # 3. Procesare si Calcul Top 50
    
    if "Winner" not in df.columns:
        return {"statusCode": 400, 
                "body": f"Eroare: Coloana 'Winner' nu a fost găsită."
        }
    
    total_wins = df.groupby("Winner").size().reset_index(name="total_wins")
    total_wins = total_wins.sort_values(by="total_wins", ascending=False).head(50)

    # 4. Salvare în S3
    csv_buffer = io.StringIO()
    total_wins.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket, Key=output_key, Body=csv_buffer.getvalue())
    
    # 5. Generare Link Public Temporar (Presigned URL)
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': output_key},
        ExpiresIn=432000
    )

    print(f"LINK_ACCES_FISIER: {presigned_url}")

    return {
        "statusCode": 200, 
        "body": f"Succes! Top 50 salvat. Link acces: {presigned_url}"
    }