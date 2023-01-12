from disl import Inject

class ProductDb:
  def __init__(self):
    self.db_path=Inject()
  
  def get_products(self):
    print(f"getting products from {self.db_path}")

from disl import Disl

di=Disl()
di.add_raw_bean("pdb", ProductDb())
di.add_raw_bean("db_path", "c:/Users/kent/test.db")
pdb=di.get_wired_bean("pdb")
pdb.get_products()
