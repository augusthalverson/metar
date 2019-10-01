# metar
A simple tool for interpreting METAR (**MET**eorological **A**erodrome **R**eports) in `Python3`.

#### Things to come:
* Function to interpret METAR segments dynamically (based on regex)
* Translate Zulu time into local time based on time zone
* Add interpretation support for short codes (e.g. AUTO, COR, SPECI, AO2, etc.)
* Translate ICAO code into name (or provide some other contextual information about the airport)
* Interpret Remarks (RMKs)
* Consider interpreting real-time metar info from the [Aviation Weather Center (AWC)](https://www.aviationweather.gov/metar).


#### Basic METAR formula:

`Airport` `Timestamp` `Report Shortcode` `Wind` `Visibility` `Clouds` `Runway` `Altimeter` `RMKs`

|Segment           |Unit          |Description
|------------------|:-------------|-----------
|`Airport`         |ICAO          |The airport of the weather station that created the report
|`Timestamp`       |Zulu Time     |The time of the report in Zulu time. _A brief explanation of Zulu time is below_
|`Report Shortcode`|_n/a_         |
|`Wind`            |Knots         |Windspeed (first 3 digits denote direction in degrees, next two denote speed in Kts)
|`Visibility`      |Statute Miles |Miles of visibility
|`Clouds`          |100s of Feet  |Describes clouds present at different altitudes
|`Runway`          |              |
|`Altimeter`       |Inchs Mercury |Altimeter of current airport
|`RMKs`            |_n/a_         |



#### Zulu Time

`Day out of the month` + `Hour of day in UTC (24hr format)` + `Minutes in hour` + Z

_For Example:_

300321Z = 30 03 21 Z = 30th of the month, 3:21 UTC
