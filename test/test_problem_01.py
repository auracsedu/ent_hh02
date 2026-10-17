import pytest

from problem_01 import align, justify, wrap

LINES = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]


@pytest.mark.parametrize(
    "text, width, expected",
    [
        ("the quick brown fox jumps over the lazy dog", 10, LINES),
        ("a bb ccc dddd", 7, ["a bb", "ccc", "dddd"]),
        ("abcdefghijkl xy", 5, ["abcdefghijkl", "xy"]),
        ("a b c d e f", 3, ["a b", "c d", "e f"]),
        ("a b c d e f", 1, ["a", "b", "c", "d", "e", "f"]),
        ("aa bb", 5, ["aa bb"]),
        ("aa bb", 4, ["aa", "bb"]),
        ("  lots   of   space  ", 8, ["lots of", "space"]),
        ("x toolongword y", 4, ["x", "toolongword", "y"]),
        ("", 10, []),
        ("   ", 10, []),
    ],
)
def test_wrap(text, width, expected):
    assert wrap(text, width) == expected


def test_wrap_default_width_is_20():
    assert wrap("hello world") == ["hello world"]
    assert wrap("one two three four five six seven") == [
        "one two three four",
        "five six seven",
    ]


def test_align_left():
    assert align(LINES, 10) == [
        "the quick ",
        "brown fox ",
        "jumps over",
        "the lazy  ",
        "dog       ",
    ]
    assert align(LINES, 10, "left") == align(LINES, 10)


def test_align_right():
    assert align(LINES, 10, "right") == [
        " the quick",
        " brown fox",
        "jumps over",
        "  the lazy",
        "       dog",
    ]


def test_align_center():
    assert align(["ab"], 7, "center") == ["  ab   "]
    assert align(["ab", "abcd"], 6, how="center") == ["  ab  ", " abcd "]
    assert align(["abc"], 6, "center") == [" abc  "]
    assert align(["abc"], 3, "center") == ["abc"]


def test_align_keeps_long_lines():
    for how in ["left", "right", "center"]:
        assert align(["toolong", "ab"], 3, how) == ["toolong", align(["ab"], 3, how)[0]]


def test_align_does_not_modify_input():
    lines = ["a", "bb"]
    align(lines, 5, "right")
    assert lines == ["a", "bb"]


def test_justify_example():
    assert justify(["a b c", "dd e", "f"], 7) == ["a  b  c", "dd    e", "f      "]


def test_justify_classic():
    assert justify(["this is an", "example of text", "justification."], 16) == [
        "this    is    an",
        "example  of text",
        "justification.  ",
    ]


def test_justify_uneven_gaps_go_left_first():
    assert justify(["a b c d", "x"], 10) == ["a  b  c  d", "x         "]
    assert justify(["a b c", "z"], 8) == ["a   b  c", "z       "]
    assert justify(["aa b c d", "z"], 12) == ["aa   b  c  d", "z           "]


def test_justify_single_word_lines_are_padded():
    assert justify(["abc", "de fg", "h"], 6) == ["abc   ", "de  fg", "h     "]


def test_justify_last_line_is_left_aligned():
    assert justify(["a b"], 5) == ["a b  "]
    assert justify(["a b", "c d"], 5) == ["a   b", "c d  "]


def test_justify_long_line_unchanged():
    assert justify(["abcdefgh", "x"], 4) == ["abcdefgh", "x   "]


def test_justify_does_not_modify_input():
    lines = ["a b", "c"]
    justify(lines, 5)
    assert lines == ["a b", "c"]


def test_wrap_then_justify():
    lines = wrap("the quick brown fox jumps over the lazy dog", 11)
    assert lines == ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
    assert justify(lines, 11) == [
        "the   quick",
        "brown   fox",
        "jumps  over",
        "the    lazy",
        "dog        ",
    ]
