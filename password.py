username=input('what is your username?')
password=input('what is your password')
pass_len=len(password)
hidden_pass='*'*pass_len
print(f'{username} your password {hidden_pass} is {pass_len} letters long')