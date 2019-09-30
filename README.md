# metar
A simple tool for interpreting METAR (METeorological Aerodrome Reports) in Python3.

#### Things to come:
* Function to interpret METAR segments dynamically (based on regex)
* Translate Zulu time into local time based on time zone
* Add interpretation support for short codes (e.g. AUTO, COR, SPECI, AO2, etc.)
* Translate ICAO code into name (or provide some other contextual information about the airport)
* Interpret Remarks (RMKs)
* Consider interpreting real-time metar info from the [Aviation Weather Center (AWC)](https://www.aviationweather.gov/metar).

Feel free to contribute/offer suggestions!

#### Basic METAR formula:

`Airport` `Timestamp` `Report Shortcode` `Wind` `Visibility` `Clouds` `Runway` `Altimeter` `RMKs`

* `Airport`
* `Timestamp`
* `Report Shortcode`
* `Wind`
* `Visibility`
* `Clouds`
* `Runway`
* `Altimeter`
* `RMKs`
