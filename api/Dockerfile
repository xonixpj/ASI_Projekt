FROM python:3.10

WORKDIR /app

RUN apt-get -y update && apt-get install -y \
    python3-dev \
    apt-utils \
    build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools
RUN pip3 install \
    cython==3.0.6 \
    numpy==1.26.0 \
    pandas==2.1.3

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 12345

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "12345"]