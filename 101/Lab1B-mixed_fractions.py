 #   Brynn Moncur
        #   ​CSCI 101 – Section D
        #   Python Lab 1B
        #   References: N/A
        #   Time: 20 minutes


numerator = int(input("Input the numerator of the improper fraction."))
print(f'NUMERATOR> {numerator}')
denominator = int(input("Input the denominator of the improper fraction."))
print(f'DENOMINATOR> {denominator}')

print(f'{numerator}/{denominator} as a mixed fraction is:')

coefficient = int(numerator/denominator)
new_numerator = int(numerator%denominator)

print(f'OUTPUT {coefficient} {new_numerator}/{denominator}')
                    
