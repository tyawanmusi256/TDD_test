# FizzBuzz の作成
#
# 入力 n
# 出力 ans
#
# nが3の倍数の時、ans="Fizz"
# nが5の倍数の時、ans="Buzz"
# nが15の倍数の時、ans="FizzBuzz"
# nが以上の全ての条件外の時、ans=str(n)
#
# nは1以上の整数を想定
# 想定外の値を入力された場合、例外処理として、ans="-1"
#

class FizzBuzz:
    def __init__(self):
        self.ans = 0
        return
    
    def test_input(self, n):
        # 入力値の例外処理ができているかどうか
        if 0 <= n:
            return
        assert self.ans == "-1"
        return

    def test_fizz(self, n):
        # 3の倍数の場合にfizzを出力できているか
        if n%3 == 0 and n%5 != 0:
            assert self.ans == "fizz"
        return

    def test_buzz(self, n):
        # 5の倍数の場合にbuzzを出力できているか
        if n%3 != 0 and n%5 == 0:
            assert self.ans == "buzz"
        return

    def test_fizzbuzz(self, n):
        # 15の倍数の場合にfizzbuzzを出力できているか
        if n%3 == 0 and n%5 == 0:
            assert self.ans == "fizzbuzz"
        return

    def test_num(self, n):
        # nが3,5の倍数でない場合にその値をそのまま出力できているか
        if n%3 != 0 and n%5 != 0:
            assert self.ans == str(n)
        return

    def calc(self, n):
        # 入力値 n に対して出力する答え ans を計算する
        if n < 0:
            self.ans = "-1"
            return
        if n%3==0 and n%5 != 0:
            self.ans = "fizz"
            return
        if n%3!=0 and n%5 == 0:
            self.ans = "buzz"
            return
        if n%3==0 and n%5 == 0:
            self.ans = "fizzbuzz"
            return
        if n%3==0 and n%5 == 0:
            self.ans = str(n)
            return
        return

