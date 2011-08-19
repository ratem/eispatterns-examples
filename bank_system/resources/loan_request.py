from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from domain.supportive.association_error import AssociationError
from domain.resource.work_item import WorkItem
from bank_system.rules.rules_of_association import rule_should_be_bank_account_instance, rule_should_be_credit_analyst_instance


class LoanRequest(WorkItem):
    ''' A Loan Request has a value, a date and time, and an associated analyst '''
    def __init__(self, account, value, analyst):
        WorkItem.__init__(self)
        self.value = value
        self.approved = False
        self.datetime = datetime.now()
        try:
           rule_should_be_bank_account_instance(account)
        except ShouldNotSatisfied:
           raise AssociationError('Bank Account instance expected, instead %s passed' % type(account))
        try:
           rule_should_be_credit_analyst_instance(analyst)
        except ShouldNotSatisfied:
           raise AssociationError('Credit Analyst instance expected, instead %s passed' % type(analyst))
        self.account = account
        self.analyst = analyst

