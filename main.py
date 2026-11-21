# main.py
# 【エントリーポイント／プレゼンテーション層】
# アプリの起動地点。各層の部品を組み立て（依存性の注入）、
# ターミナル上でユーザーの入力を受け取り、結果を表示する役割を持つ。

from infrastructure.in_memory_memo_repository import InMemoryMemoRepository
from usecases.memo_usecase import MemoUseCase

def main():
   # --- 部品の組み立て ---
   # 保存先の実装（今回はメモリ）を作成し、それをユースケースに渡す
   # 保存先を変えたいときは、この1行を別のリポジトリに差し替えるだけでよい
   repo = InMemoryMemoRepository()
   usecase = MemoUseCase(repo)

   # --- メインループ：「0」が入力されるまでメニューを繰り返し表示する ---
   while True:
       # メニュー画面の表示
       print("\n=============================")
       print("  📝 メモ帳アプリ")
       print("=============================")
       print("1. メモを作成する")
       print("2. メモの一覧を見る")
       print("3. メモを削除する")
       print("0. 終了")
       print("-----------------------------")
       # ユーザーの入力を受け取り、前後の空白を除去する
       choice = input("番号を入力してください：").strip()

       # ===== 1. メモの作成 =====
       if choice == "1":
           title = input("タイトル：").strip()
           content = input("本文　　：").strip()
           try:
               # ユースケースにメモ作成を依頼する
               memo = usecase.create_memo(title, content)
               print(f"\n✅ メモを保存しました：「{memo.title}」")
           except ValueError as e:
               # タイトルが空などでルール違反だった場合はエラーメッセージを表示
               print(f"\n❌ エラー：{e}")

       # ===== 2. メモの一覧表示 =====
       elif choice == "2":
           memos = usecase.get_all_memos()
           if not memos:
               # メモが1件もない場合
               print("\n（メモはまだありません）")
           else:
               print(f"\n📋 メモ一覧（{len(memos)}件）")
               print("-----------------------------")
               # enumerate(..., 1) で1から始まる番号を付けて順に表示する
               for i, memo in enumerate(memos, 1):
                   # 作成時刻を「時:分:秒」の形式で表示
                   print(f"{i}. [{memo.created_at.strftime('%H:%M:%S')}] {memo.title}")
                   print(f"   {memo.content}")

       # ===== 3. メモの削除 =====
       elif choice == "3":
           memos = usecase.get_all_memos()
           if not memos:
               print("\n（削除できるメモがありません）")
           else:
               # 削除候補を番号付きで一覧表示する
               print(f"\n📋 削除するメモを選んでください（{len(memos)}件）")
               for i, memo in enumerate(memos, 1):
                   print(f"{i}. {memo.title}：{memo.content}")
               num = input("番号を入力してください（キャンセル：0）：").strip()
               if num == "0":
                   # 0 ならキャンセルして何もしない
                   print("キャンセルしました。")
               elif num.isdigit() and 1 <= int(num) <= len(memos):
                   # 数字かつ範囲内の番号なら、対応するメモを特定して削除する
                   # （表示番号は1始まり、リストの添字は0始まりなので -1 する）
                   target = memos[int(num) - 1]
                   usecase.delete_memo(target.id)
                   print(f"\n🗑️  「{target.title}」を削除しました。")
               else:
                   # 数字以外や範囲外の番号が入力された場合
                   print("\n❌ 正しい番号を入力してください。")

       # ===== 0. 終了 =====
       elif choice == "0":
           print("\n👋 終了します。\n")
           break  # while ループを抜けてプログラムを終了する

       # ===== メニューにない入力 =====
       else:
           print("\n❌ 0〜3の番号を入力してください。")

# このファイルを直接実行したときだけ main() を呼び出す
# （他のファイルから import された場合は実行されない）
if __name__ == "__main__":
   main()
