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
   7. **GET**     api/logs/users/<int:pk>/warehouse-stocks/ - Retrieving a list of warehouse stocks created by a user 
   8. **GET**     api/logs/users/<int:pk>/store-stocks/  - Retrieving a list of store stocks created by a user 
   9. **GET**     api/logs/users/<int:pk>/categories/  - Retrieving a list of categories created by a user 
  10. **GET**     api/logs/users/<int:pk>/users/  - Retrieving a list of users created by a user 
  11. **GET**     api/logs/users/<int:pk>/warehouses/  - Retrieving a list of warehouses created by a user 
  12. **GET**     api/logs/users/<int:pk>/stores/  - Retrieving a list of stores created by a user
  13. **GET**     api/logs/users/<int:pk>/suppliers/  - Retrieving a list of suppliers created by a user
  14. **GET**     api/logs/users/<int:pk>/customers/  - Retrieving a list of customers created by a user
  15. **GET**     api/logs/users/<int:pk>/order-items/  - Retrieving a list of Order Items created by a user
  16. **GET**     api/logs/users/<int:pk>/orders/  - Retrieving a list of Orders created by a user
  17. **GET**     api/logs/users/<int:pk>/stock-transfers/  - Retrieving a list of Stock Transfers created by a user
**Storages**
  18. **GET**     api/storages/warehouses/  - Retrieving a list of all warehouses (Pagination and sorting implemented)
  19. **GET**     api/storages/warehouses/<int:pk>  - Retrieving a single warehouse resource
  20. **POST**    api/storages/warehouses/  - Creating a new warehouse
  21. **PUT**     api/storages/warehouses/<int:pk>  - Updating a warehouse object by sending full object
  22. **PATCH**   api/storages/warehouses/<int:pk>  - Updating a warehouse object by sending just the updated field
  23. **DELETE**  api/storages/warehouses/<int:pk>  - Deleting a warehouse object
  24. **GET**     api/storages/stores/  - Retrieving a list of all stores (Pagination and sorting implemented)
  25. **GET**     api/storages/stores/<int:pk>  - Retrieving a single store resource
  26. **POST**    api/storages/stores/  - Creating a new store
  27. **PUT**     api/storages/stores/<int:pk>  - Updating a store object by sending full object
  28. **PATCH**   api/storages/stores/<int:pk>  - Updating a store object by sending just the updated field
  29. **DELETE**  api/storages/stores/<int:pk>  - Deleting a store object
**Products**
  30. **GET**     api/products/warehouse-stocks/  - Retrieving a list of all warehouse stocks (Pagination and sorting implemented)
  31. **GET**     api/products/warehouse-stocks/?category=""&active=""&warehouse=""&supplier=""&supplier=""  
                  - (All Optional) query paramters for retrieving lists of 
                  warehouse stocks based on the category, being active or not and the particular warehouse housing it as well as suppliers 
  32. **GET**     api/products/warehouse-stocks/<int:pk>  - Retrieving a single warehouse stock resource
  33. **POST**    api/products/warehouse-stocks/  - Creating a new warehouse stock object
  34. **PUT**     api/products/warehouse-stocks/<int:pk>  -  Updating a warehouse stock object by sending full object
  35. **PATCH**   api/products/warehouse-stocks/<int:pk>  -  Updating a warehouse stock object by sending just the updated field
  36. **DELETE**  api/products/warehouse-stocks/<int:pk>  -  Deleting a warehouse stock object
  37. **GET**     api/products/store-stocks/  - Retrieving a list of all store stocks (Pagination and sorting implemented)
  38. **GET**     api/products/store-stocks/?category=""&active=""&store=""&supplier=""&supplier=""  
                  - (All Optional) query paramters for retrieving lists of 
                  store stocks based on the category, being active or not and the particular store selling it as well as suppliers 
  38. **GET**     api/products/store-stocks/<int:pk>  - Retrieving a single store stock resource
  39. **GET**     api/products/store-stocks/?barcode=(barcode)  - Retrieving a single store stock resource using a barcode parameter
  40. **POST**    api/products/store-stocks/  - Creating a new store stock object
  41. **PUT**     api/products/store-stocks/<int:pk>  -  Updating a store stock object by sending full object
  42. **PATCH**   api/products/store-stocks/<int:pk>  -  Updating a store stock object by sending just the updated field
  43. **DELETE**  api/products/store-stocks/<int:pk>  -  Deleting a store stock object
  44. **GET**     api/products/  - Retrieving a list of all products (Pagination and sorting implemented)
  45. **GET**     api/products/?category=""&active=""  
                  - (All Optional) query paramters for retrieving lists of 
                  store stocks based on the category and being active or not 
  46. **GET**     api/products/<int:pk>  - Retrieving a single product resource
  47. **PATCH**   api/products/<int:pk>  -  Updating a product object by sending just the updated field
  48. **DELETE**  api/products/<int:pk>  -  Deleting a store stock object
  49. **GET**     api/products/categories/  - Retrieving a list of all product categories (Pagination and sorting implemented)
  50. **GET**     api/products/categories/<int:pk>  - Retrieving a single product category resource
  51. **POST**    api/products/categories/  - Creating a new product category
  52. **PUT**     api/products/categories/<int:pk>  - Updating a product category by sending full object
  53. **PATCH**   api/products/categories/<int:pk>  - Updating a product category by sending just the updated field
  54. **DELETE**  api/products/categories/<int:pk>  - Deleting a product category object  

## Stretch Goals

- Low stock alerts system 
- Dynamic inventory category management
- Automatic stock reordering suggestions


## Timeline

This project is scheduled for development over a two-week period, with specific milestones for each phase of development.

## Contributing

coming soon
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
