# 读取txt文件内容
with open('111.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

# 开始构建HTML内容
html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Converted Text</title>\n</head>\n<body>\n"

# 遍历每一行，将其转换为HTML段落
for line in content:
    if line.strip():  # 处理非空行
        html_content += f"<p>{line.strip()}</p>\n"
    else:  # 处理空行，转换为换行符
        html_content += "<br>\n"

# 关闭HTML标签
html_content += "</body>\n</html>"

# 将内容写入HTML文件
with open('url4.html', 'w', encoding='utf-8') as file:
    file.write(html_content)