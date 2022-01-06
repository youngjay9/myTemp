import sys
import collections
import json
from enum import Enum
from types import LambdaType
from typing import Counter, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, key, element: T):
        self.key = key
        self.element = element
        self.parent = None
        self.left = None
        self.right = None


class LeafNode:
    def __init__(self):
        self.key = 0
        self.element = None
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def __init__(self, *args):
        self.leafnode = LeafNode()  # 為節省記憶體空間,提供其它 node 預設的 leafNode 都指向同一個
        self.root = self.leafnode
        self.root.parent = self.leafnode
        self.insertLength = 0

    def levelOrder(self, root):

        result = []

        q = collections.deque()  # 可用於多執行緒的 Queue
        q.appendleft(root)

        result.append([root.key])

        while q:
            node = q.popleft()
            tmpList = []

            if node.left:
                q.appendleft(node.left)
                tmpList.append(node.left.key)

            if node.right:
                q.appendleft(node.right)
                tmpList.append(node.right.key)

            print(f'tmpList length:{len(tmpList)}')

            if len(tmpList) > 0:
                result.append(tmpList)

        print(f'result:{result}')


if __name__ == "__main__":

    leafNode = LeafNode()

    # 指定 root
    root = Node('3', '3')

    node9 = Node('9', '9')
    node20 = Node('20', '20')
    node15 = Node('15', '15')
    node7 = Node('7', '7')

    root.left = node9
    root.right = node20
    node20.left = node15
    node20.right = node7

    solution = Solution()
    solution.levelOrder(root)
