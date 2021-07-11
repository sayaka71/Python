# -*- coding: utf-8 -*-

# Import re for regex (正規表現) class
import re

class Regex():
    def __init__(self, re_word="[pP]y", parse_args="hiyopy"):
        self.re_word = re_word
        self.parse_args = parse_args
    
    def re_pattern_word(self):
        """patternを確認"""
        print("\nParse: " + self.parse_args)
        print("Pattern: " + self.re_word)

    def re_pattern_change(self, change):
        """re_word引数を変える"""
        self.re_word = change

    def re_command(self, command="search", sub_word="piyo"):
        """
        re.compile で正規表現 object 作成して，
        いろんな命令をだす。
        """
        pattern = re.compile(self.re_word)

        if command=="search":
            result = pattern.search(self.parse_args)
            print_word = "\nSearch Result: "
            print(print_word)
            print(result)

        elif command=="sub":
            result = pattern.sub(sub_word, self.parse_args)
            print_word = "\nSub Result ({}): ".format(sub_word)
            print(print_word)
            print(result)

        elif command=="findall":
            result = pattern.findall(self.parse_args)
            print_word = "\nFindall Result: "
            print(print_word)
            print(result)


if __name__ == '__main__':
    reg = Regex()
    reg.re_pattern_word()
    reg.re_command("sub")

    reg.re_pattern_change("[Hh]i")
    reg.re_pattern_word()
    reg.re_command("sub")

    reg.re_command("findall")

    # $ python3 pra_10.python3
    # Parse: hiyopy
    # Pattern: [pP]y

    # Sub Result (piyo):
    # hiyopiyo

    # Parse: hiyopy
    # Pattern: [Hh]i

    # Sub Result (piyo):
    # piyoyopy

    # Findall Result:
    # ['hi']