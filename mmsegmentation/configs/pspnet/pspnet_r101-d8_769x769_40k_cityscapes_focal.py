_base_ = './pspnet_r50-d8_769x769_40k_cityscapes_focal.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101) )
