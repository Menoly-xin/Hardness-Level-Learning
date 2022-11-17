_base_ = [
    '../_base_/models/upernet_r50.py',
    '../_base_/datasets/cityscapes_769x769.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
model = dict(
    pretrained='open-mmlab://resnet18_v1c',
    backbone=dict(depth=18,),
    decode_head=dict(in_channels = [64,128,256,512], channels = 128, align_corners=True),
    auxiliary_head=dict(in_channels=256, channels=64,align_corners=True),
    test_cfg=dict(mode='slide', crop_size=(769, 769), stride=(513, 513)))
