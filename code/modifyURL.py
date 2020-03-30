import os
import io
import sys

def modifyURL(file): 
    print('filename:%s' % file)
    content = ""
    with io.open(os.path.join(file_dir, file), "r", encoding="utf-8", errors='ignore') as f:
        for line in f:
            # 替换链接
            if old_str in line:
                line = line.replace(old_str, new_str)
                print(line)
            # 替换shortcode
            if line.startswith('{% qnimg'):
                line = line.replace('{% qnimg', '')
                line = line.replace('%}', '')
                line = line.replace(' ', '')
                line = '![](' + new_str + line.strip('\n') + ')' + '\n'
                print(line)
            content += line
    with io.open(os.path.join(file_dir, file), "w", encoding="utf-8", errors='ignore') as f:
        f.write(content)

# 确认目录
file_dir = sys.path[0].replace('\\', '/')
file_dir = input('当前目录为' + file_dir + '，请输入工作目录或直接回车在当前目录执行')
if file_dir == '':
    file_dir = sys.path[0].replace('\\', '/')
else:
    if not os.path.exists(file_dir):
        print('目录无效，请确认后重试')
        os._exit(0)

print('请输入除图片名外完整的图片外链链接')
old_str = input('旧链接(格式为 http://q6735zi7x.bkt.clouddn.com/static/images/ )：')
new_str = input('新链接(格式为 http://img.osland.me/static/images/ ):')
comfirm = ''
while comfirm != 'y':
    comfirm = input(file_dir + '中所有Markdown文件的' + old_str + '会被替换为' + new_str + '，输入y后回车确认')

# 遍历目录下文件
for folder, subFolder, filenames in os.walk(file_dir):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.md':
            # 执行URL修改
            modifyURL(filename)

print('完成')
