import sys

sys.path.append(
    'F:\\Companies\\Hexaware\\Technical Foundation Training\\Python Training\\PyCharm learning\\PyCharm\\CaseStudy\\PayXpert\\Classes')

from DBUtil import DBUtil
from CollectionClass import CollectionClass


db_util = DBUtil(host='localhost', user='root', password='SQL@bunny11', port='3306', database='payxpert')
ccl = CollectionClass(db_util)


gross = ccl.GrossSalaryCollection()
net = ccl.NetSalaryCollection()


def test1():
    assert gross[0] == net[0]
    assert gross[1] == net[1]
    assert gross[2] == net[2]
    assert gross[3] == net[3]
    assert gross[4] == net[4]
    assert gross[8] == net[8]
    # Run the test


test1()
