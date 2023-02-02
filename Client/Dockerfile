FROM python:3.8

ADD client1.py .
ADD model.py .

RUN python -m pip install --upgrade pip
RUN pip install flwr
RUN pip install numpy
RUN pip install tensorflow
RUN pip install seaborn
RUN pip3 install PyQt5



CMD ["python3", "./client1.py"] 


