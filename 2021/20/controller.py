with open("20.txt") as data:
    lookup, img_in = data.read().split("\n\n")
    lookup = list(map(lambda x: 1 if x == "#" else 0, lookup.strip()))
    img_in = [list(map(lambda x: 1 if x == "#" else 0, x)) for x in img_in.split("\n") if x != ""]

def transcode(img_in, count):
    undefined = lookup[-1] if count % 2 == 1 else lookup[0]
    width = len(img_in[0]) + 2
    img_in.append([undefined] * (width - 2)) # Will be padded later
    img_in.append([undefined] * (width - 2))
    img_lines = [[undefined] * width] * 3

    def get_sourrounding_string(x_pos):
        list = [
            img_lines[0][x_pos - 1] if x_pos - 1 >= 0 else undefined,
            img_lines[0][x_pos],
            img_lines[0][x_pos + 1] if x_pos + 1 < width else undefined,
            img_lines[1][x_pos - 1] if x_pos - 1 >= 0 else undefined,
            img_lines[1][x_pos],
            img_lines[1][x_pos + 1] if x_pos + 1 < width else undefined,
            img_lines[2][x_pos - 1] if x_pos - 1 >= 0 else undefined,
            img_lines[2][x_pos],
            img_lines[2][x_pos + 1] if x_pos + 1 < width else undefined,
        ]
        return map(str, list)

    out_img = []
    for _ in range(len(img_in) - 1):
        img_lines.pop(0)
        img_lines.append([undefined] + img_in.pop(0) + [undefined])
        out_row = []
        for j in range(width):
            out_row.append(lookup[int("".join(get_sourrounding_string(j)),2)])
        out_img.append(out_row)
    
    # Extra row, as we skipped the last
    img_lines.pop(0)
    img_lines.append([undefined] * width)
    out_row = []
    for j in range(width):
        out_row.append(lookup[int("".join(get_sourrounding_string(j)),2)])
    out_img.append(out_row)
    
    return out_img

def get_lights(img_in):
    return sum([sum(x) for x in img_in])

for i in range(50):
    img_in = transcode(img_in, i+1)
print(get_lights(img_in))
