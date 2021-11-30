  #   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 3 - Lab A - Twitter Decoding
        #   References: zyBooks 7.13
        #   Time: 20 min
        
print("Enter the Tweet or Message abbreviation to decode.")
tweet = input('TWEET>')
print("The decoded abbreviation is:")

if tweet == 'LOL':
    print('OUTPUT LOL = laughing out loud')
elif tweet == 'BFN':
    print('OUTPUT BFN = bye for now')
elif tweet == 'FTW':
    print('OUTPUT FTW = for the win')
elif tweet == 'IRL':
    print('OUTPUT IRL = in real life')
elif tweet == 'BTW':
    print('OUTPUT BTW = by the way')
elif tweet == 'DM':
    print('OUTPUT DM = direct message')
elif tweet == 'AFAIK':
    print('OUTPUT AFAIK = as far as I know')
elif tweet == 'IDK':
    print("OUTPUT IDK = I don't know")
elif tweet == 'LMK':
    print("OUTPUT LMK = let me know")
else:
    print("OUTPUT Sorry, don't know that one")
