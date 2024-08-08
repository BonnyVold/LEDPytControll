from colorthief import ColorThief
from os.path import exists
# from os.path import isdir
# from os.path import isfile
import subprocess


def get_dominant_color(img_path: str) -> list|tuple:
    print(f'Try to open file: {img_path}')
    colorThief = ColorThief(img_path)
    r,g,b = map(lambda x: hex(x),colorThief.get_color())
    return (r, g, b)

def get_palete(img_path: str) -> list|tuple:
    colorThief = ColorThief(img_path) 
    colors = colorThief.get_palette()
    hex_colors = []
    for pallet in colors:
        hex_colors.append([*map(lambda x: hex(x), pallet)])
    # r,g,b = map(lambda x: hex(x),colorThief.get_palette())
    return hex_colors

def get_current_wallpaper_img_sway() -> str|bool:
    command = "ps aux |grep swaybg |awk -F 'swaybg' '{print $2}' |cut -d' ' -f3 |head -n1"
    path = subprocess.check_output(command, shell=True, text=True)[:-1]
    if type(path) is str and exists(path):
        return path
    return False
    
if __name__ == '__main__':
    img_path = get_current_wallpaper_img_sway()
    if type(img_path) is str:
        pallete = get_palete(img_path)
        print(pallete)
    
    
