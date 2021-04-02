class A:
    pass


class B(A):
    pass


b = B()
print("isinstance(b, A)", isinstance(b, A))
print("issubclass(B, A)", issubclass(B, A))
