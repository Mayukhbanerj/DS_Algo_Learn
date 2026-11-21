"""Chapter 12 educational binary-search-tree implementation."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterator, TypeVar, Generic

K=TypeVar("K")
@dataclass
class Node(Generic[K]):
    key: K
    left: Optional["Node[K]"]=None
    right: Optional["Node[K]"]=None
    parent: Optional["Node[K]"]=None

class BinarySearchTree(Generic[K]):
    def __init__(self):
        self.root: Optional[Node[K]]=None
        self.size=0

    def search(self,key:K)->Optional[Node[K]]:
        x=self.root
        while x is not None and x.key!=key:
            x=x.left if key<x.key else x.right
        return x

    def minimum(self,x:Optional[Node[K]]=None)->Optional[Node[K]]:
        x=self.root if x is None else x
        if x is None:return None
        while x.left is not None:x=x.left
        return x

    def maximum(self,x:Optional[Node[K]]=None)->Optional[Node[K]]:
        x=self.root if x is None else x
        if x is None:return None
        while x.right is not None:x=x.right
        return x

    def successor(self,x:Node[K])->Optional[Node[K]]:
        if x.right is not None:return self.minimum(x.right)
        y=x.parent
        while y is not None and x is y.right:
            x,y=y,y.parent
        return y

    def predecessor(self,x:Node[K])->Optional[Node[K]]:
        if x.left is not None:return self.maximum(x.left)
        y=x.parent
        while y is not None and x is y.left:
            x,y=y,y.parent
        return y

    def insert(self,key:K)->Node[K]:
        z=Node(key);y=None;x=self.root
        while x is not None:
            y=x
            x=x.left if key<x.key else x.right
        z.parent=y
        if y is None:self.root=z
        elif key<y.key:y.left=z
        else:y.right=z
        self.size+=1
        return z

    def _transplant(self,u:Node[K],v:Optional[Node[K]])->None:
        if u.parent is None:self.root=v
        elif u is u.parent.left:u.parent.left=v
        else:u.parent.right=v
        if v is not None:v.parent=u.parent

    def delete(self,z:Node[K])->None:
        if z.left is None:self._transplant(z,z.right)
        elif z.right is None:self._transplant(z,z.left)
        else:
            y=self.minimum(z.right)
            assert y is not None
            if y.parent is not z:
                self._transplant(y,y.right)
                y.right=z.right
                y.right.parent=y
            self._transplant(z,y)
            y.left=z.left
            y.left.parent=y
        z.left=z.right=z.parent=None
        self.size-=1

    def inorder(self)->list[K]:
        out=[];stack=[];cur=self.root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur);cur=cur.left
            cur=stack.pop();out.append(cur.key);cur=cur.right
        return out

    def preorder(self)->list[K]:
        if self.root is None:return []
        out=[];stack=[self.root]
        while stack:
            x=stack.pop();out.append(x.key)
            if x.right is not None:stack.append(x.right)
            if x.left is not None:stack.append(x.left)
        return out

    def postorder(self)->list[K]:
        if self.root is None:return []
        out=[];stack=[(self.root,False)]
        while stack:
            x,visited=stack.pop()
            if visited:out.append(x.key)
            else:
                stack.append((x,True))
                if x.right is not None:stack.append((x.right,False))
                if x.left is not None:stack.append((x.left,False))
        return out

    def height(self)->int:
        if self.root is None:return -1
        best=-1;stack=[(self.root,0)]
        while stack:
            x,d=stack.pop();best=max(best,d)
            if x.left is not None:stack.append((x.left,d+1))
            if x.right is not None:stack.append((x.right,d+1))
        return best

    def validate(self)->bool:
        stack=[(self.root,None,None,None)] if self.root else []
        seen=set()
        while stack:
            x,lo,hi,parent=stack.pop()
            if id(x) in seen:return False
            seen.add(id(x))
            if x.parent is not parent:return False
            if lo is not None and x.key<lo:return False
            if hi is not None and x.key>hi:return False
            if x.left:stack.append((x.left,lo,x.key,x))
            if x.right:stack.append((x.right,x.key,hi,x))
        return len(seen)==self.size
