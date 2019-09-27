# Peewee Example

API example using Flask, Peewee and Nomade.

Set the following environment variable:

```bash
export CONNECTION_STRING=sqlite:///peewee_app.db
```

Create and activate a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
```

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Run the migrations:

```bash
nomade upgrade head
```

Run the app with:

```bash
python src/main.py
```

Access the users through:

```bash
http://127.0.0.1:5000/users
```
