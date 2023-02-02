FROM python:3.8

ADD server.py .

RUN python -m pip install --upgrade pip
RUN pip install flwr
RUN pip install numpy

CMD ["python3", "./server.py"] 



