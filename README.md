# todo-back
python -m venv venv
source venv/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser


python3 manage.py runserver

# 1. Login to /admin/ with your superuser

# 2. Testing, open /graphql/ - Open two tabs
```
mutation {
  updateTodo(dateTime: "2022-12-12T12:00:00", place: "lib", title: "Borrow a book2", id: 1) {
    success
  }
}
```



```
subscription {
  notifyTodo(username: "chongyao") {
    payload
    username
  }
}
```
