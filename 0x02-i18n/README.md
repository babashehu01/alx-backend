# i18n - Internationalization in Flask

This project "i18n - Internationalization in Flask" focuses on implementing internationalization and localization features in a Flask web application. It will teach you how to parametrize Flask templates to display different languages, infer the correct locale based on URL parameters, user settings, or request headers, and localize timestamps.

By: Emmanuel Turlay, Staff Software Engineer at Cruise
Project Timeline

    Start Date: Aug 1, 2023, 6:00 AM
    End Date: Aug 2, 2023, 6:00 AM
    Checker Release: Aug 1, 2023, 12:00 PM
    Manual QA Review: Request it when you are done with the project
    Auto Review Launch: At the deadline

Learning Objectives

Upon completing this project, you will gain expertise in the following topics:

    Parametrizing Flask templates to display different languages
    Inferring the correct locale based on URL parameters, user settings, or request headers
    Localizing timestamps

Requirements

Project Structure and Tasks

The project is divided into multiple tasks, each focusing on specific i18n concepts. Here is an overview of the tasks:

    Basic Flask app: Set up a basic Flask app with a single route and an index.html template.
    Basic Babel setup: Install Flask-Babel and configure it with available languages.
    Get locale from request: Create a function to determine the best match for the supported languages based on the request.
    Parametrize templates: Use _ or gettext function to parametrize templates with message IDs.
    Force locale with URL parameter: Implement a way to force a particular locale by passing the locale parameter to the app's URLs.
    Mock logging in: Mock a user login system and display messages based on the user's login status.
    Use user locale: Change the get_locale function to use a user's preferred locale if supported.
    Infer appropriate time zone: Implement a function to infer the appropriate time zone based on URL parameters, user settings, or request headers.

How to Run the App

    Install the required packages (Flask, Flask-Babel, pytz, etc.).
    Navigate to the project directory.
    Run the app using the following command:

    php

    $ python <app_file.py>
