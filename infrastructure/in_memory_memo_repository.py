# infrastructure/in_memory_memo_repository.py
# 【インフラストラクチャ層】
# インターフェース層で決めた約束事（MemoRepository）を、具体的な方法で実装する層。
# ここでは最も単純な「Pythonの辞書（メモリ上）」に保存する。
# ※ プログラムを終了するとデータは消える。
#   ファイルやDBに保存したくなったら、同じ約束事を守る別クラスを作って差し替えればよい。

from entities.memo import Memo
from interfaces.memo_repository import MemoRepository

class InMemoryMemoRepository(MemoRepository):  # 抽象クラスを継承して約束事を実装する
   """メモリ上にメモを保存する実装（最も単純な外側の層）"""

   def __init__(self):
       # メモの保存場所。キーがメモID、値がMemoオブジェクトの辞書
       # 先頭の _ は「クラスの外から直接触らないでね」という慣習的な目印
       self._store: dict[str, Memo] = {}

   def save(self, memo: Memo) -> None:
       # IDをキーにして辞書に格納する（同じIDなら上書きされる）
       self._store[memo.id] = memo

   def find_all(self) -> list[Memo]:
       # 辞書の値（Memoオブジェクト）だけを取り出してリストにして返す
       return list(self._store.values())

   def delete(self, memo_id: str) -> None:
       # 指定IDのメモを辞書から取り除く
       # 第2引数に None を渡しているので、IDが存在しなくてもエラーにならない
       self._store.pop(memo_id, None)
