# creating  and  manipulating a dictionary
student_scores ={
    "Alice":85,
    "Bob":92,
    "charlie":78

}                          
#adding a new entry
student_scores["Diana"] = 95

#Dictionary comprehension: create a new dict with only passing grades(>80)
passing_scores =  {student_scores for student, score in student_scores.items() if score > 80}
print("passing scores:", passing_scores)}
