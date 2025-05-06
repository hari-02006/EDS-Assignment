# Taking input for number of courses
num_courses = int(input())

# Taking input for the marks in the courses
marks = list(map(int, input().split()))

# Check if the student has failed any course
if any(mark < 40 for mark in marks):
    print("Fail")
else:
    
    total_marks = sum(marks)
    aggregate_percentage = (total_marks / (num_courses * 100)) * 100
    
    
    print(f"Aggregate Percentage: {aggregate_percentage:.2f}")
    
    
    if aggregate_percentage > 75:
        print("Grade: Distinction")
    elif aggregate_percentage >= 60:
        print("Grade: First Division")
    elif aggregate_percentage >= 50:
        print("Grade: Second Division")
    elif aggregate_percentage >= 40:
        print("Grade: Third Division")

