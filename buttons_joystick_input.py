from gpiozero import Button
from time import sleep

joystick_up = Button(4)
joystick_down = Button(17)
joystick_left = Button(27)
joystick_right = Button(22)
button_top_left = Button(18)
button_top_middle = Button(15)
button_top_right = Button(14)
button_bottom_left = Button(25)
button_bottom_middle = Button(24)
button_bottom_right = Button(23)
button_blue_left = Button(10)
button_blue_right = Button(9)

while (True):
    sleep(0.1)
    if joystick_up.is_pressed:
        print("Up")
    if joystick_down.is_pressed:
        print("Down")
    if joystick_left.is_pressed:
        print("Left")
    if joystick_right.is_pressed:
        print("Right")
    if button_top_left.is_pressed:
        print("Red: Top Left")
    if button_top_middle.is_pressed:
        print("Red: Top Middle")
    if button_top_right.is_pressed:
        print("Red: Top Right")
    if button_bottom_left.is_pressed:
        print("Red: bottom Left")
    if button_bottom_middle.is_pressed:
        print("Red: bottom Middle")
    if button_bottom_right.is_pressed:
        print("Red: bottom Right")
    if button_blue_left.is_pressed:
        print("Blue: Left")
    if button_blue_right.is_pressed:
        print("Blue: Right")