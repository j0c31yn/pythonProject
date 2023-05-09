import arcade

window = arcade.Window(800, 600, "My Arcade Window")

arcade.draw_rectangle_filled(400, 200, 1000, 500, arcade.color.LIGHT_BLUE)
arcade.draw_rectangle_filled(400, 450, 1000, 500, arcade.color.DARK_BLUE)


def snowman(x, y, z):
    arcade.draw_circle_filled(x, y-150, z-((z/60)*10), arcade.color.WHITE)
    arcade.draw_circle_filled(x, y-70, z-((z/50)*10), arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, z-((z/40)*10), arcade.color.WHITE)
    arcade.draw_circle_filled(x+15, y+10, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x-15, y+10, 5, arcade.color.BLACK)

snowman(250,250,60)
snowman(550,250,120)



arcade.finish_render()
arcade.run()