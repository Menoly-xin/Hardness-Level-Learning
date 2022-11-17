| Method        | ResNet-18                        | ResNet-50                        | ResNet-101                        |
|:--------------|:---------------------------------|:---------------------------------|:----------------------------------|
| Cross-Entropy | [74.30](res18/crossentropy.json) | [78.68](res50/crossentropy.json) | [79.60](res101/crossentropy.json) |
| Balanced CE   | [74.21](res18/balanced-ce.json)  | [78.18](res50/balanced-ce.json)  | [79.16](res101/balanced-ce.json)  |
| OHEM CE       | [74.23](res18/ohem.json)         | [78.99](res50/ohem.json)         | [79.64](res101/ohem.json)         |
| Focal loss    | [73.35](res18/focal.json)        | [78.43](res50/focal.json)        | [78.95](res101/focal.json)        |
| HL            | [75.60](res18/hl.json)           | [79.58](res50/hl.json)           | [80.65](res101/hl.json)           |