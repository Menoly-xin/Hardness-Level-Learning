_base_ = './pspnet_r50-d8_769x769_40k_cityscapes.py'
model = dict(
    pretrained='open-mmlab://resnet18_v1c',
    backbone=dict(depth=18),
    decode_head=dict(
        in_channels=512,
        channels=128,
        loss_decode=dict(type='FocalSoftmax')
    ),
    auxiliary_head=dict(in_channels=256, channels=64))
