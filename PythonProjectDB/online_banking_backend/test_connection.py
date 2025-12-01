import pymysql
import yaml

# читаємо конфіг
with open("app/config/app.yml", "r") as f:
    config = yaml.safe_load(f)

dbconf = config["database"]

try:
    conn = pymysql.connect(
        host=dbconf["host"],
        user=dbconf["user"],
        password=dbconf["password"],
        database=dbconf["database"],
        port=dbconf["port"]
    )
    print("✔ Успіх! Є підключення до MySQL.")
except Exception as e:
    print("❌ Помилка підключення:")
    print(e)
