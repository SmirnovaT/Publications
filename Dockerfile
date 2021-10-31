FROM python 3.9

WORKDIR /app

COPY requirements.txt

RUN python -m pip install

COPY . .

ENV PORT 5000

EXPOSE $PORT

CMD ["python", "app.py"]