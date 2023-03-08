# from argon2 import PasswordHasher, Parameters, exceptions

# ph = PasswordHasher()
# hs = ph.hash("my name")
# print(hs)
# a = "$argon2id$v=19$m=65536,t=3,p=4$TCEQlWDXt8aXrC2HlJyoNg$zyeynOQyROFxW5puvgeViBhJ1DNq8bpD3HDb5lcfkwg"
# # print(ph.verify(a, "my name"))

# try:
#     val: bool = ph.verify('', "myname")
#     print(val)
# except exceptions.VerificationError:
#     print(False)
# except:
#     print("Error Occurred During Validation")
