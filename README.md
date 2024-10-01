Currency Conversion Application - DevOps Workflow
Project Overview
This project automates the process of fetching live currency rates, converting them to USD, and storing them for trend analysis. The solution is containerized using Docker, deployed on a Kubernetes cluster via Minikube, and monitored through Prometheus and Grafana for insights. This project demonstrates a comprehensive understanding of DevOps practices by combining development, containerization, deployment, monitoring, and visualization into a seamless workflow.

Table of Contents
Project Overview
Tech Stack
Project Workflow
DevOps Concepts
Setup Instructions
How to Run
Future Enhancements
Tech Stack
1. Python
Why: Python is the backbone of this project, handling web scraping, data processing, and conversions.
Used For: Fetching live currency rates using BeautifulSoup and regex, and converting those values into USD.
2. BeautifulSoup & Regex
Why: For effective and flexible extraction of currency data from a webpage's HTML structure.
Used For: Scraping dynamic currency values from the specified webpage.
3. Docker
Why: Docker is used for containerizing the Python application, ensuring consistency across different environments.
Used For: Packaging the Python application into a Docker container, which can then be deployed seamlessly.
4. Kubernetes (Minikube)
Why: Kubernetes provides an automated way to deploy, scale, and manage containerized applications.
Used For: Deploying the containerized Python application in a local Minikube cluster, automating deployment, and maintaining service uptime.
5. Prometheus
Why: Prometheus is used for monitoring, collecting, and scraping metrics from the running service.
Used For: Collecting key metrics and data about the currency conversion service, which can be visualized in Grafana.
6. Grafana
Why: Grafana is used for creating visual dashboards based on the data collected by Prometheus.
Used For: Displaying trends in currency rates and providing historical data insights in an intuitive manner.
7. File System & Docker Volumes
Why: To ensure that data remains persistent even when containers are restarted or recreated.
Used For: Storing currency conversion results in a file (countries_prices.txt) that tracks historical prices across multiple runs.
Project Workflow
Start: The process begins by initializing the currency conversion workflow.

Fetch Currency Rates: A Python script (testweb.py) uses BeautifulSoup and regex to scrape live currency exchange rates from a specified website.

Store Rates: The scraped currency rates are stored in a file (countries_prices.txt) or a database, ensuring data persistence for future conversions and analysis.

Convert Prices: The fetched rates are converted into USD using custom Python logic, avoiding the need for external libraries, providing better control over the conversion.

Append Converted Prices: The converted values are appended to countries_prices.txt, allowing the historical tracking of conversion trends.

Containerization: The application is containerized using Docker. A Dockerfile ensures the Python application is packaged consistently.

Kubernetes Deployment: The Docker container is deployed in a Kubernetes cluster using Minikube, allowing scalability and efficient management of the service.

Expose Service: The Kubernetes service exposes the application on port 8000, allowing it to be accessed and monitored externally.

Metrics Collection: Prometheus is set up to scrape metrics from the exposed service, capturing important operational data.

Data Visualization: Grafana visualizes the data scraped by Prometheus, enabling users to view currency conversion trends and gain insights.

DevOps Concepts
1. Containerization with Docker
I containerized my Python application using Docker, ensuring that it runs consistently across various environments. This demonstrates my ability to use Docker for application packaging and making sure dependencies are bundled with the application.
2. Kubernetes for Orchestration
The containerized application is deployed in a Kubernetes cluster using Minikube. I used Kubernetes to manage the deployment, scaling, and operation of the application, reflecting my understanding of container orchestration and service management.
3. Continuous Monitoring with Prometheus
Monitoring is a critical DevOps practice, and I set up Prometheus to scrape metrics from the service. This integration shows my ability to implement monitoring solutions, allowing me to track the performance and availability of the service.
4. Data Visualization with Grafana
I used Grafana to visualize the metrics collected by Prometheus, creating intuitive dashboards that display currency conversion trends. This highlights my ability to interpret and display operational data for decision-making.
5. Persistent Data Storage with Docker Volumes
I ensured data persistence by using Docker volumes to store currency conversion results. This demonstrates my understanding of handling persistent data in a containerized environment, a key DevOps concept for stateful applications.
6. Infrastructure as Code
The deployment is fully automated through Kubernetes YAML configuration files. This shows my understanding of managing infrastructure as code (IaC) and automating deployments, a fundamental DevOps practice.
