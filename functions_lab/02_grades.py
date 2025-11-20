grade_data = float(input())

def grade_in_words(grade: float):
    result = ''
    if 2.00 <= grade <= 2.99:
        result = 'Fail'
    elif 3.00 <= grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= grade <= 4.49:
        result = 'Good'
    elif 4.50 <= grade <= 5.49:
        result = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        result = 'Excellent'
    
    return result

final_grade = grade_in_words(grade_data)
print(final_grade)