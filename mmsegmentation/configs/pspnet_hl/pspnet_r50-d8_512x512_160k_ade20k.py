_base_ = [
    '../_base_/models/pspnet_r50-d8.py', '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
]
model = dict(
    type='WeightedEncoderDecoder',
    decode_head=dict(num_classes=150,loss_decode=dict(reduction='none')), auxiliary_head=dict(num_classes=150))

