# Unit 1: Python OOP, Namespaces, and Copying

## Project Overview

For this assignment, I created a simple university course management program to explore **object-oriented programming (OOP)** concepts in Python. My goal was to demonstrate how inheritance, namespaces, and shallow and deep copying worked through a practical example.

I also added a student enrollment feature as my student-created extension.

## Class Design

I organized my program around two classes: `Course` and `OnlineCourse`.

### Parent Class: Course

I created the `Course` class to represent a university course and store its basic information.

The class included:

- A class variable called `institution_type`
- Two instance variables: `course_name` and `credits`
- A constructor (`__init__()`) to initialize course information
- A `display_info()` method to display the course name and credits

### Child Class: OnlineCourse

I created the `OnlineCourse` class as a child class that inherited from `Course`.

Since online courses have additional information, I included:

- A class variable called `delivery_method`
- Additional instance variables: `platform`, `instructor`, and `students`
- An overridden `display_info()` method to display information specific to online courses
- A `display_platform()` method to display the learning platform

By using inheritance, I was able to reuse the functionality of the parent class without having to rewrite the same code in the child class.

## Namespace Demonstration

For the namespace demonstration, I created a function called `demonstrate_namespaces()`.

I created two `OnlineCourse` objects representing different courses and accessed the `delivery_method` class variable through both the class itself and an individual object.

I also added a `semester` attribute to only one of the objects after it was created. This helped demonstrate how individual objects could have different instance attributes even when they belonged to the same class.

Finally, I used the `__dict__` attribute to display each object's namespace and the attributes defined in the `OnlineCourse` class.

## Shallow and Deep Copying

To demonstrate shallow and deep copying, I created a function called `demonstrate_copying()`.

I started by creating an `OnlineCourse` object with a list of enrolled students. I then used Python's `copy()` and `deepcopy()` functions to create shallow and deep copies of the original object.

After creating the copies, I added another student to the original course's student list and compared the results.

I observed that:

- **Original object:** The student list included the newly added student
- **Shallow copy:** The student list also included the new student because it shared the same list as the original
- **Deep copy:** The student list remained unchanged because it had its own independent copy

This demonstration helped me better understand how shallow and deep copying behaved differently when working with mutable data.

## Student-Created Extension

For my student-created extension, I decided to add an `enroll_student()` method to the `OnlineCourse` class.

I wanted to give the program some additional functionality beyond simply displaying course information.

The method allowed students to be enrolled in an online course. I also included several checks to make the enrollment process more reliable:

- **Input validation:** I checked that student names were valid, nonempty strings
- **Duplicate prevention:** I prevented students from being enrolled more than once
- **Error handling:** I used a `ValueError` to identify invalid enrollment attempts

To test my extension, I enrolled two students, Andy and Brad, into an online course. I then attempted to enroll Andy a second time to confirm that the program correctly rejected duplicate enrollments.

### Extension Output

```text
=== Student-Created Extension ===
Before enrollment: []
After enrollment: ['Andy', 'Brad']
Invalid enrollment handled: Student is already enrolled
```

## Running the Program

I ran the program from the repository's root directory using the following command:

```bash
python3 unit1_oop/unit1_discussion.py
```

In the `main()` function, I created objects from both the parent and child classes, demonstrated inheritance and method overriding, tested my student enrollment extension, and called the namespace and copying demonstration functions.

## Results and Conclusion

After completing and testing my program, I was able to demonstrate the main OOP concepts covered in this assignment.

- **Inheritance:** I reused functionality from the `Course` class in the `OnlineCourse` class
- **Namespaces:** I demonstrated how class variables and instance attributes were accessed and stored
- **Shallow and deep copying:** I observed how changes to mutable data affected different copies of an object
- **Student enrollment:** I implemented an additional feature that managed student enrollment and prevented duplicate entries

Overall, this assignment helped me become more familiar with organizing Python programs using classes and objects. I also gained a better understanding of how these concepts could make code easier to reuse and maintain.

I successfully tested the program, and it completed execution with **exit code 0**.