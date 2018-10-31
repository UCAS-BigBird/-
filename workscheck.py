import  cv2 as cv
import numpy as np
import playsound
import os
from aip import AipSpeech
import  sys


def ou(a):
    a=np.array(a)
    strs=''
    APP_ID = '14620723'
    API_KEY = 'QaL5c6aBuCagoYGi9VCpSQ9y'
    SECRET_KEY = 'EbYWrl0dFgfn5YV31V4sdmDG5GceIaey'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    if np.var(a)>10:
        max_g=0
        suttableh=0
        number1 = 0
        number5 = 0
        for i in range(a.min(),a.max()):
            bin_img=a>i;
            bin_img_reverse=a<=i;
            fore=np.sum(bin_img);
            after=np.sum(bin_img_reverse);
            w0=float(fore)/len(a);
            w1=float(after)/len(a);
            u0=float(np.sum(a*bin_img))/fore
            u1=float(np.sum(a*bin_img_reverse))/after
            g=w0*w1*(u0-u1)*(u0-u1)
            if(g>max_g):
                max_g=g
                suttableh=i
        for i in a:
            if i > suttableh:
                number1 += 1
            else:
                number5 += 1

        str1=""
        str1='一元硬币'+str(number1)+'个，5角硬币'+str(number5)+'个，总价值'+str(number1 + 0.5 * number5)+'元'
        print(str1)
        result = client.synthesis(str1, 'zh', 1, {'vol': 5, 'per': 0})
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            strs = 'audio' + sys.argv[1][0] + '.mp3'
            # if os.path.exists(strs):
            #     playsound.playsound(strs,block=False)
            # else:
            with open(strs, 'wb') as f:
                    f.write(result)
            playsound.playsound(strs,block=False)
    else:
        if a.min()<60:
            number5=len(a)
            str1=""
            str1='一元硬币0个,5角硬币'+str(number5)+'个'+',总价值'+str(0.5*number5)+'元'
            print(str1)
            result = client.synthesis(str1, 'zh', 1,{'vol': 5, 'per': 3})
            # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
            if not isinstance(result, dict):
                strs='audio'+sys.argv[1][0]+'.mp3'
                 # if os.path.exists(strs):
                 #     playsound.playsound(strs,block=False)
                 # else:
                with open(strs, 'wb') as f:
                         f.write(result)
                playsound.playsound(strs,block=False)
        else:
            number1 = len(a)
            str1 = '一元硬币' + str(number1) + '个，5角硬币0个,总价值'+str(number1)+'元';
            print(str1)
            result = client.synthesis(str1, 'zh', 1, {'vol': 5, 'per': 1})
            # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
            if not isinstance(result, dict):
                strs = 'audio' + sys.argv[1][0] + '.mp3'
                # if os.path.exists(strs):
                #     playsound.playsound(strs,block=False)
                # else:
                with open(strs, 'wb') as f:
                        f.write(result)
                playsound.playsound(strs,block=False)

def main():
    #利用argv输入参数来处理解决这个问题
    src1 = cv.imread("C:/Users/UCAS_BigBird/Desktop/happy/"+sys.argv[1])
    src2 = cv.cvtColor(src1, cv.COLOR_BGR2GRAY);  # 先gray
    dst = cv.GaussianBlur(src2, (13, 13), 5, 5);
    circles = cv.HoughCircles(dst, cv.HOUGH_GRADIENT, 1, 40, param1=63, param2=40, minRadius=0, maxRadius=0);
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(src1, (i[0], i[1]), i[2], (124, 123, 255), 2);
        cv.circle(src1, (i[0], i[1]), 2, (255, 0, 0), 2);
    cv.namedWindow("happy3", 0);
    cv.resizeWindow("happy3", 640, 480);
    cv.imshow("happy3", src1);
    lenth = []
    for i in circles[0, :]:
        lenth.append(i[2]);
    lenth = sorted(lenth)
    print(lenth)
    ou(lenth)
    cv.waitKey(0);
    cv.destroyAllWindows();


if __name__ == '__main__':
    main();