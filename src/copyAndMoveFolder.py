import os
import shutil
import time
from tqdm import tqdm



# 源文件夹文件数量
sourceFileCount = 0;
# 目标文件夹已存在文件数量
existsFileCount = 0;
#  拷贝的文件的数量
copyFileCount = 0;
# 计算操作的文件的数量
files_count = 0;

# 计算文件夹下文件的数量
def count_folder_files (source_folder):
  num = 0; # 文件数量
  if not os.path.isdir(source_folder):
    return 0;

  for item in os.listdir(source_folder):
    src_item = os.path.join(source_folder, item)
    if os.path.isdir(src_item):
      num += count_folder_files(src_item);
    else:
      num += 1;

  return num;

# 计算多个文件夹下文件的总数量
def count_folders_files(folders_path):
  files_count = 0;
  # 计算源文件数量
  for source_Path in source_filePath:
    files_count += count_folder_files(source_Path);
  return files_count;

# 文件夹深拷贝
def merge_folders(source_folder, destination_folder):
    global files_count, sourceFileCount, existsFileCount, copyFileCount, pBar

    if not os.path.exists(destination_folder):     #目标文件夹不存在就新建
      os.makedirs(destination_folder)

    # 遍历源文件夹中的所有子文件夹和文件
    for item in os.listdir(source_folder):

        # 构建源文件或文件夹的路径
        src_item = os.path.join(source_folder, item)
        # 构建目标文件或文件夹的路径
        dest_item = os.path.join(destination_folder, item)

        # 判断是否是文件夹
        if os.path.isdir(src_item):

          #目标文件夹不存在就新建一个目标文件夹
          if not os.path.exists(dest_item):
            os.makedirs(dest_item);

          # 如果是文件夹，则递归调用merge_folders函数合并子文件夹
          merge_folders(src_item, dest_item)
        else:
            # 已经处理过的文件的数量+1;
            sourceFileCount = sourceFileCount + 1;
            # 任务进度条更新
            pbar.update(1)
            # 如果是文件 且目标文件夹下没有对应的文件路径的文件 
            # 则将该文件拷贝到对应的文件夹下 拷贝的文件数量 +1
            if not os.path.exists(dest_item):
              # 目标文件夹没有对应文件 拷贝文件数量加1
              copyFileCount = copyFileCount + 1;
              shutil.copy2(src_item, dest_item)  # 使用shutil.copy2保留文件元数据（如创建时间）
              time.sleep(0.001);
            else:
              # 目标文件夹对应层级已经有对应文件 已存在文件的重复的文件数量 + 1
              existsFileCount = existsFileCount + 1;
              time.sleep(0.001);

# 多个文件夹拷贝
def merge_folders_to_target_Folder(source_folders, destination_folder):
  for source_folder in source_folders:
     merge_folders(source_folder, destination_folder)

# 源文件夹
source_filePath = [
  os.path.abspath(r'/Users/bailing/code/python/test/data/testData/part1'),
  os.path.abspath(r'/Users/bailing/code/python/test/data/testData/part2')
]

# 目标文件夹
target_Path = os.path.abspath(r'/Users/bailing/code/python/test/result/image')

# 目标文件夹文件数量
result_Folder_Files_count = 0;
result_Folder_Files_count += count_folder_files(target_Path);
print("目标文件夹文件的数量:",result_Folder_Files_count);

# 操作的源文件的数量
files_count = count_folders_files(source_filePath);
print("操作的源文件的数量为:", files_count);

with tqdm(total=files_count, desc='文件拷贝进度', unit="img", leave=True ) as pbar:
  merge_folders_to_target_Folder(source_filePath, target_Path);

print("\n======================================文件操作处理结果统计======================================\n");
print("文件数量为:", sourceFileCount);
print("已存在文件数量为:", existsFileCount);
print("拷贝文件数量为:", copyFileCount);

print('文件夹内容拷贝合并完成');