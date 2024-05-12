from tqdm import tqdm
from PyPDF2 import PdfWriter
import os
import time
def merge(target_path):
    pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    file_merger = PdfWriter()
    for pdf in tqdm(pdf_lst, desc="正在合并"):
        file_merger.append(pdf)
    file_path = target_path+'/merge.pdf'
    file_merger.write(file_path)

if __name__ == "__main__":
    target_path = input('请输入文件夹路径：')
    merge(target_path)
    time.sleep(5)
