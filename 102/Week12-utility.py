        #   Brynn Moncur
        #   CSCI 102 – Section D
        #   Week 12 - Utility using Git and Incremental Development
        #   References: 
        #   Time: 45 minutes

def load_file(file_name):
    file = open(file_name)
    list = file.readlines()
    file.close()
    return list

lines = load_file("week12tester.txt")
print("OUTPUT", lines)
