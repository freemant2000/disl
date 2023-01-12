from disl import Disl, Inject
import pytest

class Foo:
  def __init__(self):
    self.a=Inject()

class Bar:
  pass

class Parent:
  def __init__(self):
      self.dep1=Inject()

class Child(Parent):
  def __init__(self):
    super().__init__()
    self.dep2=Inject()

def test_inject():
  f=Foo()
  f.a=6
  f.bar=Inject()
  di=Disl()
  di.add_raw_bean("foo", f)
  di.add_raw_bean("bar", "hi")
  bar=di.get_wired_bean("bar")
  assert bar=="hi"
  foo=di.get_wired_bean("foo")
  assert foo.bar=="hi"

def test_inject_name():
  f=Foo()
  f.a=6
  f.bar=Inject("baz")
  di=Disl()
  di.add_raw_bean("foo", f)
  di.add_raw_bean("baz", "hi")
  foo=di.get_wired_bean("foo")
  assert foo.bar=="hi"

def test_mutual_dep():
  f=Foo()
  f.a=6
  f.bar=Inject()
  b=Bar()
  b.x=2
  b.foo=Inject()
  di=Disl()
  di.add_raw_bean("foo", f)
  di.add_raw_bean("bar", b)
  foo=di.get_wired_bean("foo")
  assert foo.bar.x==2
  bar=di.get_wired_bean("bar")
  assert bar.foo.a==6

def test_no_name():
  di=Disl()
  di.add_raw_bean("bar", "hi")
  with pytest.raises(ValueError):
    di.get_wired_bean("foo")

def test_hier():
  c=Child()
  di=Disl()
  di.add_raw_bean("dep1", "hi")
  di.add_raw_bean("dep2", 4)
  di.add_raw_bean("child", c)
  child=di.get_wired_bean("child")
  assert child.dep1=="hi"
  assert child.dep2==4
