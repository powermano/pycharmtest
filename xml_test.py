import xml.etree.ElementTree as ET
import os
import pickle
import numpy as np

def parse_rec(filename):
  """ Parse a PASCAL VOC xml file """
  tree = ET.parse(filename)
  objects = []
  for obj in tree.findall('object'):
    obj_struct = {}
    # obj_struct['name'] = obj.find('name').text
    # obj_struct['pose'] = obj.find('pose').text
    # obj_struct['truncated'] = int(obj.find('truncated').text)
    # obj_struct['difficult'] = int(obj.find('difficult').text)
    bbox = obj.find('bndbox')
    obj_struct['bbox'] = [int(bbox.find('xmin').text),
                          int(bbox.find('ymin').text),
                          int(bbox.find('xmax').text),
                          int(bbox.find('ymax').text)]
    objects.append(obj_struct)

  return objects


if __name__ == '__main__':
    xml_path = 'D:/用户目录/下载/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/Annotations/000005.xml'
    result = parse_rec(xml_path)
    print(result)
    dump_file = 'E:/dump.txt'
    f = open(dump_file, 'wb') #must 'wb' because dump change the str into byte.Writing byte into file needs binary file
    pickle.dump(result, f)
    f.close()