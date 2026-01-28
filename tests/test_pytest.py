def test_user_login():
    print("Xola lgn!")

def test_assert_login():
    assert ("True" != "False")
    print("Xola assrt!")


class TestUserLogin:

    def test_1(self):
        print("Xola t1!")
        pass

    def test_2(self):
        print("Xola t2!")
        pass

def test_assert_positive_case():
    assert (2 + 2) == 4

def test_assert_negative_case():
    assert (2 + 2) == 5, "2 + 2 != 5"