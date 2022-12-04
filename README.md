# course-project-group-94
course-project-group-94 created by GitHub Classroom

Functionality:
The Nutrify app allows a user to input scanned labels to add to a list of purchases for a daily diet. The app uses a database to keep track of:
- Calories
- Fat
- Protein
- Sugar
- Carbohydrates
- And more

The user is able to set their preferences based on their preferred diet and biological data. The app will then keep track of whether the user’s inputted diet meets the criteria or not.


Motivation:
With new food products coming out at very fast rates, it can become tedious work to manually keep track of one’s diet or to continuously input to and update existing apps for the purpose of maintaining a diet.
Hence…
- Use the universality of food labels
- Work regardless of type of product
- Eventually would be quick and easy to scan labels on the go with PyTesseract


Backend Component:
Our Backend component will have a database that stores user input of images and nutritional information. 
We will primarily be using MySQL and SQLite for the text data storage like nutritional information and preferences for daily consumption and potentially include AWS SDK for image storage.
We are going to use OCR (Optical Character Recognition) from Pytesseract to convert an image to text by scanning the picture uploaded by the user.
Using Python and Django as our main backend development tools, we can retrieve nutritional information from the uploaded images.
We will be using Google Sign-In from Android SDK manager which will store user accounts.
The users can also interact with stored nutritional information to see if it is an appropriate food based on the user’s diet preferences. 

Frontend Component:
Our Frontend development will primarily be an Android app built with Kotlin.
The interface will prompt the user for permission to access the camera and will also allow the user to upload an image of a nutrition label and input their dietary preferences and nutritional goals. 
The UI will display a list of recommended food items and appropriate diet to follow based on the analysis of the diet and food label.
Lastly, the user can be directed to a list of research regarding certain food items by accessing the backend database from MySQL or SQLite.

Prerequisites for Use:
1. Tesseract executable installed on computer and in the path 
2. Java 11+
3. Python 3.7+ 
4. MySQL

Frontend Installation:
1. Open the frontend folder in Android Studio.
2. Build and run the app on the emulator 

Backend Installation:
1. Open the backend folder
2. Run pip install -r requirements.txt to install all python dependencies

Group Members:
Justin Chen - Frontend, Allen Guo - Backend, Andrew Zhao - Backend (Database), Maanav Agrawal - Backend
