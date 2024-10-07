# a triangle must have the sum of any two arbitrary sides be longer than
# the length of the third side; therefore, the naive way to do it is

#def is_a_triangle(a, b, c):
#    if a + b <= c:
#        return False
#   if b + c <= a:
#        return False
#   if c + a <= b:
#        return False
#   return True
#
#print(is_a_triangle(1,1,1))
#print(is_a_triangle(1,1,3))

# however, we can be more compact
#
#def is_a_triangle(a, b, c):
#    if a + b <= c or b + c <=a or a + c <= b:
#        return False
#    return True
#
#print(is_a_triangle(1,1,1))
#print(is_a_triangle(1,1,3))

# or, even more compact than that

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

#print(is_a_triangle(1,1,1))
#print(is_a_triangle(1,1,3))

# in this case, we reverse the truth values. The result is True only when the
# sum of each two sides is greater than the third, and returns False otherwise

# now, we can solicit input and then make the output better

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, this can be a triangle!')
else:
    print('No, this cannot be a triangle!')

# since we know the sides, we can also test whether this would be a right
# triangle by using the Pythagorean theorem! We just must determine which
# side (the longest) would be the hypotenuse

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
# can't be a right triangle if you aren't a triangle at all!
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
# remember that == is the equality tester, so if this a ** 2 is not equal
# to b ** 2 + c ** 2 then it will return False

if is_a_right_triangle(a, b, c):
    print('And, it is a right triangle!')
else:
    print('But it is NOT a right triangle!')

# we can also use the side lengths to find the area, given by the formula
# s = (a+b+c)/2 and Area = the square root of [(s(s-a)(s-b)(s-c)]

def area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def area_calc(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return area(a, b, c)

if is_a_triangle:
    print('And the area is', area_calc(a, b, c))
