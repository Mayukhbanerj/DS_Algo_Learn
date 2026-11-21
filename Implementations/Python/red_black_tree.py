"""Chapter 13 CLRS-style red-black tree with a shared NIL sentinel."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Iterator

K = TypeVar("K")

@dataclass(eq=False)
class RBNode(Generic[K]):
    key: Optional[K] = None
    color: str = "BLACK"
    left: Optional["RBNode[K]"] = None
    right: Optional["RBNode[K]"] = None
    parent: Optional["RBNode[K]"] = None

class RedBlackTree(Generic[K]):
    def __init__(self):
        self.nil: RBNode[K] = RBNode()
        self.nil.color = "BLACK"
        self.nil.left = self.nil.right = self.nil.parent = self.nil
        self.root: RBNode[K] = self.nil
        self.size = 0

    def _left_rotate(self, x: RBNode[K]) -> None:
        y = x.right
        if y is self.nil:
            raise ValueError("left rotation requires a non-NIL right child")
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y: RBNode[K]) -> None:
        x = y.left
        if x is self.nil:
            raise ValueError("right rotation requires a non-NIL left child")
        y.left = x.right
        if x.right is not self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.nil:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, key: K) -> Optional[RBNode[K]]:
        x = self.root
        while x is not self.nil and key != x.key:
            x = x.left if key < x.key else x.right
        return None if x is self.nil else x

    def minimum(self, x: Optional[RBNode[K]] = None) -> Optional[RBNode[K]]:
        x = self.root if x is None else x
        if x is self.nil:
            return None
        while x.left is not self.nil:
            x = x.left
        return x

    def maximum(self, x: Optional[RBNode[K]] = None) -> Optional[RBNode[K]]:
        x = self.root if x is None else x
        if x is self.nil:
            return None
        while x.right is not self.nil:
            x = x.right
        return x

    def successor(self, x: RBNode[K]) -> Optional[RBNode[K]]:
        if x.right is not self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y is not self.nil and x is y.right:
            x, y = y, y.parent
        return None if y is self.nil else y

    def insert(self, key: K) -> RBNode[K]:
        z = RBNode(key=key, color="RED", left=self.nil, right=self.nil, parent=self.nil)
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            x = x.left if key < x.key else x.right
        z.parent = y
        if y is self.nil:
            self.root = z
        elif key < y.key:
            y.left = z
        else:
            y.right = z
        self.size += 1
        self._insert_fixup(z)
        return z

    def _insert_fixup(self, z: RBNode[K]) -> None:
        while z.parent.color == "RED":
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def _transplant(self, u: RBNode[K], v: RBNode[K]) -> None:
        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, z: RBNode[K]) -> None:
        if z is self.nil:
            raise KeyError("cannot delete NIL")
        y = z
        y_original_color = y.color
        if z.left is self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "BLACK":
            self._delete_fixup(x)
        z.left = z.right = z.parent = self.nil
        self.size -= 1

    def _delete_fixup(self, x: RBNode[K]) -> None:
        while x is not self.root and x.color == "BLACK":
            if x is x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"
        self.nil.color = "BLACK"

    def inorder(self) -> list[K]:
        out: list[K] = []
        stack: list[RBNode[K]] = []
        x = self.root
        while x is not self.nil or stack:
            while x is not self.nil:
                stack.append(x)
                x = x.left
            x = stack.pop()
            out.append(x.key)
            x = x.right
        return out

    def validate(self) -> bool:
        if self.nil.color != "BLACK" or self.nil.left is not self.nil or self.nil.right is not self.nil:
            return False
        if self.root is self.nil:
            return self.size == 0
        if self.root.parent is not self.nil or self.root.color != "BLACK":
            return False
        seen: set[int] = set()
        def walk(x: RBNode[K], low, high, parent: RBNode[K]) -> Optional[int]:
            if x is self.nil:
                return 0
            if id(x) in seen or x.parent is not parent:
                raise ValueError
            seen.add(id(x))
            if low is not None and x.key < low:
                raise ValueError
            if high is not None and x.key > high:
                raise ValueError
            if x.color not in ("RED", "BLACK"):
                raise ValueError
            if x.color == "RED" and (x.left.color != "BLACK" or x.right.color != "BLACK"):
                raise ValueError
            left_bh = walk(x.left, low, x.key, x)
            right_bh = walk(x.right, x.key, high, x)
            if left_bh != right_bh:
                raise ValueError
            return left_bh + (1 if x.color == "BLACK" else 0)
        try:
            walk(self.root, None, None, self.nil)
        except (ValueError, RecursionError):
            return False
        return len(seen) == self.size

    def __len__(self) -> int:
        return self.size
