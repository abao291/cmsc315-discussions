"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Course:
    """Represent a university course offered to students"""

    # Class variable shared by all courses
    institution_type = "University"

    def __init__(self, course_name, credits):
        """Initialize a course with a name and credit value"""

        # Instance variables
        self.course_name = course_name
        self.credits = credits

    def display_info(self):
        """Display information about the course"""
        print(f"Course Name: {self.course_name}")
        print(f"Credits: {self.credits}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.


class OnlineCourse(Course):
    """Represent an online university course"""

    # Class variable
    delivery_method = "Online"

    def __init__(self, course_name, credits, platform, instructor):
        # Initialize inherited instance variables
        super().__init__(course_name, credits)

        # New instance variables
        self.platform = platform
        self.instructor = instructor
        self.students = []

    # New method
    def display_platform(self):
        """Display the platform used for the online course"""
        print(f"Course Platform: {self.platform}")


    # Student-created extension
    def enroll_student(self, student_name):
        """Enroll a student in the online course"""

        # Validate student name
        if not isinstance(student_name, str) or not student_name.strip():
            raise ValueError("Student name must be a nonempty string")

        student_name = student_name.strip()

        # Prevent duplicate enrollments
        if student_name in self.students:
            raise ValueError("Student is already enrolled")

        # Add student to the course
        self.students.append(student_name)


    # Override parent method
    def display_info(self):
        """Display information about the online course"""
        super().display_info()
        print(f"Delivery Method: {self.delivery_method}")
        print(f"Platform: {self.platform}")
        print(f"Instructor: {self.instructor}")



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.


def demonstrate_namespaces():
    """Demonstrate class and instance namespaces"""

    print("\n=== Namespace Demonstration ===")

    # Create two online course objects
    course1 = OnlineCourse("Data Structures", 3, "Canvas", "Dr. Smith")
    course2 = OnlineCourse("Computer Networks", 4, "Blackboard", "Dr. Johnson")

    # Access class variable through the class
    print("\nClass Variable Access:")
    print(f"OnlineCourse.delivery_method: {OnlineCourse.delivery_method}")

    # Access class variable through an object
    print(f"course1.delivery_method: {course1.delivery_method}")

    # Add an attribute to only one object
    course1.semester = "Fall 2026"

    # Display instance namespaces
    print("\nInstance Namespaces:")
    print(f"course1: {course1.__dict__}")
    print(f"course2: {course2.__dict__}")

    # Display class namespace
    print("\nClass Namespace:")
    print(f"Class Variable: {OnlineCourse.delivery_method}")
    print(f"Class Attributes: {list(OnlineCourse.__dict__.keys())}")



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.


def demonstrate_copying():
    """Demonstrate shallow and deep copying"""

    print("\n=== Copy Demonstration ===")

    # Create an online course object
    original = OnlineCourse("Data Structures", 3, "Canvas", "Dr. Smith")

    # Add a list of enrolled students
    original.students = ["Andy", "Brad", "Chuck"]

    # Create shallow and deep copies
    shallow = copy(original)
    deep = deepcopy(original)

    # Modify the original object's nested list
    original.students.append("David")

    # Display the original object and copies
    print("\nOriginal Course:")
    print(original.__dict__)

    print("\nShallow Copy:")
    print(shallow.__dict__)

    print("\nDeep Copy:")
    print(deep.__dict__)

    # Shallow copies share references to nested mutable objects
    # Deep copies create independent copies of nested mutable objects



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


def main():
    """Create and test course objects"""

    print("=== Unit 1 OOP Assignment ===")

    # Create and test parent object
    print("\n=== Parent Course ===")
    course1 = Course("Introduction to Programming", 3)
    course1.display_info()

    # Create and test child object
    print("\n=== Online Course ===")
    online1 = OnlineCourse("Data Structures", 3, "Canvas", "Dr. Smith")
    online1.display_info()

    # Call child class method
    print("\n=== Course Platform ===")
    online1.display_platform()


    # Demonstrate student-created extension
    print("\n=== Student-Created Extension ===")

    print("Before enrollment:", online1.students)

    online1.enroll_student("Andy")
    online1.enroll_student("Brad")

    print("After enrollment:", online1.students)

    # Test duplicate enrollment
    try:
        online1.enroll_student("Andy")
    except ValueError as error:
        print("Invalid enrollment handled:", error)

    # Demonstrate namespaces and copying
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()

