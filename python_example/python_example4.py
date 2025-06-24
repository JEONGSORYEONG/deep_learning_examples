import cv2
import numpy as np

# 1. 흑백 이미지 로드: shape (H, W)
img = cv2.imread('apple.jpeg', cv2.IMREAD_GRAYSCALE)
print("원본 shape:", img.shape)

# 2. (H, W) → (1, H, W): 배치 차원 추가
img_expanded = np.expand_dims(img, axis=0)
print("배치 차원 추가 후:", img_expanded.shape)

# 3. (1, H, W) → (1, 1, H, W): 채널 차원도 추가
img_final = np.expand_dims(img_expanded, axis=1)
print("최종 shape (batch, channel, height, width):", img_final.shape)