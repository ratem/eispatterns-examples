from datetime import datetime
from should_dsl import should
from domain.supportive.association_error import AssociationError
from domain.supportive.rule import rule
from domain.resource.work_item import WorkItem


class LoanRequest(WorkItem):
    ''' A Loan Request has a value, a date and time, and an associated analyst '''
    def __init__(self, account, value, analyst):
        WorkItem.__init__(self)
        self.value = value
        self.approved = False
        self.datetime = datetime.now()
        self.analyst = analyst
        try:
           self.rule_should_be_credit_analyst_instance(analyst)
           self.rule_should_be_bank_account_instance(account)
        except:
           raise AssociationError('Bank Account instance expected, instead %s passed' % type(account))
        else:
           self.account = account

    #Rules import locally to avoid circular references
    @rule('association')
    def rule_should_be_bank_account_instance(self, account):
        ''' Account should be of type Bank Account Decorator '''
        from bank_system.decorators.bank_account_decorator import BankAccountDecorator
        account |should| be_instance_of(BankAccountDecorator)

    @rule('association')
    def rule_should_be_credit_analyst_instance(self, analyst):
        ''' Analyst should be of type Credit Analyst Decorator '''
        from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
        analyst |should| be_instance_of(CreditAnalystDecorator)

