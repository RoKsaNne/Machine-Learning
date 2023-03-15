# Object Detection

## R-CNN
Selective Search finding region proposals in the input image.
      Regions of Interest(RoI) from a prrposal method(~2k)
Use as input of CNN, classify regions with SVMs, Linear Regression for bounding box offsets. 

Problems:
      Training is slow
      Inference is slow

## Fast R-CNN
Forward whole image through CNN (shared convelution), find RoI in the feature map.

RoI Pooling Layer (Get same sized RoI) => Connect to FCs => Softmax classifier + Bounding-nox regressor

Problems: Slow when finding RoIs, runtime dominated by region proposals

## Faster R-CNN (Two-stage)
Use CNN do proposals. Insert Region Proposal Network (RPN) to predict proposals from features

Jointly train with 4 losses:
      1. RPN classify object / not object | Classification loss
      2. RPN regress box coordinates | Bounding-box regression loss
      3. Final classification score (object classes) | Classification loss
      4. Final box coordinates | Bounding-box regression loss

Resize -> RestNet/VGG extract feature -> Feature Map(38\*38\*1024) + Proposal -> ROI Pooling
                                          -> Convelution -> Proposal  
                                          