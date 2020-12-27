from PIL import Image
import os

def conpreess(files):
    # 缩小图片
    i = 0
    multiple = 3  # 压缩倍数
    for file in files:
        imgName = files[i].split('gallery')[-1]
        img = Image.open(file)
        img = img.convert("RGB")
        weith = img.size[0]
        height = img.size[1]
        img.thumbnail((int(weith/multiple), int(height/multiple)))
        img.save("image\galleryCompress\\" + imgName)
        i += 1
        print("共{0}张，完成{1}张".format(len(files), i))

def get_all_files(dir, suffix = ["jpg"]):
    # 返回目录下所有指定后缀文件的绝对路径
    files_ = []
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            if path.split('.')[-1] in suffix:
                files_.append(path)
    return files_


if __name__ == "__main__":
    work_dir = os.getcwd() + "\image\gallery"
    files = get_all_files(work_dir)
    conpreess(files)
    print("OK")
