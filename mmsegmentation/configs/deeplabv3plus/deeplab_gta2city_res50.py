_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/gta_to_cityscapes_512x512.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)

optimizer = dict(
    _delete_=True,type='AdamW', lr=0.00006, betas=(0.9, 0.999), weight_decay=0.01)
