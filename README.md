# ForsenPlace Orders

Forsen related orders. Forsen commands, pixels, colors, image processing, total r/place domination. Everything that is somewhat related to Forsen.

## Reference
![reference](reference.png)

## Priority
![priority](priority.png)

## How it works

Orders are generated using `reference.py` from the `reference.png` image. Orders are prioritized according to the alpha channel in `priority.png`. The end result is a bunch of orders grouped into a list of priorities, from more to less important.

The client script will try to pick a random wrong pixel from the top priority, if they are all correct move into the next priority and so on. Each order is just a list of three things:

- x-coordinate of the pixel
- y-coordinate of the pixel
- color of the pixel according to reddit index

Reddit color indexing (hints to a future update):
```
'#BE0039': 1,
'#FF4500': 2,
'#FFA800': 3,
'#FFD635': 4,
'#00A368': 6,
'#00CC78': 7,
'#7EED56': 8,
'#00756F': 9,
'#009EAA': 10,
'#2450A4': 12,
'#3690EA': 13,
'#51E9F4': 14,
'#493AC1': 15,
'#6A5CFF': 16,
'#811E9F': 18,
'#B44AC0': 19,
'#FF3881': 22,
'#FF99AA': 23,
'#6D482F': 24,
'#9C6926': 25,
'#000000': 27,
'#898D90': 29,
'#D4D7D9': 30,
'#FFFFFF': 31
```