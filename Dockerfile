FROM pypy:latest
WORKDIR /app
COPY . /app
run pip install -r requirements.txt
CMD python watch_next.py