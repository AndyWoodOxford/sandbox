#!/usr/bin/env python
"""
A sandbox for trying out OO ideas in Python
"""

class Worker():
    """ My first class - taken from the O'Reilly guide """
    def __init__(self, name, job_title = 'Unknown', pay = None):
        self.name = name
        self.job_title = job_title
        self.pay = pay

    def firstname(self):
        return self.name.split()[0]

    def surname(self):
        return self.name.split()[-1]

    def payrise(self, percent):
        """
        Given a 'pay rise' (expressed as a fraction), returns the new salary
        """
        self.pay *= (1.0 + percent)

    def describe(self):
        pass

    def __repr__(self):
        return 'Worker: {0} (role {1}, pay {2})'.format(self.name, self.job_title, self.pay)

class Manager(Worker):
    """ A managerial worker """
    def __init__(self, name, pay):
        Worker.__init__(self, name, 'Manager', pay)

    def payrise(self, percent, bonus = 0.1):
        Worker.payrise(self, percent + bonus)

class Department:
    """ A group of workers """



    def __init__(self, *args):
        self.company = 'Acme Corporation'
        self.members = list(args)

    def __repr__(self):
        display = self.company + ':\n'
        for member in self.members:
            display += member.__repr__()
        return display

    def addMember(self, worker):
        self.members.append(worker)

    def headCount(self):
        return len(self.members)

    def showNames(self):
        for member in self.members:
            print member.firstname()


if __name__ == '__main__':

    abraham = Worker('Abraham Aardvark', 'Founder', 50000)
    print('Abraham\'s surname is ', abraham.surname())
    print('Abraham pay: ' + unichr(163) + '{0:5.0f}'.format(abraham.pay))
    abraham.payrise(.25)
    print(abraham)

    barry = Worker('Barry Bazzer')
    print(barry)

    charlie = Manager('Charlie Chappers', 100000)
    print(charlie)
    charlie.payrise(.1)
    print(charlie)

    dev = Department(abraham, charlie)
    print 'Initial Department list:'
    dev.showNames()
    dev.addMember(barry)
    print 'Updated Department:'
    dev.showNames()
    print 'Updated Department (full):'
    print dev
