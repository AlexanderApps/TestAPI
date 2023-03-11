from typing import Union

from pydantic import EmailStr

from schemas.iuser import IUser, IUserUpdate


# class UserValidator:
#     @staticmethod
#     def user_validate(user: IUser | IUserUpdate):
#         if user.first_name:
#             user.first_name = user.first_name.upper()
#         if user.last_name:
#             user.last_name = user.last_name.upper()
#         if user.middle_name:
#             user.middle_name = user.middle_name.upper()
#         if user.email:
#             user.email = EmailStr(user.email.lower())
#         if user.personal_detail:
#             if user.personal_detail.bank_account_name:
#                 user.personal_detail.bank_account_name = user.personal_detail.bank_account_name.upper()
#             if user.personal_detail.user_parent_name:
#                 user.personal_detail.user_parent_name = user.personal_detail.user_parent_name.upper()
#             if user.personal_detail.bank_name:
#                 user.personal_detail.bank_name = user.personal_detail.bank_name.upper()
#             if user.personal_detail.bank_branch:
#                 user.personal_detail.bank_branch = user.personal_detail.bank_branch.upper()
#             if user.personal_detail.next_of_kin_name:
#                 user.personal_detail.next_of_kin_name = user.personal_detail.next_of_kin_name.upper()
#             if user.personal_detail.next_of_kin_email:
#                 user.personal_detail.next_of_kin_email = EmailStr(
#                     user.personal_detail.next_of_kin_email.lower())
#         return user
