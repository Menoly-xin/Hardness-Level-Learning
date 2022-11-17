_base_ = [
    '../_base_/models/pspnet_r50-d8.py', '../_base_/datasets/totaltext.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
model = dict(
    decode_head=dict(num_classes=2), auxiliary_head=dict(num_classes=2))
data_root = 'data/TextSeg/'
#dataset_type = 'TotalTextDataset'
data = dict(
    #samples_per_gpu=4,
    #workers_per_gpu=4,
    train=dict(
       # type=dataset_type,
        data_root=data_root,),
       # img_dir='images/Train',
       # ann_dir='annotations/Train',
       # pipeline=train_pipeline),
    val=dict(
        #type=dataset_type,
        data_root=data_root,),
        #img_dir='images/Test',
        #ann_dir='annotations/Test',
        #pipeline=test_pipeline),
    test=dict(
        #type=dataset_type,
        data_root=data_root,))
        #img_dir='images/Test',
        #ann_dir='annotations/Test',
        #pipeline=test_pipeline))
#evaluation = dict(metric=['mIoU', 'mFscore'])
