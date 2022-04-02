import json
from PIL import Image

reference = Image.open('reference.png')
pixels_reference = reference.load()
priority = Image.open('priority.png')
pixels_priority = priority.load()

color_mappings = {
    '#FF4500': 2,
    '#FFA800': 3,
    '#FFD635': 4,
    '#00A368': 6,
    '#7EED56': 8,
    '#2450A4': 12,
    '#3690EA': 13,
    '#51E9F4': 14,
    '#811E9F': 18,
    '#B44AC0': 19,
    '#FF99AA': 23,
    '#9C6926': 25,
    '#000000': 27,
    '#898D90': 29,
    '#D4D7D9': 30,
    '#FFFFFF': 31
}

prio_mappings = {
    '#FF4500': 2,
    '#FFA800': 3,
    '#FFD635': 4,
    '#00A368': 6,
    '#7EED56': 8,
    '#2450A4': 12,
    '#3690EA': 13,
    '#51E9F4': 14,
    '#811E9F': 18,
    '#B44AC0': 19,
    '#FF99AA': 23,
    '#9C6926': 25,
    '#000000': 27,
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

for x in range(1000):
    for y in range(1000):
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
