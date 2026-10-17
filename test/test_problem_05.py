import pytest

from problem_05 import count_round, elimination_order, runoff

ABC = ["a", "b", "c"]
EXAMPLE = [["a", "b"], ["a", "c"], ["b", "c"], ["b", "a"], ["c", "b"]]
PLURALITY_LOSER = [["a", "c", "b"]] * 4 + [["b", "c", "a"]] * 3 + [["c", "b", "a"]] * 2
EXHAUSTED = [["a"], ["a"], ["b", "c"], ["b", "c"], ["c"]]
ABCD = ["a", "b", "c", "d"]
THREE_ROUNDS = (
    [["a", "d"]] * 3 + [["b", "d"]] * 3 + [["c", "b"]] * 2 + [["d", "c", "a"]] * 2
)


@pytest.mark.parametrize(
    "candidates, ballots, eliminated, expected",
    [
        (ABC, EXAMPLE, set(), {"a": 2, "b": 2, "c": 1}),
        (ABC, EXAMPLE, {"c"}, {"a": 2, "b": 3}),
        (ABC, EXAMPLE, {"a", "c"}, {"b": 4}),  # ["a", "c"] 용지는 버려짐
        (ABC, [["a"], ["a"]], set(), {"a": 2, "b": 0, "c": 0}),
        (ABC, [["a"], ["a"]], {"a"}, {"b": 0, "c": 0}),  # 전부 탈락한 용지는 버림
        (ABC, [["c", "b", "a"], ["b"], ["c"]], {"c"}, {"a": 0, "b": 2}),
        (ABCD, THREE_ROUNDS, {"d", "b"}, {"a": 3, "c": 4}),
    ],
)
def test_count_round(candidates, ballots, eliminated, expected):
    counts = count_round(candidates, ballots, eliminated)
    assert counts == expected
    assert list(counts) == list(expected)  # candidates 순서 유지


def test_count_round_does_not_modify_inputs():
    eliminated = {"c"}
    ballots = [["a", "b"], ["c"]]
    count_round(ABC, ballots, eliminated)
    assert eliminated == {"c"}
    assert ballots == [["a", "b"], ["c"]]


def test_runoff_example():
    assert runoff(ABC, EXAMPLE) == "b"
    assert elimination_order(ABC, EXAMPLE) == ["c"]


def test_runoff_immediate_majority():
    ballots = [["a"], ["a", "b"], ["b"], ["a", "c"]]
    assert runoff(ABC, ballots) == "a"
    assert elimination_order(ABC, ballots) == []


def test_runoff_single_candidate():
    assert runoff(["solo"], [["solo"], ["solo"]]) == "solo"
    assert elimination_order(["solo"], [["solo"], ["solo"]]) == []


def test_runoff_plurality_leader_can_lose():
    assert runoff(ABC, PLURALITY_LOSER) == "b"
    assert elimination_order(ABC, PLURALITY_LOSER) == ["c"]


def test_runoff_tie_eliminates_later_candidate():
    assert runoff(["x", "y"], [["x"], ["y"]]) == "x"
    assert elimination_order(["x", "y"], [["x"], ["y"]]) == ["y"]
    assert runoff(["y", "x"], [["x"], ["y"]]) == "y"
    assert elimination_order(["y", "x"], [["x"], ["y"]]) == ["x"]


def test_runoff_exhausted_ballots():
    assert runoff(ABC, EXHAUSTED) == "a"
    assert elimination_order(ABC, EXHAUSTED) == ["c", "b"]


def test_runoff_three_rounds():
    # 1라운드 a3 b3 c2 d2 -> d 탈락 / 2라운드 a3 b3 c4 -> b 탈락 / 3라운드 a3 c4 (7표) -> c
    assert runoff(ABCD, THREE_ROUNDS) == "c"
    assert elimination_order(ABCD, THREE_ROUNDS) == ["d", "b"]


def test_runoff_does_not_modify_inputs():
    ballots = [["a", "b"], ["b"], ["c", "a"]]
    runoff(ABC, ballots)
    elimination_order(ABC, ballots)
    assert ballots == [["a", "b"], ["b"], ["c", "a"]]
    assert ABC == ["a", "b", "c"]
