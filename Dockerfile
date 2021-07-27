FROM python:3.9.6
COPY main.py pools.txt ./
CMD ["python", "main.py"]
