# Создание и развертка приложений

## Frontend
### React:


### Создание проекта
```bash
cd D:\DEV # Каталог с приложениями
npx create-react-app name_app # Создаем проект с именем name_app
cd name_app
npm start # Запуск приложения
```

### Билдинг приложения
```bash
npm run build # Запуск деплоя. Папка размещается на сервере
```
До билдинга смените путь в вайле .env! Иначе клиент будет обращаться к локалке!


### Копирование с GitHub 
Клонируем репозиторий

``` shell
git clone https://github.com/Ardbot/open_agro_client.git
npm install    # Устанавливает зависимости с package.json
npm start      # Стартуем
```


## По необходимости:
### Устанавка дополнительных компонентов:
```bash
npm install @mui/material @emotion/react @emotion/styled # Установка Material-UI
``` 
### Загружаем на GitHub

### Авторазвертывание на GitHub
В процессе

## BackEnd:
<!-- ### FastAPI -->

#### Создание проекта
```bash
cd /home # Преходим в папку с приложениями
mkdir my_app
```

#### Копирование с GitHub
```bash
cd /home
git clone <url my_app>
````

#### Установка виртуального окружения 
``` bash
cd my_app # Преходим в папку с приложением
python -m venv env # Виртуальное окружение
source env/bin/activate # Активация окружение (Linux)
.\env\Scripts\activate  # Активация окружение (Windows)
```

#### Установка зависимостей  с репозитория:
```bash
pip freeze > requirements.txt #  Создает список с пакетами
```

## Запуск приложения:

### В режиме отладки:
```bash
uvicorn app.main:app --reload
```
### В продакшн:
#### Создание службы:
+ В новом окне putty переходим в папку `/etc/systemd/system`
+ Редактируем и копируем [файл](/documentation/files/openagro.service)
+ Запускаем службу: 
```
systemctl start my_app    # Старт
```
Работа с службой:
```bash
systemctl restart my_app  # Перезагрузка
systemctl status my_app   # Статус
systemctl stop my_app     # Стоп
```

Проверьте работу службы:
```bash
systemctl status my_app   # Статус
```

Добавьте в автозагрузку:
```bash
systemctl enable my_app
```

 ### Настройка NGINX:
  + В директорию `/etc/nginx/sites-available` положить [файл конфигурации](/documentation/files/openagro-nginx)
  + Отредактировать его.
  + Создать символическую ссылку на файл в каталоге `/etc/nginx/sites-enabled`:
  ```bash
  ln /etc/nginx/sites-available/my_app-nginx /etc/nginx/sites-enabled/
  ```
  + Перезагрузите NGINX:
  ```bash
  nginx -t
  systemctl reload nginx
  ```