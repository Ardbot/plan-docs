# Распознание сорняков
## Установка окружения (рабочей среды)
Установка серверной части производится в Linux (ubuntu) на базе Windows.
#### Стек:
* linux
* PyTorch
* Ultralytics YOLOv8
### Создаем виртуальное окружение и активируем ноутбук:
Этот блок выполняется В КОНСОЛЕ LINUX.
```bash
mkdir -p /home/app/weed          # Создаем папку weed (Сорняки)
cd /home/app/weed                # Папка c проектом (linux)
python3 -m venv env              # Создаем виртуальное окружение с именем env (Только 1 раз)
source env/bin/activate          # Активируем виртуальное окружение (env)
pip install notebook             # Устанавливаем ноутбук для работы
pip install ultralytics          # Устанавливаем SOTA модель (много трафика)
```
Для дальнейшего использования необходимо будет в консоле linux выполнить код:
```bash
cd /home/app/weed                # Папка c проектом (linux)
source env/bin/activate          # Активируем виртуальное окружение
jupyter notebook                 # Запускаем приложение
# jupyter notebook --allow-root    # Запускаем приложение из под root
```
После выполнения команд выше, отобразится ссылка для входа в ноутбук 
```bash
http://localhost:8888/tree?token=75f...002
```
Переходим по ссылке и открываем файл weed.ipynb