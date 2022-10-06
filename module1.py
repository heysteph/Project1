from math import sqrt
import module1 as mp

def dist(a,b):
    dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return dist
            
#def mergexy(trial):
 #   for i in range(1,27):
  #      trial["Player{}".format(i)] = tuple(zip(*trial[['Player{}_x','Player{}_y']].values.T)).format(i)
   # return trial

def mergexy(trial):
    for x in range(1,27):
        trial["Player"+str(x)] = tuple(zip(*trial[['Player'+str(x)+'_x','Player'+str(x)+'_y']].values.T))
    return trial

def types(passes):
    classes=[]
    for value in passes:
        if value == "REG":
            classes.append(1)
        elif value =="HEAD":
            classes.append(2)
        elif value =="CROSS":
            classes.append(3)
        elif value =="DEEP BALL":
            classes.append(4)
        else:
            classes.append(5)
    return classes

def normal(data):
    newval=[]
    maxi = max(data)
    for oldval in data:
        newval.append(oldval/maxi)
    return newval