import cv2
import numpy as np

def optimize_canny(image, sigma=0.33):
    # 1. 调整图像的亮度和对比度
    image = cv2.convertScaleAbs(image, alpha=1.5, beta=10)

    # 2. 使用高斯滤波进行图像平滑处理，降噪
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # 3. 根据Sigma计算Canny的minVal和maxVal thresholds
    median = np.median(blurred)
    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))

    # 4. 应用Canny边缘检测算法
    edges = cv2.Canny(blurred, lower, upper)

    # 5. 进一步优化边缘图像，提高连续性
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(edges, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    # 6. 返回最终优化后的边缘图像
    return eroded

# 加载输入图像
image = cv2.imread("crack_image.jpg", 0)

# 优化Canny算法应用于裂缝分析
edges = optimize_canny(image)

# 查找并绘制裂缝线条
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=5)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 保存检测结果
# cv2.imshow("Optimized Canny Edges", image)
cv2.imwrite('result.png', image)

# 展示结果
# cv2.imshow("Optimized Canny Edges", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
