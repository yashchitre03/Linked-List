# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:55:24 2020

@author: yashc
"""

class Node:
    """
    Used to created objects that represents one node in a linked list.
    
    """
    def __init__(self, val):
        self.val = val
        self.next = None


    def set_next(self, node):
        self.next = node


    def get_next(self):
        return self.next
    
    
    def get_val(self):
        return self.val


class LinkedList:
    """
    Represents the overall linked list with methods to manipulate data within the linked list.
    
    """
    def __init__(self):
        self.head = None


    def insert_at_start(self, new_val):
        """
        Inserts a new node at the start of the linked list.

        Args:
            new_val (int): Value of a node in a linked list.

        Returns:
            None.

        """
    
        new = Node(new_val)
        new.set_next(self.head)
        self.head = new
        print("Node added to the start of the linked list with value:", new_val)        


    def insert_at_end(self, new_val):
        """
        Inserts a new node at the end of the linked list.

        Args:
            new_val (int): Value of a node in a linked list.

        Returns:
            None.

        """
        new = Node(new_val)
        if self.is_empty():
            self.head = new
        else:
            temp = self.head
            while temp.get_next() is not None:
                temp = temp.get_next()
            temp.set_next(new)
        print("Node added to the end of the linked list with value:", new_val)
        
        
    def insert_after(self, current, new_val):
        """
        Inserts a new node after a node with given value.

        Args:
            current (int): Value of a node in a linked list.
            new_val (int): Value of a node in a linked list.

        Returns:
            index (int): Index of the new node inserted.

        """
        if not self.is_empty():
            new = Node(new_val)
            index = 0
            node = self.head
            while node is not None:
                index +=1
                if node.get_val() == current:
                    new.set_next(node.get_next())
                    node.set_next(new)
                    return index
                node = node.get_next()
            print("Item", current, "not found!")
            
            
    def insert_before(self, current, new_val):
        """
        Inserts a new node before a node with given value.

        Args:
            current (int): Value of a node in a linked list.
            new_val (int): Value of a node in a linked list.

        Returns:
            index (int): Index of the new node inserted.

        """
        if not self.is_empty():
            new = Node(new_val)
            index = 0
            if self.head.get_val == current:
                list.insert_at_start(new_val)
                return index
            node = self.head
            while node.get_next() is not None:
                if node.get_next().get_val() == current:
                    break
                node = node.get_next()
            if node.get_next() is None:
                print("Item", current, "not found")
            new.set_next(node.get_next())
            node.set_next(new)
        
        
    def insert_at_index(self, index, new_val):
        """
        Inserts a new node at a given index with given value.

        Args:
            index (int): Index at which to insert the new node
            new_val (TYPE): Value of a node in a linked list.

        Returns:
            new (Node object): Newly created object.

        """
        new = Node(new_val)
        if self.is_empty() and index == 0:
            self.head = new
            return new
        elif index == 0:
            new.set_next(self.head)
            self.head = new
        else:
            i = 1
            temp = self.head
            while i != index and temp.get_next() is not None:
                temp = temp.get_next()
                i +=1
            if i == index:
                new.set_next(temp.get_next())
                temp.set_next(new)
                return new
            else:
                print("Index not found!")
                
        
    def delete_first(self):
        """
        Deletes the first node in the linked list.

        Returns:
            None.

        """
        if not self.is_empty():
            print("First Node deleted with value:", self.head.get_val())
            self.head = self.head.get_next()
        
        
    def delete_last(self):
        """
        Deletes the last node in the linked list.

        Returns:
            None.

        """
        if not self.is_empty():
            temp = self.head
            if temp.next is None:
                t_val = temp.get_val()
                self.head = None
            else:
                while temp.get_next().get_next() is not None:
                    temp = temp.get_next()
                t_val = temp.get_next().get_val()
                temp.set_next(None)
            print("Last node deleted with value:", t_val)       
            
            
    def delete_at_index(self, index):
        """
        Deletes a node at a given index.

        Args:
            index (int): Position of node to delete.

        Returns:
            None.

        """
        if not self.is_empty():
            if index == 0:
                self.head = self.head.get_next()
            else:
                i = 1
                node = self.head
                while node.get_next() is not None:
                    if i == index:
                        node.set_next(node.get_next().get_next())
                    node = node.get_next()
                    
                    
    def delete_item(self, item):
        """
        Deletes an item with the given value

        Args:
            item (int): Value of node to delete.

        Returns:
            None.

        """
        if not self.is_empty():
            if self.head.get_val() == item:
                self.head = self.head.get_next()
            else:
                node = self.head
                while node.get_next() is not None:
                    if node.get_next().get_val == item:
                        node.set_next(node.get_next().get_next())
                    node = node.get_next()
          
            
    def traverse(self):
        """
        Traverses and prints all the node values in the list.

        Returns:
            None.

        """
        if not self.is_empty():
            temp = self.head
            while temp is not None:
                print("Value:", temp.get_val())
                temp = temp.get_next()
    
    
    def is_empty(self):
        """
        Returns whether the list is empty or not.

        Returns:
            bool: True if list is empty.

        """
        if self.head is None:
            print("Linked List is empty!")
            return True
        else:
            return False
    
    
    def size(self):
        """
        Returns the length of the linked list.

        Returns:
            size (int): size of list.

        """
        if not self.is_empty():
            size = 1
            temp = self.head
            while temp.get_next() is not None:
                size += 1
                temp = temp.get_next()
        else:
            size = 0
        print("Size is", size)
        return size
    
    
    def find(self, x):
        """
        Finds an item and returns the index.

        Args:
            x (int): Value of the node to find.

        Returns:
            TYPE (int/boolean): index of found else boolean value False.

        """
        if not self.is_empty():
            temp = self.head
            i = 0
            while temp is not None:
                if temp.get_val() == x:
                    print("Element", x, "found at index", i)
                    return i
                i += 1
                temp = temp.get_next()
            print("Element", x, "not found")
            return False
             
        
    def rev(self):
        """
        Reverses the linked list.

        Returns:
            None.

        """
        if not self.is_empty():
            prev = None
            node = self.head
            while node is not None:
                next = node.get_next()
                node.set_next(prev)
                prev = node
                node = next
            self.head = prev
        
        
if __name__ == "__main__":
    print("Program starts")
    list = LinkedList()
    list.insert_at_start(1)
    list.insert_at_end(2)
    list.insert_at_start(3)
    list.insert_at_end(4)
    list.insert_after(5, 9)
    list.insert_before(3, 10)
    list.insert_at_index(2, 55)
    list.delete_item(3)
    list.delete_at_index(0)
    list.traverse()
    list.size()
    list.find(5)
    list.rev()
    list.traverse()                 
    list.delete_first()
    list.delete_last()
    list.delete_first()
    list.delete_last()
    list.delete_first()
    list.size()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    