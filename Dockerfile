FROM python:3.13

RUN apt-get install -y pkg-config libicu-dev libssl-dev
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb
RUN dpkg -i libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

RUN apt-get update
RUN apt-get install poppler-utils -y
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y tesseract-ocr-rus

ENV LANG en_US.UTF-8
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT 1

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]