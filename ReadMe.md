

## The Whole Process of Stereo Camera Calibration 

### devices：
mindvision工业黑白相机，信号为MV-MSU130GM2-T

### why？
yaml配置文件支持多种不同语言读取数据，为了利用其方便、易读、快速的性质，编写脚本存放在此仓库，对matlab下双目相机标定的保存数据（mat文件）进行脚本式转化。

### QS
- step1: 使用mindvision演示程序采集标定图片，设置图片大小(建议为1280x2560），保存在Pictures文件夹；
- step2: 运行脚本`split_pictures.py`，完成图片切割；
- step3: 使用MATLAB相机标定工具箱（Stereo Camera Calibrator，棋盘格大小为35mm）；如图设置：
![img.png](Src/setupParams.png)
- step4: 标定完成后，在工作区导出stereoParams，运行`processStereoParams.m`，得到CameraParams.mat；
- step5: 运行脚本`writeYaml.py`，生成新的相机配置文件`camera_paras.yaml`

### FD-文件描述和处理流程

对主文件夹中各文件/脚本的文件说明:
处理流程：图片 -> `split_picture.py` -> matlab双目标定 ->  `processStereoParams.m` -> `writeYaml.py` -> 生成相机参数yaml文件，处理完成

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

### 特别说明
在生成当中的`yaml`文件当中，没有单独列出基线长度，基线长度为外参平移向量当中的第一个元素（取绝对值）





