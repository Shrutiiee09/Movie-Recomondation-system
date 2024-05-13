# Movie-Recomondation-system
Movie Recommendation System
Overview

This is a web application built using Django framework for recommending movies to users based on their preferences and behavior. The system utilizes collaborative filtering techniques to analyze user interactions and recommend movies that are likely to be of interest to them.

Features

User authentication: Sign up, login, and logout functionalities.

Movie recommendation: Recommends movies to users based on their past interactions and preferences.

Movie ratings: Users can rate movies to improve the recommendation accuracy.

Search functionality: Users can search for movies by title, genre, or other attributes.

Responsive design: Compatible with various devices and screen sizes.

Requirements
Python 3.x
Django 3.x
Pandas
Scikit-learn (for collaborative filtering)

Installation

Clone the repository to your local machine:

git clone https://github.com/Shrutiiee09/movie-recommendation.git

Navigate to the project directory:

cd movie-recommendation

Create a virtual environment:

python -m venv env

Activate the virtual environment:

On Windows:

env\Scripts\activate

On macOS and Linux:

source env/bin/activate

Install the required packages:

pip install -r requirements.txt

Usage

Run database migrations:

python manage.py migrate

Create a superuser to access the Django admin panel:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

Open a web browser and go to http://localhost:8000 to access the website.

Contributing
Contributions are welcome. Feel free to submit pull requests or open issues for any improvements or suggestions.

License
This project is licensed under the MIT License - see the LICENSE file for details.
Movie recomandation system using django
