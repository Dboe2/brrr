FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY pyetrade-main/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY pyetrade-main /app
RUN cd /app && \
    make init && \
    make install

# Run the flask app
EXPOSE 5000
CMD [ "python", "webapi/api.py" ]