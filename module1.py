from math import sqrt
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

def counter(trial):
    count=[]
    home = list(range(1,15))
    away = list(range(15,27))
    for i in range(0,963):
        s = trial["startpasses"].iloc[i]
        d = []
    if s < 15:
        for j in away:
            d.append(mp.dist(trial["Player"+str(s)].iloc[i], trial["Player"+str(j)].iloc[i] ))
    else:
        for j in home:
            d.append(mp.dist(trial["Player"+str(s)].iloc[i], trial["Player"+str(j)].iloc[i] ))
    count.append(sum(k < 10 for k in d))
    return count