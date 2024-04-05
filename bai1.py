import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('BaiVeNhaBuoi-12\provinces_updated.xls - Sheet1.csv')

df = df.sort_values('Dân số (nghìn người)')

plt.figure(figsize=(20, 10))
plt.barh(df["Tên"], df["Dân số (nghìn người)"])
plt.xlabel("Dân số")
plt.ylabel("Tỉnh/Thành phố")
plt.title("Dân số các tỉnh/thành phố ở Việt Nam")
plt.show()