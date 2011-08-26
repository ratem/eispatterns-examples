from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from domain.supportive.association_error import AssociationError
from domain.resource.work_item import WorkItem
from bank_system.rules.bank_system_rule_manager import BankSystemRuleManager


class LoanRequest(WorkItem):
    ''' A Loan Request has a value, a date and time, and an associated analyst '''
    def __init__(self, account, value, analyst):
        WorkItem.__init__(self)
        self.value = value
        self.approved = False
        self.datetime = datetime.now()
        if not BankSystemRuleManager.get_instance().check_rule('should_be_instance_of_bank_account', account):
           raise AssociationError('Bank Account instance expected, instead %s passed' % type(account))
        self.account = account
        if not BankSystemRuleManager.get_instance().check_rule('should_be_instance_of_credit_analyst', analyst):
            raise AssociationError('Credit Analyst instance expected, instead %s passed' % type(analyst))
        self.analyst = analyst

