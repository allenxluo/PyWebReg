from WebReg import WebReg

wr = WebReg().login('luoax@uci.edu', 'Veneer74912!')
print("LOGGED IN")
if wr.add_waitlist('38000') == -1:
    print("WAITLIST FULL")
else:
    print("ADDED TO WAITLIST")