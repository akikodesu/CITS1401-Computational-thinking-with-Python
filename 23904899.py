def readFile(csvfile):
    with open(csvfile, "r") as files:  # open the csvfile
        yearList = []  # create an empty list to store the lines match years and specific country
        readFiles = files.readlines()  # read every lines in csvfile and save it in a variable
    return readFiles

def main(csvfile, country):
    content = readFiles(csvfile)
    for lines in content[1:]:  # loop every line except header line
        lines = lines.strip().split(",")  # remove spaces in lines and split them using comma
        if 1981 <= lines[4] <= 2000 and lines[3] == country:  # compare if the actual parameter is match the condition
            yearList.append(lines)  # if it meets both conditions then append the lines into list

    empNum = []  # create an empty list to store number of employees
    for lines in yearList:  # loop every line under yearList
        empNum.append(lines[6])  # add number of employees into empList
        
    index_maxEmp = empNum.index(max(empNum))  # find the index of list which contains the max number of employees
    index_minEmp = empNum.index(min(empNum))  # find the index of list which contains the min number of employees

    maxEmp_org = empNum[index_maxEmp][1]  # find out the org name has max number of employees 
    minEmp_org = empNum[index_minEmp][1]  # find out the org name has min number of employees

    maxMin = [maxEmp_org, minEmp_org]


