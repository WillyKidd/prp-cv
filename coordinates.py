import numpy as np
from matplotlib import pyplot as plt

def coord_map(b, f, pixel_coord):
  # pixel_coord
  #    0   |    1   |    2    |    3 
  # x_left | y_left | x_right | y_right
  x = b * pixel_coord[0] / (pixel_coord[2] - pixel_coord[0])
  y = b * pixel_coord[1] / (pixel_coord[2] - pixel_coord[0])
  z = b * f / (pixel_coord[2] - pixel_coord[0])
  if int(z) == 658 and int(x) == 175 and int(y) == 521:
    print(pixel_coord)
  return [int(x), int(y), int(z)]

def get_coords(pairs):
  pairCoord3d = []
  cameraMatrixL = np.load('./calib_result/cam_mats_left.npy')
  cameraMatrixR = np.load('./calib_result/cam_mats_right.npy')
  fx_L = cameraMatrixL[0][0]
  fx_R = cameraMatrixR[0][0]
  fy_L = cameraMatrixL[1][1]
  fy_R = cameraMatrixR[1][1]
  # cx_L = cameraMatrixL[0][2]
  # cx_R = cameraMatrixR[0][2]
  # cy_L = cameraMatrixL[1][2]
  # cy_R = cameraMatrixR[1][2]
  f = (fx_L + fx_R + fy_L + fy_R) / 4 
  # I don't know how to deal with so many focus values so I took the average
  b = 52 
  # unit: mm
  # b: distance between the optical centers
  # obtained by measuring directly
  for p1, p2 in pairs:
    coord1 = coord_map(b, f, p1)
    coord2 = coord_map(b, f, p2)
    pairCoord3d.append([coord1, coord2])
  return pairCoord3d

def plot_3d(pairCoord3d):
  fig = plt.figure()
  # print(pairCoord3d)
  ax = fig.add_subplot(111, projection="3d")
  ax.set_box_aspect((1, 1, 1))
  for p1, p2 in pairCoord3d:
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    z = [p1[2], p2[2]]
    # print(x[0], y[0], z[0])
    # print('=================================')
    ax.scatter(x, y, z, c='red', s=100)
    ax.plot(x, y, z, color='black')

  plt.show()
