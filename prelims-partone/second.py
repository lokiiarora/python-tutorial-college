def vat(amt, rate):
   return (amt * rate/100)

amt = float(input("Enter the gross amount of purchase:"))
rate = float(input("Enter the VAT percentage:"))

total = amt + vat(amt,rate)
print "Vat amount is = %d" % (vat(amt,rate))
print "The computed net amount is %d" % (total)
