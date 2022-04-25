# AnomalousTrichromatismHelper
Help anomalous trichromatism to pass the test
考虑算法所使用的颜色空间  
学习不同色弱/色盲的分辨力区别
考虑帮助色弱/色盲分辨观看图像的UI设计
考虑Mobile端分析颜色RGB模式及色盲模式的算法设计
考虑Mobile端的UI设计  

Desktop端实现思路：Python + OpenCV
Mobile端实现思路：Android studio + OpenCV-Android-SDK (Java!!!)
先从调用手机摄像头开始，后熟悉OpenCV-Android-SDK的Sample
先从色盲/色弱的理论知识先准备。 

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD201501&filename=1015000121.nh&uniplatform=NZKPT&v=zNnYlDi0QOBXTNqKVPiVTocDXTR-XQsF4kmbRXDaxQWv3fMiLuDsALQ7PzGLt_jL

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD2012&filename=1011194956.nh&uniplatform=NZKPT&v=g3BuGagE3d9R3Lbesew953aDMEWYMqwZSlLwURWJasCaxKlGzXurpXKJELJsa4HQ

https://kns.cnki.net/kcms/detail/detail.aspx?filename=WDZC201715021&dbcode=CJFD&dbname=CJFD2017&v=k5uzzrJrowZTTp5wuD11rqUeBekD4XUgFb97FO8kcnJxpOwNuWGhX6aJG9E3_zwV

---------------------------------------------------------------------------
https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD202201&filename=1021805320.nh&uniplatform=NZKPT&v=ihnSnJodNOjO8ZUD25O1IdrNpqWG8U1wq80AlS5xKWlYBlvydbCCqXOh4x2aSXwF

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDZHYX&filename=ZXYK202105013&uniplatform=NZKPT&v=4p01ZP2JHMWGgudOD18A-uP8RF3kMmnn7hksmnUCE7QqvdusM0YgxI8o5n1j5GvM

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2017&filename=XTYY201703034&uniplatform=NZKPT&v=rc4DAFnHvdL9a2AiJMCfO7rkAjZCGCxKCZdTMgsu4OxBJycNH9mQY0Ji2gR8rxZr

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD201501&filename=1014385313.nh&uniplatform=NZKPT&v=l7pP05OFmhEbEzyI-cQ6H2NYUDy0Wp3nzGjQDmVXA1Cp8drwdAKPliFFCmRjxArO

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD201501&filename=1015000121.nh&uniplatform=NZKPT&v=zNnYlDi0QOBXTNqKVPiVTocDXTR-XQsF4kmbRXDaxQXW2Tq9-kBxbCtq5Ycnw43Z

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD2009&filename=2009182512.nh&uniplatform=NZKPT&v=-bUEB_7KxKtJS1el1YbIjztn-eLyxnAiOOVRGfjqHgYJBQZcdviJ_qpSXOpOMMYs

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFD2008&filename=SHYC200803003&uniplatform=NZKPT&v=XGiHIxJshI-MGm0mrKTXjypyYEtAHoO8cAKtwko_7TH0HHoUDsJTT5tBQbWTyvP2

https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD2012&filename=1011194956.nh&uniplatform=NZKPT&v=g3BuGagE3d9R3Lbesew953aDMEWYMqwZSlLwURWJasA4Xxei9nSlxPsiAqr0AJ5W


准备知识：
LSM颜色空间
人眼LSM视锥细胞
原理：颜色空间几何变换映射

1.全色盲
全色盲是色盲中最为严重的，也是极为少见的一种色盲，属于完全性视锥细胞功能障碍（三种锥细胞缺失），与夜盲（视杆细胞功能障碍）恰好相反，患者尤喜暗、畏光，表现为昼盲。
全色盲不能识别颜色，只能感知亮度信息，七彩世界在其眼中是一片灰暗，如同观黑白电视一般仅有明暗之分，而无颜色差别。
而且所见红色发暗、蓝色光亮、此外还有视力差、弱视、中心性暗点、摆动性眼球震颤等症状。

2.红二色盲
又称第一色盲，是由于L锥细胞的缺失造成的。患者主要是不能分辨红色。对(红色与深绿色)、(蓝色与紫红色以及紫色)不能分辨。
常把(绿色视为黄色)，(紫色看成蓝色)，将((绿色和蓝色相混)为白色)。

3.绿二色盲
又称第二色盲，是由于M锥细胞的缺失造成的。患者不能分辨(淡绿色与深红色)、(紫色与青蓝色)、(紫红色与灰色)，把(绿色视为灰色或暗黑色)。
临床上把红二色盲与绿二色盲统称为红绿色盲，患者较常见,平常说的色育一般就是指红绿色盲。

4.蓝二色盲
又称第三色盲，是由于S锥细胞的缺失造成的。患者(蓝黄色混淆不清），对红、绿色可辨，较少见。

5.全色反
又称三原色盲，也是所有色盲病中较严重的一种视觉障碍。现实世界在其眼睛中如同一幅底片，患者将(红色视为绿色)，(黑色视为白色Z)，所有看到的颜色与现实完全相反。

5.色弱
色弱又叫三色觉异常，是色盲中最轻的一种，患者一般感知不到自己有色觉问题，只有通过专业的色觉测试才能发现。
三色觉异常是三种锥细胞的一种变异造成的，其中L锥细胞的变异对应红色弱，M锥细胞的变异对应绿色弱，S锥细胞的变异对应蓝色弱。
色弱表现为对部分颜色区分力的降低，红色弱和绿色弱对颜色的区分能力相近，都是对红、绿颜色的区分能力下降，而蓝色弱是对蓝、绿颜色的区分能力下降。

色盲矫正镜的原理：是根据补色拓扑学原理，在镜片土进行特殊镀膜，产生截止波长的作用。
对长波长者可透射，对短波长者发生反射。色盲患者戴上色盲眼镜，可在一定程度上使原来辨认不清的图案变为能正确辨认，达到矫正色觉障碍的效果。
实际上，这种方式只是对色彩进行简单的滤除，并不能达到很好矫正的目的。


