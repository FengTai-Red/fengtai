def main():
    filepath = "head.html"
    file_list = text2list(filepath)
    file_list = list_recode(file_list)
    list2text(file_list)

def text2list(filepath):
    #传入一个文件路径，返回一个以每行为一个元素的列表
    file_list = []
    line = ""
    files = []
    with open(filepath, 'r', encoding='UTF-8') as file:
        for file_line in file:
            file_list.append(file_line)
    print("文件转列表完成")
    return file_list

def list2text(file_list):
    # 传入一个列表，将其转为字符型文件
    with open("pythonScript/zzz.txt", 'w', encoding='UTF-8') as file:
        for html in file_list:
            file.write(html + "\n")
    print("列表转字符文件完成")

def list_recode(file_list):
    # 传入一个列表，将其按指定格式进行转换,这里将其转为JS的document.writeln()输出的格式
    le = len(file_list)
    for i in range(le):
        file_list[i] = "document.writeln(\"" + file_list[i].replace("\n", "").replace("\"", "\\\"") + "\");"
    print("列表格式转换完成")
    return file_list


if __name__ == "__main__":
    main()
