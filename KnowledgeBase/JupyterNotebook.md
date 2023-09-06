# Установка Jupyter Notebook
Обучение нейросетей, обычно, проходит в `JupyterNotebook`. Он позволяет поэтапно выполнять команды, что сильно экономит время. 

Создаем папку с проектом нейросети `JupyterNotebook`. <br>
Устанавливаем JupyterNotebook (желательно в linux) [Инструкция](https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server-ru):

    mkdir -p /home/app/JN           # Создаем папку JN (JupyterNotebook)
    cd /home/app/JN                 # Папка c проектом (linux) 
    python3 -m venv JN_env          # Создаем виртуальное окружение с именем JN_env (Только 1 раз)
    source JN_env/bin/activate      # Активируем виртуальное окружение (JN_env)
    pip install notebook            # Устанавливаем JupyterNotebook (Только 1 раз)
    jupyter notebook --allow-root   # Запускаем приложение

Открываем в браузере ссылку на Jupyter Notebook: 
http://127.0.0.1:8888/tree?token=fa8....707

`Выбираем ядро`. У меня было выбрано ядро с другой папки. <br> Но при загрузке, библиотеки ставятся в ядро текущей папки (JN)

## Источники:
* [Установка](https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server-ru)