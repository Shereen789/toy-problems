from lru_cache import LRU

def main():
  test = LRU(5)
  test.put(4,"Java")
  test.put(1,"CT")
  test.put(2,"CSPP1")
  test.put(3,"IDS")
  assert test.getcache() == {4:"Java",1:"CT",2:"CSPP1",3:"IDS"}
  print("Assert 1 passed")
  test.put(2,"Python")
  assert test.getcache() == {4:"Java",1:"CT",2:"Python",3:"IDS"}
  print("Assert 2 passed")
  test.put(5,"ADS")
  test.put(6,"DataBases")
  assert test.getcache() == {1:"CT",2:"Python",3:"IDS",5:"ADS",6:"DataBases"}
  print("Assert 3 passed")
if __name__ == '__main__':
  main()
