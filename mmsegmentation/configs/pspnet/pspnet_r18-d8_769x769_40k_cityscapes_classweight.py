_base_ = './pspnet_r50-d8_769x769_40k_cityscapes.py'
model = dict(
    pretrained='open-mmlab://resnet18_v1c',
    backbone=dict(depth=18),
    decode_head=dict(
        in_channels=512,
        channels=128,
        loss_decode=dict(class_weight=[0.8373, 0.9180, 0.8660, 1.0345, 1.0166, 0.9969, 0.9754,
                                    1.0489, 0.8786, 1.0023, 0.9539, 0.9843, 1.1116, 0.9037,
                                                            1.0865, 1.0955, 1.0865, 1.1529, 1.0507])
    ),
    auxiliary_head=dict(in_channels=256, channels=64))
