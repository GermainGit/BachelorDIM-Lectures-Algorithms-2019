# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:37:48 2019

@author: PREVOT Germain
"""
import cv2
import numpy as np

img_gray=cv2.imread('img_s3.png',0)
img_bgr=cv2.imread('img_s3.png',1)

print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))

cv2.waitKey()

def invert_colors_manual(input_img):
    img_reverse=255-input_img
    cv2.imshow("BGR image", img_reverse)
    
invert_colors_manual(img_bgr)

# =============================================================================
# ####  EXEMPLE A NE PAS FAIRE
#
# #def invert_colors_manual(input_img):
#     ## Function which return an image with reverse color
#     #
#     # @param input_img: cv2.img
#     # return cv2.img
# 
#     
# # =============================================================================
# #     for idrow in range(input_img.shape[0]):
# #         for idcol in range(input_img.shape[1]):
# #             for idcomp in range(input_img.shape[2]):
# #                 input_img[idrow, idcol, idcomp]= 255-input_img[idrow, idcol, idcomp]
# #     cv2.imshow("Reverse levels image", input_img)          
# # =============================================================================
# 
# ####  EXEMPLE A NE PAS FAIRE
# =============================================================================
    
    

