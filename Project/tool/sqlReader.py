import sqlite3

def save_sql(df, item_code):
    con = sqlite3.connect("kiwoom_tick" + item_code)
    df.to_sql(item_code, con, if_exists='append')