from colorthief import ColorThief
from os import path
from subprocess import Popen
import asyncio


class WindowsController:

    __wallpaper_content_base_path: str = r"C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine"
    __wallpaper_base_path: str = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\431960'
    __wallpaper_exe_type = 'wallpaper64.exe'
    __wallaper_get_current_wallpaper_command_set = ['-control', 'getWallpaper']
    __WINDOWS_DIR_SEPARATOR = "\\"
    _current_wallpaper_path: str|int = None
    _current_scene_id: str|int = None
    _file_buffer_name = 'current_scene_buffer.txt'

    def __init__(self, wallpaper_dir: str=None):

        if (wallpaper_dir is None):
            self.__wallpaper_content_base_path = wallpaper_dir
    
    async def get_current_wallpapaper_path(self):
        print(f'Command is:  {self.__wallpaper_base_path}\{self.__wallpaper_exe_type} {self.__wallaper_get_current_wallpaper_command_set}')
        # with Popen(self.)

        
        
        
