#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
已知id 和 employees（employees类型，其中id，importance，subordinates）
先得到root,employees当前的id和其emp的对应关系
递归方式: 通过 当前的importance + 其subordinates的递归下得到的值
"""

"""
# Employee info
"""
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # 这里的id被我固定死了
        # edict = {id: emp for emp in employees.subordinates}
        # 先得到employees当前的id和其emp的对应关系
        edict = {emp.id : emp for emp in employees}
        def solve(id):
            # python的dict的取值可以这么
            emp = edict[id]
            return emp.importance + sum(solve(subid) for subid in emp.subordinates)
        return solve(id)

if __name__ == '__main__' :
    a = Employee(1, 5, [2, 3])
    b = Employee(2,3,[])
    c = Employee(3,3,[])
    d = [a,b,c]
    solution = Solution()
    print solution.getImportance(d,1)
