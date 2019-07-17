FROM python:3.7-alpine
WORKDIR /app
COPY . /app/
RUN pip install -r requirements -i https://pypi.douban.com/simple
CMD ["python", "runserver.py"]
