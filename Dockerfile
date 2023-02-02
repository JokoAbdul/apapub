FROM gojo07/gojo-userbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b main https://github.com/JokoAbdul/apapub /home/apapub/ \
    && chmod 777 /home/apapub \
    && mkdir /home/apapub/bin/

WORKDIR /home/apapub/

CMD [ "bash", "start" ]
