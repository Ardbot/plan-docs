---
aliases:
  - Реакт
share: true
"update:": 2024-01-09
---

# React
## Установка
```bash
cd /home/app # Переходим в папку с проектами
npx create-react-app my-app # Создаем шаблон приложения
cd my-app # Переход в директорию проекта
npm start # Запуск приложения
```

## Установка с Github
```bash
git clone https://github.com/Ardbot/my-app.git
npm install    # Устанавливает зависимости с `package.json`
npm start      # Стартуем
```

При возникновении ошибок установите недостающие пакеты с помощью команды:
```bash
npm install <name-pack>
```

## Развертывание 
```shell
npm run build # Генерация страницы для размещения на сервере. 
```
В настройках NGINX указываем путь к папке build. Как вариант, разместить рядом с backend на FastApi и сделать переадресацию с `/` на `home`


