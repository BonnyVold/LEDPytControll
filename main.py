import io as asy
import time
# import os
from colorPicker import get_current_wallpaper_img_sway
from colorPicker import get_dominant_color
from colorPicker import get_palete
from bleak import BleakScanner
from bleak import BleakClient
from WindowsController import WindowsController
from LinuxController import LinuxController



address_of_controller='BE:96:73:00:0A:EB'
device_find = False
prev_color = None
prev_img_path = ''
prefix = ''
UUID = '0000fff3-0000-1000-8000-00805f9b34fb'
prefix = '7e'
postfix = 'ef'
moduleColorId = '0705'
moduleBrightnessId = '0401'
num_of_cycle_per_color = 10
brightness_max = 74


def have_update() -> bool|str:
    global prev_img_path
    current_img_path = get_current_wallpaper_img_sway()
    if (current_img_path and prev_img_path != current_img_path):
        prev_img_path = current_img_path
        return current_img_path
    return False

def normalize_colors_to_hex(colors: list|tuple) -> list|tuple:
    normalize_colors = []
    for color in colors:
        color = color.replace('0x','')
        if len(color) == 1:
            color = f'0{color}'
        normalize_colors.append(color)
    return normalize_colors

def get_device():
    while True:
        device =  BleakScanner.find_device_by_address(address_of_controller)
        if (device):
            return device
    
def run():
    pass
    # try:
        # controller =  get_device()
         # with BleakClient(address_of_controller) as controller:
         #    while True:
         #        new_path =  have_update()
                # if(new_path and type(new_path) is str):
                #     pallets = get_palete(new_path)
                #     for pallete in pallets: 
                #         normalize_colors = normalize_colors_to_hex(pallete)
                #         print(normalize_colors)
                #         r = normalize_colors[0] 
                #         g = normalize_colors[1] 
                #         b = normalize_colors[2] 
                #         print(f'Send new color R:{r} G:{g} B:{b}')
                #         command_color = f'{prefix}{moduleColorId}03{r}{g}{b}10{postfix}'
                #          controller.write_gatt_char(UUID, bytes.fromhex(command_color))
                #         for index in range(1,num_of_cycle_per_color+1):
                #             brightness_value = hex(round(brightness_max*(index/10)))
                #             print(f'Set new brightness value: {brightness_value}')
                #             command_brightness = f'{prefix}{moduleBrightnessId}{brightness_value}ffffff00{postfix}'
                #             print(command_brightness)
                #              controller.write_gatt_char(UUID, bytes.fromhex(command_brightness))
                #             time.sleep(.5)
                #     if (type(have_update()) is str):
                #         break
                # if type(new_path) is str:
                #     new_colors = get_dominant_color(new_path)
                #     new_colors = normalize_colors_to_hex(new_colors)
                #     r = new_colors[0]
                #     g = new_colors[1]
                #     b = new_colors[2]
                #     print(f'Send new color R:{r} G:{g} B:{b}')
                #     command = f'{prefix}{moduleColorId}03{r}{g}{b}10{postfix}'
                #      controller.write_gatt_char(UUID, bytes.fromhex(command))
                # else:
                #     print("Sleep")
                #     time.sleep(.5)
    # except RuntimeWarning as ex:
    #     pass

def test():
    img_path = get_current_wallpaper_img_sway() 
    pallets = get_palete(str(img_path))
    for pallete in pallets: 
        normalize_colors = normalize_colors_to_hex(pallete)
        for index in range(1,num_of_cycle_per_color+1):
            brightness_value = hex(round(brightness_max*(index/10)))
        exit()

def windows_test():
    controller = WindowsController()
    print(controller.get_img_palette())
    #  controller.check_update()

def linux_test():
    controller = LinuxController()
    print(controller.get_color())

def main(): 
    linux_test()
    
if __name__ == "__main__":
    print(f'Start time: {time.strftime('S')}')
    main()
    print(f'End time: {time.strftime('S')}')
    
