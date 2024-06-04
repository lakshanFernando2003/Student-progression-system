'''A function i created to write all the lists i have created to a textfile called "CWTEXTFILE.txt" '''
def save_data(Data, filename='CWTEXTFILE.txt'):
        with open(filename, 'w') as file:
            for item in Data:
                file.write(f"{item[3]} - {item[0]}, {item[1]}, {item[2]}\n")
'''A function i created to read the above textfile'''
def read_data(filename='CWTEXTFILE.txt'):
        with open(filename, 'r') as file:
            content = file.read
            return content()# returning the file
