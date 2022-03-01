import pandas as pd  # import pandas to work with data/dataframes

# Asking for file name so that this may be used with other files
file1 = input("Please enter the file name you would like to use: ")
# Converting the csv file to a pandas dataframe for readability and
# so the script can work with the data more easily
df = pd.read_csv(file1)
num_columns = int(input("How many columns in the data set? "))
# Assigning arbitrary column labels, so I can specify which column I need
column_labels = []
# Just labeling columns "data1", "data2", etc.
for i in range(1, num_columns + 1):
    column_labels.append(f"data{str(i)}")
df.columns = column_labels
# Converting column 'data9' (names) to a list called list_of_names
list_of_names = df['data9'].to_list()
# Asking for text file to use to compare for and remove common names from the list_of_names
file2 = input("Please enter the file name of the comparison file: ")
common_names = open(file2, 'r')
list_of_commons = []
# Scroll through each line/row of the text file
# Strip leading and ending spaces
# Append each common name to the list list_of_commons for comparison
for line in common_names:
    stripped_line = line.strip()
    list_of_commons.append(stripped_line)
# Make sure the names are all first letter capitalized
for i in range(len(list_of_names)):
    list_of_names[i] = list_of_names[i].capitalize()
# Compare original names to common names and if there is a match,
# remove from the list_of_names
for name in list_of_names:
    if name in list_of_commons:
        list_of_names.remove(name)
output1 = input("Please enter tha name of the text file you would like to use for export: ")
# Export remaining names in list_of_names to text file
with open(output1, 'w') as f:
    for name in list_of_names:
        f.write(name.capitalize())
        f.write('\n')