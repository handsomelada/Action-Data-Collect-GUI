import os


def format_convert(data_path, anno_path):

    file_list = os.listdir(data_path)
    ann = []
    for i, dir in enumerate(file_list):
        file = os.listdir(data_path + '/' + dir)
        dir_name = '{r}/{f}'.format(r=data_path, f=dir)
        ann.append(dir_name + ' ')
        num_frame = str(len(file))
        ann.append(num_frame + ' ')
        anno = str(int(dir[-3:])) + '\n'
        ann.append(anno)
    print(ann)
    fp = open(anno_path, 'w')
    fp.writelines(ann)

if __name__ == '__main__':
    dataset_path = r'G:\data_collect\S001'
    annotation_path = 'annotation.txt'
    format_convert(dataset_path, annotation_path)
