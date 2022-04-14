FROM python:3.7.5

WORKDIR /usr/src/app

RUN python -m pip install requests

COPY matchChecker.py .

CMD ["python3", "matchChecker.py"]
