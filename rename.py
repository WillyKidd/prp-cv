# rename the photos used for calibration

import os

def rename():
  os.chdir('./img_original')

  for i, file in enumerate(os.listdir()):
    os.rename(file, str(i)+'.jpg')

def main():
  rename()

if __name__ == '__main__':
  main()