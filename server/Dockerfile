FROM python:3.6.10

ENV CONTAINER_HOME=/var/www
WORKDIR $CONTAINER_HOME

# keep the parent server directory structure for relative imports
RUN mkdir server
ADD ./ $CONTAINER_HOME/server

RUN pip install --no-cache-dir -r $CONTAINER_HOME/server/requirements.txt

WORKDIR $CONTAINER_HOME/server/

ENTRYPOINT [ "flask" ]
CMD ["run","--host=0.0.0.0" , "--port=5022"]
