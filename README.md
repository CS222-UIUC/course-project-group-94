# course-project-group-94
course-project-group-94 created by GitHub Classroom

Pitch:
People all across the globe who are interested in fitness and nutrition pay very close attention to what they consume.
Our Nutrify application makes it easier for people to determine what food items are healthy to eat for their desired diet just from an input of a food label image and are also given recommendations for how to achieve their fitness goals using an algorithm that calculates calorie deficit or calorie surplus and suggests a diet to follow by diversifying vegetables and fruits.

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
