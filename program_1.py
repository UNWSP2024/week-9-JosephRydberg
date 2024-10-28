#Item Counter Joseph Rydberg 10/28/2024

def count_file_lines():
    totalLines = 0
    for lines in open("names.txt", "r"):
        totalLines += 1
    print("Total names", str(totalLines))



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()