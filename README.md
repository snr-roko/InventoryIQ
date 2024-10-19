# InventoryIQ

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Test Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

InventoryIQ is a powerful Django-based API for intelligent inventory management, designed to provide a scalable and secure backend solution for businesses of all sizes.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Project Phases](#project-phases)
- [API Endpoints](#api-endpoints)
- [Stretch Goals](#stretch-goals)
- [Timeline](#timeline)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

InventoryIQ is a comprehensive Inventory Management API built with Django and Django REST Framework. It allows authenticated users to perform CRUD operations on inventory items, manage user accounts, and track inventory changes in a robust manner.

## Features

- User authentication and authorization
- CRUD operations for inventory items and storages
- Barcode Requests
- Inventory change tracking
- RESTful API design
- JWT Authentication
- Secure and efficient data management
- Multi-store inventory management
- Supplier management functionality
- Detailed inventory reporting
- Audit logs using Created_by fields
- Dynamic inventory category management

## Technology Stack

- Backend: Django
- API Framework: Django REST Framework
- Database: MySQL
- Authentication: Django's built-in authentication system and JWT Authentication
- Deployment: PythonAnywhere

## Getting Started

For detailed usage instructions and API documentation, please visit our live Swagger UI at [snrRoko.pythonanywhere.com/api/schema/swagger-ui](https://snrRoko.pythonanywhere.com/api/schema/swagger-ui).

To request access or for any inquiries, please contact the project maintainer at [rbbagyei@outlook.com].

## Project Phases

1. **Core API Development**
   - Set up Django project structure and database
   - Implement User and Inventory Item models
   - Develop basic CRUD operations for Inventory Items
   - Implement user authentication and authorization
   - Supplier management functionality
   - Detailed inventory reporting
   - Multi-store inventory management
   - Audit Logs using Created_by fields 
   - Dynamic inventory category management

2. **Advanced Features Implementation**
   - Develop inventory change tracking system
   - Implement filters and sorting for inventory views
   - Create endpoints for viewing inventory levels and change history

3. **Optimization and Security Enhancements**
   - Implement pagination for large datasets
   - Enhance error handling and input validation
   - Conduct security audit and implement necessary measures

4. **Testing and Deployment**
   - Write unit and integration tests
   - Deploy API to PythonAnywhere
   - Perform final testing and optimization in production environment

## API Endpoints

For a comprehensive list of API endpoints and their documentation, please visit our Swagger UI at [snrRoko.pythonanywhere.com/api/schema/swagger-ui](https://snrRoko.pythonanywhere.com/api/schema/swagger-ui).

Here's a summary of the main endpoint categories:

1. **Accounts**: User registration, login, and profile management
2. **Logs**: Retrieving logs for various actions performed by users
3. **Storages**: Managing warehouses and stores
4. **Products**: CRUD operations for warehouse stocks, store stocks, and product categories
5. **Sales**: Managing customers, orders, order items, and stock transfers

## Stretch Goals

- Low stock alerts system 
- Email System
- Password Change Requests
- Dynamic inventory category management
- Automatic stock reordering suggestions
- User Management Accross Storages 

## Timeline

This project is scheduled for development over a two-week period, with specific milestones for each phase of development.

## Contributing

We welcome contributions to the InventoryIQ project! If you're interested in contributing, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive messages
4. Push your changes to your fork
5. Submit a pull request to the main repository

Please ensure your code adheres to our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
