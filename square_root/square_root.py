n = int(input())
my_inputs = dict()
for numbers in range(1, n+1):
    my_inputs[numbers] = int(input())

from math import sqrt
from decimal import Decimal
results = dict()
for k in list(my_inputs.values()):
    results[k] = sqrt(k)

output =dict()
for v in list(results.values()):
    output[v] = Decimal(str(v)).quantize(Decimal('1.0000'))

for every in list(output.values()):
    print(every)