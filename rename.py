# rename the photos used for calibration

import os

def rename_files():
  os.chdir('./img_original')

  for i, file in enumerate(os.listdir()):
    os.rename(file, str(i)+'.jpg')

def main():
  rename_files()

if __name__ == '__main__':
  main()