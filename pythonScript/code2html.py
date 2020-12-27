def code2Html(filename):
    # 将.py文件每行写入Html的标签里
    file_list = []
    line = ""
    files = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for file_line in file:
            for file_byte in file_line:
                file_list.append(file_byte)  # 将文件中以每个字符的形式保存成列表
    for i in range(0, len(file_list)):  # 将转码的字符进行替换
        if file_list[i] == "<":
            file_list[i] = "&lt;"
        if file_list[i] == ">":
            file_list[i] = "&gt;"
        if file_list[i] == "&":
            file_list[i] = "&amp;"
        # if file_list[i] == " ":
        #     file_list[i] = "&nbsp;"
        if file_list[i] != "\n":
            line = line + (file_list[i])  # 将字符组成行
        else:
            files.append(line)
            line = ""
    for a in files:
        htmls = []
        a = "    <p class=\"code\">"
        b = "</p>"
        for c in files:
            s = a + c + b + '\n'
            htmls.append(s)
    htmls.insert(0, "<div class=\"code_box\">\n")
    htmls.append("</div>")
    with open("pythonScript\zzz.txt", 'w', encoding='UTF-8') as file:
        for html in htmls:
            file.write(html)
if __name__ == "__main__":
    code2Html('pythonScript\copy.py')
    print("完成")
