def pulsador_nombre():
    basic.show_string("Diego")

def pulsador_edad():
    basic.show_string("30")

input.on_button_pressed(Button.A, pulsador_nombre)
input.on_button_pressed(Button.B, pulsador_edad)