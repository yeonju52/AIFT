import os
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import xml.etree.ElementTree as elemTree

csv_paths = [
  ('069500', r'..\AIFT2022_Wiki\data\kodex_200.csv'),
  ('114800', r'..\AIFT2022_Wiki\data\kodex_inverse.csv'),
  ('226490', r'..\AIFT2022_Wiki\data\kodex_kospi.csv'),
  ('001', r'..\AIFT2022_Wiki\data\kospi.csv'),
  ('201', r'..\AIFT2022_Wiki\data\kospi200.csv')
]

dfs = []
for st_code, csv_path in tqdm(csv_paths):
  df = pd.read_csv(csv_path, dtype={'체결시간':str})[['체결시간', '시가', '고가', '저가', '현재가', '거래량']]
  df.columns = ['dt', 'open', 'high', 'low', 'close', 'volume']
  # sqlite3에서는 datetime을 지원하지 않으므로, str로 유지한다.
  # df['dt'] = pd.to_datetime(df['dt'], format='%Y%m%d%H%M%S')
  df['st_code'] = st_code
  for col in ['open', 'high', 'low', 'close', 'volume']:
    df[col] = df[col].abs()
  dfs.append(df)
whole_df = pd.concat(dfs, ignore_index=True)

tree = elemTree.parse(r'..\AIFT2022_Wiki/config/.config.xml')
root = tree.getroot()
node_sqlite3 = root.find('./DBMS/sqlite3')
config_db = {tag:node_sqlite3.find(tag).text for tag in ['database']}

db_engine = create_engine(f'sqlite:///{config_db["database"]}', echo=False)
db_engine.execute('DROP TABLE IF EXISTS data_in_minute')
table_query = 'CREATE TABLE data_in_minute (st_code TEXT not NULL, dt TEXT not NULL, open INTEGER, high INTEGER, low INTEGER, close INTEGER, volume INTEGER, PRIMARY KEY (st_code, dt))'
db_engine.execute(table_query)

whole_df.to_sql('data_in_minute', db_engine, if_exists='append', index=False)

print(db_engine.execute("select * from data_in_minute where st_code='069500' and dt >= '20220601000000'").fetchall())
print(len(whole_df))