FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./


RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y locales && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    update-locale && \
    apt-get install -y libaio1 libaio-dev zip unzip vim inotify-tools && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove && \
    pip install --no-cache-dir -r requirements.txt
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:UTF-8
ENV LC_ALL en_US.UTF-8
ENV TZ=Asia/Hong_Kong

COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "/bin/bash" ]
