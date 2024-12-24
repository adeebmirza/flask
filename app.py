from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define a route and its corresponding request handler
@app.route('/')
def home():
    return "Hello, Flask! Adeeb is the owner of this app...."


# Run the Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True,port=5000)
