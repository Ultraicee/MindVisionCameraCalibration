## The Whole Process of Stereo Camera Calibration 
### QS
- step1: 使用mindvision演示程序采集标定图片，设置图片大小(建议为1280x2560），保存在Pictures文件夹；
- step2: 运行脚本`split_pictures.py`，完成图片切割；
- step3: 使用MATLAB相机标定工具箱（Stereo Camera Calibrator，棋盘格大小为35mm）；如图设置：
![img.png](Src/setupParams.png)
- step4: 标定完成后，在工作区导出stereoParams，运行`processStereoParams.m`，得到CameraParams.mat；
- step5: 运行脚本`writeYaml.py`，生成新的相机配置文件`camera_paras.yaml`

### FD-文件描述

对`master`文件当中各文件/脚本的文件说明:

```
├── Output
│  ├── CameraParams.mat         # 脚本:processStereoParams.m 默认输出结果
│  ├── calibrationSession.mat   # (若存在),相机标定会话,包含标定过程的所有相机参数
│  └── camera_paras.yaml        # 生成的相机参数配置文件
├── ReadMe.md
├── Script
│  ├── file_input_output.py     # File Input and Output using XML and YAML files
│  ├── processStereoParams.m    # 处理导出到Matlab工作区的stereoParams并输出.
│  ├── split_picture.py         # 分割双目图像
│  └── writeYaml.py             # 写入配置文件
└── Src
  ├── Pictures                  # 默认采集到的图片读取位置
  ├── L                         # 默认分割后左相机的保存位置
  ├── R                         # 默认分割后右相机的保存位置
  └──writeYaml.py               # 写入配置文件
```





push test
