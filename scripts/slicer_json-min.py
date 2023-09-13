# Скрипт нарезает изображение по рамкам из Label Studio с учетом поворота.
# * При явном отсутсвии данных о вращении - пересохраните json файл, предварительно подвигав рамки. 

# 1. Добавте в папку изображения с корневого каталога ЛС
# 2. Экспортируйте разметку с ЛС и сохраните файл json  в папке 
# Больше в файле knowledgeBase\LabelStudio.md

import os
import json
import math
import matplotlib.pyplot as plt
import cv2 # Import opencv
import glob


# Папка с исходными фотографиями и json файлом ()
imagePath = os.path.join('pic') 
# Путь к изображениям label Studio root\.local\share\label-studio\media\upload
# я просто скопировал оттуда исходники и закинунул в папку pic в корне виртуального окружения
# Туда же добавил файл json 

# print(imagePath) # выведет путь

# Ищем файл (первый)
jsonFiles = []
for json_file in glob.glob(imagePath + '/*.json'):
    jsonFiles.append(json_file)

# название файла
# print(jsonFiles[0])

# Открываем файл
with open(jsonFiles[0], 'r') as f:
    # print('This will be written to /some/dir/test.txt', file=f)
    # print(f'Открыт файл "{jsonFiles[0]}"')
    data = json.loads(f.read())

# i используется для имени
i = 1 

# Хранит список изображений
# listImage = []

for block in data:

    # Список изображений
    image = block.get('image')
    image = image.split('/')
    image = image[-1]
    # listImage.append(image)
    
    # Возвращает список с разметкой и поворотом
    boxs = block.get('label')
    # print(label)

    # Считываем изображение в pictureO riginal
    pictureO = cv2.imread(imagePath +'/'+ image)
    pictureO = cv2.cvtColor(pictureO, cv2.COLOR_BGR2RGB)
    
    for box in boxs:
        # print(json.dumps(box, indent=4))
        i+=1

        width =  box.get('original_width')
        height = box.get('original_height')


        # Имеется погрешность! 
        onePercW = width/100
        onePercH = height/100

        # print(onePercW*100)
        # print(onePercH*100)
        
        coordX = math.ceil(onePercW * box.get('x'))
        coordY = math.ceil(onePercH * box.get('y'))

        # Размеры обрезанной части
        wCrop = math.ceil(box.get('width') * onePercW)
        hCrop = math.ceil(box.get('height') *onePercH)

        # center = (coordX + (wCrop//2), coordY + (hCrop//2))
        center = (coordX, coordY)
        
        rotation = math.ceil(box.get('rotation'))

        # data = [image, f'id_{str(i)}', coordX, coordY,wCrop, hCrop, rotation]
        # listImage.append(data)
        # print(image, f'id_{str(i)}', coordX, coordY,wCrop, hCrop, rotation)

        # Создаем копию изображения
        tmp = pictureO.copy()

        # Тестовые блоки

        # tmp1 = pictureO.copy()
        
        # M1 = cv2.getRotationMatrix2D(center, rotation, 1) 
        # tmp1 = cv2.warpAffine(tmp1, M1,(width,  height)) 

        # рисуем круг
        # cv2.circle(tmp1, center, 10,(0,0,200), -1)
        # cv2.rectangle(tmp1,(coordX,coordY),(coordX+wCrop,coordY+hCrop),(0,150,0),2)
        
        
        # рисуем круг
        # cv2.circle(tmp, center, 5,(0,255,0), -1)
        # cv2.rectangle(tmp,(coordX,coordY),(coordX+wCrop,coordY+hCrop),(0,0,200),2)  

        # Поварачиваем изображение вокруг центра обрезаемой части
        M = cv2.getRotationMatrix2D(center, rotation, 1) 
        tmp = cv2.warpAffine(tmp, M,(width,  height)) 
        
        # Обрезка c буфером 100 px (y1 y2, x1,x2)/ тестовый
        # cv2.rectangle(tmp,(coordX,coordY),(coordX+wCrop,coordY+hCrop),(0,255,0),2)
        # cv2.putText(tmp, str(rotation), (coordX,coordY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
        
        cropImg = tmp[coordY:coordY+hCrop, coordX:coordX+wCrop]

        # pic_box.add_subplot(3,5, i+1)
        # plt.imshow(resize)

        # Сохраняем изображение (необходимо создать папки)
        cv2.imwrite(f'/home/exampeTF/pic/finish/{i}.png', cropImg)

print('Выполнено. Нарезано изображений:', i)