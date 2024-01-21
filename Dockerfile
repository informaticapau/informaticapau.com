FROM python:3.12

COPY ./src/ /opt/www/src/

WORKDIR /opt/www/src/
RUN pip install --no-cache-dir pipenv \
    && python3 -m pipenv lock \
    && python3 -m pipenv requirements > requirements.txt \
    && pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "-m" , "gunicorn", "-w", "2", "-b", "0.0.0.0", "app:create_app()"]