import os
print("123"+str(1))
total = 0
for i in range(10):
    print(str(i))
    print(os.environ['TWILIO_ACCOUNT_SID'])
    print(os.environ['TWILIO_AUTH_TOKEN'])
    # print(os.environ.keys())c