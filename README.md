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
人眼LSM椎细胞