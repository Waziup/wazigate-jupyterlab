##FROM python:3.7.12-slim-buster
FROM python:3.8.16-bullseye

## INSTALL WITH APK
RUN apt-get update && apt-get install -y \
    g++ \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    make \
    wget \
    libatlas-base-dev \
    libffi-dev \
    zip

## INSTALL WITH PIP
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pillow && \
    pip install --no-cache-dir matplotlib && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir setuptools && \
    pip install --no-cache-dir cffi && \
    pip install --no-cache-dir GLIBC && \
    pip install --no-cache-dir numpy && \
    pip install --no-cache-dir scipy && \
    pip install --no-cache-dir jupyterlab


# Copy whole folder to container
COPY . /root

WORKDIR /root

# Create zip to be able to install from gateways UI
RUN zip /index.zip docker-compose.yml package.json

# Make port available
EXPOSE 9000/tcp

# Uncomment For development
#ENTRYPOINT ["tail", "-f", "/dev/null"]

# Uncomment For production
RUN chmod +x /root/entrypoint.sh
ENTRYPOINT ["/root/entrypoint.sh"]