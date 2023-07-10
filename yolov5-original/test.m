clc;
clear all;
command = 'python train.py --data spine.yaml --weights yolov5s.pt';
[status,cmdout] = system(command)
% python train.py --data spine.yaml --weights yolov5s.pt