"""
Пакет для работы с файлами:
* групповое переименование файлов,  
* сортировка файлов по директориям: видео, изображения, текст и т.п.
"""

from .task1 import rename_group_files
from .task7_from_s7 import replace_files

__all__ = ['rename_group_files', 'replace_files']