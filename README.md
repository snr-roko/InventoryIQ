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
   1. api/accounts/users/register  - Registering a user
   2. api/accouns/users/login/  - Logging in a user
   3. api/accounts/users/login/refresh/  - Refreshing login token
   4. api/accounts/users/  - Retrieving collection of users (pagination as page and sorting as order parameters accepted)
   5. api/accounts/profile/me/  - Retrieving a logged-in user's profile 
   6. api/accounts/profile-update/me/  - Updating a logged-in user's profile
**Logs** __Pagination and Ordering parameters accepted__
   7. api/logs/warehouse-stocks/users/<int:pk>/ - Retrieving a list of warehouse stocks created by a user 
   8. api/logs/store-stocks/users/<int:pk>/  - Retrieving a list of store stocks created by a user 
   9. api/logs/categories/users/<int:pk>/  - Retrieving a list of categories created by a user 
  10. api/logs/users/<int:pk>/  - Retrieving a list of users created by a user 
  11. api/logs/warehouses/users/<int:pk>/  - Retrieving a list of warehouses created by a user 
  12. api/logs/stores/users/<int:pk>/  - Retrieving a list of stores created by a user
  13. api/logs/suppliers/users/<int:pk>/  - Retrieving a list of suppliers created by a user
  14. api/logs/customers/users/<int:pk>/  - Retrieving a list of customers created by a user
  15. api/logs/order-items/users/<int:pk>/  - Retrieving a list of Order Items created by a user
  16. api/logs/orders/users/<int:pk>/  - Retrieving a list of Orders created by a user
  17. api/logs/stock-transfers/users/<int:pk>/  - Retrieving a list of Stock Transfers created by a user

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
