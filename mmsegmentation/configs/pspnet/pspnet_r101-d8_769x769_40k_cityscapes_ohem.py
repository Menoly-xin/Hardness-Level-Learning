_base_ = './pspnet_r50-d8_769x769_40k_cityscapes.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101),
        decode_head = dict(sampler=dict(type='OHEMPixelSampler', thresh=0.7, min_kept=100000)))
