# Сбор статистики об эмоциях человека.

---

## О проекте

Цель - получение статистики используя видеофайл.

Возможная область применения - полученные в результате работы программы
данные можно использовать для улучшения качества продукта, 
так как это позволит анализировать реакции пользователей куда быстрее.

Язык - [Python 3.7](https://www.python.org/downloads/release/python-370/)

Библиотеки - для работы с веб-камерой/видеофайлом используется [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html), 
для распознания эмоций [deepface](https://pypi.org/project/deepface/). Для более удобного понимания полученных данных используется [matplotlib](https://matplotlib.org/stable/tutorials/introductory/pyplot.html). Также для ускорения используется [threading](https://docs.python.org/3/library/threading.html).

## Важное

Матрица для распознания эмоций достаточно обьёмная её загрузка займёт некоторое время. 

## Пример



https://user-images.githubusercontent.com/108991734/185974157-c589d19d-a7d0-4a4d-ba5a-cb1346717bf4.mp4

