import cv2 as cv
import numpy as np

def get_pairs(img, points):
  pairs = []
  for p1 in points:
    for p2 in points:
      count = 0
      if np.array_equal(p1, p2):
        continue
      pts_judge = np.linspace(p1, p2, 20, endpoint=False)
      for pt in pts_judge:
        pixel_judge = img[int(pt[0]), int(pt[1])]
        if (pixel_judge[0] <= 10 and
            pixel_judge[1] <= 10 and 
            pixel_judge[2] >= 245):
          count += 1
    print(count)
    if count >= 15:
      pairs.append([p1, p2])
      print(count)
  return pairs

def hough_mark(img_name, display=False):
  img = cv.imread(img_name)
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  edges = cv.Canny(gray, 50, 200)
  lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=20, maxLineGap=30)
  for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 20)
  if display == True:
    cv.imshow("Marked image", img)
    cv.waitKey(0)
  return img

def main():
  marked_img = hough_mark('crystal_right.jpg')
  points = np.load('test_value.npy')
  get_pairs(marked_img, points)

if __name__ == '__main__':
  main()
    
