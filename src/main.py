from lib import *

acc = []
wanted_month = 1
input_file = path("discover.csv")
[if_date, if_desc, if_amount] = ["Post Date", "Description", "Amount"]
output_file = path("out.csv")
unwanted = read_filter(path("filter.txt"))

# note that you can comment out the parse/filter methods
read_in(acc, input_file, if_date, if_desc, if_amount) # first read input file
filter_month(acc, wanted_month, if_date) # then parse out desired month
filter_unwanted(acc, unwanted, if_desc) # then filter out unwanted
write_out(acc, output_file) # then output to file
