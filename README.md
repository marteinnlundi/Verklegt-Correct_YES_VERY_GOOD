# Verklegt-II-PizzaLair

**Verklegt námskeið II, Group 3**

**Projects 's Title: Pizza Lair**

_Project Description:_
Pizza Lair is an online pizza ordering application built with the Django web framework. It allows users to browse available pizza options and offers.
Users can also create an account.

_How to Install and Run the Project:_

1. Clone the repository
2. Navigate to the project directory:
   cd pizza-lair
3. Install the required dependencies:
   pip install -r requirements.txt
4. Set up the database
   python manage.py migrate
5. Run the server
   python manage.py runserver
6. Open the application in your browser at http://

_How to Use the Project:_
Pizza Lair is a user-friendly web application that can be used like any other website. Here are some basic instructions:

    Browse available pizzas by clicking on the "Menu" link in the navigation bar.
    [...]

_Project Structure:_
The project directory has the following structure:

    ```bash

pizza-lair/
├── pizza_lair/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── menu/
│ ├── migrations/
│ ├── templates/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── orders/
│ ├── migrations/
│ ├── templates/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── static/
├── templates/
├── db.sqlite3
├── manage.py
└── requirements.txt

```
    pizza_lair/: the main project directory containing settings and configuration files.
    menu/: an app that handles pizza menu functionality, including displaying available pizzas and customizing orders.
    orders/: an app that handles order processing, including submitting orders and displaying order history.
    static/: a directory containing static assets like CSS and JavaScript files.
    templates/: a directory containing HTML templates used by the project.
    db.sqlite3: the SQLite database used by the project.
    manage.py: a command-line utility for performing various Django tasks.
    requirements.txt: a file listing the Python packages required by the project.

_Include Credits:_
Pizza Lair was created by:

    Ágústa Björk Sch. Bergsveinsdóttir - agustabb
    Guðbjörg E. Sigurjósndóttir - GElisabet
    Marteinn Lundi Kjartansson - marteinnlundi

Thank you for using Pizza Lair!
```
