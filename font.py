def font_to_hex(font):
    hex_font = {}
    for char, pixels in font.items():
        hex_pixels = []
        for row in pixels:
            byte = 0
            for i, bit in enumerate(row):
                if bit == 1:
                    byte |= 1 << (7 - i)
            hex_pixels.append(byte)
        hex_font[char] = hex_pixels
    return hex_font

font = {
    'h': [
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0]
    ],
    'e': [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0],
        [1,0,0,0,0,0,1,0],
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0]
    ],
    'l': [
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0]
    ],
    'o': [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0],
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [1,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0]
    ]
}

res = font_to_hex(font)
# print res as hexidcimal
for char, pixels in res.items():
    print(char, ':')
    for row in pixels:
        print('0x{:02x}'.format(row))

