https://neural-university.ru/stazejune

# СИСТЕМА ОПРЕДЕЛЕНИЯ ПАРАМЕТРОВ ОЧКОВ ПО НОМЕНКЛАТУРЕ

## ОПИСАНИЕ ПРОЕКТА

В рамках стажировки необходимо по номенклатуре, размещенной на оправе, определить характеристики очков (ширина линзы, мост, ширина оправы, высота линзы, длина заушника и тд) и занести информацию в таблицу для размещения в карточке товара.

В рамках проекта также будет рассмотрена задача по созданию онлайн-примерочной очков, чтобы клиент мог загрузить свое фото в сервис, выбрать очки и система могла бы объединить эти 2 изображения в 1, и клиент мог посмотреть насколько та или иная модель ему подходит визуально. В рамках стажировки необходимо будет подготовить материалы для второго этапа стажировки по онлайн-примерочной


## Задачи
https://docs.google.com/spreadsheets/d/1Ji_EEA2baYM4twhGF07cMqD-f6E0GCEDUMEXLOKfATA/edit?usp=sharing

## Ссылка на датасет
DOWNLOAD_LINK = 'https://drive.google.com/uc?id=1ZHufLy0UljaBNRiBNBOeANQiF7G14oXH'

## Архив с картинками materials_pictures_archive.zip
ID = '1TbNlUyjgMBIcDUpUW_Etk-A5BoyePLQ3'
## Архив с картинками materials_pictures_aug_3_classes.zip
ID = '1DvzHznZM-oFCD2ekCNA4nif1e6vVRrY_'
## Архив с картинками materials_pictures_aug.zip (2 класса)
ID = '15foJXYoLP0W_ZGWnu8hauOyg8CpIktYx'
========================================================================
1. Парсинг сайта и создание датасета:
https://colab.research.google.com/drive/1BOgWyj7Vv23g6k54gF43X-uRAlOXcjLh?usp=sharing
2. Скачивание картинок по папкам классов:
https://colab.research.google.com/drive/109flMrcT2z98tCB3zamN8jgbkC4RHtIO?usp=sharing
3. Аугментация изображений:
https://colab.research.google.com/drive/1vHQCCwlxJmifVUSqnUEG8lzQp7gFOzJo?usp=sharing
4. Подготовка модели и её обучение с помощью ГА:
https://colab.research.google.com/drive/199W4hodCTV5Nn62TdBc0RuZt393ite5K?usp=sharing
5. Подготовка модели и её обучение с помощью AutoKeras:
https://colab.research.google.com/drive/14Fe2DpLjOvW83MpZomPJurAb_OX3XU5B?usp=sharing
6. Model training Keras Tuner
https://colab.research.google.com/drive/1MCCJAVpePBpPxz4KZTPPxhtK0XPHftSS?usp=sharing
========================================================================
+-----------------------+-------------+
| Папка металл          | 1878 файлов |
+-----------------------+-------------+
| Папка комбинированный | 1870 файлов |
+-----------------------+-------------+
| Папка пластик         | 1869 файлов |
+-----------------------+-------------+
========================================================================
https://github.com/mdbloice/Augmentor
