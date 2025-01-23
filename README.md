# Microservice-Based E-Commerce Platform

This project is a fully containerized, microservice-based e-commerce platform designed to demonstrate modern software development practices. It includes user management, product management, and order management functionalities, all built using a microservice architecture. The system leverages **Docker**, **Nginx**, **Golang**, and **Streamlit** to create a scalable, secure, and efficient e-commerce solution.

---

## Project Overview

This project is a proof-of-concept e-commerce platform built using a microservice architecture. It consists of the following services:
- **Frontend Service**: A Streamlit-based web application for user interaction.
- **User Service**: Manages user-related operations (e.g., creating and listing users).
- **Product Service**: Handles product-related operations (e.g., adding and listing products).
- **Order Service**: Manages order-related operations (e.g., creating and listing orders).
  ![Arayuz](https://github.com/user-attachments/assets/b558fc57-123b-4367-b89f-44c6cc741135)


All services are containerized using Docker and communicate through an **Nginx reverse proxy**, which acts as the central gateway for all incoming requests.

---

## Features

- **Microservice Architecture**: Each service is independent and can be developed, deployed, and scaled separately.
- **Nginx Reverse Proxy**: Centralized request handling, load balancing, and enhanced security.
- **Dockerized Environment**: Easy setup and deployment using Docker Compose.
- **RESTful APIs**: Each microservice exposes RESTful endpoints for seamless communication.
- **Real-Time Frontend**: Streamlit-based frontend for a user-friendly interface.
- **Scalable Design**: Ready for horizontal scaling with additional service instances.

---

## Architecture

The project follows a microservice architecture with the following components:

![Software Architecture Model](https://github.com/user-attachments/assets/95a6b6ba-bbe0-42a8-9807-dbdf89a0512d)

1. **Frontend Service**:
   - Built with **Streamlit**.
   - Provides a user interface for interacting with the platform.
   - Communicates with backend services via Nginx.

2. **Backend Services**:
   - **User Service**: Manages user data (Golang).
   - **Product Service**: Manages product data (Golang).
   - **Order Service**: Manages order data (Golang).
   - Each service runs in its own Docker container and exposes RESTful APIs.

3. **Nginx Reverse Proxy**:
   - Acts as the entry point for all incoming requests.
   - Routes requests to the appropriate backend service.
   - Provides load balancing and WebSocket support.

4. **Docker Compose**:
   - Manages the entire system as a multi-container application.
   - Simplifies development and deployment.

---

## Technologies Used

- **Backend**: Golang (Gin framework)
- **Frontend**: Streamlit (Python)
- **Reverse Proxy**: Nginx
- **Containerization**: Docker, Docker Compose
- **API Communication**: RESTful APIs
- **Real-Time Communication**: WebSocket (via Nginx)

---

## Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:
- Docker ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose ([Install Docker Compose](https://docs.docker.com/compose/install/))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/microservice-ecommerce.git
   cd microservice-ecommerce
   ```

2. Build and start the containers using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: Open your browser and go to `http://localhost`.
   - API Endpoints: Use the endpoints listed in the [API Endpoints](#api-endpoints) section.

### Running the Project

Once the containers are up and running, you can access the application as follows:

1. **Frontend**:
   - Open your browser and go to `http://localhost:8501`.
   - This will load the Streamlit-based frontend where you can interact with the platform
---
## API Endpoints

### User Service
- **POST /api/users**: Create a new user.
- **GET /api/users**: List all users.

### Product Service
- **POST /api/products**: Add a new product.
- **GET /api/products**: List all products.

### Order Service
- **POST /api/orders**: Create a new order.
- **GET /api/orders**: List all orders.

---

## Future Improvements

- **Database Integration**: Add persistent storage using databases like PostgreSQL or MongoDB.
- **Authentication**: Implement user authentication and authorization (e.g., JWT).
- **Advanced Load Balancing**: Use Kubernetes for orchestration and advanced load balancing.
- **Logging and Monitoring**: Integrate tools like Prometheus and Grafana for monitoring.
- **Frontend Enhancements**: Improve the Streamlit frontend with more features and a better UI/UX.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` provides a comprehensive overview of your project, making it easy for users and contributors to understand, set up, and extend the system. Let me know if you'd like to adjust or add anything!
