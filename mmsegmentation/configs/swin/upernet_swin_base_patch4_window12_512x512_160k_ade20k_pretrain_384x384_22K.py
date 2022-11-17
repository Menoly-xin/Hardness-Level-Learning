_base_ = [
    './upernet_swin_base_patch4_window12_512x512_160k_ade20k_'
    'pretrain_384x384_1K.py'
]
checkpoint_file = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/swin/swin_base_patch4_window12_384_22k_20220317-e5c09f74.pth'
model = dict(pretrained=checkpoint_file)
