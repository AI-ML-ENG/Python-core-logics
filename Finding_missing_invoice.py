invoices=[102,105,106,103,101]
invoices.sort()
invoice=set(range(min(invoices),max(invoices)+1))
final_invoice=invoice-set(invoices)
missing_element=final_invoice.pop()
print('the misssing element is',missing_element)
invoices.append(missing_element)
invoices.sort()
print(list(invoice))



