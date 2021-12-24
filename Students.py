import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
mathList = df["math score"].to_list()
readingList = df["reading score"].to_list()
writingList = df["writing score"].to_list()

mathMean = statistics.mean(mathList)
readingMean = statistics.mean(readingList)
writingMean = statistics.mean(writingList)
mathMedian = statistics.median(mathList)
readingMedian = statistics.median(readingList)
writingMedian = statistics.median(writingList)
mathMode = statistics.mode(mathList)
readingMode = statistics.mode(readingList)
writingMode = statistics.mode(writingList)
stdDevMath = statistics.stdev(mathList)
stdDevReading = statistics.stdev(readingList)
stdDevWriting = statistics.stdev(writingList)
print("Math mean ", mathMean)
print("Reading mean ", readingMean)
print("Writing mean ", writingMean)
print("Math median ", mathMedian)
print("Reading median ", readingMedian)
print("Writing median ", writingMedian)
print("Math mode ",mathMode)
print("Reading mode ",readingMode)
print("Writing mode ",writingMode)

math_first_std_dev_start, math_first_std_dev_end = mathMean-stdDevMath, mathMean+stdDevMath
math_second_std_dev_start, math_second_std_dev_end = mathMean-(2*stdDevMath), mathMean+(2*stdDevMath)
math_third_std_dev_start, math_third_std_dev_end = mathMean-(3*stdDevMath), mathMean+(3*stdDevMath)

math_list_of_data_first_std_dev = [result for result in mathList if result>math_first_std_dev_start and result<math_first_std_dev_end]
math_list_of_data_second_std_dev = [result for result in mathList if result>math_second_std_dev_start and result<math_second_std_dev_end]
math_list_of_data_third_std_dev = [result for result in mathList if result>math_third_std_dev_start and result<math_third_std_dev_end]

print("{}% of data for math lies within first std dev ".format(len(math_list_of_data_first_std_dev)*100/len(mathList)))
print("{}% of data for math lies within second std dev ".format(len(math_list_of_data_second_std_dev)*100/len(mathList)))
print("{}% of data for math lies within third std dev ".format(len(math_list_of_data_third_std_dev)*100/len(mathList)))

##

reading_first_std_dev_start, reading_first_std_dev_end = readingMean-stdDevReading, readingMean+stdDevReading
reading_second_std_dev_start, reading_second_std_dev_end = readingMean-(2*stdDevReading), readingMean+(2*stdDevReading)
reading_third_std_dev_start, reading_third_std_dev_end = readingMean-(3*stdDevReading), readingMean+(3*stdDevReading)

reading_list_of_data_first_std_dev = [result for result in readingList if result>reading_first_std_dev_start and result<reading_first_std_dev_end]
reading_list_of_data_second_std_dev = [result for result in readingList if result>reading_second_std_dev_start and result<reading_second_std_dev_end]
reading_list_of_data_third_std_dev = [result for result in readingList if result>reading_third_std_dev_start and result<reading_third_std_dev_end]

print("{}% of data for reading lies within first std dev ".format(len(reading_list_of_data_first_std_dev)*100/len(readingList)))
print("{}% of data for reading lies within second std dev ".format(len(reading_list_of_data_second_std_dev)*100/len(readingList)))
print("{}% of data for reading lies within third std dev ".format(len(reading_list_of_data_third_std_dev)*100/len(readingList)))

##

writing_first_std_dev_start, writing_first_std_dev_end = writingMean-stdDevWriting, writingMean+stdDevWriting
writing_second_std_dev_start, writing_second_std_dev_end = writingMean-(2*stdDevWriting), writingMean+(2*stdDevWriting)
writing_third_std_dev_start, writing_third_std_dev_end = writingMean-(3*stdDevWriting), writingMean+(3*stdDevWriting)

writing_list_of_data_first_std_dev = [result for result in writingList if result>writing_first_std_dev_start and result<writing_first_std_dev_end]
writing_list_of_data_second_std_dev = [result for result in writingList if result>writing_second_std_dev_start and result<writing_second_std_dev_end]
writing_list_of_data_third_std_dev = [result for result in writingList if result>writing_third_std_dev_start and result<writing_third_std_dev_end]

print("{}% of data for writing lies within first std dev ".format(len(writing_list_of_data_first_std_dev)*100/len(writingList)))
print("{}% of data for writing lies within second std dev ".format(len(writing_list_of_data_second_std_dev)*100/len(writingList)))
print("{}% of data for writing lies within third std dev ".format(len(writing_list_of_data_third_std_dev)*100/len(writingList)))




