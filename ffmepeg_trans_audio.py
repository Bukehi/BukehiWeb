from tkinter import filedialog
from tqdm import tqdm
import tkinter
import subprocess
import os

root = tkinter.Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames(
    title='选择压缩的音频文件', filetypes=[('音频', ['.mp3'])])
for file in tqdm(file_paths, desc='正在压缩：'):
    outfile = file.replace('.mp3', '')+"_out.mp3"
    subprocess.call(['ffmpeg', '-i', file, '-b:a', '128k', outfile])
end = input('')
