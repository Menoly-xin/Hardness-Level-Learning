_base_ = './pspnet_r50-d8_769x769_40k_cityscapes.py'
model = dict(pretrained='open-mmlab://resnext101_64x4d',
            backbone=dict(
                type='ResNeXt',
                depth=101,
                groups=64,
                base_width=4,
                num_stages=4,
                dilations=(1, 1, 2, 4),
                strides=(1, 2, 1, 1),
                out_indices=(0, 1, 2, 3),
                norm_eval=False,
                style='pytorch',
                contract_dilation=True))
