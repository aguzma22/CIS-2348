# Anthony Guzman              Homework #2                          CIS 2348

# Months need to be set with their proper number for dates
month_list={"january":"1","february":"2", "march": "3","april":"4","may":"5","june":"6",
"july":"7","august":"8","september":"9","october":"10","november":"11","december":"12"}

# Input_file will open the file and output _file will obtain the copy of the final output of the code.
input_file=open('C:\\Users\\Public\\inputDates.txt','r')
output_file=open('C:\\Users\\Public\\outputDates.txt','w')

# This will split the dates in order by month, date, and year
for each in input_file:
    if each!="-1":
        lis= each.split()
        if len(lis) >=3:
            month=lis[0]
            day=lis[1]
            year=lis[2]

# Will retract from the month_list and turn dates into numbers separating them with /
            if month.lower() in month_list:
                comma=day[-1]
                if comma==',':
                    day=day[:len(day)-1]
                    month_number=month_list[month.lower()]
                    ans=month_number+"/" + day + "/" + year

# The copy is finalized to the output_file
                    output_file.write(ans)
                    output_file.write("\n")

output_file.close()
input_file.close()