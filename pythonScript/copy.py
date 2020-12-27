import shutil
import os
import tkinter as tk
import win32api

class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.project_name = "S630Ajax"
        self.java_project_dir = r"D:\File\Java\SXT\07"
        self.tomcat_project_dir = r"D:\File\Java\Tomacat\apache-tomcat-9.0.37"
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        """
        定义按钮
        """
        self.btn01 = tk.Button(root, text = "启动服务", width = 7, height = 2, command = self.startup)
        self.btn02 = tk.Button(root, text = "停止服务", width = 7, height = 2, command = self.shutdown)
        self.btn03 = tk.Button(root, text = "加载文件", width = 7, height = 2, command = self.load_file)
        self.btn01.pack(side = "left", padx = "10")
        self.btn02.pack(side = "left", padx = "10")
        self.btn03.pack(side = "left", padx = "10")

    def startup(self):
        """
        开启服务
        """
        file_path = self.tomcat_project_dir + r'\bin\startup.bat'
        result = win32api.ShellExecute(0, 'open', file_path, '', '', 0)
        if (result > 32):
            print("服务启动:" + str(result))

    def shutdown(self):
        """
        停止服务
        """
        file_path = self.tomcat_project_dir + r'\bin\shutdown.bat'
        result= win32api.ShellExecute(0, 'open', file_path, '', '', 0)
        if (result > 32):
            print("服务关闭:" + str(result))

    def load_file(self):
        """
        导入文件
        """
        pass
        # self.load_xml_file()
        self.load_class_file()
        self.load_web_file()

    def load_xml_file(self):
        """
        导入web.xml文件
        """
        print(self.project_name)
        file_source_directory = self.java_project_dir + "\src\{0}\web.xml".format(self.project_name)
        file_destination_directory = r"D:\File\Java\Tomacat\apache-tomcat-9.0.37\webapps\FengTai\WEB-INF"
        shutil.copy(file_source_directory, file_destination_directory)

    def load_class_file(self):
        """
        导入class文件
        """
        file_source_directory = self.java_project_dir + "\\bin\{0}".format(self.project_name)
        file_destination_directory = self.tomcat_project_dir + "\webapps\FengTai\WEB-INF\classes\{0}".format(self.project_name)
        file_type = ["class"]
        self.getDirAndCopyFile(file_source_directory, file_destination_directory, file_type)

    def load_web_file(self):
        """
        导入Web文件
        """
        file_source_directory = self.java_project_dir + "\src\{0}".format(self.project_name)
        file_destination_directory = self.tomcat_project_dir + "\webapps\FengTai\{0}".format(self.project_name)
        file_type = ["jsp", "css", "js", "jpg", "ico", "png", "gif"]
        self.getDirAndCopyFile(file_source_directory, file_destination_directory, file_type)

    def getDirAndCopyFile(self, sourcePath,targetPath,file_type):
        """
        利用递归实现目录的遍历
        @para sourcePath:原文件目录
        @para targetPath:目标文件目录
        """
        if not os.path.exists(sourcePath):
            return
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        for fileName in os.listdir(sourcePath):
            absourcePath = os.path.join(sourcePath, fileName)
            abstargetPath = os.path.join(targetPath, fileName)
            if os.path.isdir(absourcePath):
                if (not os.path.exists(absourcePath)):
                    os.makedirs(abstargetPath)
                self.getDirAndCopyFile(absourcePath, abstargetPath, file_type)
            if os.path.isfile(absourcePath) and (absourcePath.split(".")[-1] in file_type):
                print("复制文件:" + absourcePath)
                rbf = open(absourcePath, "rb")
                wbf = open(abstargetPath, "wb")
                while True:
                    content = rbf.readline(1024*1024)
                    if len(content)==0:
                        break
                    wbf.write(content)
                    wbf.flush()
                rbf.close()
                wbf.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("240x50+1110+640")  # 窗口大小(长*宽+距离屏幕左边+距离屏幕上边)
    root.title("Tomcat")  # 标题
    app = Application(master = root)
    root.mainloop()
