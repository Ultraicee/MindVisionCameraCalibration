% 相机外参，以左相机为原点，则其T为单位阵
LeftRotation = eye(3);
LeftTranslation = zeros(3,1);
RightRotation = stereoParams.RotationOfCamera2';
RightTranslation = stereoParams.TranslationOfCamera2';
% 相机内参
LeftIntrinsic = stereoParams.CameraParameters1.IntrinsicMatrix';
RightIntrinsic = stereoParams.CameraParameters2.IntrinsicMatrix';
% 畸变系数
k = stereoParams.CameraParameters1.RadialDistortion;
r = stereoParams.CameraParameters1.TangentialDistortion;
disMl = [k(1), k(2), r, k(3)];
k = stereoParams.CameraParameters2.RadialDistortion;
r = stereoParams.CameraParameters2.TangentialDistortion;
disMr = [k(1), k(2), r, k(3)];
% 基础矩阵
F = stereoParams.FundamentalMatrix;
% 保存
save CameraParams.mat LeftRotation LeftTranslation RightRotation RightTranslation LeftIntrinsic RightIntrinsic disMl disMr F
