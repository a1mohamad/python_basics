import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    my_input = str(input_file_name)
    my_output = str(output_file_name)
    with open(my_input) as h:
        reader = csv.reader(h)
        outputs =''
        for row in reader:
            name = row[0]
            grade = []
            for item in row[1:]:
                grade.append(float(item))
            output = '%s,%f\n' %(name, mean(grade))
            outputs += output
            
        w = open(my_input, 'w')
        w.write(outputs) 
        w.close()

calculate_averages('./grades.csv', './results.csv')

def calculated_sorted_average(input_file_name, output_file_name):
    my_input = str(input_file_name)
    my_output = str(output_file_name)
    with open(my_input) as h:
        reader = csv.reader(h)
        outputs =''
        averages =dict()
        for row in reader:
            name = row[0]
            grade = []
            for item in row[1:]:
                grade.append(float(item))
            average = mean(grade)
            averages[name] = average
        sorted_averages = dict(sorted(averages.items(), key=lambda item:item[::-1]))
        for item in sorted_averages.keys():
            one = item
            two = sorted_averages[item]
            output = '%s,%f\n' %(one, two)
            outputs += output
            
        w = open(my_output, 'w')
        w.write(outputs)
        w.close()

calculated_sorted_average('./grades.csv', './results.csv')

def calculated_three_best(input_file_name, output_file_name):
    my_input = str(input_file_name)
    my_output = str(output_file_name)
    with open(my_input) as h:
        reader = csv.reader(h)
        outputs = ''
        averages = dict()
        for row in reader:
            name = row[0]
            grade = []
            for item in row[1:]:
                grade.append(float(item))
            average = mean(grade)
            averages[name] = average
        sorted_averages = dict(sorted(averages.items(), key=lambda item: item[::-1] ,reverse=True))
        for k, v in list(sorted_averages.items())[:3]:
            one, two = k, v
            output = '%s,%f\n' %(one, two)
            outputs += output
        w = open(my_output, 'w')
        w.write(outputs)
        w.close()

calculated_three_best('./grades.csv', './results.csv')

def calculated_three_worst(input_file_name, output_file_name):
    my_input = str(input_file_name)
    my_output = str(output_file_name)
    outputs = ''
    averages = []
    with open(my_input) as h:
        reader = csv.reader(h)
        for row in reader:
            grade = []
            for item in row[1:]:
                grade.append(float(item))
            average = mean(grade)
            averages.append(average)
            averages.sort()
        for three_worst in averages[:3]:
            output = '%f\n' %three_worst
            outputs += output
        w = open(my_output, 'w')
        w.write(outputs)
        w.close()

calculated_three_worst('./grades.csv', './results.csv')

def calculate_average_of_averages(input_file_name, output_file_name):
    my_input = str(input_file_name)
    my_output = str(output_file_name)
    outputs = ''
    averages = []
    with open(my_input) as h:
        reader = csv.reader(h)
        for row in reader:
            grade = []
            for item in row[1:]:
                grade.append(float(item))
            average = mean(grade)
            averages.append(average)
        final_result = mean(averages)
        output = '%f' %final_result
        outputs += output
        w = open(my_output, 'w')
        w.write(outputs)
        w.close()
        
calculate_average_of_averages('./grades.csv','./results.csv')
            

            
    
    