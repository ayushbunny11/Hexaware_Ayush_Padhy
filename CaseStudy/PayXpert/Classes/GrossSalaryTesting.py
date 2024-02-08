import sys

sys.path.append(
    'F:\\Companies\\Hexaware\\Technical Foundation Training\\Python Training\\PyCharm learning\\PyCharm\\CaseStudy\\PayXpert\\Classes')

from util.DBUtil import DBUtil
from CollectionClass import CollectionClass

db_util = DBUtil(host='localhost', user='root', password='SQL@bunny11', port='3306', database='payxpert')
ccl = CollectionClass(db_util)

gross = ccl.GrossSalaryCollection()
net = ccl.NetSalaryCollection()


def test1():
    for i, j in zip(gross, net):
        assert i == j
    # Run the test


test1()
