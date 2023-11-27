# Dockerfile per creare l'immagine docker per il progetto

# Immagine Python 3.11 come immagine di base
FROM python:3.11

# Imposta la directory di lavoro all'interno del contenitore
WORKDIR /app

# copiare il file requisiti.txt nella directory e installare le dipendenze dal file requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il contenuto di questa directory in /app/ nel contenitore
COPY . /app/

# impostazione del comando predefinito da eseguire all'avvio del contenitore
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
