import xlrd

def main():
    filepath = "D:\File\Office\Anime.xlsx"
    file_list =obtain_excel_information(filepath)
    file_list = list_to_html(file_list)
    list2text(file_list)
    

def obtain_excel_information(filepath):
    # 用于获取表格的信息
    print("表格转列表开始")
    workbook = xlrd.open_workbook(filepath)
    sheet = workbook.sheet_by_index(0)
    rows_num = sheet.nrows
    cols_num = sheet.ncols
    file_list = []  # 用于存储所有表格的信息
    title_list = []  # 用于储存标题信息
    for col in range(0, cols_num):
        title_list.append(sheet.cell_value(0, col))
    for row in range(1, rows_num):
        anime_dict = {}  # 用于储存某一动画
        for col in range(0, cols_num):
            cell_row_col_type = sheet.cell_type(row, col)
            cell_row_col_value =  sheet.cell_value(row, col)
            if (cell_row_col_type == 3):
                cell_row_col_value = xlrd.xldate_as_tuple(cell_row_col_value, workbook.datemode)
                cell_row_col_value = "{0}年{1}月".format(cell_row_col_value[0], cell_row_col_value[1])  # 以YYYYMM的格式储存日期
            anime_dict[title_list[col]] = cell_row_col_value
        file_list.append(anime_dict)
    print("表格转列表完成")
    return file_list

def list_to_html(file_list):
    # 将获取的信息转为html语句
    lists = []
    html_str = ""
    for a_information in file_list:
        html_str += "<tr>\n"
        for key, value in a_information.items():
            html_str += "    <td>{0}</td>\n".format(value)
        html_str += "</tr>\n"
        lists.append(html_str)
        html_str = ""
    return lists

def list2text(file_list):
    # 传入一个列表，将其转为字符型文件
    with open("pythonScript/zzz.txt", 'w', encoding='UTF-8') as file:
        for html in file_list:
            file.write(html + "\n")
    print("列表转字符文件完成")



if __name__ == "__main__":
    main()
