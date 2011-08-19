from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from domain.supportive.association_error import AssociationError
from domain.supportive.rule import rule
from domain.resource.work_item import WorkItem
from bank_system.resources.loan_request import LoanRequest
from bank_system.rules.rules_of_association import rule_should_be_loan_request_instance

class Loan(WorkItem):
    ''' A Loan is generated from a Loan Request '''
    def __init__(self, loan_request):
        WorkItem.__init__(self)
        try:
           rule_should_be_loan_request_instance(loan_request)
        except ShouldNotSatisfied:
           raise AssociationError('Loan Request instance expected, instead %s passed' % type(loan_request))
        self.loan_request = loan_request
        self.datetime = datetime.now()

