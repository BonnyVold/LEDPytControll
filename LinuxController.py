from colorthief import ColorThief
from os import path
from subprocess import Popen
import io as asy
import subprocess as sp


class LinuxController:
    
    __base_wallpaper_path: str = '/home/bonnyvold/.wallpaper'
    __get_current_wlp_command: str = "ps aux |grep swaybg |awk -F 'swaybg' '{print $2}' |cut -d' ' -f3 |head -n1"
    _prev_img_name: str|None = None
    _current_wlp_name: str|None = None
    _current_wlp_path: str|None = None
    __have_update_flag: bool = False


    def __init__(self, base_wallpaper_path: str|None = None):
        if (base_wallpaper_path):
            self.__base_wallpaper_path = base_wallpaper_path
        self.__setup()

    def __setup(self):
        current_wlp_path = self._get_current_wallpapaper_path() 
        wlp_name = current_wlp_path.split('/')[-1]
        self._current_wlp_name = wlp_name
        self._current_wlp_path = current_wlp_path
        
    
    def _get_current_wallpapaper_path(self, return_list = False) -> str|list:
        current_wlp_path = sp.check_output(self.__get_current_wlp_command, shell=True, text=True)[:-1]
        wlp_name = current_wlp_path.split('/')[-1]
        if return_list:
            return [current_wlp_path, wlp_name]
        return current_wlp_path

    def get_have_update_flag(self):
        return self.__have_update_flag
    
    def check_udpate(self) -> bool: 
        runtime_wlp_path, runtime_wlp_name = self._get_current_wallpapaper_path(return_list=True)
        if runtime_wlp_name != self._current_wlp_name:
            self.__have_update_flag = True
            self._runtime_wlp_path = runtime_wlp_path
            self._runtime_wlp_name = runtime_wlp_name
            return True
        return False

    def update(self):
        if self.__have_update_flag:
              
            self._current_wlp_path = self._runtime_wlp_path
            self._current_wlp_name = self._runtime_wlp_name
            self.__have_update_flag = False

    def get_color(self):
        colorThief = ColorThief(self._current_wlp_path)
        print(colorThief.get_color())
        exit()
        
