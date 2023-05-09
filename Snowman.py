import arcade

window = arcade.Window(800, 600, "My Arcade Window")

arcade.draw_rectangle_filled(400, 200, 1000, 500, arcade.color.LIGHT_BLUE)
arcade.draw_rectangle_filled(400, 450, 1000, 500, arcade.color.DARK_BLUE)


def snowman(x, y):
    arcade.draw_circle_filled(x, y-150, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y-70, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x+15, y+10, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x-15, y+10, 5, arcade.color.BLACK)

snowman(250,250)

arcade.finish_render()
arcade.run()