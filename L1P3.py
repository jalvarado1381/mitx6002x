import pylab

def loadFile():
    inFile = open('julyTemps.txt')
    highl = []
    lowl = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            highl.append(int(fields[1]))
            lowl.append(int(fields[2]))
    inFile.close()
    return(highl,lowl)

def producePlot(lowTemps, highTemps):
    diffTemps = []
    for i in range(len(lowTemps)):
        diffTemps.append(highTemps[i - 1] - lowTemps[i - 1])
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
h,l = loadFile()
producePlot(l, h)
    
    


