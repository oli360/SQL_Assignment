from Who_Lived_The_Longest import question_one
from Top_Artists import question_two
from Most_Surface_Area import question_three
from Art_Aquired_During_Lifetime import question_four
from Data_Quality import question_five
import datetime
import sys


# function, if used saved all logs to a external out.txt file
def output_to_log(sys):
    orig_stdout = sys.stdout  # get original output
    f = open('out.txt', 'w')  # open out.txt file
    sys.stdout = f  # sets out put to out.txt file


# function used to print all questions
def my_submission():
    print('\n     This is my submission for JOLIEOI test:\n')
    question_one()
    print('\n')
    question_two()
    print('\n')
    question_three()
    print('\n')
    question_four()
    print('\n')
    question_five()


start_time = datetime.datetime.now()  # start timer to measure the execution time

#output_to_log(sys)    #uncomment to save outputs to log file
my_submission()  # calls submission function

end_time = datetime.datetime.now()  # retrieve the end time
time_diff = (end_time - start_time)  # calculate the difference between start time and end time
execution_time = time_diff.total_seconds()  # measure the execution tme in seconds
