import pysnooper

tp = ('key', 'laptop', 'cloth', 212)
total_string = 0
for x in tp:
    if isinstance(x, str):
        total_string = 1 + total_string
print(total_string)


@pysnooper.snoop()
def add():
    final_result = 0
    for i in range(1,11):
        final_result = i + final_result
    return final_result


print(add())

"""--------------------------------------------"""

students = [{"student1":{"maths":50,"physics":60,"chemistry":70}},{"student2":{"maths":54,"physics":66,"chemistry":75}},{"student3":{"maths":60,"physics":63,"chemistry":67}},{"student4":{"maths":90,"physics":40,"chemistry":50}}]

#student_name got this_many_marks/300
for student_info in students:
    for k,v in student_info.items():
        total_mark = 0
        percentage = 0
        for marks in v.values():
            total_mark = marks + total_mark
        percentage = total_mark/300 * 100
        print("{} got {} percentage.".format(k,round(percentage)))
#         print(k,"---------",v.values())


