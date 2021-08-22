from math import sin, cos, radians



class Model:
    def __init__(self, verticies: list, edges: list, color: tuple):
        self.verticies = verticies
        self.edges = edges
        
        self.color = color
    

    def get(self) -> None:
        return [self.verticies, self.edges, self.color]


    def rotate_model(self, rotation: list):
        """
        :param rotation: pitch, yaw, roll rotation values (γ, β, α)

        γ: pitch (x rotation)
        β: yaw   (y rotation)
        α: roll  (z rotation)

                            [ cosα -sinα  0 ] [ cosβ   0   sinβ ] [ 1   0     0   ]
        Rz(α) Ry(β) Rx(γ) = [ sinα  cosα  0 ] [ 0      1    0   ] [ 0  cosγ -sinγ ]
                            [  0     0    1 ] [ -sinβ  0   cosβ ] [ 0  sinγ  cosγ ]

            [cosα cosβ    cosα sinβ sinγ - sinα cosγ    cosα sinβ cosγ + sinα sinγ]
        R = [sinα cosβ    sinα sinβ sinγ + cosα cosγ    sinα sinβ cosγ - cosα sinγ]
            [ -sinβ              cosβ sinγ                      cosβ cosγ         ]

        """
        γ = radians(rotation[0])
        β = radians(rotation[1])
        α = radians(rotation[2])
        
        matrix = [
            [cos(α) * cos(β),    cos(α) * sin(β) * sin(γ) - sin(α) * cos(γ),    cos(α) * sin(β) * cos(γ) + sin(α) * sin(γ)],
            [sin(α) * cos(β),    sin(α) * sin(β) * sin(γ) + cos(α) * cos(γ),    sin(α) * sin(β) * cos(γ) - cos(α) * sin(γ)],
            [    -sin(β),                   cos(β) * sin(γ),                                   cos(β) * cos(γ)            ]
        ]


        self.verticies = [v for v in self.verticies]
        for index, (x, y, z) in enumerate(self.verticies):
            new_point = []
            for vector in matrix:
                new_point.append(
                    ((x * vector[0]) + (y * vector[1]) + (z * vector[2]))
                )
            self.verticies[index] = new_point
