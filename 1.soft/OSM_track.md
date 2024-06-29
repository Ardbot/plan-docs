## Отрисовка дорог в OSM (OpenStreatMap)

Отрисовка полевых дорог затруднительна. На орто или фотофотоснимках дороги не всегда видны и их можно спутать с мелиоративыми каналами (канавыми).
На помощь приходят треки работы техники учавствующей в сельхоз. работах.

В OSM их можно отобразить несколькими способами:
* Загрузить .gpx файл с треком техники
* Отобразить в виде подложки на пользовательском слое.
* По собственным ортофотоснимкам.

У каждого способа есть свои плюсы и недостатки.  
gpx файл - Не во всех системах можно выгрузить треки в данном формате.
В виде подложки - слой отображается на черном фоне. Других ориентиров нет. 
Для качественного результата необходимо способы комбинировать. 

1. Порядок действий. Выгружаем трек в формате kml. Один тип машин. Срок - уборочная (активность).
2. Загружаем треки с однотипных по проходимости машин в QGIS
3. Соединяем все треки в 1 слой.
4. * Применяем инструмент "Буфер". Выставляем радиус буфера в 0,0001 градуса. Это объеденить все линии в проезжую часть. (долго)
5. Извлекаем вершины из путей.


 [Инструкция](https://gis.stackexchange.com/questions/319412/simplifying-multiple-lines-to-create-central-axis)


#### Вариант с растризацией карты и обратной оцифровкой
1. Загрузить треки. Оформить стиль КРАСНОЙ линией. Толщина 0,26 мм
2. Удалить погреность треков
3. Объединить или растрировать на белом фоне.
4. Преобразовать карту в растр (10m/px) (Инструменты обработки данных)
5. Преобразовать в Полигоны изолиний. Канал 2, интервал цвета 255 (дискретно)
6. Упростить до 12 метров
7. Разукрасить согласно легенде. 
- Легковушки зеленым
- Малые внедорожники оранжевым
- Камазы - синим
- Спец. техника (проходимая) красным

#### Или Вариант растрации по-треково.
   1. Каждый трек растрируем 
   2. Складываем треки и считаем пересечения для каждого пикселя (10 метров)
   3. Разукрашиваем

#### Анализ треков по акселерометру. Дорожная карта покрытия. 
На основании показаний акселерометра предсказываем тип покрытия и ямы на дорогах. GPS.