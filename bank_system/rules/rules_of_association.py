''' Repository for rules of association
    Local imports are used to avoid circular references
'''
from domain.supportive.rule import rule
from should_dsl import should


@rule('association')
def rule_should_be_loan_request_instance(loan_request):
    ''' Loan Request should be of type Loan Request '''
    from bank_system.resources.loan_request import LoanRequest
    loan_request |should| be_instance_of(LoanRequest)

@rule('association')
def rule_should_be_bank_account_instance(account):
    ''' Account should be of type Bank Account Decorator '''
    from bank_system.decorators.bank_account_decorator import BankAccountDecorator
    account |should| be_instance_of(BankAccountDecorator)

@rule('association')
def rule_should_be_credit_analyst_instance(analyst):
    ''' Analyst should be of type Credit Analyst Decorator '''
    from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
    analyst |should| be_instance_of(CreditAnalystDecorator)

#@rule('association')
#def rule_should_contain_employee_decorator(decorated):
#    ''' Decorated object should be already decorated by Employee '''
#    from bank_system.decorators.employee_decorator import EmployeeDecorator
#    decorated |should| be_decorated_by(EmployeeDecorator)

