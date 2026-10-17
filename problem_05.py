"""
[도전] 문제 5. 결선 투표

후보가 여럿일 때 쓰는 "결선 투표(instant-runoff)" 방식으로 당선자를 정하는 함수를
작성하세요. 유권자는 후보 전체 또는 일부를 좋아하는 순서대로 적어 냅니다.

count_round(candidates, ballots, eliminated)
- 아직 탈락하지 않은 후보(candidates 중 eliminated 에 없는 후보)별 득표수를
  딕셔너리로 돌려줍니다. 키는 candidates 순서를 따르고, 0표인 후보도 들어 있어야
  하며, 탈락한 후보는 들어 있으면 안 됩니다.
- 각 투표 용지는 적힌 순서대로 보아 "탈락하지 않은 첫 후보"에게 1표를 줍니다.
- 적힌 후보가 전부 탈락한 용지는 아무에게도 표를 주지 않습니다.

runoff(candidates, ballots)
- 다음을 당선자가 나올 때까지 반복합니다.
    1. count_round 로 이번 라운드 득표수를 셉니다.
    2. 어떤 후보의 득표수가 이번 라운드에 집계된 표 수의 절반보다 많으면 그 후보가
       당선입니다. (집계된 표 수 = 득표수의 합. 전부 탈락한 용지는 들어가지 않습니다.)
    3. 남은 후보가 한 명이면 그 후보가 당선입니다.
    4. 아니면 득표수가 가장 적은 후보를 탈락시킵니다. 가장 적은 후보가 여럿이면
       그중 candidates 에 뒤에 적힌 후보를 탈락시킵니다.
- 당선자 이름을 돌려줍니다.

elimination_order(candidates, ballots)
- runoff 와 같은 과정을 거치며 탈락한 후보 이름을 탈락한 순서대로 담은 리스트를
  돌려줍니다. 당선자는 들어 있지 않습니다. 첫 라운드에 바로 당선되면 빈 리스트입니다.

- candidates 에는 후보가 1명 이상 있고 중복이 없습니다.
- 투표 용지의 이름은 모두 candidates 에 있고, 한 용지 안에 같은 이름이 두 번 나오지
  않습니다. 빈 용지는 없지만, 1명만 적힌 용지는 있습니다. ballots 는 비어 있지
  않습니다.

예시
    candidates = ["a", "b", "c"]
    ballots = [["a", "b"], ["a", "c"], ["b", "c"], ["b", "a"], ["c", "b"]]

    count_round(candidates, ballots, set())    -> {"a": 2, "b": 2, "c": 1}
        5표 중 절반(2.5)을 넘는 후보가 없으므로, 가장 적은 c 탈락
    count_round(candidates, ballots, {"c"})    -> {"a": 2, "b": 3}
        b 가 5표 중 3표로 절반을 넘음
    runoff(candidates, ballots)                -> "b"
    elimination_order(candidates, ballots)     -> ["c"]

힌트
    - 전체를 한 번에 짜려 하지 말고, count_round 부터 만들어 테스트를 통과시킨 뒤
      나머지를 쓰세요. (python -m pytest -k count_round 로 count_round 만 따로
      테스트할 수 있습니다.)
    - 남은 후보 리스트를 먼저 만들고 dict.fromkeys(남은후보, 0) 으로 시작하면
      0표 후보가 저절로 들어갑니다.
    - 용지 하나에서 "탈락하지 않은 첫 후보" 를 찾으면 그 용지는 끝이므로 break 로
      다음 용지로 넘어가세요.
    - 탈락자는 set 에 모아 두면 name in eliminated 로 빠르게 확인됩니다. 탈락은
      eliminated.add(name) 이고, 순서가 필요하니 리스트에도 append 하세요.
    - 집계된 표 수는 sum(counts.values()) 입니다. 당선 조건 "절반보다 많으면" 은
      등호 없이 2 * 득표수 > 집계된 표 수 로 쓰면 나눗셈 없이 깔끔합니다.
    - "가장 적은 후보 중 candidates 에서 뒤쪽" 을 고르려면, 득표수가 같을 때도
      바꿔 끼우는 쪽(<=)으로 최솟값을 찾으세요.
    - runoff 와 elimination_order 는 같은 반복을 돕니다. 반복을 도는 함수 하나를
      만들어 (당선자, 탈락자리스트) 튜플을 돌려주게 하고, 두 함수는 각각 그중
      하나만 꺼내 돌려주세요. 같은 코드를 두 번 쓰지 않는 것이 함수를 배우는
      이유입니다.
    - 라운드마다 꼭 한 명이 탈락하므로 while True: 로 돌려도 반드시 끝납니다.
"""


def count_round(candidates: list, ballots: list, eliminated: set) -> dict:
    raise NotImplementedError


def runoff(candidates: list, ballots: list) -> str:
    raise NotImplementedError


def elimination_order(candidates: list, ballots: list) -> list:
    raise NotImplementedError
