_base_ = './deeplab_gta2city_res50.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
