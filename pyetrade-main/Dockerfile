FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY pyetrade-main/requirements.txt ./
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb &&\
    dpkg -i /chrome.deb || apt-get install -yf && \
    rm /chrome.deb
RUN curl https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip -o /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver
RUN pip install -r requirements.txt

# Bundle app source
COPY pyetrade-main /app
RUN cd /app && \
    make init && \
    make install

# Run the flask app
EXPOSE 5000
CMD [ "python", "webapi/api.py" ]