import pandas as pd

score=pd.read_excel("score.xlsx")

sum=score['学分'].sum()

grade_sum=0
for i in range(1,len(score)):
    item=score.iloc[i]
    grade=item['成绩']
    if type(grade) is int or type(grade) is float:
        if grade>=90:
            grade=4.0
        elif grade>=80:
            grade=3.0
        elif grade>=70:
            grade=2.0
        elif grade>=60:
            grade=1.0
        else:
            grade=0
    else:
        if grade=='优':
            grade=4.0
        elif grade=='良':
            grade=3.0
        elif grade=='中':
            grade=2.0
        elif grade=='及格':
            grade=1.0
        else:
            grade=0.0

    grade_sum+=grade*item['学分']

GPA=grade_sum/sum
print('{:.2f}'.format(GPA))