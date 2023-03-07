from collections import deque
class BITreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None
class BST:
    def __init__(self,li):
        self.root=None
        if li:
            for i in li:
                self.insert_no_sec(i)
    def insert(self,node,val):
        if not node:
            node=BITreeNode(val)
        elif val>node.data:
            node.lchild=self.insert(node.lchild,val)
            node.lchild.parent=node
        elif val<node.data:
            node.rchild=self.insert(node.rchild,val)
            node.rchild.parent=node
        return node
    def insert_no_sec(self,val):

        if not self.root:
            self.root=BITreeNode(val)
            return  self.root
        p=self.root;
        while p:
            if val<p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=BITreeNode(val)
                    p.lchild.parent=p
                    return
            elif val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BITreeNode(val)
                    p.rchild.parent=p
                    return
            else:
                return
    def pre_order(self,root):
        if root:
            print(root.data)
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data)
            self.in_order(root.rchild)
    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data)
    def level_order(self):
        q=deque()
        if self.root:
            q.append(self.root)
        while q:
            node=q.popleft()
            print(node.data)
            if node.lchild:
                q.append(node.lchild)
            if node.rchild:
                q.append(node.rchild)
    def query(self,node,val):
        if not self.root:
            return None
        if val >node.data:
            self.query(node.lchild,val)
        elif val>node.data:
            self.query(node.rchild,val)
        else:
            return node
    def query_no_rec(self,val):
        p=self.root
        while p:
            if p.data<val:
                p=p.rchild
            elif p.data>val:
                p=p.lchild
            else:
                return p
        else:
            return None
    def __remove_node_1(self,node):
        if not node.parent:
            self.root=None
        else:
            if node == node.parent.lchild:
                node.parent.lchild=None
            elif node == node.parent.rchild:
                node.parent.rchild=None
    def __remove_node_21(self,node):#node只有一个左孩子
        if not node.parent:
            self.root=node.lchild
            node.parent=None
        elif node == node.parent.lchild:
            node.parent.lchild=node.lchild
            node.lchild.parent=node.parent
        elif node == node.parent.rchild:
            node.parent.lchild=node.lchild
            node.lchild.parent=node.parent
    def __remove_node_22(self,node):#node只有一个右孩子
        if not node.parent:
            self.root=node.rchild
        elif node==node.parent.lchild:
            node.parent.lchild=node.rchild
            node.rchild.parent=node.parent
        elif node==node.parent.rchild:
            node.parent.rchild=node.rchild
            node.rchild.parent=node.parent
    def delete(self,val):
        if  self.root:
            node=self.query_no_rec(val)
            if  not node:
                print("不存在")
                return None
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:
                self.__remove_node_21(node)
            elif not node.lchild:
                self.__remove_node_22(node)
            else:
                min_node=node.rchild
                while min_node.lchild:
                    min_node=min_node.lchild
                node.data=min_node.data
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

class AVLNode(BITreeNode):
    def __init__(self,data):
        BITreeNode.__init__(self,data)
        self.bf=0

class AVLTree(BST):
    def __init__(self,li):
        BST.__init__(self,li)

    def rotate_left(self,p,c):
        s2=c.lchild
        p.rchild=s2
        if s2:
            s2.parent=c.parent
        c.lchid=p
        p.parent=c
        p.bf=0
        c.bf=0
        return c
    def rotate_right(self,p,c):
        s2=c.rchild
        p.lchild=s2
        if s2:
            s2.parent=c.parent
        c.rchild=p
        p.parent=c
        p.bf=0
        c.bf=0
        return c
    def rotate_right_left(self,p,c):
        g=c.lchild
        s3=g.rchild
        c.lchild=s3
        if s3:
            s3.parent=c
        g.rchild=c
        c.paernt=g
        s2=g.lchild
        p.rchild=s2
        if s2:
            s2.parent=p
        g.lchild=p
        p.paernt=g

        if g.bf>0:
            p.bf=-1
            c.bf=0
        elif g.bf<0:
            p.bf=0
            c.bf=1
        g.bf=0
        return g
    def rotate_left_right(self,p,c):
        g=c.rchild
        s2=g.lchild
        c.rchild=s2
        if s2:
            s2.parent=c
        g.lchild=c
        c.parent=g
        s3=g.rchild
        p.lchild=s3
        if s3:
            s3.parent=p
        g.rchild=p
        p.parent=g

        if g.bf>0:
            c.bf=-1
            p.bf=0
        elif g.bf<0:
            c.bf=0
            p.bf=1
        g.bf=0
        return g
    def insert_no_rec(self,val):
        if not self.root:
            self.root=BITreeNode(val)
            return
        p=self.root;
        while p:
            if val<p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=BITreeNode(val)
                    p.lchild.parent=p
                    node=p.lchild
                    break
            elif val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BITreeNode(val)
                    p.rchild.parent=p
                    node=p.rchild
                    break
            else:
                return
        while node.parent:
            if node.parent.lchild==node:
                if node.parent.bf <0:
                    g=node.parent.parent
                    x=node.parent
                    if node.bf>0:
                        n=self.rotate_left_right(node.parent,node)
                    else:
                        n=self.rotate_right(node.parent,node)
                elif node.parent.bf>0:
                    node.parent.bf=0
                else:
                    node.parent.bf=-1
                    node=node.parent
                    continue
            else:
                if node.parent.bf>0:
                    g=node.parent.parent
                    x=node.parent
                    if node.bf<0:
                        n=self.rotate_right_left(node.parent,node)
                    else:
                        n=self.rotate_left(node.parent,node)
                elif node.parent.bf<0:
                    node.parent.bf=0
                    break
                else:
                    node.parent.bf=1
                    node=node.parent
                    continue

            n.parent=g
            if g:
                if x==g.lchild:
                    g.lchild=n
                else:
                    g.rchild=n
                break
            else:
                self.root = n
                break
tree=AVLTree([6,7,8,])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("\n")
print(tree.level_order())
print("\n")

