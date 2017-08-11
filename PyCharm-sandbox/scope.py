def scope_test():
    def do_local():
        v = 'local var'

    def do_nonlocal():
        nonlocal v    # スコープの外側の v（13 行目）を参照する
        v = 'nonlocal var'

    def do_global():
        global v    # モジュールスコープの v（24 行目）を参照する
        v = 'global var'

    v = 'test var'
    do_local()
    print('After local assignment:', v)
    do_nonlocal()
    print('After nonlocal assignment:', v)
    do_global()
    print('After global assignment:', v)


if __name__ == '__main__':
    scope_test()
    print('In global scope:', v)