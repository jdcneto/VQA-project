from PIL import Image, ImageDraw
from random import randint
from shape import Shape
from location import IM_SIZE, IM_DRAW_SCALE, IM_DRAW_SIZE
import math

MIN_SHAPE_SIZE = IM_DRAW_SIZE / 16
MAX_SHAPE_SIZE = IM_DRAW_SIZE / 4

TRIANGLE_ANGLE_1 = 0
TRIANGLE_ANGLE_2 = -math.pi / 3

def create_image(filename, shape, color, location):
  r = randint(230, 255)
  g = randint(230, 255)
  b = randint(230, 255)
  im = Image.new('RGB', (IM_DRAW_SIZE, IM_DRAW_SIZE), (r, g, b))

  draw = ImageDraw.Draw(im)
  draw_shape(draw, shape, color, location)
  del draw

  im = im.resize((IM_SIZE, IM_SIZE), resample=Image.BILINEAR)

  im.save(filename, 'png')

def draw_shape(draw, shape, color, location):
  if shape is Shape.RECTANGLE:
    w = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    h = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    x = randint(location.value[0], IM_DRAW_SIZE / 2 + location.value[0] - w)
    y = randint(location.value[1], IM_DRAW_SIZE / 2 + location.value[1] - h)
    draw.rectangle([(x, y), (x + w, y + h)], fill=color.value)

  elif shape is Shape.CIRCLE:
    d = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    x = randint(location.value[0], IM_DRAW_SIZE / 2 + location.value[0] - d)
    y = randint(location.value[1], IM_DRAW_SIZE / 2 + location.value[1] - d)
    draw.ellipse([(x, y), (x + d, y + d)], fill=color.value)

  elif shape is Shape.TRIANGLE:
    s = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    x = randint(location.value[0], IM_DRAW_SIZE / 2 + location.value[0] - s)
    y = randint(math.ceil(s * math.sin(math.pi / 3)), IM_DRAW_SIZE / 2 + location.value[1])
    draw.polygon([
      (x, y),
      (x + s * math.cos(TRIANGLE_ANGLE_1), y + s * math.sin(TRIANGLE_ANGLE_1)),
      (x + s * math.cos(TRIANGLE_ANGLE_2), y + s * math.sin(TRIANGLE_ANGLE_2)),
    ], fill=color.value)

  else:
    raise Exception('Invalid shape!')
