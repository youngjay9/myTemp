from functools import lru_cache
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.items = {}  # 用來存放 key 對應的 Node, 這樣就不用花 O(n) 的時間搜尋key 對應的 Node

    def put(self, key, val: T):
        # key 不存在, 將新增的 Node 新增至鏈表頭部
        if key not in self.items.keys():
            newNode = Node(key, val)
            self.items[key] = newNode
            # 第一次新增 Node, 指定 head 跟 tail
            if self.head is None and self.tail is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            # 新增 Node 以後, 超過鏈表的長度需將 tail 的 Node 刪除,以維護 capacity
            if len(self.items) > self.capacity:
                tail_node = self.tail
                # 將 items 對應的 tail_node.key 刪除
                self.items.pop(tail_node.key)
                # 變更 tail 指標
                self.tail = tail_node.prev
                del tail_node
        # key 存在, 需對該 Node 是 head、tail、others 去處理
        else:
            cur_node = self.items[key]
            if cur_node is self.head:
                cur_node.val = val
            elif cur_node is self.tail:
                # 變更 tail 指標
                self.tail = cur_node.prev
                self.tail.next = None
                # 將 cur_node 移至鏈表頭部
                cur_node.next = self.head
                self.head.prev = cur_node
                self.head = cur_node
            else:
                prev_node = cur_node.prev
                next_node = cur_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                # 將 cur_node 移至鏈表頭部
                cur_node.next = self.head
                self.head.prev = cur_node
                self.head = cur_node


if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put('2', '2')
    lru_cache.put('3', '3')
    lru_cache.put('4', '4')
