class Node:
    def __init__(self, keys=None, count=None):
        self.keys = keys
        self.count = count
        self.before = None
        self.after = None

    def __repr__(self):
        return f"<{str(self.keys)}, {self.count}>"


class DLL(object):
    def __init__(self):
        self.head = Node({""}, 0)
        self.tail = Node({""}, 999999)
        self.head.after = self.tail
        self.tail.before = self.head

    def insert_after(self, node, after):
        after.before = node
        after.after = node.after
        node.after.before = after
        node.after = after
        return after

    def remove(self, node):
        node.before.after = node.after
        node.after.before = node.before

    def __repr__(self):
        s = []
        node = self.head
        while node:
            s.append(f"{node}")
            if node.after:
                assert node == node.after.before
            node = node.after
        return ", ".join(s)


class AllOne(object):
    def __init__(self):
        self.entry_dict = {}
        self.entry_list = DLL()

    def discard_key(self, node, key):
        node.keys.discard(key)
        if not node.keys:
            self.entry_list.remove(node)

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        node = self.entry_dict.get(key, self.entry_list.head)
        if node.after.count == node.count + 1:
            new_node = node.after
            new_node.keys.add(key)
        else:
            new_node = self.entry_list.insert_after(node, Node({key}, node.count + 1))

        self.entry_dict[key] = new_node
        self.discard_key(node, key)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        node = self.entry_dict.get(key)

        if node.count > 1:
            if node.before.count == node.count - 1:
                new_node = node.before
                new_node.keys.add(key)
            else:
                new_node = self.entry_list.insert_after(
                    node.before, Node({key}, node.count - 1)
                )

            self.entry_dict[key] = new_node
        else:
            del self.entry_dict[key]

        self.discard_key(node, key)

    def getMaxKey(self):
        """
        :rtype: str
        """
        return next(iter(self.entry_list.tail.before.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        return next(iter(self.entry_list.head.after.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()