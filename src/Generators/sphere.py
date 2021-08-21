from math import radians, cos, sin



def generate(radius=2, rings=30, color=(255, 255, 255)) -> dict:
    model = {
        'verticies': [],
        'edges': [],
        'color': color
    }

    for vertical in range(rings):
        v_angle = radians((360 / rings) * vertical)
        for horizontal in range(rings):
            h_angle = radians((360 / rings) * horizontal)

            x = radius * cos(v_angle) * cos(h_angle)
            y = radius * cos(v_angle) * sin(h_angle)
            z = radius * sin(v_angle)

            model['verticies'].append([x, y, z])
            # ! add support for edges !

    return model