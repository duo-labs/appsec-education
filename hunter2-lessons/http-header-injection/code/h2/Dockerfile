# 0Clone
FROM debian:latest

EXPOSE 35000-55000

RUN apt update -y \
  && apt install -y software-properties-common sudo gnupg procps git build-essential wget curl nano vim emacs \
  && add-apt-repository -y "deb http://openresty.org/package/debian $(lsb_release -sc) openresty" \
  && wget -qO - https://openresty.org/package/pubkey.gpg | apt-key add - \
  && add-apt-repository -y "deb http://openresty.org/package/debian $(lsb_release -sc) openresty" \
  && apt update -y \
  && apt install --no-install-recommends openresty -y \
  && useradd -ms /bin/bash whitehat \
  && echo '%whitehat       ALL= NOPASSWD: /usr/bin/apt-get' | sudo EDITOR='tee -a' visudo \
  && echo '%whitehat       ALL= NOPASSWD: /usr/bin/apt' | sudo EDITOR='tee -a' visudo \
  && echo '%whitehat       ALL= NOPASSWD: /usr/sbin/service openresty start,/usr/sbin/service openresty stop,/usr/sbin/service openresty restart' | sudo EDITOR='tee -a' visudo \
  && echo '%whitehat       ALL= NOPASSWD: /usr/local/openresty/bin/openresty' | sudo EDITOR='tee -a' visudo \
  && echo 'export PATH=/usr/local/openresty/bin:$PATH' >> /home/whitehat/.bashrc \
  && echo 'export PS1="\w\$ "' >> /home/whitehat/.bashrc

ADD ./nginx.conf /etc/openresty/

RUN mkdir /var/log/nginx \
  && chown -R whitehat:whitehat /etc/openresty \
  && touch /var/log/nginx/access.log \
  && touch /var/log/nginx/error.log \
  && touch /var/log/nginx/nginx.pid \
  && chown -R whitehat:whitehat /var/log/nginx \
  && chown -R whitehat:whitehat /usr/local/openresty \
  && chown -R whitehat:whitehat /var/log/nginx

## On build, must include --build-arg's to git clone:
## --build-arg REPO_READER_AUTH=user:pass
## --build-arg REPO_NAME=project
ARG REPO_READER_AUTH
ARG REPO_NAME

## Optionally install and run MongoDB server by setting HAS_MONGODB=true
ARG HAS_MONGODB

RUN apt install -y python3-pip python3-dev libsqlite3-dev \
  && pip3 install --upgrade pip setuptools \
  && hash -r pip \
  && pip3 install gunicorn

RUN [ "$HAS_MONGODB" != "true" ] && ( echo 'alias boot="sed -i \"s/VPORT/${VIRTUAL_PORT}/\" /etc/openresty/nginx.conf && sed -i \"s/VHOST/${VIRTUAL_HOST}/\" /etc/openresty/nginx.conf && pkill gunicorn; cd /home/whitehat/web && gunicorn -D -w 1 -b 0.0.0.0:5000 app:app --reload && cd - > /dev/null && sudo service openresty restart && echo App is running at: http://$VIRTUAL_HOST"' >> /home/whitehat/.bashrc ) || ( mkdir -p /data/db && sudo apt-get install -y mongodb-server && chown -R whitehat:whitehat /data/db /var/log/mongodb && echo 'alias boot="pkill mongod; sed -i \"s/VPORT/${VIRTUAL_PORT}/\" /etc/openresty/nginx.conf && sed -i \"s/VHOST/${VIRTUAL_HOST}/\" /etc/openresty/nginx.conf && pkill gunicorn; cd /home/whitehat/web && gunicorn -D -w 1 -b 0.0.0.0:5000 app:app --reload && cd - > /dev/null && sudo service openresty restart && mongod --fork --logpath /var/log/mongodb/mongod.log > /dev/null && echo App is running at: http://$VIRTUAL_HOST"' >> /home/whitehat/.bashrc )

RUN git clone https://$REPO_READER_AUTH@bitbucket.org/whitehatacademy/$REPO_NAME /home/whitehat/web

WORKDIR /home/whitehat/web
RUN rm -rf .git \
  && rm README.md \
  && pip3 install -r requirements.txt

RUN chown -R whitehat:whitehat /home/whitehat
USER whitehat

CMD ["bash"]