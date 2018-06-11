# django-calculator

Learning Objectives
After completing this assignment, you should be able to:

Implement new features into Django applications
Understand how to use Djoser with the Django authentication system including:
Djoser/Django's Login/Logout Views
Djoser/Django's User creation form
Be able to create models that have a ForeignKey to a Custom Django User instance.
Normal Mode
Create a new project called django-calculator and implement the following features to the program.

Create an Operation model to your application and include all important fields relevant to tracking operation history.
operand_one, operand_two, operator, result, created (timestamp), owner (FK)
Create a REST url that allows a user to log in to your application
Create a REST url that allows a user to log out of your application
Create a REST url that allows a user to signup for your application
Create a REST url that allows a user to create a new operation for their user and that calculates the total of the operation and stores it on the model.
Create a REST url that allows a user to view all operations in the database.
[Hard] Have that view filter down by the currently logged in user to only show their operations they have created.
