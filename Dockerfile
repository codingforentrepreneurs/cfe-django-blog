FROM python:3.10.3-slim

# copy your local files to your
# docker container
COPY . /app

# update your environment to work
# within the folder you copied your 
# files above into
WORKDIR /app

# /opt: reserved for the installation of add-on application software packages.
# We'll use this to create & store our virtual environment

# Create a virtual environment in /opt
RUN python3 -m venv /opt/venv

# Install requirments to new virtual environment
# requirements.txt must have gunicorn & django
RUN /opt/venv/bin/pip install -r requirements.txt

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    /opt/venv/bin/pip install mysqlclient && \
    # /opt/venv/bin/pip install mysqlclient && \
    chmod +x config/entrypoint.sh

# entrypoint.sh to run our gunicorn instance
CMD [ "/app/config/entrypoint.sh" ]