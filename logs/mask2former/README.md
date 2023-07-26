Mask2Former results on using the HL map obtained from PSPNet.

## ADE20K
| Method    | Backbone     | Crop Size | mIoU (paper) | mIoU (mmseg official) | mIoU (our, based on mmseg)|
|-----------|--------------|-----------|--------------|-----------------------|--------------------------|
|Mask2Former| Swin-T       | 512x512   | 47.7         |    [48.66](https://download.openmmlab.com/mmsegmentation/v0.5/mask2former/mask2former_swin-t_8xb2-160k_ade20k-512x512/mask2former_swin-t_8xb2-160k_ade20k-512x512_20221203_234230.json)              | [49.67](20230725_165931.log)                    |
|Mask2Former| Swin-B(in22k)| 640x640   | -            |    [53.90](https://download.openmmlab.com/mmsegmentation/v0.5/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-160k_ade20k-640x640/mask2former_swin-b-in22k-384x384-pre_8xb2-160k_ade20k-640x640_20221203_235230.json)              | [54.51](20230724_075547.log)                    |
|Mask2Former| Swin-L(in22k)| 640x640   | 56.1         |    [56.01](https://download.openmmlab.com/mmsegmentation/v0.5/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-160k_ade20k-640x640/mask2former_swin-b-in22k-384x384-pre_8xb2-160k_ade20k-640x640_20221203_235230.json)              | [56.31](20230723_221527.log)                    |

