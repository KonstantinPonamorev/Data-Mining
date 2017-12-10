# SQL


Проект по DataMining в среде Python.

Cкрипт (AvitoRazdelenie.py) собирает и формирует данные о продаваемых квартирах с сайта Avito и записывает их в файл (kvartiry.csv).

Скрипт (SQL.py) используется для перевода данных из csv файла в db формат (kvartiry.db).



При записи в бд промежуточно создаётся файл (kvartirysql.csv) для удаления дубликатов.



В самом db файле поле "id" (формат integer, соответствует номеру при парсе) используется как ключ. Ниже представлены скриншоты из бд.



![Скриншот 1](https://github.com/deadwindxkn/Data-Mining/blob/SQL/db1.PNG)


![Скриншот 2](https://github.com/deadwindxkn/Data-Mining/blob/SQL/db2.PNG)