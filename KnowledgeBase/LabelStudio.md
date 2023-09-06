# 1. Установка label-studio (linux)

Программа устанавливается отдельно от проектов. В дальнейшем используется в других проектах.

    mkdir -p /home/app/LS   # Создаем папку LS (labelStudio)
    cd /home/app/LS         # Переходим в неё

Внутри папки /home/app/LS:

    python3 -m venv LS_env      # Создаем виртуальное окружение LS_env (Только 1 раз)
    source LS_env/bin/activate  # Активируем виртуальное окружение
    pip install label-studio    # Устанавливаем label-studio в внутри виртуального окружения
    

Ждем установки и командой `label-studio` запускаем программу в браузере на предложенном порту (`localhost:8080`)

    pip install -U label-studio # Обновление программы по необходимости

Размечаем наш датасет.