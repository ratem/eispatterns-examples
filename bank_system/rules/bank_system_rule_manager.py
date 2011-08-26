from should_dsl import should, ShouldNotSatisfied
from domain.supportive.rule import rule
from domain.supportive.rule_manager import RuleManager


class BankSystemRuleManager(RuleManager):
    def __init__(self):
        RuleManager.__init__(self)

    @rule('association')
    def should_be_instance_of_bank_account(self, associated):
        '''Associated object should be instance of Bank Account Decorator'''
        from bank_system.decorators.bank_account_decorator import BankAccountDecorator
        try: associated |should| be_instance_of(BankAccountDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_credit_analyst(self, associated):
        '''Associated object should be instance of Credit Analyst Decorator'''
        from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
        try: associated |should| be_instance_of(CreditAnalystDecorator)
        except ShouldNotSatisfied: return False
        else: return True
