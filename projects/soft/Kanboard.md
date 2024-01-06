## Установка
[Инструкция](https://docs.kanboard.org/v1/admin/ubuntu/)<br>

    cd /home/app
    mkdir kanboard
    cd kanboard
    python3 -m venv KB_env          # Создаем виртуальное окружение с именем KB_env (Только 1 раз)
    source KB_env/bin/activate      # Активируем виртуальное окружение (KB_env)

    sudo apt install nginx php-fpm php-mysql php-pgsql php-gd php-mbstring php-sqlite3 php-xml

Скачиваем последнюю версию (см. по [ссылке](https://github.com/kanboard/kanboard/releases))

    wget https://github.com/kanboard/kanboard/archive/refs/tags/v1.2.32.tar.gz

Распаковываем в папку и даем права:

    tar xzvf v1.2.32.tar.gz -C /home/app/kanboard
    chown -R www-data:www-data /home/app/kanboard/kanboard-1.2.32/data

Удаляем файл:

    rm  v1.2.32.tar.gz

Настраиваем адрес /kb в NGINX и PHP
...
