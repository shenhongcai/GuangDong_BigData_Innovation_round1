# 运行环境：
    操作系统(os)：ubuntu14.04.5
    python版本： python3.5.2
    packages ：  pandas 0.23.4; 
                pillow 5.2.0;  
                numpy 1.15.1; 
                tqdm 4.26.0;  
                sklearn 0.20.0; 
                torch 0.4.1;
                pretrainedmodels  0.7.0;
                opencv-python 3.4.3.18
# 算法模型

本设计使用了谷歌推出的nasnet开源模型
下载链接： （https://github.com/AkatsukiCC/pretrained-models.pytorch）
参考文献：Zoph B, Vasudevan V, Shlens J, et al. Learning Transferable Architectures for Scalable Image Recognition[J]. 2017.
本设计为单模型，没有使用模型融合，nasnet为我们的核心网络模型

# 数据集说明：

  由于原始数据集存在数据不均衡，标注错误，某些类别下数据差异过大（如擦花（defect2），脏点（defect10），其他（defect11）），我们对原始数据集做了一下处理。
  
  ## 一， 删除掉错误标注图片
  
        如guangdong_round1_train2_20180916中擦花类别中的图片(擦花20180830164545对照样本.jpg)
        
  ## 二， 对某些类别做了更细的划分
|项目|说明|
| ---- | ---- |
|1.对于擦花类别，我们将其细分为3个新类别:|  擦花1(defect2):细长条形的擦伤；擦花2(defect12):伤口面积较宽，伤口较浅的擦伤，擦花3(defect16):黄色长条铝合金上分布较广的擦伤|
|2.对于凸粉，我们将其细分为2个新类别:|凸粉1（defect8）：长条形香槟金色铝合金；凸粉2 （defect14）：乳白色铝合金|
|3.对于脏点，我们将其细分为3个新类别:|脏点1 （defect10）：铝合金面积较大且脏点明显突出的样本 脏点2 (15):长条形铝合金且脏点defect分散，脏点不明显的样本；脏点3  （defect17）：为铝合金面积较大且脏点不明显的样本;脏点2   (defect15)  :  长条形铝合金且脏点分散，脏点不明显的样本|
|4.对于其他类，我们将其细分为2个新类别:|其他1 （defect11）：除去划伤外的所有其他;其他2（defect13）：其他类中的划伤类别|
             
  ## 三， 由于数据不均衡，我们对不同类别做了不同程度的扩充
        我们主要使用了对比度，亮度调整，随机角度旋转，水平，垂直镜像的手段对数据集进行了扩充，具体实现见code下
             bright_And_contrast_Enhance.py
             image_mirror_v2.py
             imageRotate.py
    以guangdong_round1_train2_20180916文件中的norm类别为基准(1018张)，每个类别下的图片通过数据增强后数目如下
    
### 调整

|瑕疵类型|数量|                                              
| -- | -- |                                                 
|defect1(不导电)|846|
|defect2(擦花1)|702|
|defect3(横条压凹)|741|
|defect4(桔皮)|747|
|defect5(漏底)|794|
|defect6(碰伤)|748|
|defect7(起坑)|735|
|defect8(凸粉1)|807|
|defect9(涂层开裂)|843|
|defect10(脏点1)|456|
|defect11(其他1)|1136|
|defect12(擦花2)|456|
|defect13(其他2)|560|
|defect14(凸粉2)|118|
|defect15(脏点2)|630|
|defect16(擦花3)|648|
|defect17(脏点3)|608|
|norm|1018|


# 瑕疵样例

| 瑕疵名称 |瑕疵图片示例 |
| ------ | ------ |
| 擦花（擦伤） |![](https://github.com/shenhongcai/ImageStore/blob/master/cahua.png)|
| 杂色 | ![](https://github.com/shenhongcai/ImageStore/blob/master/zase.png)|
| 漏底 | ![](https://github.com/shenhongcai/ImageStore/blob/master/loudi.png)|
| 不导电 | ![](https://github.com/shenhongcai/ImageStore/blob/master/budaodian.png)|
| 橘皮 | ![](https://github.com/shenhongcai/ImageStore/blob/master/jupi.png)|
| 喷流 | ![](https://github.com/shenhongcai/ImageStore/blob/master/penliu.png)|
| 漆泡 | ![](https://github.com/shenhongcai/ImageStore/blob/master/qipao.png)|
| 起坑 | ![](https://github.com/shenhongcai/ImageStore/blob/master/qikeng.png) |
| 脏点 | ![](https://github.com/shenhongcai/ImageStore/blob/master/zangdian.png) |
| 角位漏底 | ![](https://github.com/shenhongcai/ImageStore/blob/master/jiapweiloudi.png)|


# 数据集下载链接

https://tianchi.aliyun.com/competition/entrance/231682/information


