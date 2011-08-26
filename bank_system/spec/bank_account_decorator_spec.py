import unittest
from should_dsl import should, should_not
from domain.node.machine import Machine
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from domain.supportive.association_error import AssociationError


class BankAccountDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_bank_account_decorator = BankAccountDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_machine = Machine()

    def it_decorates_a_machine(self):
        #should work
        self.a_bank_account_decorator.decorate(self.a_machine)
        self.a_bank_account_decorator.decorated |should| be(self.a_machine)
        self.a_bank_account_decorator.decorated |should| have(1).decorators
        #should fail
        decorate, _, _ = self.a_bank_account_decorator.decorate('I am not a machine')
        decorate |should| equal_to(False)

    def it_registers_a_credit(self):
        self.a_bank_account_decorator.balance = 100
        self.a_bank_account_decorator.register_credit(50)
        self.a_bank_account_decorator.balance |should| equal_to(150)

    def it_sends_a_message_to_the_account_holder(self):
        message = 'This is a message'
        self.a_bank_account_decorator.send_message_to_account_holder(message) |should| equal_to(message)

