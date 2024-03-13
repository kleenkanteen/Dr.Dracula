import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

biomarker = {'biomarker': 'Glucose Fasting', 'value': 4.1, 'measuring_unit': 'mmol/L', 'normal_range': '4.3-6.4'}

medical_reference = supabase.table("biomarker_reference").select("*").eq("biomarker", "Non-High Density Lipoprotein Cholesterol Testing").execute()

print(medical_reference.data[0]["biomarker"])