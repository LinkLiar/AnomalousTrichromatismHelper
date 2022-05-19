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

A New Color Blindness Cure Model Based on BP Neural Network
Visual contents adaptation for colour vision deficiency
A fixed transformation of color images for dichromats based on similarity matrices

准备知识：
LSM颜色空间
人眼LSM视锥细胞
原理：颜色空间几何变换映射

图像处理四种矫正色盲的算法：
自适应的矫正算法
旋转H分量的矫正算法
几何变换的矫正算法
角度自适应的矫正算法


1．按使用类别分类

彩色色度学模型：CIE-RGB、CIE-XYZ、均匀色差彩色模型（CIE 1976Luv和CIE Lab）

工业彩色模型：RGB彩色显示模型、CMYK彩色印制模型、彩色传输模型YUV（PAL）、YIQ（NTSC）、YCrCb（数字高清晰度电视）

视觉彩色模型：HVC（孟赛尔）、HSB（Photoshop）、HLS（Windows画图和Apple Color Picker）、HSI（图像分割）、HSY（电视）、Ohta（图像分割）等。

2．按颜色感知分类

混合颜色模型：按3种基色的比例混合而成的颜色。RGB、CMYK、XYZ等

非线形亮度/色度颜色模型：用一个分量表示非色彩的感知，用两个分量表示色彩的感知，这两个分量都是色差属性。L*a*b、L*u*v、YUV、YIQ等。

强度/饱和度/色调模型：用强度描述亮度或灰度等光强的感知，用饱和度和色调描述色彩的感知，这两个分量接近人眼对颜色的感觉。如HIS、HSL、HSV、LCH等


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


#include <opencv2\opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

Mat RGB2LAlphBeta(Mat3b &src)
{
    Mat3f L_AlphBeta(src.rows, src.cols);
    //cvtColor(src,dest,CV_BGR2XYZ);
    float X, Y, Z, L, M, S, _L, Alph, Beta;
    int R, G, B;
    for (int i = 0; i < src.rows; i++)
    {
        for (int j = 0; j < src.cols; j++)
        {
            B = src(i, j)[0];
            G = src(i, j)[1];
            R = src(i, j)[2];
            
            X = (0.4124 * R) + (0.3576 * G) + (0.1805 * B);
            Y = (0.2126 * R) + (0.7152 * G) + (0.0722 * B);
            Z = (0.0193 * R) + (0.1192 * G) + (0.9505 * B);
            L = (0.3897 * X) + (0.6890 * Y) + (-0.0787 * Z);
            M = (-0.2298 * X) + (1.1834* Y) + (0.0464 * Z);
            S = (0.0000 * X) + (0.0000 * Y) + (1.0000 * Z);

            //for handling log
            if (L == 0.0000) L = 1.0000;
            if (M == 0.0000) M = 1.0000;
            if (S == 0.0000) S = 1.0000;


            //LMS to Lab
            _L = (1.0 / sqrt(3.0)) *((1.0000 * log10(L)) + (1.0000 * log10(M)) + (1.0000 * log10(S)));
            Alph = (1.0 / sqrt(6.0)) * ((1.0000 * log10(L)) + (1.0000 * log10(M)) + (-2.0000 * log10(S)));
            Beta = (1.0 / sqrt(2.0)) * ((1.0000 * log10(L)) + (-1.0000 * log10(M)) + (-0.0000 * log10(S)));

            L_AlphBeta(i, j)[0] = _L;
            L_AlphBeta(i, j)[1] = Alph;
            L_AlphBeta(i, j)[2] = Beta;
        }
    }

    return L_AlphBeta;
}

Mat LAlphBeta2RGB(Mat3f &src)
{
    Mat3f XYZ(src.rows, src.cols);
    Mat3b BGR(src.rows, src.cols);

    float X, Y, Z, L, M, S, _L, Alph, Beta;
    for (int i = 0; i < src.rows; i++)
    {
        for (int j = 0; j < src.cols; j++)
        {
            _L = src(i, j)[0] * 1.7321;
            Alph = src(i, j)[1] * 2.4495;
            Beta = src(i, j)[2] * 1.4142;

            /*Inv_Transform_logLMS2lab =

            0.33333   0.16667   0.50000
            0.33333   0.16667  -0.50000
            0.33333  -0.33333   0.00000*/
            L = (0.33333*_L) + (0.16667 * Alph) + (0.50000 * Beta);
            M = (0.33333 * _L) + (0.16667 * Alph) + (-0.50000 * Beta);
            S = (0.33333 * _L) + (-0.33333 * Alph) + (0.00000* Beta);

            L = pow(10, L);
            if (L == 1) L = 0;
            M = pow(10, M);
            if (M == 1) M = 0;
            S = pow(10, S);
            if (S == 1) S = 0;
            /*Inv_Transform_XYZ2LMS

            1.91024  -1.11218   0.20194
            0.37094   0.62905   0.00001
            0.00000   0.00000   1.00000*/

            X = (1.91024 *L) + (-1.11218 * M) + (0.20194 * S);
            Y = (0.37094 * L) + (0.62905 * M) + (0.00001 * S);
            Z = (0.00000 * L) + (0.00000 * M) + (1.00000 * S);
            /*Inv_Transform_RGB2XYZ
            3.240625  -1.537208  -0.498629
            -0.968931   1.875756   0.041518
            0.055710  -0.204021   1.056996*/

            BGR(i, j)[2] = saturate_cast<uchar>((3.240625 * X) + (-1.537208 * Y) + (-0.498629 * Z));
            BGR(i, j)[1] = saturate_cast<uchar>((-0.968931 * X) + (1.875756 * Y) + (0.041518 * Z));
            BGR(i, j)[0] = saturate_cast<uchar>((0.055710 * X) + (-0.204021 * Y) + (1.056996 * Z));
        }
    }
    //normalize(BGR,BGR, 255, 0, NORM_MINMAX, CV_8UC3 );
    return BGR;
}


int main()
{
    Mat3b img = imread("path_to_image");

    Mat3f labb = RGB2LAlphBeta(img);

    Mat3b rgb = LAlphBeta2RGB(labb);

    Mat3b diff;
    absdiff(img, rgb, diff);

    // Check if all pixels are equals
    cout << ((sum(diff) == Scalar(0, 0, 0, 0)) ? "Equals" : "Different");

    return 0;
}

https://blog.51cto.com/u_15353042/3751269

https://chaphlagical.icu/DIP/index/report1.pdf

https://arxiv.org/pdf/1711.10662.pdf

https://blog.css8.cn/post/18674723.html

https://wikichi.icu/wiki/LMS_color_space
https://wikichi.icu/wiki/chromatic_adaptation

https://yylifen.github.io/color-from-hexcodes-to-eyeballs/color/chapter/ch11.html