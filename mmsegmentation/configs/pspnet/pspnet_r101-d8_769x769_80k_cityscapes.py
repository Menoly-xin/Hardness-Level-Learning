_base_ = './pspnet_r50-d8_769x769_80k_cityscapes.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
data = dict(
        samples_per_gpu=6,
        workers_per_gpu=6,)
