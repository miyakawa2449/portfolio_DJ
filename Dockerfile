FROM ubuntu:24.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# APT設定（hash sum mismatchエラー対策）
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom && \
    echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99custom && \
    echo "Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99custom

# Python 3.13.9のソースからビルド
RUN apt-get update && apt-get install -y \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
        wget \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        libbz2-dev \
        liblzma-dev \
        tk-dev && \
    rm -rf /var/lib/apt/lists/*

# Python 3.13.9をソースからビルド・インストール
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.13.9/Python-3.13.9.tgz && \
    tar xzf Python-3.13.9.tgz && \
    cd Python-3.13.9 && \
    ./configure --enable-optimizations --with-ensurepip=install && \
    make -j$(nproc) && \
    make altinstall && \
    cd / && \
    rm -rf /tmp/Python-3.13.9*

# Python 3.13.9をデフォルトに設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.13 1 && \
    update-alternatives --install /usr/bin/python python /usr/local/bin/python3.13 1 && \
    update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.13 1

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]