# Import the Flask class from the flask module
# (notice the capitalization, classes start with a capital letter, modules do not)
from flask import Flask

# Create an app by creating a new Flask object
# Pass in the __name__ variable
app = Flask(__name__)

# This line is called a "decorator", don't worry too much about them
# Decorators are how Flask defines routes
# you don't need to know a lot about them, just remember that how you make a route
@app.route('/')
# Define the function that gets called when that above route gets a request
# This functions need to immediately follow the decorator
def return_something():
    # Here's where you logic would go if you needed any
    # Return something, usually a string
    return "here's some content coming from the webserver"


# If we run this module directly (not importing it from somewhere else)
if __name__ == '__main__':
    # Call the run() method of the Flask object (that we named app)
    # Pass in '0.0.0.0' to tell it to run on localhost
    # Default port is 5000, which is fine for us
    app.run('0.0.0.0')
