from tinygrad import Tensor
import tinygrad.function as F

a = Tensor([1, 2, 3])
b = Tensor([2, 3, 4]) 
#c = a + b
d = F.Add.apply(a, b)
#print(c.numpy() == d.numpy())
#print("final result:", c.numpy())