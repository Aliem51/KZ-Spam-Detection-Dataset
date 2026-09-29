import pandas as pd
import os

# 1. Получаем путь к папке, в которой лежит этот скрипт (load_data.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Создаем точный путь до файла (если CSV лежит в той же папке, что и скрипт)
file_path = os.path.join(current_dir, 'spam_kz_dataset.csv') 

# Примечание: если CSV лежит внутри папки data, то напиши так:
# file_path = os.path.join(current_dir, 'data', 'spam_kz_dataset.csv')

# 3. Читаем файл
df = pd.read_csv(file_path)

# Выводим первые 5 строк
print(df.head())

# Выводим баланс классов
print(df['label'].value_counts())