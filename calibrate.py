import os
import cv2 as cv
import glob
import re
from numpy import array
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from stereovision.exceptions import ChessboardNotFoundError

def crop_image(img_orig, img_left=None, img_right=None):
  img = cv.imread(img_orig)
  if img_left == None:
    orig_name = re.search('^(.+)\.jpg$', img_orig).group(1)
    img_left = orig_name + '_left.jpg'
    img_right = orig_name + '_right.jpg'
  width = int(img.shape[1])
  height = int(img.shape[0])
  cv.imwrite(img_left, img[0:height, 0:int(width / 2)])
  cv.imwrite(img_right, img[0:height, int(width / 2):width])
  return list(img_left, img_right)

def stereo_calibrate():
  # Global variables preset
  # total_photos = 24
  # photo_width = 3040
  # photo_height = 1520
  img_width = 1520
  img_height = 1520
  image_size = (img_width, img_height)

  # Chessboard parameters
  rows = 6
  columns = 8
  square_size = 2.5

  # Read images and crop into left and right
  img_original = glob.glob(os.getcwd() + '/img_original/*.jpg')
  if len(img_original) < 1:
    print("Error: no images found in ./img_original/. Program will now exit...")
    exit(-1)

  count = 1
  for jpg_name in img_original:
    left_name = './imgL/' + str(count) + '.jpg'
    right_name = './imgR/' + str(count) + '.jpg'
    crop_image(jpg_name, left_name, right_name)
    count = count + 1

  calibrator = StereoCalibrator(rows, columns, square_size, image_size)
  count = 0
  imagesLeft = glob.glob('imgL/*.jpg')
  imagesRight = glob.glob('imgR/*.jpg')
  print('Start cycle')

  # Attempt to read checkerboard patterns
  for imLeft, imRight in zip(imagesLeft, imagesRight):
    print('Import pair No ' + str(count))
    if os.path.isfile(imLeft) and os.path.isfile(imRight):
      img_left = cv.imread(imLeft, 1)
      img_right = cv.imread(imRight, 1)
      try:
        calibrator._get_corners(img_left)
        calibrator._get_corners(img_right)
      except ChessboardNotFoundError as error:
        print(error)
        print("Pair No " + str(count) + " ignored")
      else:
        calibrator.add_corners((img_left, img_right), False)
    count = count + 1

  print('End cycle')

  # start calibration and export results
  print('Starting calibration... It can take a while...')
  calibration = calibrator.calibrate_cameras()
  calibration.export('calib_result')
  print('Calibration complete!')

def image_rectify(img_orig=None, img_left=None, img_right=None):
  if img_orig != None:
    names = crop_image(img_orig)
    img_left = names[0]
    img_right = names[1]
  calibration = StereoCalibration(input_folder='calib_result')
  targetLeft = cv.imread(img_left)
  targetRight = cv.imread(img_right)
  rectified_target = calibration.rectify((targetLeft, targetRight))
  cv.imwrite("rectifyed_"+img_left, rectified_target[0])
  cv.imwrite("rectifyed_"+img_right, rectified_target[1])

def main():
  stereo_calibrate()
  image_rectify(img_orig='crystal.jpg')

if __name__ == '__main__':
  main()
  