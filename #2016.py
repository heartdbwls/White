#2016
def solution(a, b):
    month_list=[0,31,29,31,30,31,30,31,31,30,31,30]
    day_rest={0:"THU",1:"FRI",2:"SAT",3:"SUN",4:"MON",5:"TUE",6:"WED"}
    day_total = sum(month_list[0:a])+b
    i=day_total%7
    answer = day_rest[i]
    return answer
    