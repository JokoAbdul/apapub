FROM gojo07/gojo-userbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b main https://github.com/JokoAbdul/apapub /home/Gojo-Userbot/ \
    && chmod 777 /home/Gojo-Userbot \
    && mkdir /home/Gojo-Userbot/bin/

WORKDIR /home/Gojo-Userbot/

CMD [ "bash", "start" ]
