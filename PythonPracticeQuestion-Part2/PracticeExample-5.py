#You have a log file as attached in sample input with various operations and time taken by each of them. Write a script to find the min and max time taken for each operation. Sample output is attached.
import pandas as pd
data = pd.read_csv("/home/mukul/PycharmProjects/ImportingData/PythonPracticeQuestion-Part2/operations.csv", header=None, names=['operation', 'Time'])
df = data.groupby('operation').agg([min, max])
print(df)