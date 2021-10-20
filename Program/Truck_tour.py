def truckTour(petrolpumps):
    index=0
    distance=0
    for i in range(len(petrolpumps)):
        distance+=(petrolpumps[i][0]-petrolpumps[i][1])
        if distance<0:
            index=i+1
            distance=0
            
        
    return index
