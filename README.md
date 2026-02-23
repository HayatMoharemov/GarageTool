# GarageTool

GarageTool is a **Django-based web application** designed to help manage garage / auto service businesses. It provides tools for vehicle service tracking, employee management, parts catalogue/inventory, and service-related calculations.

## Table of Contents
- [1. Features](#features)
- [2. Tech Stack](#tech-stack)
- [3. Project Structure](#project-structure)
- [4. Quick Start](#quick-start)
- [5. Main URLs](#main-urls)
- [6. Database Structure](#database-structure)
  - [6.1 Models](#models)
  - [6.2 Relationships](#relationships)
  - [6.3 Forms](#forms)
  - [6.4 Validators](#validators)
- [7. Views](#views)
- [8. Templates and Styling](#templates-and-styling)
- [9. Data Seeding](#data-seeding)
- [Post Scriptum](#post-scriptum)



## 1. Features

- **Garage** module – manage vehicles, service orders, service history
- **Employees** module – track mechanics, work hours, manage employees
- **Catalogue** module – parts inventory, spare parts catalog, services, services management
- **Calculator** module – service cost estimation, labor + parts calculation
- **Common** utilities – shared models, helpers, or base functionality

## 2. Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML + CSS (Bootstrap or custom styles possible)
- **Database**: PostgreSQL

## 3. Project Structure

```markdown
GarageTool/
├── GarageTool/ ------> # Main Django project (settings.py, urls.py, wsgi.py, etc.)
├── calculator/ ------> # Cost estimation & calculator logic
├── catalogue/  ------> # Parts, inventory, suppliers
├── common/     ------> # Shared models, utilities, mixins
├── employees/  ------> # Staff, mechanics, roles, schedules
├── garage/     ------> # Vehicles, service orders, history
├── static/     ------> # CSS, JS, images
├── templates/  ------> # HTML templates (base.html, etc.)
├── manage.py
└── requirements.txt
```


## 4. Quick Start

1. Clone the repository

```bash
git clone https://github.com/HayatMoharemov/GarageTool.git
cd GarageTool
```
2. Create and activate virtual environment

- Windows
```bash
python -m venv venv
venv\Scripts\activate
```
- macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Apply migrations
```bash
python manage.py migrate
```
5. Create superuser(optional)
```bash
python manage.py createsuperuser
```
6. Run the server
```bash
python manage.py runserver
```

- Open → http://127.0.0.1:8000/
- Admin panel → http://127.0.0.1:8000/admin/

## 5. Main URLs (example – depends on your urls.py)

- `/`            → Home 
- `/garage/`     → Vehicles & Vehicle management 
- `/employees/`  → Staff & Staff management  
- `/catalogue/`  → Parts & services catalogue + Management
- `/calculator/` → Service cost calculator 
- `/admin/`      → Django admin

## 6. Database structure
### 6.1 Models
- **TimeStampModel** - Base model for BaseVehicle (possible reusability with other models in future).
- **BaseVehicle** - Base model (Parent class) for Cars and Motorcycles.
- **CarModel** and **MotorcycleModel** - Inheriting BaseVehicle and its attributes and some unique ones for each type.
- **EmployeeModel** - Model for employees.
- **BaseProduct** - Base model (Parent class) for Services and Parts.
- **PartsModel** and **ServicesModel** - Inheriting BaseProduct. Models for parts and services available.
- **CalculatorModel** - Model used to calculate costs for the client.

### 6.2 Relationships

- Calculator → Car  
  (one calculator can link to one car – optional)

- Calculator → Motorcycle  
  (one calculator can link to one motorcycle – optional)

- Calculator ↔ Parts  
  (many-to-many: one offer can use many parts)

- Calculator ↔ Services  
  (many-to-many: one offer can include many services)

**Simple rule:**  
Each calculation/offer picks **one vehicle** (car or motorcycle) + any number of **parts** and **services**.

### 6.3 Forms
#### Garage app
- **BaseForm** - BaseForm for vehicles
- **CarForm** and **MotorcycleForm**  - Inherited from BaseForm
#### Employee app
- **EmployeeForm**
#### Catalogue app
- **ServicesForm**

### 6.4 Validators

Validators make sure bad data cannot be saved.

Main rules used in the project:

- Prices and costs must be positive (> 0)
- Quantities cannot be negative
- Mileage must be ≥ 0
- Some fields cannot be empty when they should not (required checks)

Most important validators are in:
- garage/models.py
- catalogue/models.py
- calculator/models.py
- common/validators.py

They show clear error messages when something is wrong.

## 7. Views

- **CreateView, DeleteView, UpdateView, ListView** implemented appropriately in the project.
- Mostly **Class Based Views**. They automatically validate forms and handle GET and POST methods.
- Successful implementation of **redirect**

## 8. Templates and styling
### 8.1 Base templates
- The project has ```base.html``` as a base HTML file and is being inherited by every template in the project.
- ```footer.html``` and ```navbar.html``` are also shared across the templates in the project.
```text
templates/base.html
templates/shared/footer.html
templates/shared/navbar.html
```
### 8.2 Templatetags & Filters

#### Pagination
```common\templatetags\pagination.py```
- For the purposes of the project It also has pagination which is in a separate ```.html``` file, so it can be reused.

#### Currency filter
```common\templatetags\currency.py```
- For the calculation purposes of the project, since it also depends on calculations as a part of its functionality, there is a custom ```currency.py``` filter.
It can be used in templates to automatically add the currency, which can also be changed in the filter itself.

### 8.3 Template types

- 22 **Templates** (Excluding ```navbar.html```,```footer.html```,```base.html```,```paginator.html```)
  - 20 **Dynamic Templates**
  - 2 **Static Templates**
- Appropriate **CSS** styling stored in ```static\css```
- Custom **404** page.
- No orphan pages

## 9. Data seeding

- In the ```manage.py``` file there is already preloaded scripts that will automatically seed the DB with data.
In order to run the script, please uncomment the code from line ```28``` and after running the data should be seeded.

## Post Scriptum

This project was developed by **Hayat Moharemov** as an assignment for the first part of Python Web courses in **SoftUni**.
