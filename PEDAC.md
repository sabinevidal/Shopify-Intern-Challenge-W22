# Problem
https://docs.google.com/document/d/1eg3sJTOwtyFhDopKedRD6142CFkDfWp1QvRKXNTPIOc/edit

Create an image repository with tests. Focus on backend, allow for auth. Choose between SEARCH, ADD, DELETE and/or SELL/BUY functionality (choose 1/2).

Image repository, allowing for images to be added, stored, deleted and searched by tags.

-  Inputs: Image files with information (file name, image name, tags, description, username)
-  Output: Json messages confirming success/ explaining failure

## Problem Domain:
CRUD experience with image files.
Authorisation access to different controls.
Adding multiple images with different descriptions, tags etc.

## Implicit Requirements:
- Access control to CRUD images
    - users with different names and access rights to images
- Must be able to save/delete multiple images at once
    - with access control
- Uploading bulk images must include a point where tags and descriptions are added
- Search based on characterists, text, from similar images
- Must be able to select images to update/delete
    - update would be tags and description
- Testing of features

## Clarifying Questions:
1. What would the limit be of 'bulk' images?
    - check limit of SQLite
2. Would users create their own accounts?
    - not for this case, but have option for future.
3. What authorisation should be used? Auth0 is time-sensitive, other options less secure.
    - Use Flask-HTTPauth due to time contraints

## Mental Model:
App must allow for images (one, multiple, bulk) to be added to the repository linked to their username.
In order to update or delete images, user must be logged in and have access to rights for the selected images.

# Examples
**Examples / Test Cases / Edge Cases**

**Examples:**
-  Example 1:
User uploading one image 'example.jpg'
  -  Inputs: example.jpg, name: 'example image', description: 'An example image'
  -  Output: { message: "Success! your image 'example.jpg' has been uploaded"}
-  Example 2:
User uploading multiple images
  -  Inputs: {example1.jpg, name:"", description:""}, {example2.jpg, name:"", description: ""}
  -  Output: { message: "Success! your images 'example1.jpg' and 'example2.jpg' have been uploaded"}
- Example 3:
User updating an image
- Example 4:
User deleting one image
    - Inputs:
    - Outputs:
- Example 5:
User deleting multiple images
    - Inputs:
    - Outputs:


**Test Cases:**

**Edge Cases:**
- Corrupted image files?
- Empty names and descriptions
- In bulk uploads if one or more images fail validation( ie corrupt, wrong file), but others succeed


# Data Structure
**Models:**
User
- ID (int)
- name (String)
- bio(String)
- password ()
- Role (int)
- images (One-to-many relationship)

Image
- ID (int)
- filename ()
- name (String)
- description (String)
- tags (List of Strings)
- user_id (int, foreign key to User, one-to-one)

# Algorithm

**Login**
Use Flask-login
https://flask-login.readthedocs.io/en/latest/

**Upload image/s**
Using Flask-wtf

**Update image**
Using Flask-wtf

**Delete image/s**

**View images**
