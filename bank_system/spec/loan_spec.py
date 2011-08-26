import unittest
from should_dsl import should, should_not
from domain.supportive.association_error import AssociationError
from bank_system.resources.loan_request import LoanRequest
from bank_system.resources.loan import Loan
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator

class LoanSpec(unittest.TestCase):

    def it_check_association_with_loan_request(self):
        (Loan, 'I am not a loan request') |should| throw(AssociationError)
        a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')
        an_account = BankAccountDecorator('1234567-8')
        a_loan_request = LoanRequest(an_account, 7000, a_credit_analyst_decorator)
        (Loan, a_loan_request) |should_not| throw(AssociationError)

