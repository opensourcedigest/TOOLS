import pathlib

# Python3 批量修改指定目录下文件名
# 适用于将指定目录下的大批量文件名中相同字符串，替换或者删除

my_dir = "d:\\New_Caillou\\"
my_path = pathlib.Path(my_dir)

count = 0
for x in my_path.iterdir():
    old_name = x.name  # 取出旧文件名
    # 将就文件名中的指定字符串替换，
    # 如果需要替换的字符比较复杂，可以考虑使用正则表达式
    new_name = old_name.replace("【高清英语资源】[www.xuebu.co]", "")
    # 构造新的文件名，和要保存的路径
    new_name = my_dir + new_name
    x.rename(new_name)
    count = count + 1
print("共{}个文件被成功重命名".format(count))
