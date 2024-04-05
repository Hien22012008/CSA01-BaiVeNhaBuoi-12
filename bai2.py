import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BaiVeNhaBuoi-12\Region_areas.xls - Sheet1.csv")

plt.figure(figsize = (20, 10))
plt.pie(df['Total Area (km2)'], labels=df['Region'], autopct='%1.1f%%', startangle=140)
plt.axis('equal') 
plt.title('Tỉ lệ diện tích của các vùng địa lý ở Việt Nam')
plt.show()