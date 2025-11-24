students = {
    "students": [ "Angela", "Mutai", "Mwangi" ],
    "scores": [ 50,60,70]
}
# Loopiing through dictionaries
# for (key,value) in students.items():
#     print(value)
# DataFrame
import pandas
df = pandas.DataFrame(students)
for (index, row) in df.iterrows():
    print(f"{index} : {row.students} scored {row.scores}" )
