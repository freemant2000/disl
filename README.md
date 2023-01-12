# disl: super lightweight (only 35 lines) dependency injection (ioc) support for Python

A super simple and risk-free way to do dependency injection (ioc) in Python.
The entire code base is only 35 lines (empty lines included). No need to
use a complex 3rd-party framework or be concerned about the long-term viability
of the library.

## How to use
Suppose you have a module to read some products' info from a DB file, so the
path to the DB file should be injected:

    from disl import Inject

    class ProductDb:
      def __init__(self):
        self.db_path=Inject()  # this variable will be set automatically
      
      def get_products(self):
        print(f"getting products from {self.db_path}")

In your main program, you link up the ProductDb object and the db_path:

    from disl import Disl

    di=Disl()  # this is the container
    di.add_raw_bean("pdb", ProductDb()) # add the bean under the name "pdb"
    di.add_raw_bean("db_path", "c:/Users/kent/test.db") # another bean
    pdb=di.get_wired_bean("pdb")  # the db_path field in the pdb bean will be set
    pdb.get_products()  # this pdb object is just the plain object you created

If the path to the DB is named "database_path" but your variable name is
just "db_path", you can do it like this:

    from disl import Inject

    class ProductDb:
      def __init__(self):
        self.db_path=Inject("database_path") # specify the bean name
      
      def get_products(self):
        print(f"getting products from {self.db_path}")

    from disl import Disl

    di=Disl()
    di.add_raw_bean("pdb", ProductDb())
    di.add_raw_bean("database_path", "c:/Users/kent/test.db")
    pdb=di.get_wired_bean("pdb")
    pdb.get_products()
