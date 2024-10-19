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
| Number | Method | Endpoint | Description |
|--------|--------|----------|-------------|
| 1 | POST | snrroko.pythonanywhere.com/api/accounts/users/register | Registering a user |
| 2 | POST | snrroko.pythonanywhere.com/api/accouns/users/login/ | Logging in a user |
| 3 | POST | snrroko.pythonanywhere.com/api/accounts/users/login/refresh/ | Refreshing login token |
| 4 | GET | snrroko.pythonanywhere.com/api/accounts/users/ | Retrieving collection of users (pagination as page and sorting as order parameters accepted) |
| 5 | GET | snrroko.pythonanywhere.com/api/accounts/profile/me/ | Retrieving a logged-in user's profile |
| 6 | PUT | snrroko.pythonanywhere.com/api/accounts/profile-update/me/ | Updating a logged-in user's profile |
| 7 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/warehouse-stocks/ | Retrieving a list of warehouse stocks created by a user |
| 8 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/store-stocks/ | Retrieving a list of store stocks created by a user |
| 9 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/categories/ | Retrieving a list of categories created by a user |
| 10 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/users/ | Retrieving a list of users created by a user |
| 11 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/warehouses/ | Retrieving a list of warehouses created by a user |
| 12 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/stores/ | Retrieving a list of stores created by a user |
| 13 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/suppliers/ | Retrieving a list of suppliers created by a user |
| 14 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/customers/ | Retrieving a list of customers created by a user |
| 15 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/order-items/ | Retrieving a list of Order Items created by a user |
| 16 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/orders/ | Retrieving a list of Orders created by a user |
| 17 | GET | snrroko.pythonanywhere.com/api/logs/users/<int:pk>/stock-transfers/ | Retrieving a list of Stock Transfers created by a user |
| 18 | GET | snrroko.pythonanywhere.com/api/storages/warehouses/ | Retrieving a list of all warehouses (Pagination and sorting implemented) |
| 19 | GET | snrroko.pythonanywhere.com/api/storages/warehouses/<int:pk> | Retrieving a single warehouse resource |
| 20 | POST | snrroko.pythonanywhere.com/api/storages/warehouses/ | Creating a new warehouse |
| 21 | PUT | snrroko.pythonanywhere.com/api/storages/warehouses/<int:pk> | Updating a warehouse object by sending full object |
| 22 | PATCH | snrroko.pythonanywhere.com/api/storages/warehouses/<int:pk> | Updating a warehouse object by sending just the updated field |
| 23 | DELETE | snrroko.pythonanywhere.com/api/storages/warehouses/<int:pk> | Deleting a warehouse object |
| 24 | GET | snrroko.pythonanywhere.com/api/storages/stores/ | Retrieving a list of all stores (Pagination and sorting implemented) |
| 25 | GET | snrroko.pythonanywhere.com/api/storages/stores/<int:pk> | Retrieving a single store resource |
| 26 | POST | snrroko.pythonanywhere.com/api/storages/stores/ | Creating a new store |
| 27 | PUT | snrroko.pythonanywhere.com/api/storages/stores/<int:pk> | Updating a store object by sending full object |
| 28 | PATCH | snrroko.pythonanywhere.com/api/storages/stores/<int:pk> | Updating a store object by sending just the updated field |
| 29 | DELETE | snrroko.pythonanywhere.com/api/storages/stores/<int:pk> | Deleting a store object |
| 30 | GET | snrroko.pythonanywhere.com/api/products/warehouse-stocks/ | Retrieving a list of all warehouse stocks (Pagination and sorting implemented) |
| 31 | GET | snrroko.pythonanywhere.com/api/products/warehouse-stocks/?category=""&active=""&warehouse=""&supplier=""&supplier=""&low-stock="" | (All Optional) query parameters for retrieving lists of warehouse stocks based on the category, being active or not, low stocks and the particular warehouse housing it as well as suppliers |
| 32 | GET | snrroko.pythonanywhere.com/api/products/warehouse-stocks/<int:pk> | Retrieving a single warehouse stock resource |
| 33 | POST | snrroko.pythonanywhere.com/api/products/warehouse-stocks/ | Creating a new warehouse stock object |
| 34 | PUT | snrroko.pythonanywhere.com/api/products/warehouse-stocks/<int:pk> | Updating a warehouse stock object by sending full object |
| 35 | PATCH | snrroko.pythonanywhere.com/api/products/warehouse-stocks/<int:pk> | Updating a warehouse stock object by sending just the updated field |
| 36 | DELETE | snrroko.pythonanywhere.com/api/products/warehouse-stocks/<int:pk> | Deleting a warehouse stock object |
| 37 | GET | snrroko.pythonanywhere.com/api/products/store-stocks/ | Retrieving a list of all store stocks (Pagination and sorting implemented) |
| 38 | GET | snrroko.pythonanywhere.com/api/products/store-stocks/?category=""&active=""&store=""&supplier=""&supplier=""&low-stock="" | (All Optional) query parameters for retrieving lists of store stocks based on the category, being active or not, low stocks and the particular store selling it as well as suppliers |
| 39 | GET | snrroko.pythonanywhere.com/api/products/store-stocks/<int:pk> | Retrieving a single store stock resource |
| 40 | GET | snrroko.pythonanywhere.com/api/products/store-stocks/barcode/<int:pk> | Retrieving a single store stock resource using a barcode |
| 41 | POST | snrroko.pythonanywhere.com/api/products/store-stocks/ | Creating a new store stock object |
| 42 | PUT | snrroko.pythonanywhere.com/api/products/store-stocks/<int:pk> | Updating a store stock object by sending full object |
| 43 | PATCH | snrroko.pythonanywhere.com/api/products/store-stocks/<int:pk> | Updating a store stock object by sending just the updated field |
| 44 | DELETE | snrroko.pythonanywhere.com/api/products/store-stocks/<int:pk> | Deleting a store stock object |
| 45 | GET | snrroko.pythonanywhere.com/api/products/ | Retrieving a list of all products (Pagination and sorting implemented) |
| 46 | GET | snrroko.pythonanywhere.com/api/products/?category=""&active=""&low-stock="" | (All Optional) query parameters for retrieving lists of store stocks based on the category, low stocks and being active or not |
| 47 | GET | snrroko.pythonanywhere.com/api/products/<int:pk> | Retrieving a single product resource |
| 48 | PATCH | snrroko.pythonanywhere.com/api/products/<int:pk> | Updating a product object by sending just the updated field |
| 49 | DELETE | snrroko.pythonanywhere.com/api/products/<int:pk> | Deleting a store stock object |
| 50 | GET | snrroko.pythonanywhere.com/api/products/categories/ | Retrieving a list of all product categories (Pagination and sorting implemented) |
| 51 | GET | snrroko.pythonanywhere.com/api/products/categories/<int:pk> | Retrieving a single product category resource |
| 52 | POST | snrroko.pythonanywhere.com/api/products/categories/ | Creating a new product category |
| 53 | PUT | snrroko.pythonanywhere.com/api/products/categories/<int:pk> | Updating a product category by sending full object |
| 54 | PATCH | snrroko.pythonanywhere.com/api/products/categories/<int:pk> | Updating a product category by sending just the updated field |
| 55 | DELETE | snrroko.pythonanywhere.com/api/products/categories/<int:pk> | Deleting a product category object |
| 56 | GET | snrroko.pythonanywhere.com/api/sales/customers/ | Retrieving a list of all customers (Pagination and sorting implemented) |
| 57 | GET | snrroko.pythonanywhere.com/api/sales/customers/<int:pk> | Retrieving a single customer resource |
| 58 | POST | snrroko.pythonanywhere.com/api/sales/customers/ | Creating a new customers resource |
| 59 | PUT | snrroko.pythonanywhere.com/api/sales/customers/<int:pk> | Updating a customers resource by sending the whole object |
| 60 | PATCH | snrroko.pythonanywhere.com/api/sales/customers/<int:pk> | Updating a single customer object by sending just the updated field |
| 61 | DELETE | snrroko.pythonanywhere.com/api/sales/customers/<int:pk> | Deleting a customer object |
| 62 | GET | snrroko.pythonanywhere.com/api/sales/orders/ | Retrieving a list of all orders (Pagination and sorting implemented) |
| 63 | GET | snrroko.pythonanywhere.com/api/sales/orders/<int:pk> | Retrieving a single order resource |
| 64 | GET | snrroko.pythonanywhere.com/api/sales/orders/?customer=""&date-from=""&date-to=""&status="" | Optional query parameters to filter lists of orders by customers, order dates and status |
| 65 | POST | snrroko.pythonanywhere.com/api/sales/orders/ | Creating a new order resource |
| 66 | PUT | snrroko.pythonanywhere.com/api/sales/orders/<int:pk> | Updating an order resource by sending the whole object |
| 67 | PATCH | snrroko.pythonanywhere.com/api/sales/orders/<int:pk> | Updating a single order object by sending just the updated field |
| 68 | DELETE | snrroko.pythonanywhere.com/api/sales/orders/<int:pk> | Deleting an order object |
| 69 | GET | snrroko.pythonanywhere.com/api/sales/order-items/ | Retrieving a list of all order items (Pagination and sorting implemented) |
| 70 | GET | snrroko.pythonanywhere.com/api/sales/order-items/<int:pk> | Retrieving a single order item resource |
| 71 | GET | snrroko.pythonanywhere.com/api/sales/order-items/?customer=""&date-from=""&date-to=""&status=""&product=""&store="" | Optional query parameters to filter lists of orders by customers, order dates, status, product and store |
| 72 | POST | snrroko.pythonanywhere.com/api/sales/order-items/ | Creating a new order item resource |
| 73 | PUT | snrroko.pythonanywhere.com/api/sales/order-items/<int:pk> | Updating an order item resource by sending the whole object |
| 74 | PATCH | snrroko.pythonanywhere.com/api/sales/order-items/<int:pk> | Updating a single order item object by sending just the updated field |
| 75 | DELETE | snrroko.pythonanywhere.com/api/sales/order-items/<int:pk> | Deleting an order item object |
| 76 | GET | snrroko.pythonanywhere.com/api/sales/stock-transfers/ | Retrieving a list of all stock transfers (Pagination and sorting implemented) |
| 77 | GET | snrroko.pythonanywhere.com/api/sales/stock-transfers/<int:pk> | Retrieving a single stock transfer resource |
| 78 | GET | snrroko.pythonanywhere.com/api/sales/stock-transfers/?warehouse=""&date-from=""&date-to=""&status=""&stock=""&store="" | Optional query parameters to filter lists of stock transfers by source, destination, status, product and date transferred |
| 79 | POST | snrroko.pythonanywhere.com/api/sales/stock-transfers/ | Creating a new stock transfer resource |
| 80 | PUT | snrroko.pythonanywhere.com/api/sales/stock-transfers/<int:pk> | Updating a stock transfer resource by sending the whole object |
| 81 | PATCH | snrroko.pythonanywhere.com/api/sales/stock-transfers/<int:pk> | Updating a single stock transfer object by sending just the updated field |
| 82 | DELETE | snrroko.pythonanywhere.com/api/sales/stock-transfers/<int:pk> | Deleting a stock transfer object |

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
