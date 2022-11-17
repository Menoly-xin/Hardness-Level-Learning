_base_ = [
    './upernet_swin_base_patch4_window12_640x640_160k_ade20k_pretrain_384x384_1K.py'
]

checkpoint_file = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/swin/swin_base_patch4_window12_384_22k_20220317-e5c09f74.pth'
crop_size = (640, 640)
#train_pipeline = [
#    dict(type='LoadImageFromFile'),
#    dict(type='LoadAnnotations', reduce_zero_label=True),
#    dict(type='Resize', img_scale=(2560, 640), ratio_range=(0.5, 2.0)),
#    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
#    dict(type='RandomFlip', prob=0.5),
#    dict(type='PhotoMetricDistortion'),
#    dict(type='Normalize', **img_norm_cfg),
#    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
#    dict(type='DefaultFormatBundle'),
#    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
#]
#test_pipeline = [
#    dict(type='LoadImageFromFile'),
#    dict(
#        type='MultiScaleFlipAug',
#        img_scale=(2560, 640),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
#        flip=False,
#        transforms=[
#            dict(type='Resize', keep_ratio=True),
#            dict(type='RandomFlip'),
#            dict(type='Normalize', **img_norm_cfg),
#            dict(type='ImageToTensor', keys=['img']),
#            dict(type='Collect', keys=['img']),
#       ])
#]

model = dict(pretrained=checkpoint_file,
        test_cfg=dict(mode='slide', crop_size=crop_size, stride=(426, 426)),)
