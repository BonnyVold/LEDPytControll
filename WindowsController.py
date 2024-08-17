from colorthief import ColorThief
from os import path
from subprocess import Popen
from subprocess import PIPE
import asyncio
import os


class WindowsController:

    __wallpaper_content_base_path: str = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\431960'
    __wallpaper_base_path: str = r'C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine'
    __wallpaper_exe_type = 'wallpaper64.exe'
    __wallaper_get_current_wallpaper_command_set = ['-control', 'getWallpaper']

    __WINDOWS_DIR_SEPARATOR = "\\"

    _current_wallpaper_path: str|int = None
    _avilible_preview_type = ['preview.jpg', 'preview.gif']

    _current_scene_id: str|int = None
    _buffer_scene_id: str|int = None
    _file_buffer_name = 'current_scene_buffer.txt'
    __have_update = True

    def __init__(self, wallpaper_dir: str|None = None):

        if (wallpaper_dir is not None):
            self.__wallpaper_content_base_path = wallpaper_dir
        self.__init_update_buffer()
    
    def __init_update_buffer(self):
        command = f'{self.__wallpaper_base_path}\\{self.__wallpaper_exe_type} {self.__wallaper_get_current_wallpaper_command_set[0]} {self.__wallaper_get_current_wallpaper_command_set[1]}'
        with open(self._file_buffer_name, 'w') as buffer_file:
            proccess = Popen([
                self.__wallpaper_exe_type,
                self.__wallaper_get_current_wallpaper_command_set[0],
                self.__wallaper_get_current_wallpaper_command_set[1],
            ], 
                            stdout=buffer_file,
                            stderr=PIPE,
                            text=True)

            proccess.wait()
            with open(self._file_buffer_name, 'r') as buffer_file:
                current_scene = buffer_file.read()
                scene_id = current_scene.split('/')[-2]
                self._buffer_scene_id = scene_id 


    def get_scene_id(self):
        return self._current_scene_id

    async def update_buffer(self):
        command = f'{self.__wallpaper_base_path}\\{self.__wallpaper_exe_type} {self.__wallaper_get_current_wallpaper_command_set[0]} {self.__wallaper_get_current_wallpaper_command_set[1]}'
        with open(self._file_buffer_name, 'w') as buffer_file:
            proccess = Popen([
                self.__wallpaper_exe_type,
                self.__wallaper_get_current_wallpaper_command_set[0],
                self.__wallaper_get_current_wallpaper_command_set[1],
            ], 
                            stdout=buffer_file,
                            stderr=PIPE,
                            text=True)

            proccess.wait()

            with open(self._file_buffer_name, 'r') as buffer_file:
                current_path = buffer_file.read()
                scene_id = current_path.split('/')[-2]
                self._buffer_scene_id = scene_id


    async def get_img_palette(self):
        with open(self.__get_scene_path(), 'rb') as prev_file:
            colorThief = ColorThief(prev_file)
            return colorThief.get_palette()
    

    async def get_img_dominant_color(self):
        with open(self.__get_scene_path(), 'rb') as prev_file:
            colorThief = ColorThief(prev_file)
            return colorThief.get_color()


    def __get_scene_path(self):
        path_to_img = f'{self.__wallpaper_content_base_path}{self.__WINDOWS_DIR_SEPARATOR}{self._buffer_scene_id}'
        file_list = os.listdir(path_to_img)
        if (file_list[0] in self._avilible_preview_type):
            preview_file_name = file_list[0]
            full_path_to_img = f'{path_to_img}\{preview_file_name}'
            return full_path_to_img

    # async def get_img_file_data(self): 
    #     path_to_img = f'{self.__wallpaper_content_base_path}{self.__WINDOWS_DIR_SEPARATOR}{self._buffer_scene_id}'
    #     file_list = os.listdir(path_to_img)
    #     if (file_list[0] in self._avilible_preview_type):
    #         preview_file_name = file_list[0]
    #         full_path_to_img = f'{path_to_img}\{preview_file_name}'
    #         return await self.__read_img_file(full_path_to_img)
    #     else:
    #         print('Availible preview type not found!')

    # async def __get_file(self, img_path: str):
    #     with open(img_path, 'rb') as img_file:
    #         return img_file

    # async def __read_img_file(self, img_path: str):
    #     with open(img_path, 'rb') as img_file:
    #         return img_file.read()


    async def check_update(self):
        # If is init check update -> check if not set current scene id and have buffer scene id -> set current scene id from buffer 
        if self._current_scene_id is None and self._buffer_scene_id:
            self._current_scene_id = self._buffer_scene_id 
            self._buffer_scene_id = None
            self.__have_update = False
            return False
        elif self._current_scene_id:
            pass

            




        

