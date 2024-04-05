import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('BaiVeNhaBuoi-12\cyclones - cyclones.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['cyclone_events'])
plt.xlabel('Năm')
plt.ylabel('Số lốc xoáy')
plt.title('Số lốc xoáy ở Việt Nam qua các năm')
plt.grid(True)
plt.show()