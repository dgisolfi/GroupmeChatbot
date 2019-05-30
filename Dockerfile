FROM python:3.6
MAINTAINER Daniel Gisolfi
RUN apt-get update -y \
    && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential


EXPOSE 5525

WORKDIR /bot
COPY ./src ./src
COPY requirements.txt .

RUN pip install -r requirements.txt

# CMD ["python3", "-m", "src"]
CMD ["python3","./src/run.py"]

