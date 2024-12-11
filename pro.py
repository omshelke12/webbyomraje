import streamlit as st

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C+'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

# Function to calculate overall grade based on multiple subjects
def calculate_overall_grade(subject_grades):
    avg_marks = sum(subject_grades) / len(subject_grades)
    return calculate_grade(avg_marks)

# Streamlit UI
st.title('Student Grading System')

# Instructions
st.markdown("""
### Enter your marks for each subject.
The system will calculate your final grade based on the marks you provide.
""")

# Input fields for marks of different subjects
subject_names = ['Mathematics', 'Science', 'English', 'History', 'Geography']
marks = {}

for subject in subject_names:
    marks[subject] = st.number_input(f'Enter marks for {subject}', min_value=0, max_value=100, step=1)

# Calculate individual grades
grades = {subject: calculate_grade(mark) for subject, mark in marks.items()}

# Display individual grades
st.subheader("Individual Grades:")
for subject, grade in grades.items():
    st.write(f"{subject}: {grade}")

# Calculate and display the overall grade
overall_grade = calculate_overall_grade(list(marks.values()))
st.subheader(f"Overall Grade: {overall_grade}")

# Optiona
