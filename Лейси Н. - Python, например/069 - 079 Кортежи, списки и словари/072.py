
school_subjects = ['physics', 'mathematics', 'history', 'biology']
print(school_subjects)
del_subject = str(input('Which of these subject you dont like? '))
index_subjects = school_subjects.index(del_subject)
del school_subjects[index_subjects]
print(sorted(school_subjects))
