# https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory(object):
    def __init__(self, homepage):
        self.homepage = Node(homepage)
        self.currentPage = self.homepage

    def visit(self, url):
        newNode = Node(url)
        self.currentPage.next = newNode
        newNode.prev = self.currentPage
        self.currentPage = newNode
        return None

    def back(self, steps):
        i = 0
        while i < steps or self.currentPage.prev is not None:
            i += 1
            self.currentPage = self.currentPage.prev
        return self.currentPage.val

    def forward(self, steps):
        i = 0
        while i < steps or self.currentPage.next is not None:
            i += 1
            self.currentPage = self.currentPage.next
        return self.currentPage.val
