"""Assignment1 (programming):
Given two lists A and B. Find the sum of squares of elements in A and cubes of elements in B.
Example: A = [1,2,3] and B=[2,3]. The sum would be 1^2 + 2^2 + 3^2 + 2^3 + 3^3."""


A = [1, 2, 3]
B = [2, 3]
C = len(A)
D = len(B) + 1
total = ((C * (C + 1) * (2 * C + 1)) / 6) + (((D * (D + 1) / 2) ** 2) - 1)
print(total)
