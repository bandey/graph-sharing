FROM python:3.8.10-slim

# Create app directory
WORKDIR /usr/src/app

# Copy app source
COPY . .

# Install app dependencies
RUN pip install -r requirements.txt

CMD [ "python", "graph-sharing.py" ]
