def getBasicStats(verbose, method, vehicles):
    totalVeh = 0.
    totalTravelTime = 0.
    totalTravelLength = 0.
    totalTravelSpeed = 0.
    totalWaitTime = 0.
    totalDiffTime = 0.
    totalDiffSpeed = 0.
    totalDiffLength = 0.
    totalDiffWaitTime = 0.
    totalDiffTravelTime = 0.
    totalDepartDelay = 0.

    for veh in vehicles:
        totalVeh += 1
        veh.method = method
        # unit: speed - m/s; traveltime - s; travel length - m
        veh.speed = veh.travellength / veh.traveltime
        totalTravelTime += veh.traveltime
        totalTravelLength += veh.travellength
        totalWaitTime += veh.waittime
        totalTravelSpeed += veh.speed
        totalDepartDelay += veh.departdelay
    if verbose:
        print('totalVeh:', totalVeh)
    avgTravelTime = totalTravelTime / totalVeh
    print("avgTravelTime: ", avgTravelTime)
    avgTravelLength = totalTravelLength / totalVeh
    print("avgTravelLength: ", avgTravelLength)
    avgTravelSpeed = totalTravelSpeed / totalVeh
    print("avgTravelSpeed: ", avgTravelSpeed)
    avgWaitTime = totalWaitTime / totalVeh
    print("avgWaitTime: ", avgWaitTime)
    avgDepartDelay = totalDepartDelay / totalVeh
    print("avgDepartDelay: ", avgDepartDelay)
    for veh in vehicles:
        totalDiffTravelTime += (veh.traveltime - avgTravelTime) ** 2
        totalDiffSpeed += (veh.speed - avgTravelSpeed) ** 2
        totalDiffLength += (veh.travellength - avgTravelLength) ** 2
        totalDiffWaitTime += (veh.waittime - avgWaitTime) ** 2

    # SD: standard deviation
    SDTravelTime = (totalDiffTravelTime / totalVeh) ** (0.5)
    print("SDTravelTime: ", SDTravelTime)
    SDLength = (totalDiffLength / totalVeh) ** (0.5)
    print("SDLength: ", SDLength)
    SDSpeed = (totalDiffSpeed / totalVeh) ** (0.5)
    print("SDSpeed: ", SDSpeed)
    SDWaitTime = (totalDiffWaitTime / totalVeh) ** (0.5)
    print("SDWaitTime: ", SDWaitTime)
