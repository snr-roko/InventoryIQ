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
- Inventory change tracking
- RESTful API design
- JWT Authentication
- Secure and efficient data management

## Technology Stack

- Backend: Django
- API Framework: Django REST Framework
- Database: 
- Authentication: Django's built-in authentication system and JWT Authentication
- Deployment: 

## Getting Started

coming soon
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
   - Deploy API to -----
   - Perform final testing and optimization in production environment

## API Endpoints
**Accounts**
   1. **POST** api/accounts/users/register  - Registering a user
   2. **POST** api/accouns/users/login/  - Logging in a user
   3. **POST**    api/accounts/users/login/refresh/  - Refreshing login token
   4. **GET**     api/accounts/users/  - Retrieving collection of users (pagination as page and sorting as order parameters accepted)
   5. **GET**     api/accounts/profile/me/  - Retrieving a logged-in user's profile 
   6. **PUT**     api/accounts/profile-update/me/  - Updating a logged-in user's profile
**Logs** __Pagination and Ordering parameters accepted__
   7. **GET**     api/logs/warehouse-stocks/users/<int:pk>/ - Retrieving a list of warehouse stocks created by a user 
   8. **GET**     api/logs/store-stocks/users/<int:pk>/  - Retrieving a list of store stocks created by a user 
   9. **GET**     api/logs/categories/users/<int:pk>/  - Retrieving a list of categories created by a user 
  10. **GET**     api/logs/users/<int:pk>/  - Retrieving a list of users created by a user 
  11. **GET**     api/logs/warehouses/users/<int:pk>/  - Retrieving a list of warehouses created by a user 
  12. **GET**     api/logs/stores/users/<int:pk>/  - Retrieving a list of stores created by a user
  13. **GET**     api/logs/suppliers/users/<int:pk>/  - Retrieving a list of suppliers created by a user
  14. **GET**     api/logs/customers/users/<int:pk>/  - Retrieving a list of customers created by a user
  15. **GET**     api/logs/order-items/users/<int:pk>/  - Retrieving a list of Order Items created by a user
  16. **GET**     api/logs/orders/users/<int:pk>/  - Retrieving a list of Orders created by a user
  17. **GET**     api/logs/stock-transfers/users/<int:pk>/  - Retrieving a list of Stock Transfers created by a user
**Storages**
  18. **GET**     api/storages/warehouses/  - Retrieving a list of all warehouses (Pagination and sorting implemented)
  19. **GET**     api/storages/warehouses/<int:pk>  - Retrieving a single warehouse resource
  20. **POST**    api/storages/warehouses/  - Creating a new warehouse
  21. **PUT**     api/storages/warehouses/<int:pk>  - Updating a warehouse object by sending full object
  22. **PATCH**   api/storages/warehouses/<int:pk>  -Updating a warehouse object by sending just the updated field
  23. **DELETE**  api/storages/warehouses/<int:pk>  -Deleting a warehouse object
  24. **GET**     api/storages/stores/  - Retrieving a list of all stores (Pagination and sorting implemented)
  25. **GET**     api/storages/stores/<int:pk>  - Retrieving a single store resource
  26. **POST**    api/storages/stores/  - Creating a new store
  27. **PUT**     api/storages/stores/<int:pk>  - Updating a store object by sending full object
  28. **PATCH**   api/storages/stores/<int:pk>  -Updating a store object by sending just the updated field
  29. **DELETE**  api/storages/stores/<int:pk>  -Deleting a store object

## Stretch Goals

- Low stock alerts system 
- Dynamic inventory category management
- Barcode scanning support
- Automatic stock reordering suggestions


## Timeline

This project is scheduled for development over a two-week period, with specific milestones for each phase of development.

## Contributing

coming soon
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
