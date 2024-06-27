служит для создания картографического сервиса

    mkdir mapserver                    # Создаем папку mapserver
    cd mapserver
    python3 -m venv ms_env             # Виртувальное окружение
    source ms_env/bin/activate         # Активируем его
    apt install nginx

Проверяем localhost. Должна отобразиться страница с приветствием nginx

[Документация](https://download.osgeo.org/mapserver/docs/MapServer.pdf)
  

    sudo apt install fcgiwrap # Установка FastCGI
    sudo apt install cgi-mapserver   # Установка MapServera

    sudo touch /etc/nginx/sites-available/ows   # Создаем файл для NGINX
    sudo ln -s /etc/nginx/sites-available/ows /etc/nginx/sites-enabled/ows  # Добавляем его в список включеных сайтов

    nano /etc/nginx/sites-available/ows # Редактируем файл с настройками

<details>
    <summary>Код:</summary>

    server {
    listen       80;
    server_name  127.0.0.1;

    gzip                             off;
    fastcgi_param GATEWAY_INTERFACE  CGI/1.1;
    fastcgi_param SERVER_SOFTWARE    nginx;
    fastcgi_param SERVER_ADDR        $server_addr;
    fastcgi_param SERVER_PORT        $server_port;
    fastcgi_param SERVER_NAME        $server_name;
    fastcgi_param SERVER_PROTOCOL    $server_protocol;
    fastcgi_param REMOTE_ADDR        $remote_addr;
    fastcgi_param REMOTE_PORT        $remote_port;
    fastcgi_param DOCUMENT_URI       $document_uri;
    fastcgi_param DOCUMENT_ROOT      $document_root;
    fastcgi_param CONTENT_TYPE       $content_type;
    fastcgi_param CONTENT_LENGTH     $content_length;
    fastcgi_param SCRIPT_NAME        $fastcgi_script_name;
    fastcgi_param REQUEST_URI        $request_uri;

    location /wfs {
        fastcgi_pass                     unix:/var/run/fcgiwrap.socket;
        fastcgi_param SCRIPT_FILENAME    /usr/lib/cgi-bin/mapserv;
        fastcgi_param MS_MAPFILE         /home/rykovd/wfs.map;
        fastcgi_param REQUEST_METHOD     $request_method;
        fastcgi_param QUERY_STRING       $query_string;
    }

    location /wms {
        fastcgi_pass                     unix:/var/run/fcgiwrap.socket;
        fastcgi_param SCRIPT_FILENAME    /usr/lib/cgi-bin/mapserv;
        fastcgi_param MS_MAPFILE         /home/rykovd/wms.map;
        fastcgi_param REQUEST_METHOD     $request_method;
        fastcgi_param QUERY_STRING       $query_string;
    }

    location /qgis {
        fastcgi_pass                     unix:/var/run/fcgiwrap.socket;
        fastcgi_param SCRIPT_FILENAME    /usr/lib/cgi-bin/qgis_mapserv.fcgi;
        fastcgi_param QGIS_PROJECT_FILE  /home/rykovd/RU-SPE/qgis-mapnik.qgs;
        fastcgi_param REQUEST_METHOD     $request_method;
        fastcgi_param QUERY_STRING       $query_string;
    }
    }

Источник: [nextgis.github.io/](http://nextgis.github.io/webgis_course/2/mapserver_install.html)
</details>

Перезагружаем NGINX

    sudo systemctl restart nginx

Открываем ссылку [http://localhost/wms](http://localhost/wms) и видим ошибку. mapServer запущен

<!-- Жмём <kbd>Ctrl</kbd> + <kbd>1</kbd>  -->

## Настройка MapServer

инструкция по установке https://mapserver.org/installation/unix.html

### Установка компонентов
1. Установка [GDAL](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html)
    + 1.1. Collecting GDAL==3.7.1.1

хоспади! эти сборщики... я не осилил. устанавливаю версию для винды. Но еще вернусь сюда! 