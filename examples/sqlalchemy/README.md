# SQLAlchemy Example

API example using Flask, SQLAlchemy and Nomade.

Create the database:

```bash
create database sqlalchemy_test;
```

Set the following environment variable:

```bash
export CONNECTION_STRING="mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy_test"
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
