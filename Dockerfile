#gives Python + Linux
FROM python:3.10-slim 

#The folder inside container
WORKDIR /app 

#Copy the dependencies list
COPY requirements.txt .

#Installs : sklearn , xgboost , flask etc
RUN pip install --no-cache-dir -r requirements.txt 

#Stores the dependencies in 'app'
COPY . . 

#Documents that Flask runs on port 5000
EXPOSE 5000 

#The entry point
CMD ["python" , "app.py"]