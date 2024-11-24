import pandas as pd
from .models import DataRecord

def import_excel(file_path):
    # قراءة ملف Excel
    df = pd.read_excel(file_path)
    
    # إدخال البيانات إلى قاعدة البيانات
    for _, row in df.iterrows():
        DataRecord.objects.create(
            name=row['Name'],  # اسم العمود في ملف Excel
            age=row['Age'],
            email=row['Email'],
        )
