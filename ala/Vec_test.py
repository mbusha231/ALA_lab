from Vec import Vec

print("running test cases")
v_empty = Vec()
assert v_empty == []
#add
v1 = Vec([1,2,3])
v2 = Vec([4,5,6])
result = v1 + v2
#print(result)
assert result == [5,7,9], "add failed"
#sub
v1 = Vec([4,8,15])
v2 = Vec([4,5,6])
result = v1 - v2
#print (result)
assert result == [0,3,9], "sub failed"
#rmul
v1 = Vec([4,3,6])
scalar = 3
result = scalar * v1
#print(result)
assert result == [12,9,18]
#imul
v1 = Vec([4,3,6])
scalar = 2
v1 *= scalar
#print(v1)
assert v1 == [8,6,12]
#repr
v = Vec([6,4])
#result_str = repr(v)
#print(result_str)
assert v == [6,4]
#len
v1 = Vec([3,8,0])
v2 = Vec([1,7,3,13,56,2])
Vec.__len__(v2)
assert len(v1) == 3
assert len(v2) == 6
#neg
v = Vec([16,-42,-7])
result = -v
#print(result)
assert result == [-16, 42,7]
#radd
v1 = Vec([23,64,9])
v2 = Vec([11,63,0])
result = v1 + v2
#print(result)
assert result == [34,127,9]

#iadd
v1 = Vec([3,8,15])
v2 = Vec([6,1,21])
v1 += v2
#print(v1)
assert v1 == [9,9,36]

#zeros
result_zeros = Vec.zeros(5)
#print(result_zeros)
assert result_zeros == [0,0,0,0,0]

#ones
result_ones = Vec.ones(3)
#print(result_ones)
assert result_ones == [1,1,1]

#uniform
result_uniform = Vec.uniform(3)
#print(result_uniform)
assert len(result_uniform) == 3

#euclidean norm
result_norm = Vec([3,4]).norm()
#print(result_norm)
assert result_norm == 5

#mean
v1 = Vec([3,8,14])
assert round(v1.mean(), 3) == 8.333
print(v1.mean())
v2 = Vec([-9, -14, -3])
assert round(v2.mean(), 3) == -8.667
print(v2.mean())

exception_raised = False
try:
    Vec().mean()
except RuntimeError: 
    exception_raised = True
assert exception_raised == True, "mean did not raise exception for empty vector"
print("mean vec test case passed")

#demean
v1 = Vec([4,17, 23])
demean_vec = v1.demean()
rounded_res = [round(x,3) for x in demean_vec.elements]
assert rounded_res == [-10.667, 2.333, 8.333], "demean fails"
v2 = Vec([2,6,14])
demean_vec = v2.demean()
rounded_res = [round(x, 3) for x in demean_vec.elements]
assert rounded_res == [-5.333, -1.333, 6.667], "demean fails"

exception_raised = False
try:
    Vec().demean()
except RuntimeError:
    exception_raised = True
assert exception_raised == True, "demean did not raise exception for empty vector"
print("demean vec test case passes")

#variance
v1 = Vec([2,8])
vari_vec = v1.variance()
assert vari_vec == 9.0, "variance fails"
v2 = Vec([-8, -5, -13])
vari_vec = v2.variance()
rounded_res = round(vari_vec, 3)
assert rounded_res == 10.889, "variance fails"

exception_raised = False
try:
    Vec().variance()
except RuntimeError:
    exception_raised = True
assert exception_raised == True, "variance did not raise exception for empty vector"
print("variance vec test case passes")
