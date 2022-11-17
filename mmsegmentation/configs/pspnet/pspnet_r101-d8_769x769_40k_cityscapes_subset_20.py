_base_ = './pspnet_r50-d8_769x769_40k_cityscapes.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
data = dict(
        train = dict(data_root = 'data/cityscapes_subset'),
        val = dict(
                data_root = 'data/cityscapes_subset'))
runner = dict(type='IterBasedRunner', max_iters=20000)
checkpoint_config = dict(by_epoch=False, interval=4000)
evaluation = dict(interval=4000, metric='mIoU', pre_eval=True)
