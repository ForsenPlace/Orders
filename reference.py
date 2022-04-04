import json
from PIL import Image

reference = Image.open('reference.png')
pixels_reference = reference.load()
priority = Image.open('priority.png')
pixels_priority = priority.load()

color_mappings = {
    '#6D001A': 0,
    '#BE0039': 1,
    '#FF4500': 2,
    '#FFA800': 3,
    '#FFD635': 4,
    '#FFF8B8': 5,
    '#00A368': 6,
    '#00CC78': 7,
    '#7EED56': 8,
    '#00756F': 9,
    '#009EAA': 10,
    '#00CCC0': 11,
    '#2450A4': 12,
    '#3690EA': 13,
    '#51E9F4': 14,
    '#493AC1': 15,
    '#6A5CFF': 16,
    '#94B3FF': 17,
    '#811E9F': 18,
    '#B44AC0': 19,
    '#E4ABFF': 20,
    '#DE107F': 21,
    '#FF3881': 22,
    '#FF99AA': 23,
    '#6D482F': 24,
    '#9C6926': 25,
    '#FFB470': 26,
    '#000000': 27,
    '#515252': 28,
    '#898D90': 29,
    '#D4D7D9': 30,
    '#FFFFFF': 31
}

def rgb_to_hex(rgb):
    return '#' + (('%02x%02x%02x' % rgb).upper())

prio1 = []
prio2 = []
prio3 = []
prio4 = []
prio5 = []

for x in range(2000):
    for y in range(2000):
        colors = pixels_reference[x, y]
        if colors[3] == 0:
            continue
        hex = rgb_to_hex((colors[0], colors[1], colors[2]))
        colorid = color_mappings[hex]
        prio_alpha = pixels_priority[x, y][3]
        if prio_alpha == 255:
            prio1.append([x, y, colorid])
        elif prio_alpha >= 200:
            prio2.append([x, y, colorid])
        elif prio_alpha >= 150:
            prio3.append([x, y, colorid])
        elif prio_alpha >= 100:
            prio4.append([x, y, colorid])
        else:
            prio5.append([x, y, colorid])


with open('orders.json', 'w') as f:
    f.write(json.dumps([prio1, prio2, prio3, prio4, prio5]))
