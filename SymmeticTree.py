# ノードクラスの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None): # コンストラクタ
        self.val = val #ノードがもつ数値
        self.left = left # ノードの左エッジ
        self.right = right # 右エッジ

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if not t1 and not t2: # t1,t2どちらもfalseの時
            return True # 左右対称
        if not t1 or not t2: # どちらかがtrueでない時
            return False # 左右非対称
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

if __name__ == '__main__':
    root1 = [1,2,2,3,4,4,3]
    Sol = Solution(root1)
    Sol.isSymmetric()
    