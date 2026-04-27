import os
import pandas as pd
import shutil
import numpy as np


csv_path = "dataset/train.csv"
images_path = "dataset/train_images"
output_path = "dataset/organized"

df = pd.read_csv(csv_path)


for i in range(5):
    os.makedirs(f"{output_path}/{i}", exist_ok=True)


for _, row in df.iterrows():
    img_name = row['id_code'] + ".png"
    label = str(row['diagnosis'])

    src = os.path.join(images_path, img_name)
    dst = os.path.join(output_path, label, img_name)

    if os.path.exists(src):
        shutil.copy(src, dst)

print("Images organized!")


data = {
    "id_code": df["id_code"],
    "age": np.random.randint(30, 80, len(df)),
    "glucose": np.random.randint(80, 250, len(df)),
    "bp": np.random.randint(90, 180, len(df)),
    "bmi": np.random.randint(18, 35, len(df))
}

patient_df = pd.DataFrame(data)
patient_df.to_csv("dataset/patient_data.csv", index=False)

print("Patient data created!")