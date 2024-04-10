## Установка TensorFlow
```bash
    mkdir -p /home/app/TF           # Создаем папку TF (TensorFlow)
    cd /home/app/TF                 # переходим в папку TF
    python3 -m venv TF_env          # Создаем виртуальное окружение с именем TF_env
    source TF_env/bin/activate      # Активируем виртуальное окружение (JN_env)

    python -m pip install --upgrade pip                 # Обновляем pip
    pip install ipykernel                               # Устанавливаем ipykernel (ядро)
    python -m ipykernel install --user --name=TF_env    # Устанавливаем глобальную видимость ядра

    pip install –r “requirements.txt”                   # Список библиотек для повторяемости
```
## Ядра:
* `General_env`
Располагается в папке с ноутбуком. Предназначено для тестов и быстрого прототипирования.

* `TF_env`
Содержит готовый набор библиотек и файлов для работы Tensor Flow. 
В дальнешем на базе этого ядра будут выполняться другие ноутбуки.

## Источники: