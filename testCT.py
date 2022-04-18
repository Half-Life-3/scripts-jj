import transactionGenerator as tg
import createTransactions as create
from faker import Faker


fake = Faker()
print(create.createTransaction("0011013146",fake.credit_card_number()))
