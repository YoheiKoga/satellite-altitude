# satellite-altitude

- Calculate satellite altitude from Two Line Elements(TLE) file
- Add TLE file to TLE-file directory
    - I added one example file, for ISS TLE from 2020-01-01 to 2020-01-31
- For example, you can get TLE data from [Space-Track.Org](https://www.space-track.org/auth/login)
    - You can use [python-astrodynamics/spacetrack: Python client for space-track.org](https://github.com/python-astrodynamics/spacetrack) library if you want

<br>

### 

### using

- for example
- There is an TLE data is in TLE-file/ISS-20200101-20200201.tle

```
$ python satellite-altitude.py TLE-file/ISS-20200101-20200201.tle
```