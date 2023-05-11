# Verklegt-II-PizzaLair

**Verklegt námskeið II, Group 3**

**Projects 's Title: Pizza Lair**

_Project Description:_
Pizza Lair is an online pizza ordering application built with the Django web framework. It allows users to browse available pizza options and offers.
Users can also create an account.

_How to Install and Run the Project:_

1. Navigate to the project directory:
   cd pizza-lair
2. Install the required dependencies:
   pip install -r requirements.txt
3. Set up the database:
   python manage.py migrate
4. Run the server:
   python manage.py runserver
5. Open the application in your browser at: http://

_How to Use the Project:_
Pizza Lair is a user-friendly web application that can be used like any other website. User navigates through the website by clicking the mouse on a desired route.


_Project Structure:_
The project directory has the following structure:

```bash

    pizza-lair/
    ├── pizza_lair/
    │ ├── **init**.py
    │ ├── settings.py
    │ ├── urls.py
    │ ├── asgi.py
    │ └── wsgi.py
    ├── products/
    │ ├── migrations/
    │ ├── **init**.py
    │ ├── admin.py
    │ ├── apps.py
    │ ├── models.py
    │ ├── tests.py
    │ ├── urls.py
    │ ├── wsgi.py
    │ └── views.py
    ├── orders/
    │ ├── migrations
    │ ├── **init**.py
    │ ├── admin.py
    │ ├── apps.py
    │ ├── forms.py
    │ ├── models.py
    │ ├── tests.py
    │ ├── urls.py
    │ ├── wsgi.py
    │ └── views.py
    ├── users/
    │ ├── migrations/
    │ ├── forms/
    │ ├── **init**.py
    │ ├── admin.py
    │ ├── apps.py
    │ ├── urls.py
    │ ├── models.py
    │ ├── tests.py
    │ ├── wsgi.py
    │ └── views.py
    ├── static/
    ├── templates/
    ├── media/
    ├── user_images/
    ├── db.sqlite3
    ├── manage.py
    ├── population_script.sql
    ├── gitignore
    ├── dagbók.txt
    └── requirements.txt
```
__Programming Rules__
Below are listed a few rules that will be followed during the development phase of this
project. These rules will help the project look cohesive, clean, and readable.
HTML:
   1. Use semantic HTML tags to improve the accessibility and readability of the code.
   2. Use lowercase letters for all HTML tags and attributes.
   3. Do not use any inline styles or scripts.
CSS:
   4. Use a consistent naming convention for CSS classes.
   5. Use shorthand properties to simplify the code and reduce redundancy.
Python:
   7. All functions and classes will have a docstring that explains their purpose.
   8. All names of variables should be unique and descriptive.
   10. Use exceptions instead of returning error codes.
   11. Avoid using global variables.
JavaScript:
   13. Use arrow functions to simplify code and avoid binding issues.
   14. Use the === operator for strict equality comparisons
All programming languages:
   15. A simple code is a readable code, shorter and simple functions are better.
   16. There should be a minimum of two lines of whitespace between functions to
   separate code.
   17. If a line of code is to be complicated, a comment shall be added to explain it.
   18. Git merge to master should be reviewed by another team member before the
   merge.
   19. All functions, classes and variables will have a good and descriptive name.
   Team members should either work together on one computer, or on separate and
   new branches, pulled from master to minimize mishaps

_Include Credits:_
Pizza Lair was created by:

    Ágústa Björk Sch. Bergsveinsdóttir - agustabb
    Guðbjörg E. Sigurjósndóttir - GElisabet
    Marteinn Lundi Kjartansson - marteinnlundi

Thank you for using Pizza Lair!
