pwd=float(input('Price:'))
d=int(input('discount %:'))
dp=pwd*(1-d/100)
r=pwd-dp
print(f"""Price: {pwd} 
      Discount: {d}%
      Price after discount: {dp: .2f}
      Reduction: {r: .2f}""")