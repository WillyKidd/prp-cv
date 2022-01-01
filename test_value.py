# generates test coordinate values
# format:
# point coordinates: x_left | y_left | x_right | y_right

import numpy as np
points = [[12, 299, 176, 294],
          [97, 705, 246, 706],
          [178, 1006, 292, 990],
          [205, 366, 432, 366],
          [284, 816, 468, 807],
          [384, 1144, 528, 1142],
          [580, 494, 888, 505],
          [595, 993, 836, 982],
          [610, 1366, 807, 1371]]

np.save('test_value.npy', points)