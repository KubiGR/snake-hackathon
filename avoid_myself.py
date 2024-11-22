import random
import typing

def avoid_myself(my_body: typing.Dict, is_move_safe: typing.Dict):
    for body_element in my_body:
        if is_adjacent(my_body[0], body_element):
            collision_direction = get_direction_from_source(my_body[0], body_element)
            is_move_safe[collision_direction] = False

    return is_move_safe

def is_adjacent(pos1, pos2):
    return (abs(pos1["x"] - pos2["x"]) == 1) ^ (abs(pos1["y"] - pos2["y"]) == 1)

def get_direction_from_source(fromPosition, toPosition):
    if fromPosition["x"] < toPosition["x"]:
        return "right"
    elif fromPosition["x"] > toPosition["x"]:
        return "left"
    elif fromPosition["y"] < toPosition["y"]:
        return "up"
    return "down"