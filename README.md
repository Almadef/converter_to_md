## О проекте
Основная задумка проекта - конвертировать популярные файлы в Markdown текст. Это может быть нужно, если требуется отправлять ИИ агентам содержимое файлов на анализ. Имеется два апи метода - для отправки файла или base64 строки.

## Полезные комманды
* `docker build -t converter_to_md .` - сбилдить Docker контейнер
* `docker run -p 8000:80 converter_to_md` - запускает сбилженный Docker контейнер
* `python -W ignore:ImportWarning -m unittest discover -s tests -p "*_test.py"` запустить автотесты
* `black .` отформировать код в соответсвии с PEP 8
* `python -m venv venv` - создает локальную среду
* `source venv/bin/activate` - запустит локальную среду
* `pip freeze > requirements.txt` записать зависимости из локальной среды в requirements.txt
* `pip install -r requirements.txt` установит все зависимости проекта
* `uvicorn main:app --host 0.0.0.0 --port=80 --reload` запустит дев сервер