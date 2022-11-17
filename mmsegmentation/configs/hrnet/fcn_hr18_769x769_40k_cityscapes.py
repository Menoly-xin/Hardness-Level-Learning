_base_ = [
    '../_base_/models/fcn_hr18.py', '../_base_/datasets/cityscapes_769x769.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
model = dict(test_cfg=dict(mode='slide', crop_size=(769, 769), stride=(513, 513)))