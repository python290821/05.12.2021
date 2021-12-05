from Customer import Customer

_lst = [Customer('danny', 'cohen'), Customer('Boris', 'rusnikov'),
        Customer('moshe', 'levi')]

print(_lst)

print('current_id before reset', Customer.current_id)
Customer.reset_id()
print('current_id after reset', Customer.current_id)

print('last creation time', Customer.last_customer_creation_time)
input('Press Enter ...')

_lst = [Customer('shimon', 'cohen'), Customer('tomer', 'rusnikov'),
        Customer('shuki', 'levi')]
print(_lst)
print('last creation time', Customer.last_customer_creation_time)
