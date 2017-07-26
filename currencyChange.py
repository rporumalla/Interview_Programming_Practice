def currChange(amt):
  coins=[(25,'quarter'),(10,'dime'),(5,'nickel'),(1,'penny')]
  ans={}
  for coin_value, coin_name in coins:
    if amt==0:
      break
    if amt>=coin_value:
      num_coin,amt=divmod(amt,coin_value)
      ans[coin_name]=num_coin
  return ans

if __name__ == '__main__':
  print currChange(26)
  print currChange(69)
  print currChange(199)
