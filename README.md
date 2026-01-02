This project is a simple Flask web application containerized using Docker.
It displays:
	•	My name
	•	My local time
	•	A list of my favorite movies 
  Features
	•	Flask web application
	•	Displays dynamic local time
	•	Dockerized using Docker Engine
	•	Image published to Docker Hub
  Technologies Used
	•	Python 3.9
	•	Flask
	•	Docker
	•	Docker Hub
	•	Ubuntu (Linux)
  Project structure
  project1-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── .gitignore
Run the application with Docker hub
docker pull euniceo/project1-flask-app
Run the container
docker run -d -p 5000:5000 euniceo/project1-flask-app
Open in your browser
http://localhost:5000
Docker hub repository
👉 https://hub.docker.com/r/euniceo/project1-flask-app


  
