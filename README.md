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

Below is a comprehensive table of all API endpoints. For interactive documentation, please visit our Swagger UI at [snrRoko.pythonanywhere.com/api/schema/swagger-ui](https://snrRoko.pythonanywhere.com/api/schema/swagger-ui).

| Category | Method | Endpoint | Description |
|----------|--------|----------|-------------|
| **Accounts** | POST | [snrroko.pythonanywhere.com/api/accounts/users/register](https://snrroko.pythonanywhere.com/api/accounts/users/register) | Register a new user |
| | POST | [snrroko.pythonanywhere.com/api/accounts/users/login/](https://snrroko.pythonanywhere.com/api/accounts/users/login/) | Log in a user |
| | POST | [snrroko.pythonanywhere.com/api/accounts/users/login/refresh/](https://snrroko.pythonanywhere.com/api/accounts/users/login/refresh/) | Refresh login token |
| | GET | [snrroko.pythonanywhere.com/api/accounts/users/](https://snrroko.pythonanywhere.com/api/accounts/users/) | Retrieve collection of users |
| | GET | [snrroko.pythonanywhere.com/api/accounts/profile/me/](https://snrroko.pythonanywhere.com/api/accounts/profile/me/) | Retrieve logged-in user's profile |
| | PUT | [snrroko.pythonanywhere.com/api/accounts/profile-update/me/](https://snrroko.pythonanywhere.com/api/accounts/profile-update/me/) | Update logged-in user's profile |
| **Logs** | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/warehouse-stocks/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/warehouse-stocks/) | Retrieve warehouse stocks created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/store-stocks/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/store-stocks/) | Retrieve store stocks created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/categories/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/categories/) | Retrieve categories created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/users/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/users/) | Retrieve users created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/warehouses/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/warehouses/) | Retrieve warehouses created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/stores/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/stores/) | Retrieve stores created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/suppliers/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/suppliers/) | Retrieve suppliers created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/customers/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/customers/) | Retrieve customers created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/order-items/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/order-items/) | Retrieve order items created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/orders/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/orders/) | Retrieve orders created by a user |
| | GET | [snrroko.pythonanywhere.com/api/logs/users/{pk}/stock-transfers/](https://snrroko.pythonanywhere.com/api/logs/users/{pk}/stock-transfers/) | Retrieve stock transfers created by a user |
| **Storages** | GET | [snrroko.pythonanywhere.com/api/storages/warehouses/](https://snrroko.pythonanywhere.com/api/storages/warehouses/) | Retrieve list of all warehouses |
| | GET | [snrroko.pythonanywhere.com/api/storages/warehouses/{pk}](https://snrroko.pythonanywhere.com/api/storages/warehouses/{pk}) | Retrieve a single warehouse |
| | POST | [snrroko.pythonanywhere.com/api/storages/warehouses/](https://snrroko.pythonanywhere.com/api/storages/warehouses/) | Create a new warehouse |
| | PUT | [snrroko.pythonanywhere.com/api/storages/warehouses/{pk}](https://snrroko.pythonanywhere.com/api/storages/warehouses/{pk}) | Update a warehouse (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/storages/warehouses/{pk}](https://snrroko.pythonanywhere.com/api/storages/warehouses/{pk}) | Update a warehouse (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/storages/warehouses/{pk}](https://snrroko.pythonanywhere.com/api/storages/warehouses/{pk}) | Delete a warehouse |
| | GET | [snrroko.pythonanywhere.com/api/storages/stores/](https://snrroko.pythonanywhere.com/api/storages/stores/) | Retrieve list of all stores |
| | GET | [snrroko.pythonanywhere.com/api/storages/stores/{pk}](https://snrroko.pythonanywhere.com/api/storages/stores/{pk}) | Retrieve a single store |
| | POST | [snrroko.pythonanywhere.com/api/storages/stores/](https://snrroko.pythonanywhere.com/api/storages/stores/) | Create a new store |
| | PUT | [snrroko.pythonanywhere.com/api/storages/stores/{pk}](https://snrroko.pythonanywhere.com/api/storages/stores/{pk}) | Update a store (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/storages/stores/{pk}](https://snrroko.pythonanywhere.com/api/storages/stores/{pk}) | Update a store (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/storages/stores/{pk}](https://snrroko.pythonanywhere.com/api/storages/stores/{pk}) | Delete a store |
| **Products** | GET | [snrroko.pythonanywhere.com/api/products/warehouse-stocks/](https://snrroko.pythonanywhere.com/api/products/warehouse-stocks/) | Retrieve list of all warehouse stocks |
| | GET | [snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}) | Retrieve a single warehouse stock |
| | POST | [snrroko.pythonanywhere.com/api/products/warehouse-stocks/](https://snrroko.pythonanywhere.com/api/products/warehouse-stocks/) | Create a new warehouse stock |
| | PUT | [snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}) | Update a warehouse stock (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}) | Update a warehouse stock (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/warehouse-stocks/{pk}) | Delete a warehouse stock |
| | GET | [snrroko.pythonanywhere.com/api/products/store-stocks/](https://snrroko.pythonanywhere.com/api/products/store-stocks/) | Retrieve list of all store stocks |
| | GET | [snrroko.pythonanywhere.com/api/products/store-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/store-stocks/{pk}) | Retrieve a single store stock |
| | GET | [snrroko.pythonanywhere.com/api/products/store-stocks/barcode/{pk}](https://snrroko.pythonanywhere.com/api/products/store-stocks/barcode/{pk}) | Retrieve a store stock by barcode |
| | POST | [snrroko.pythonanywhere.com/api/products/store-stocks/](https://snrroko.pythonanywhere.com/api/products/store-stocks/) | Create a new store stock |
| | PUT | [snrroko.pythonanywhere.com/api/products/store-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/store-stocks/{pk}) | Update a store stock (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/products/store-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/store-stocks/{pk}) | Update a store stock (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/products/store-stocks/{pk}](https://snrroko.pythonanywhere.com/api/products/store-stocks/{pk}) | Delete a store stock |
| | GET | [snrroko.pythonanywhere.com/api/products/](https://snrroko.pythonanywhere.com/api/products/) | Retrieve list of all products |
| | GET | [snrroko.pythonanywhere.com/api/products/{pk}](https://snrroko.pythonanywhere.com/api/products/{pk}) | Retrieve a single product |
| | PATCH | [snrroko.pythonanywhere.com/api/products/{pk}](https://snrroko.pythonanywhere.com/api/products/{pk}) | Update a product (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/products/{pk}](https://snrroko.pythonanywhere.com/api/products/{pk}) | Delete a product |
| | GET | [snrroko.pythonanywhere.com/api/products/categories/](https://snrroko.pythonanywhere.com/api/products/categories/) | Retrieve list of all product categories |
| | GET | [snrroko.pythonanywhere.com/api/products/categories/{pk}](https://snrroko.pythonanywhere.com/api/products/categories/{pk}) | Retrieve a single product category |
| | POST | [snrroko.pythonanywhere.com/api/products/categories/](https://snrroko.pythonanywhere.com/api/products/categories/) | Create a new product category |
| | PUT | [snrroko.pythonanywhere.com/api/products/categories/{pk}](https://snrroko.pythonanywhere.com/api/products/categories/{pk}) | Update a product category (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/products/categories/{pk}](https://snrroko.pythonanywhere.com/api/products/categories/{pk}) | Update a product category (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/products/categories/{pk}](https://snrroko.pythonanywhere.com/api/products/categories/{pk}) | Delete a product category |
| **Sales** | GET | [snrroko.pythonanywhere.com/api/sales/customers/](https://snrroko.pythonanywhere.com/api/sales/customers/) | Retrieve list of all customers |
| | GET | [snrroko.pythonanywhere.com/api/sales/customers/{pk}](https://snrroko.pythonanywhere.com/api/sales/customers/{pk}) | Retrieve a single customer |
| | POST | [snrroko.pythonanywhere.com/api/sales/customers/](https://snrroko.pythonanywhere.com/api/sales/customers/) | Create a new customer |
| | PUT | [snrroko.pythonanywhere.com/api/sales/customers/{pk}](https://snrroko.pythonanywhere.com/api/sales/customers/{pk}) | Update a customer (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/sales/customers/{pk}](https://snrroko.pythonanywhere.com/api/sales/customers/{pk}) | Update a customer (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/sales/customers/{pk}](https://snrroko.pythonanywhere.com/api/sales/customers/{pk}) | Delete a customer |
| | GET | [snrroko.pythonanywhere.com/api/sales/orders/](https://snrroko.pythonanywhere.com/api/sales/orders/) | Retrieve list of all orders |
| | GET | [snrroko.pythonanywhere.com/api/sales/orders/{pk}](https://snrroko.pythonanywhere.com/api/sales/orders/{pk}) | Retrieve a single order |
| | POST | [snrroko.pythonanywhere.com/api/sales/orders/](https://snrroko.pythonanywhere.com/api/sales/orders/) | Create a new order |
| | PUT | [snrroko.pythonanywhere.com/api/sales/orders/{pk}](https://snrroko.pythonanywhere.com/api/sales/orders/{pk}) | Update an order (full update) |
| | PATCH | [snrroko.pythonanywhere.com/api/sales/orders/{pk}](https://snrroko.pythonanywhere.com/api/sales/orders/{pk}) | Update an order (partial update) |
| | DELETE | [snrroko.pythonanywhere.com/api/sales/orders/{pk}](https://snrroko.pythonanywhere.com/api/sales/orders/{pk}) | Delete an order |
| | GET | [snrroko.pythonanywhere.com/api/sales/order-items/](https://snrroko.pythonanywhere.com/api/sales/order-items/) | Retrieve list of all order items |
| | GET | [snrroko.pythonanywhere.com/api/sales/order-items/{pk}](https://snrroko.pythonanywhere.com/api/sales/order-items/{pk}) | Retrieve a single order item |
| | POST | [snrroko.pythonanywhere.com/api/sales/order-items/](https://snrroko.pythonanywhere.com/api/sales/order-items/) | Create a new order item |
| | PUT | [snrroko.pythonanywhere.com/api/sales/order-items/{pk}](https://snrroko.pythonanywhere.com/api/sales


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
