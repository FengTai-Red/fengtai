import re
import os

def main():
    code_path = "D:/File/Python/LeetCode/0107.py"  # LeetCode代码的位置
    html_path = "LeetCode.html"  # 要更新的HTML位置
    code_list = letCode_to_gtml(text2list(code_path))
    html_list = insert_to_html(text2list(html_path), code_list[0], code_list[1], code_list[2])
    save_path = "LeetCode.html"  # 保存的位置
    list2text(html_list, save_path)
    leetcode_num()
    print("完成")

def leetcode_num():
    leetcode_dir = "D:/File/Python/LeetCode" 
    print("完成的题目数量:",len(os.listdir(leetcode_dir)))

def text2list(filepath):
    #传入一个文件路径，返回一个以每行为一个元素的列表
    # filepath : 文件路径
    # return 转化的列表
    file_list = []
    line = ""
    files = []
    with open(filepath, 'r', encoding='UTF-8') as file:
        for file_line in file:
            file_list.append(file_line.replace("\n", ""))
    return file_list

def list2text(file_list, save_path):
    # 传入一个列表，将其转为字符型文件
    # file_list : 要存成文件的列表
    with open(save_path, 'w', encoding='UTF-8') as file:
        for html in file_list:
            file.write(str(html) + "\n")

def letCode_to_gtml(file_list):
    # 传入一个列表，将其按指定格式进行转换,这里传入的为leetcode的题目解答，文件格式为前半部分为注释写的题目，后半部为代码
    # 返回一个列表，以及题目的编号
    index_and_text = file_list[0].split('.')
    questions_index = index_and_text[0][2:len(index_and_text[0])].zfill(4)
    questions_text = index_and_text[1][1:len(index_and_text[1])]
    file_list[0] = "<p class=\"letterpress_title\" id=\"{0}\">{0} .{1}</p>".format(questions_index, questions_text)
    le = len(file_list)
    i = 1
    code_start = False
    end = -1
    while(i < le - 1):
        if (file_list[i].lstrip() != "" and file_list[i].lstrip()[0] == "#"):
            file_list[i] = "<p class=\"letterpress\">" + file_list[i][2:].replace("\n", "").replace(" ", "&nbsp;") + "</p>"
            code_start = False
        elif(code_start == False):
            code_start = True
            file_list.insert(i, "<div class=\"code_box\">")
            le += 1
        else:
            file_list[i] = "    <p class=\"code\">" + file_list[i].replace("\n", "") + "</p>"
        i += 1
        if (file_list[i].lstrip()[0:13] == "if __name__ ="):
            file_list.insert(i, "</div>")
            end = i + 1
            break
    return (file_list[0:end], questions_index, questions_text)

def insert_to_html(html_list, code_list, questions_index, questions_text):
    # 将写转好的leetcode插入HTML
    le = len(html_list)
    is_doing = False  # 该题是否做过
    pattern_index = "(?<=\\bclass\=\"index\"\shref\=\"#)\w+\\b"  # 用于查找索引的正则
    subject_insert_index = 0  # 题目索引的HTML语句插入的位置
    end_subject_index_insert = False  # 结束题目索引的插入
    pattern_letterpress_title = "(?<=class\=\"letterpress_title\"\sid=\")\w+\\b"  # 用于查找题目正文的正则
    pattern_subject_insert_index = 0  # 题目正文的HTML语句插入的位置
    end_subject_letterpress_insert = False  # 结束题目正文的插入
    subject_letterpress_line_num = 0 # 题目正文的行数
    for i in range(le):
        cls_index = re.search(pattern_index, html_list[i])
        cls_letterpress_title = re.search(pattern_letterpress_title, html_list[i])
        if (cls_index and not end_subject_index_insert):  
            # 进行题目索引位置的查找和插入
            if (int(cls_index.group()) == int(questions_index)):
                print("这题已经做过了")
                is_doing = True
                break
            elif(int(cls_index.group()) > int(questions_index)):
                subject_insert_index = i
                end_subject_index_insert = True
            else:
                subject_insert_index = i + 1

        if (cls_letterpress_title and not end_subject_letterpress_insert):
            # 进行题目正文引位置的查找和插入
            if(int(cls_letterpress_title.group()) > int(questions_index)):
                pattern_subject_insert_index = i
                end_subject_letterpress_insert = True
            else:
                pattern_subject_insert_index = i
            subject_letterpress_line_num = 0 # 题目正文的行数归零
        # 找到正文位置后进行正文行数的判断
        subject_letterpress_line_num += 1
        between_subject = "(?<=</di)\w+\\b"
        if (between_subject and end_subject_letterpress_insert):
            break
        last_subject = re.search("(?<=<\!\-\-\s===================)\w+\\b", html_list[i])  # 已经是最后一个题目
        if (last_subject):
            if(last_subject.group() == "底线"):
                break
    pattern_subject_insert_index += subject_letterpress_line_num
    if (end_subject_letterpress_insert):
        pattern_subject_insert_index -= 1
    if (not is_doing):
        html_list.insert(subject_insert_index, "        <a class=\"index\" href=\"#{0}\">{0}.{1}</a>".format(questions_index, questions_text))
        html_list.insert(pattern_subject_insert_index, "        <!-- ===================分界线=================== -->")
        le = len(code_list)
        for i in range(le):
            html_list.insert(pattern_subject_insert_index + i + 1, "        " + code_list[i])
    return html_list


if __name__ == "__main__":
    main()
