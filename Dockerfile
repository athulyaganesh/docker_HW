FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /home 

COPY dock.py ./

CMD ["python3", "dock.py"]