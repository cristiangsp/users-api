# Requirements
In order to follow the workshop, please come with your laptop and the following requirements installed:

- Python 3.7+
- You favourite IDE (vim, PyCharm, Visual Studio Code, ...)
- Your favourite tool for making HTTP Requests (curl, Postman, Paw, ...)

# Installation

Clone this repository:
```
$> git clone https://github.com/cristiangsp/users-api.git .
```

Let's create a virtual environment and let's activate it.
```
$> python3 -m venv vnev
$> . venv/bin/activate
```

Let's install the project dependencies:
```
$> pip3 install -r requirements.txt
```

# Run the project
To run the users API application execute the runserver.sh script:
```
$> make run
```

Now you can make a request to:
```
http://127.0.0.1:5000/users
```

If everything is set up properly you should see an empty result:
```
[]
```

# Slides
Find next the slides to follow the workshop: [Refactoring a web application with Python](https://www.slideshare.net/cristiangsp/refactoring-a-web-application-with-python)
