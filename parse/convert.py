import pandas as pd

# Загружаем CSV
df = pd.read_csv("matched_prices.csv")

# Сохраняем в Excel
df.to_excel("matched_prices.xlsx", index=False)