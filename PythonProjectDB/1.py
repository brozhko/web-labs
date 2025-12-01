import os

# Базова структура проєкту
directories = [
    "online_banking_backend/app/config",
    "online_banking_backend/app/my_project",
    "online_banking_backend/app/my_project/auth",
    "online_banking_backend/app/my_project/auth/controller",
    "online_banking_backend/app/my_project/auth/dao",
    "online_banking_backend/app/my_project/auth/domain",
    "online_banking_backend/app/my_project/auth/route",
    "online_banking_backend/app/my_project/auth/service",
    "online_banking_backend/app/my_project/ui",
    "online_banking_backend/app/my_project/ui/utils",
    "online_banking_backend/tests",
]

files = [
    "online_banking_backend/app/config/app.yml",

    "online_banking_backend/app/my_project/__init__.py",
    "online_banking_backend/app/my_project/auth/__init__.py",
    "online_banking_backend/app/my_project/auth/controller/__init__.py",
    "online_banking_backend/app/my_project/auth/controller/client_controller.py",
    "online_banking_backend/app/my_project/auth/dao/__init__.py",
    "online_banking_backend/app/my_project/auth/dao/client_dao.py",
    "online_banking_backend/app/my_project/auth/domain/__init__.py",
    "online_banking_backend/app/my_project/auth/domain/models.py",
    "online_banking_backend/app/my_project/auth/route/__init__.py",
    "online_banking_backend/app/my_project/auth/route/client_routes.py",
    "online_banking_backend/app/my_project/auth/service/__init__.py",
    "online_banking_backend/app/my_project/auth/service/client_service.py",
    "online_banking_backend/app/my_project/ui/__init__.py",
    "online_banking_backend/app/my_project/ui/utils/__init__.py",
    "online_banking_backend/app/my_project/ui/utils/responses.py",

    "online_banking_backend/tests/__init__.py",

    "online_banking_backend/app.py",
    "online_banking_backend/data.sql",
    "online_banking_backend/requirements.txt",
    "online_banking_backend/setup.py",
    "online_banking_backend/.gitignore",
]


def main():
    # Створюємо папки
    for d in directories:
        os.makedirs(d, exist_ok=True)
        print(f"Dir ok: {d}")

    # Створюємо порожні файли
    for f in files:
        # Переконуємось, що директорія для файлу існує
        os.makedirs(os.path.dirname(f), exist_ok=True)
        # Створюємо файл, якщо його ще нема
        if not os.path.exists(f):
            with open(f, "w", encoding="utf-8") as fp:
                pass
            print(f"File created: {f}")
        else:
            print(f"File exists: {f}")


if __name__ == "__main__":
    main()
