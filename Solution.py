import csv, os
if __name__ =="__main__":
    
    # Read file using CSV module
    with open('Shares.csv', 'rb') as fileHand:
        fileReader = csv.reader(fileHand)
        fileList = list(fileReader)
    # loop for each company    
    for index in range(len(fileList[0][2:])):
        #company name
        print fileList[0][2:][index]
        # sort to get maximum value
        result = sorted(fileList[1:], key = lambda value: int(value[index+2]))[-1]# Take max from end
        #print year month value
        print result[0:2], result[index+2]
