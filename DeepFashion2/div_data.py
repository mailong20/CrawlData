import os
# from filter_data import filterbysub
path = r'E:\Dataset_Fashion\cc'
arrname = os.listdir(path)
import shutil
for p in arrname:
  print(p)
  data_train = []
  data_vail = []
  path_sub = os.path.join(path, p)
  arr_path_sub= os.listdir(path_sub)
  for p_ in ['train', 'valid']:
    path_data = os.path.join(path_sub, p_)
    arr_path_ = os.listdir(path_data)
    # print(arr_path_)
    path_images = os.path.join(path_data, arr_path_[0])
    path_labels = os.path.join(path_data, arr_path_[1])
    arr_images = os.listdir(path_images)
    arr_images = [os.path.join(path_images, path_image) for path_image in arr_images ]
    arr_labels = os.listdir(path_labels)
    arr_labels = [os.path.join(path_labels, path_label) for path_label in arr_labels ]
    if p_ =='train':
      data_train.append(arr_images)
      data_train.append(arr_labels)
    else:
      data_vail.append(arr_images)
      data_vail.append(arr_labels)
  import random
  print(data_train[0][:10])
  train_images = data_train[0]
  random.shuffle(train_images)
  random.shuffle(train_images)
  random.shuffle(train_images)
  sum_ex = len(train_images)
  sum_vail = int(sum_ex* 0.2)-67
  vail_data = train_images[:sum_vail]
  for vail_image in vail_data:
    # id_image = vail_image.split('\\')[-1].split('.')[0]
    print(vail_image)
    vail_label = vail_image.replace('jpg', 'xml').replace('images', 'labels')
    shutil.move(vail_image, 'E:/Dataset_Fashion/cc/cc/valid/images')
    shutil.move(vail_label, 'E:/Dataset_Fashion/cc/cc/valid/labels')