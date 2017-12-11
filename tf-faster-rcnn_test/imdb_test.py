import os
import os.path as osp
import PIL




class imdb(object):
  """Image database."""

  def __init__(self, name, classes=None):
    self._name = name
    self._num_classes = 0
    if not classes:
      self._classes = []
    else:
      self._classes = classes
    self._image_index = []
    self._obj_proposer = 'gt'
    self._roidb = None
    #self._roidb_handler = self.default_roidb
    # Use this dict for storing dataset specific config options
    self.config = {}
    self.gt_roidb = 'generated value'

  @property
  def name(self):
    return self._name

  @property
  def num_classes(self):
    return len(self._classes)

  @property
  def classes(self):
    return self._classes

  @property
  def image_index(self):
    return self._image_index

  @property
  def roidb_handler(self):
    return self._roidb_handler

  @roidb_handler.setter
  def roidb_handler(self, val):
    self._roidb_handler = val

  def set_proposal_method(self, method):
    method = eval('self.' + method + '_roidb') # >>> x = 1 >>eval('x+1') >>>2   eval() take string as input.动态执行
    self.roidb_handler = method


if __name__=="__main__":
    a=imdb('voc')
    a.set_proposal_method('gt')
    print(a.roidb_handler)
