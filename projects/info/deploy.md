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
.\env\Scripts\activate # Активация окружение (для Windows)
```

#### Установка зависимостей  с репозитория:
```bash
pip freeze > requirements.txt #  Создает список с пакетами
```