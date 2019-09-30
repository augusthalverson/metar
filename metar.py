def metarToEnglish(metarString):
    metar = metarString.split(" ")

    # settings:
    utc = -5

    # Airport
    airport = metar[0]

    # Date & Time
    rawTimestamp = metar[1]
    day = rawTimestamp[0:2]
    zuluTime = rawTimestamp[2:len(rawTimestamp)]

    # Short Code

    # Wind 
    rawWind = metar[2]
    windHdg = rawWind[0:3]
    windStrength = rawWind[3:5]

    # Short Wind Visibility
    rawVisibility = metar[3]
    visDistance = 0
    visSuffix = ""
    if rawVisibility.endswith("SM"):
        visDistance = rawVisibility[0:2]
        visSuffix = "Statute Miles"

    # Runway Visibility

    # Cloud Cover
    # EVENTUALLY use key/value pairs in dict for multiple
    rawCloud = metar[4]
    cloudStatus = rawCloud[0:3]
    rawCloudElevation = rawCloud[3:6]
    formattedCloudElevation = int(rawCloud[3:6]) * 100

    # Active Runways?

    # Temperature and Dew Point
    rawTempAndDew = metar[6]
    
    #Altimeter
    rawAlt = metar[6]
    altimeter = rawAlt[1:5]
    altimeter = altimeter[0:2] + "." + altimeter[2:4] + "\" Hg"

    # RMKs

    print(altimeter)

metarToEnglish("KMSP 302053Z 18009KT 10SM BKN050 29/22 A2968 RMK AO2 SLP046 T02890222 56008 $")