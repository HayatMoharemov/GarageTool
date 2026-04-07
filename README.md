# GarageTool
The web application is deployed on Azure and is live. It can be tested in real time, without the need of installing anything. Just click the following link.

https://garagetool-b5dkf0g9g6dfhgec.swedencentral-01.azurewebsites.net/

GarageTool is a **Django-based web application** designed to help manage garage / auto service businesses. It provides tools for vehicle service tracking, employee management, parts catalogue/inventory, and service-related calculations.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Main URLs](#main-urls)
- [Database Structure](#database-structure)
  - [Models](#models)
  - [Relationships](#relationships)
  - [Forms](#forms)
  - [Validators](#validators)
- [Views](#views)
- [Rest API](#rest-api)
- [Signals](#signals)
- [Async tasks](#async-tasks)
- [Templates and Styling](#templates-and-styling)
- [Data Seeding](#data-seeding)
- [Post Scriptum](#post-scriptum)



## Features

- **Garage** module – manage vehicles, service orders, service history
- **Employees** module – track mechanics, work hours, manage employees
- **Catalogue** module – parts inventory, spare parts catalog, services, services management
- **Calculator** module – service cost estimation, labor + parts calculation
- **Common** utilities – shared models, helpers, or base functionality

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML + CSS (Bootstrap or custom styles possible)
- **Database**: PostgreSQL

## Project Structure

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


## Quick Start

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
---
4. .env Template
    `GarageTool\.env.template` File is a .env template file, where you can add your own .env data.
---
5. Apply migrations
```bash
python manage.py migrate
```
6. Create superuser(optional)
```bash
python manage.py createsuperuser
```
7. Run the server
```bash
python manage.py runserver
```

- Open → http://127.0.0.1:8000/
- Admin panel → http://127.0.0.1:8000/admin/

## Main URLs

- `/`            → Home 
- `/accounts/`   → Accounts management
- `/contact/`    → Contact inquiries management
- `/garage/`     → Vehicles & Vehicle management 
- `/employees/`  → Staff & Staff management  
- `/catalogue/`  → Parts & services catalogue + Management
- `/calculator/` → Service cost calculator 
- `/admin/`      → Django admin

## Database structure
### Models
- **TimeStampModel** - Base model for BaseVehicle (possible reusability with other models in future).
- **BaseVehicle** - Base model (Parent class) for Cars and Motorcycles.
- **CarModel** and **MotorcycleModel** - Inheriting BaseVehicle and its attributes and some unique ones for each type.
- **EmployeeModel** - Model for employees.
- **BaseProduct** - Base model (Parent class) for Services and Parts.
- **PartsModel** and **ServicesModel** - Inheriting BaseProduct. Models for parts and services available.
- **CalculatorModel** - Model used to calculate costs for the client.
- **BusinessUser & IndividualUser** - GeneralUser models for Business accounts and Individual accounts.
- **ContactModel** - Model used for communication between IndividualUser and BusinessUser

### Relationships
- User(Individual/Business) → Car
  (one user can be linked to many cars )

- User(Individual/Business) → Motorcycle
  (one user can be linked to many motorcycles)

- User(Individual/Business) → Contact(Inquiry)  
  (IndividualUser is linked to the sender of the inquiry, BusinessUser is linked to receiver)

- Company → Contact(Inquiry  
  (one calculator can link to one car – optional)

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

### Forms
#### Accounts app
- **GeneralUser** - UserCreation Form
- **IndividualUser** - Type of GeneralUser
- **BusinessUser** - Type of GeneralUser
#### Garage app
- **BaseForm** - BaseForm for vehicles
- **CarForm** - Inherited from BaseForm
- **MotorcycleForm**  - Inherited from BaseForm
#### Employee app
- **EmployeeForm**
#### Catalogue app
- **ServicesForm**
#### Contact app
- **ContactForm**

### Validators

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

## Views

- **CreateView, DeleteView, UpdateView, ListView** implemented appropriately in the project.
- Mostly **Class Based Views**. They automatically validate forms and handle GET and POST methods.
- Successful implementation of **redirect**
- 
## REST API
The project includes a **REST API built with Django REST Framework**.

Location:

```
vehicles_api/
```

### Example endpoints

```
/api/cars/
/api/motorcycles/
```

### Filtering

Example:

```
/api/cars/?make=BMW
```

### Ordering

```
/api/cars/?ordering=id
```

### Owner-based access

Vehicles returned by the API are filtered using:

```
OwnerFilterMixin
```

This ensures users only see vehicles they own.

### Serializers

The API uses:

```
CarSerializer
MotorcycleSerializer
```

to convert model instances into JSON.

## Signals
- `accounts\signals.py`

  Signal that automatically creates a profile for a new GeneralUser.
    - Triggered after a GeneralUser instance is created.
    - If the user is a business, a BusinessUser profile is created.
    - If the user is an individual, an IndividualUser profile is created.

```
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            if instance.is_business:
                BusinessUser.objects.create(
                    user=instance
                )
            elif instance.is_individual:
                IndividualUser.objects.create(
                    user=instance
                )
```
---
```
@receiver(post_migrate)
def create_default_user_groups(sender, **kwargs):

    if sender.name != 'accounts':
        return

    editor_group, created = Group.objects.get_or_create(name='Editor')

    try:
        CarModel = apps.get_model('garage', 'CarModel')
        MotorcycleModel = apps.get_model('garage', 'MotorcycleModel')

        car_permission = Permission.objects.get(content_type__app_label='garage', codename='change_carmodel')
        moto_permission = Permission.objects.get(content_type__app_label='garage', codename='change_motorcyclemodel')

        editor_group.permissions.set([car_permission, moto_permission])
    except (LookupError, Permission.DoesNotExist):
        pass

    admin_group, created = Group.objects.get_or_create(name='Admin')
    all_perms = Permission.objects.all()
    admin_group.permissions.set(all_perms)

```

- Signal that automatically creates two User Groups in Django Admin upon making the first migrations.
    - Editor Group (allowed to edit vehicles)
    - Admin Group (full permissions)

## Async tasks
- `garage\tasks.py`
    - A task that runs on the background and checks every 1 hour for unrepaired vehicles.
    - Returns information for the unrepaired vehicles in the console. If none, returns that no vehicles need repair at the moment.
## Templates and styling
### Base templates
- The project has ```base.html``` as a base HTML file and is being inherited by every template in the project.
- ```footer.html``` and ```navbar.html``` are also shared across the templates in the project.
```text
templates/base.html
templates/shared/footer.html
templates/shared/navbar.html
```
### Templatetags & Filters

#### Pagination
```common\templatetags\pagination.py```
- For the purposes of the project It also has pagination which is in a separate ```.html``` file, so it can be reused.

#### Currency filter
```common\templatetags\currency.py```
- For the calculation purposes of the project, since it also depends on calculations as a part of its functionality, there is a custom ```currency.py``` filter.
It can be used in templates to automatically add the currency, which can also be changed in the filter itself.

### Template types

- 32 **Templates** (Excluding ```navbar.html```,```footer.html```,```base.html```,```paginator.html```)
  - 30 **Dynamic Templates**
  - 2 **Static Templates**
- Appropriate **CSS** styling stored in ```static\css```
- Custom **404** page.
  - Test on http://127.0.0.1:8000/Krushi
- No orphan pages

## Data seeding

- In the ```manage.py``` file there are already preloaded scripts that will automatically seed the DB with data.
In order to run the script, please uncomment the code from line ```25``` and after running the data should be seeded.
The script is for Parts and Services app.
## Post Scriptum

This project was developed by **Hayat Moharemov** as an assignment for the first part of Python Web courses in **SoftUni**.
