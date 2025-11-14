from ti_draw import *
def rect_angle():
  rect_input = input("Say 'yes' if you would like to draw a rectangle.")
  if rect_input == "yes":
    draw_rect(0, 0, 500, 800)
  else:
    return False
def tri_angle():
  triangle_input = input("Say 'yes2' if you would like to draw a circle.")
  if triangle_input == "yes2":
    draw_circle(1, 2, 40)
  else:
    return False

rect_angle()
tri_angle()

show_draw()
