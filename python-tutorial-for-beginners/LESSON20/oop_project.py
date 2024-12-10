from bank_accounts import *

Koufax = BankAccount(1000, "Koufax")
Kamoni = BankAccount(2000, "Kamoni")

Koufax.getBalance()
Kamoni.getBalance()

Kamoni.deposit(500)

Koufax.withdraw(10000)
Koufax.withdraw(10)

Koufax.transfer(10000, Kamoni)
Koufax.transfer(100, Kamoni)

Kam = InterestRewardsAcct(1000, "Kam")

Kam.getBalance()

Kam.deposit(100)

Kam.transfer(100, Koufax)

Shaila = SavingsAcct(1000, "Shaila")

Shaila.getBalance()

Shaila.deposit(100)

Shaila.transfer(10000, Kamoni)
Shaila.transfer(1000, Kamoni)