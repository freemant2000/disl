
from dataclasses import dataclass


@dataclass
class Inject:
  name: str = None

class Disl:
  def __init__(self):
    self.raw_beans={}
    self.wired_beans={}

  def add_raw_bean(self, name, bean):
    self.raw_beans[name]=bean

  def get_wired_bean(self, name):
    if name in self.wired_beans:
      return self.wired_beans[name]
    if name in self.raw_beans:
      b=self.raw_beans[name]
      self.wired_beans[name]=b  #must do this first in case of mutual dependencies
      self.wire_bean(name, b)
      return b
    else:
      raise ValueError(f"no bean named {name} found")

  def wire_bean(self, name, b):
    if not hasattr(b, "__dict__"): #built-in object such as a string
      return b
    attrs=vars(b)
    for n,v in attrs.items():
      if isinstance(v, Inject):
        dep_name=v.name if v.name else n
        attrs[n]=self.get_wired_bean(dep_name)
