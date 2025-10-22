FROM ubuntu:24.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# Python 3.13のインストール
RUN apt-get update && apt-get install -y \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y \
        python3.13 \
        python3.13-dev \
        python3.13-venv \
        python3-pip \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config && \
    rm -rf /var/lib/apt/lists/*

# python3.13をデフォルトに
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.13 1

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]