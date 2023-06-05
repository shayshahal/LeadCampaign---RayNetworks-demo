# LeadCampaign - RayNetworks demo

## Learning

This is a demo project to learn to technologies in ray networks:

-   Facebook Business API/SDK
-   Flask
-   Ariadne
-   SQLAlchemy
-   Alembic

For the project I was tasked with making an endpoint with flask that does the following:
**POST**: Create a Lead Form campaign.
**GET**: Gets all leads that have been entered in the last 24 hours.

At first, in order to fully understand what a Lead is and how it is structured and accessed in the Facebook API, I go to [Facebook's API docs](https://developers.facebook.com/docs/) and search for the word "Lead" in the search bar.
With a further read that also included searching through [Facebook-python-business-sdk Github](https://github.com/facebook/facebook-python-business-sdk/) and the examples in it I manage to understand how to programmatically create a new lead form.

Secondly, I use the following sources to create the **GET** request:

-   [SQLAlchemy docs](https://docs.sqlalchemy.org/)
-   [Flask-SQLalchemy docs](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
-   [Flask's docs on SQLalchemy with flask](https://flask.palletsprojects.com/en/2.3.x/patterns/sqlalchemy/)
-   [Alembic docs](https://alembic.sqlalchemy.org/en/latest/)
-   [flask-migrate docs](https://flask-migrate.readthedocs.io/en/latest/)

_note_: I skimmed through the big library's docs and mostly used the integrations with flask, I should probably read the actual SQLAlchemy and Alembic docs more thoroughly to get a better understanding on how things work.

## Pre-requisites

-   A facebook Page Id as env variable _PAGE_ID_
-   A facebook Page Access Token as env variable _ACCESS_TOKEN_

## Usage

Create a new venv:

```
> py -3 -m venv .venv
```

Activate venv:

```
> . .venv/bin/activate
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

Create a .env file:

```
|--demo
|-- app.py
|-- .env <----
```

Write the required environment variables in the .env:

```
PAGE_ID = '<YOUR-PAGE-ID-HERE>'
ACCESS_TOKEN = '<YOUR-ACCESS-TOKEN-HERE>
```

Run the script:

```
python app.py
```

Both requests should go to `http://localhost:3000/leads-campaign`.
