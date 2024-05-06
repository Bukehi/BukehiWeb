import PyPDF2
import tqdm


def compress_by_page(src, dst):
    pdf_file = open(src, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in tqdm.tqdm(range(len(pdf_reader.pages)), desc="压缩中："):
        page = pdf_reader.pages[page_num]
        page.compress_content_streams()
        pdf_writer.add_page(page)
    out_file = open(dst, "wb")
    pdf_writer.write(out_file)
    out_file.close()
    pdf_file.close()
    print("压缩完成！")


if __name__ == "__main__":
    # work_path1 = r'Z:/彭俊喜/.pdf'
    in_path = r"../人民日报/人民日报.pdf"  # 需要压缩的PDF文件
    out_path = r"../人民日报/人民日报-compress.pdf"  # 压缩后的PDF文件路径
    compress_by_page(in_path, out_path)
