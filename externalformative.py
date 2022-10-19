#############
# Formative #
#############
def read_file():
    file = open('txtfile.txt', 'r')
    lines = file.read()
    print(lines)
    file.close()
def list_file():
    file = open('txtfile.txt', 'r')
    lines = file.readlines()
    print(lines)
    consoles = (lines[0])
    print("Some console electronics are", consoles)
    file.close()
def listlist():
    file = open('txtfile.txt', 'r')
    total = 9
    while total > 0:
        lines = file.readline()
        print("An electronic is", lines)
        total = total - 1
        
def main():
    read_file()
    list_file()
    listlist()
main()