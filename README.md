# Shopify Intern Challenge W22
 
 **!!Work in Progress!!** 
 [PEDAC.md](https://github.com/sabinevidal/Shopify-Intern-Challenge-W22/blob/main/PEDAC.md) for outline of problem and process.
 
 ## Application the W22 Shopify internship 
 **Task:** [Build an Image repository] (https://docs.google.com/document/d/1eg3sJTOwtyFhDopKedRD6142CFkDfWp1QvRKXNTPIOc/edit)
Demonstrates proficiency in the following areas:

* Data modeling
    * Architect relational database models in Python and SQLite
    * Utilize SQLAlchemy to conduct database queries
* API Architecture and Testing
    * Follow RESTful principles of API development using Flask
    * Structure endpoints to perform CRUD operations, as well as error handling
    * Demonstrate validity of API behavior using the unittest library
* Third Party Authentication (TODO)
    * Configure Role Based Authentication and roles-based access control (RBAC) in a Flask application utilizing Auth0
    * Decode and verify JWTs from Authorization headers
* Deployment
    * API will be hosted (TODO)
* Front End (TODO)
    * Design and create a frontend which works with the API and redirects the user to Auth0 for login.
    * Uses Flask and Jinja Templates

## 

## Getting Started
### Installing Dependencies

Developers should have Python3, and pip3 installed

### Frontend dependencies
**!!TODO!!**

### Backend Dependencies 
#### Virtual Environment
In the main directory run:
```bash
python -m venv venv
```
To activate the virtual environment, in the main directory run:
```bash
souce venv/bin/activate
```
#### Dependencies
Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```
## Running Your Frontend in Dev Mode
**!!TODO!!**

## Database Setup
**!!TODO!!**

## Running the server

From within the main directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
imagerepo run
```

## Testing
**!!TODO!!**

## API Reference

### Getting Started
**!!TODO!!**
Base URL: Currently this application is only hosted locally. The backend is hosted at (to do)
Authentication:
In order to use the API users need to be authenticated. Users can either have a user or admin role. An overview of the API can be found below as well. There's also a Postman Collection(to do) provided.


### Error Handling (to do)

There are four types of errors the API will return`;
- 400 - bad request
- 401 - unauthorised
- 404 - resource not found
- 422 - unprocessable
- 500 - internal server error

## API

### Roles and Permissions

#### Admin

Admin have the following permissions:

* get:image
* post:image
* delete:image

email: admin@email.com
password: 
user_id: 

#### User
 
 User has the following permissions:
 
 * get:image

### Endpoints
#### GET '/'
- Returns the home page and a welcome message

#### GET '/upload'
- returns the upload image form

#### POST '/upload/images'
- Uploads a new image (or images) to the database
- Requires admin account authorisation
- TODO

#### GET '/update'
- returns the upload image form for updating an image
- 

#### POST '/update'
- updates the image on the database with any updated information
- Requires admin account authorisation
- TODO

#### GET and POST '/register'
- creates a new user
- TODO
