# ALPR
    Automatic License Plate Recognition software that works in all environments, optimized for your location.
## Instructions

1. Install:

```
pip install alpr
```

2. Generate an aesthetic ASCII visual:

```python
from ALPR import license_recognition as lr

# DEMO Version
license_plates = lr.GetLicensePlateDemo("/path/to/image.jpg")
license_plates.get_license_img("/path/to/image.jpg")


# REAL Version
# initialize object with token
app =lr.GetLicensePlateDemo("token")
# Get more info from your image
app.get_license("/path/to/image.jpg")


```

3. Enjoy!


## To Do
1. Add more options
2. Add ability to inoput video or stream