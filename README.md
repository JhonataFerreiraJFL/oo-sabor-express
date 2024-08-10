# FastAPI Base Project

## Overview

This repository is a foundational project for studying and building applications using FastAPI, a modern, fast (high-performance) web framework for Python. The goal is to create a solid base that can be extended for various web applications, focusing on performance, scalability, and best practices.

## Features

- FastAPI setup with basic routing and middleware.
- Asynchronous support for high-performance endpoints.
- Integration with a PostgreSQL database using SQLAlchemy.
- Pydantic models for data validation.
- JWT-based authentication and authorization.
- API documentation automatically generated with Swagger and Redoc.
- Docker support for easy deployment.

## Structure

- **app/**: Contains the main application code.
  - **main.py**: Entry point for the FastAPI application.
  - **models/**: SQLAlchemy models for database tables.
  - **schemas/**: Pydantic models for request/response validation.
  - **routers/**: FastAPI routers for organizing endpoints.
  - **services/**: Business logic and service layer.
  - **core/**: Core configuration and settings.
  - **auth/**: Authentication and authorization utilities.
- **tests/**: Unit and integration tests for the FastAPI application.
- **Dockerfile**: Docker configuration for containerizing the application.
- **requirements.txt**: Python dependencies.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JhonataFerreiraJFL/oo-sabor-express.git
   cd oo-sabor-express
