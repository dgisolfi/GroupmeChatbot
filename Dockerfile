FROM python:3.6
MAINTAINER Daniel Gisolfi
RUN apt-get update -y \
    && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential

ENV BOT_NAME=<PLACEHOLDER>
ENV BOT_ID=<PLACEHOLDER>
ENV GROUP_ID=<PLACEHOLDER>
ENV API_TOKEN=<PLACEHOLDER>

EXPOSE 5525

WORKDIR /bot
COPY ./src ./src
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "-m", "src"]

