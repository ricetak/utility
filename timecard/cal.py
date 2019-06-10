# coding: utf-8
import csv
import datetime

f = open("./data/timecard.tsv", 'r', encoding="utf-8")
tsv = csv.reader(f, delimiter = '\t')

# format : [date]\t[note]\t[start_time]\t[]\t[end_time]

line_str = "-----------------------------------"

print()
print(line_str)

total_overtime_minute = 0
for row in tsv:
    if row == []:
        continue

    target_date_str = row[0]
    start_time_str = row[2]
    end_time_str = row[4]

    start_time = datetime.datetime.strptime(start_time_str, '%H:%M')
    end_time   = datetime.datetime.strptime(end_time_str, '%H:%M')
        
    regular_minute = 9 * 60;
    overtime_minute = (end_time - start_time).total_seconds() / 60 - regular_minute
    overtime_minute = int(overtime_minute)
    
    total_overtime_minute += overtime_minute
    
    overtime_minute_str  = str(overtime_minute)
    overtime_minute_str = overtime_minute_str.rjust(5, " ")
    print(target_date_str, start_time_str, "-" , end_time_str, ":", overtime_minute_str)
    
total_overtime_minute_str = str(total_overtime_minute)

print(line_str)
print(total_overtime_minute_str.rjust(33, " "))
print(line_str)
print()

f.close()

