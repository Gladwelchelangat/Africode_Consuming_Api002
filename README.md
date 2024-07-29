Flask JSONPlaceholder API Viewer
This project is a simple Flask application that fetches and displays data from the JSONPlaceholder API. It includes several routes to display posts, comments, albums, photos, todos, and users.

Features
Home Page: A welcome page rendered from index.html.
Posts Page: Fetches and displays posts from the JSONPlaceholder API.
Comments Page: Fetches and displays comments from the JSONPlaceholder API.
Albums Page: Fetches and displays albums from the JSONPlaceholder API.
Photos Page: Fetches and displays photos from the JSONPlaceholder API.
Todos Page: Fetches and displays todos from the JSONPlaceholder API.
Users Page: Fetches and displays users from the JSONPlaceholder API.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/flask-jsonplaceholder-viewer.git
cd flask-jsonplaceholder-viewer
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Running the Application
Run the Flask application:

bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5002/ to view the home page.

Project Structure
app.py: The main Flask application file that defines routes and handles requests to the JSONPlaceholder API.
templates/: Contains HTML templates for rendering different pages.
index.html: The home page template.
posts.html: Template for displaying posts.
comments.html: Template for displaying comments.
albums.html: Template for displaying albums.
photos.html: Template for displaying photos.
todos.html: Template for displaying todos.
users.html: Template for displaying users.
requirements.txt: Lists the required Python packages.
API Endpoints
/: Home page.
/posts: Displays posts fetched from https://jsonplaceholder.typicode.com/posts.
/comments: Displays comments fetched from https://jsonplaceholder.typicode.com/comments.
/albums: Displays albums fetched from https://jsonplaceholder.typicode.com/albums.
/photos: Displays photos fetched from https://jsonplaceholder.typicode.com/photos.
/todos: Displays todos fetched from https://jsonplaceholder.typicode.com/todos.
/users: Displays users fetched from https://jsonplaceholder.typicode.com/users.


