import os
import glob
import sys
import argparse
from os import path
from PIL import Image

def main():
  parse_cmd_args(sys.argv[1:])
  cwd = os.getcwd()
  args = sys.argv[1:]
  width = int(args[0])
  height = int(args[1])
  ext = args[2] or '.webp'
  option = ''
  if len(args) > 3:
    option = args[3]
  # folder
  dir_name = 'pyfiles'
  if path.exists(dir_name):
    print('directory already exists...\nprocessing...')
  else:
    os.mkdir(dir_name)
    print('pyfiles directory created...')
  if option == 'resize':
    print('resizing image...')
  # function
  arr = glob.glob(cwd+'/*.jpg')
  for arrpath in arr:
    if '\\' in arrpath:
      file_url = arrpath.split('\\')
    elif '/' in arrpath:
      file_url = arrpath.split('/')
    file_name = file_url[-1].split('.')[0]
    image = Image.open(arrpath)
    os.chdir(dir_name)
    if option == 'resize':
      new_image = image.resize((width, height))
      new_image.save(file_name+ext)
    else:
      image.thumbnail((width, height))
      image.save(file_name+ext)
    os.chdir('../')

def parse_cmd_args(cmd_args):
  parser = argparse.ArgumentParser(prog='pysize', usage='%(prog)s <width> <height> <ext> <option>')
  if len(cmd_args) < 3:
    parser.print_help()
    sys.exit(1)

if __name__ == '__main__':
  main()