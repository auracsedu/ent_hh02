"""
문제 2. 가게와 장바구니

가게의 재고 stock 과 손님의 장바구니 cart 는 둘 다 품목 이름을 키, 개수를 값으로
갖는 딕셔너리입니다. 재고에서 장바구니로 물건을 옮기는 함수, 되돌리는 함수,
영수증을 만드는 함수를 작성하세요.

add_items(cart, stock, **items)
- 키워드 인자로 받은 품목을 개수만큼 재고에서 꺼내 장바구니에 넣습니다.
  재고가 모자라면 있는 만큼만 옮기고, 재고에 없는 품목은 하나도 옮기지 않습니다.
- cart 와 stock 둘 다 그 자리에서 고칩니다. 재고가 0 이 된 품목은 stock 에서
  지웁니다.
- 다 못 담은 품목만 모아 {품목: 모자란 개수} 딕셔너리로 돌려줍니다. 다 담았으면
  빈 딕셔너리입니다.

remove_items(cart, stock, **items)
- 키워드 인자로 받은 품목을 개수만큼 장바구니에서 꺼내 재고로 되돌립니다.
  장바구니에 든 것보다 많이 빼라고 하면 든 만큼만 빼고, 장바구니에 없는 품목은
  무시합니다.
- 장바구니에서 0 이 된 품목은 cart 에서 지웁니다. 아무것도 돌려주지 않습니다.

receipt(cart, prices)
- prices 는 품목별 단가 딕셔너리입니다. prices 에 없는 품목은 0원으로 칩니다.
- 장바구니의 품목마다 "품목 N개 M원" (M = 개수 x 단가) 한 줄씩, 장바구니에 들어
  있는 순서대로 만들고, 마지막에 "합계 T원" 을 붙인 문자열 리스트를 돌려줍니다.
- 장바구니가 비어 있으면 ["합계 0원"] 입니다.

예시
    stock = {"apple": 5, "milk": 1, "egg": 30}
    cart = {}
    add_items(cart, stock, apple=2, milk=3, bread=1)    -> {"milk": 2, "bread": 1}
    cart     -> {"apple": 2, "milk": 1}
    stock    -> {"apple": 3, "egg": 30}
    add_items(cart, stock, apple=1, egg=10)             -> {}
    cart     -> {"apple": 3, "milk": 1, "egg": 10}
    stock    -> {"apple": 2, "egg": 20}
    remove_items(cart, stock, milk=5, egg=4, bread=1)
    cart     -> {"apple": 3, "egg": 6}
    stock    -> {"apple": 2, "egg": 24, "milk": 1}
    receipt(cart, {"apple": 1000, "egg": 300, "milk": 2500})
        -> ["apple 3개 3000원", "egg 6개 1800원", "합계 4800원"]

힌트
    - def add_items(cart, stock, **items): 처럼 받으면 items 는
      {"apple": 2, "milk": 3, "bread": 1} 같은 딕셔너리가 됩니다.
      for name, count in items.items(): 로 훑으세요. (교재 1.2.2 가변 키워드 인자)
    - 옮길 수 있는 개수는 min(count, stock.get(name, 0)) 입니다. 그만큼 stock 에서
      빼고 cart 에 더하되, cart 에 없던 품목은 cart.get(name, 0) + 옮긴개수 로
      새로 만드세요. 모자란 개수는 count - 옮긴개수 이고, 0 보다 클 때만 결과
      딕셔너리에 넣습니다.
    - 딕셔너리는 가변 객체라서 cart[name] = ... 으로 고치면 함수 밖의 장바구니도
      바뀝니다. cart = {} 처럼 새 딕셔너리를 대입하면 함수 안의 이름만 바뀌고
      밖은 그대로입니다. (교재 2.1 가변 객체)
    - 0 이 된 품목은 stock.pop(name) / cart.pop(name) 으로 지웁니다. 반복문으로
      cart 를 훑는 도중에 cart 에서 지우면 오류가 나니, items 쪽을 훑으세요.
    - receipt 는 f"{name} {count}개 {count * price}원" 줄을 리스트에 모으고,
      합계를 누적 변수에 더해 두었다가 마지막 줄로 붙이세요.
"""


def add_items(cart: dict, stock: dict, **items) -> dict:
    raise NotImplementedError


def remove_items(cart: dict, stock: dict, **items) -> None:
    raise NotImplementedError


def receipt(cart: dict, prices: dict) -> list:
    raise NotImplementedError
