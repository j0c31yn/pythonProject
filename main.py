import arcade

window = arcade.Window(800, 600, "Drawing Trees")
arcade.start_render()

arcade.draw_rectangle_filled(400, 400, 1000, 1000, arcade.color.LIGHT_BLUE)
arcade.draw_rectangle_filled(400, 5, 1000, 400, arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(150, 200, 50, 100, arcade.color.RED_BROWN)
arcade.draw_circle_filled(150, 265, 55, arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(300, 200, 50, 100, arcade.color.RED_BROWN)
arcade.draw_ellipse_filled(300, 290, 100, 140, arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(550, 200, 50, 100, arcade.color.RED_BROWN)
points = ((550, 370),
          (500, 220),
          (600, 220))
arcade.draw_polygon_filled(points, arcade.color.DARK_GREEN)
points = ((700, 400),
          (680, 360),
          (670, 320),
          (730, 320),
          (720, 360))
arcade.draw_polygon_filled(points, arcade.color.DARK_GREEN)

arcade.finish_render()
arcade.run()
