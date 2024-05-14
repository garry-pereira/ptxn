from lib import *

acc = []
wanted_month = 1
input_file = "in.csv"
output_file = "out.csv"
unwanted = read_filter("filter.txt")

# note that you can comment out the parse/filter methods
read_in(acc, input_file) # first read input file
filter_month(acc, wanted_month) # then parse out desired month
filter_unwanted(acc, unwanted) # then filter out unwanted
write_out(acc, output_file) # then output to file
