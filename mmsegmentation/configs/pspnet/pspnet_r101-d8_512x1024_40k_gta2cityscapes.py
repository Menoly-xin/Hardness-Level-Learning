_base_ = './pspnet_r50-d8_512x1024_40k_gta2cityscapes.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
lr_config=dict(
        _delete_=True,
        policy='poly',
        warmup='linear',
        warmup_iters=1000,

