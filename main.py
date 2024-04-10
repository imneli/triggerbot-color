import pyautogui
import time

#get the color of the center pixel / pega a cor do pixel do centro da tela (mira)

def get_center_pixel_color():
    # get the screen resolution / identifica a resolução do monitor
    screen_width, screen_height = pyautogui.size()
    # get coordinates of the center pixel / pega as coordenadas do pixel no meio da tela
    center_x = screen_width // 2
    center_y = screen_height // 2
    # get the color of the center pixel / pega a cor do pixel do centro
    return pyautogui.pixel(center_x, center_y)

#check if the color has changed / verifica se a cor mudou

def color_changed(last_color, current_color):
    return last_color != current_color

#main function to continuously monitor the center pixel color / função principal para monitorar continuamente a cor do pixel do centro

def monitor_pixel():
    last_color = None

    while True:
        current_color = get_center_pixel_color()
        if last_color is None:
            last_color = current_color
        elif color_changed(last_color, current_color):
            print("Color Changed. Clicking.")
            pyautogui.click()  # mouse click
            last_color = current_color

        time.sleep(1)  #sleep 

if __name__ == "__main__":
    monitor_pixel()
