from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError


class EmployeeDecorator(Decorator):
    '''A general purpose Employee decorator'''
    decoration_rules = ['should_be_instance_of_person']
    def __init__(self):
        Decorator.__init__(self)
        self.description = "Supplies the basis for representing employes"

    def generate_register(self, register):
        ''' generates the register number for the employee '''
        self.register = register

