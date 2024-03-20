import os
import re
from pypinyin import Style, pinyin

music_path = 'D:/Python Program/BukehiWeb/music'
name_path = 'D:/QQMusic v18.51/QQMusic/download/VipSongsDownload'



def chinese_to_pinyin(chinese):
    key = pinyin(chinese, style=Style.FIRST_LETTER)
    return key[0]


files = os.listdir(music_path)
filenames = os.listdir(name_path)
print(chinese_to_pinyin(filenames[0]))
filenames.sort(key=chinese_to_pinyin)

for index, filename in enumerate(files):
    filename_ = re.findall(r'(\S+)\s*', filenames[index])[0]
    code = f"""<tr>
	<td><a href="./music/{filename}">{filename_}</a></td>
	<td><a href=""></a></td>
	<td><a href=""></a></td>
	<td><a href=""></a></td>
</tr>"""
    print(code)
