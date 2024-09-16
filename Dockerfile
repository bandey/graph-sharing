FROM python:3.8.10-slim

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install flask

# Bundle app source
COPY . .

CMD [ "python", "graph-sharing.py" ]
