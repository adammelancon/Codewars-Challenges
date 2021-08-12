# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

'''
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
'''

def past(h, m, s):
    if h <= 23:
        hms = h * 3600000
    if m <= 59:
        mms = m * 60000
    if s <= 59:
        sms = s * 1000
    print(hms)
    print(mms)
    print(sms)
    totalms = hms + mms + sms
    print(totalms)
    print("--------")





past(0,1,1) #,61000)
past(1,1,1) #,3661000)
past(0,0,0) #,0)
past(1,0,1) #,3601000)
past(1,0,0) #,3600000)