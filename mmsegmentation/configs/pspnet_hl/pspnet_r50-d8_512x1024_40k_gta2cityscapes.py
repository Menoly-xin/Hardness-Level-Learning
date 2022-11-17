_base_ = [
    '../_base_/models/pspnet_r50-d8_weight.py', '../_base_/datasets/gta_to_cityscapes_512x1024.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
