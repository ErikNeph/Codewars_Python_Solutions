"""
Write a function that returns the total surface area and volume of a box.

The given input will be three positive non-zero integers: width, height, and depth.

The output will be language dependant, so please check sample tests
for the corresponding data type, (list, tuple, struct, query, etcetera).
"""

def get_size(w, h, d) -> list:
    total_surface_area = 2 * (h * w + h * d + w * d)
    volume_of_a_box = w * h * d
    return [total_surface_area, volume_of_a_box]
