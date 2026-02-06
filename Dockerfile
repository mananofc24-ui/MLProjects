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
CMD ["streamlit" , "run" , "streamlit_app.py" , "--server.port=5000" , "--server.address=0.0.0.0"]

#To pull docker image from dockerhub
'''
docker pull man2406/student-performance-app 
'''

#To run the container
'''
docker run -p 5000:5000 man2406/student-performance-app
'''

#Test in browser
'''
http://localhost:5000 
'''