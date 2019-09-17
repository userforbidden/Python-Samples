maxTravelDist = 11000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

maxTravelled = 0
result = []

for id1, dist1 in forwardRouteList:
    for id2, dist2 in returnRouteList:
        currentDistanceTravelled = dist1 + dist2
        if currentDistanceTravelled <= maxTravelDist and currentDistanceTravelled >= maxTravelled:
            if currentDistanceTravelled > maxTravelled:
                result = []
                maxTravelled = currentDistanceTravelled
            result.append([id1,id2])

print(result)