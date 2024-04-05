import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('BaiVeNhaBuoi-12\provinces_updated.xls - Sheet1.csv')

plt.figure(figsize=(20, 10))
plt.hist(df["Mật độ dân số"], bins = 20, edgecolor='black')
plt.xlabel('Mật độ dân số')
plt.ylabel('Tần suất')
plt.title('Tần suất của mật độ dân số các tỉnh/thành phố ở Việt Nam')
plt.grid(True)
plt.show()