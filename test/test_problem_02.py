from problem_02 import add_items, receipt, remove_items


def test_example_sequence():
    stock = {"apple": 5, "milk": 1, "egg": 30}
    cart = {}
    assert add_items(cart, stock, apple=2, milk=3, bread=1) == {"milk": 2, "bread": 1}
    assert cart == {"apple": 2, "milk": 1}
    assert stock == {"apple": 3, "egg": 30}
    assert add_items(cart, stock, apple=1, egg=10) == {}
    assert cart == {"apple": 3, "milk": 1, "egg": 10}
    assert stock == {"apple": 2, "egg": 20}
    assert remove_items(cart, stock, milk=5, egg=4, bread=1) is None
    assert cart == {"apple": 3, "egg": 6}
    assert stock == {"apple": 2, "egg": 24, "milk": 1}
    assert receipt(cart, {"apple": 1000, "egg": 300, "milk": 2500}) == [
        "apple 3개 3000원",
        "egg 6개 1800원",
        "합계 4800원",
    ]


def test_add_nothing():
    cart = {"apple": 1}
    stock = {"apple": 1}
    assert add_items(cart, stock) == {}
    assert cart == {"apple": 1}
    assert stock == {"apple": 1}


def test_add_exact_stock_removes_it_from_stock():
    cart = {}
    stock = {"pen": 3, "cup": 1}
    assert add_items(cart, stock, pen=3) == {}
    assert cart == {"pen": 3}
    assert stock == {"cup": 1}


def test_add_unknown_item_adds_nothing():
    cart = {}
    stock = {"pen": 1}
    assert add_items(cart, stock, cup=2) == {"cup": 2}
    assert cart == {}
    assert stock == {"pen": 1}


def test_add_partial_reports_only_shortfall():
    cart = {"pen": 1}
    stock = {"pen": 2, "cup": 9}
    assert add_items(cart, stock, pen=5, cup=4) == {"pen": 3}
    assert cart == {"pen": 3, "cup": 4}
    assert stock == {"cup": 5}


def test_remove_returns_items_to_stock():
    cart = {"a": 2, "b": 1}
    stock = {}
    remove_items(cart, stock, a=1)
    assert cart == {"a": 1, "b": 1}
    assert stock == {"a": 1}
    remove_items(cart, stock, b=9, zzz=1)
    assert cart == {"a": 1}
    assert stock == {"a": 1, "b": 1}
    remove_items(cart, stock, a=1)
    assert cart == {}
    assert stock == {"a": 2, "b": 1}


def test_same_dict_objects_are_modified():
    cart = {}
    stock = {"x": 1}
    same_cart, same_stock = cart, stock
    add_items(cart, stock, x=1)
    assert same_cart == {"x": 1}
    assert same_stock == {}
    remove_items(cart, stock, x=1)
    assert same_cart == {}
    assert same_stock == {"x": 1}


def test_receipt_empty_and_missing_price():
    assert receipt({}, {}) == ["합계 0원"]
    assert receipt({"a": 2, "b": 1}, {"a": 500}) == ["a 2개 1000원", "b 1개 0원", "합계 1000원"]


def test_receipt_order_follows_cart():
    assert receipt({"z": 1, "a": 1}, {"z": 10, "a": 20}) == ["z 1개 10원", "a 1개 20원", "합계 30원"]
