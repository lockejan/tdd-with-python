FROM jenkins/jenkins

# if we want to install via apt
USER root
RUN apt update && apt install -y xvfb nodejs npm firefox \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# install python
RUN wget https://www.python.org/ftp/python/3.7.13/Python-3.7.13.tgz && \
tar xzf Python-3.7.13.tgz && \
cd Python-3.7.13 && \
./configure --enable-optimizations --prefix=/usr && \
make altinstall
#RUN cd .. && rm -rf Python-3.7.13

# install geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz && \
tar -xvzf geckodriver-v0.33.0-linux64.tar.gz && \
mv geckodriver /usr/local/bin
RUN rm geckodriver-v0.33.0-linux64.tar.gz

# drop back to the regular jenkins user - good practice
USER jenkins

# RUN jenkins-plugin-cli --plugins xvfb
