import problem_03 as hangman


def test_example_game():
    hangman.start("apple", 3)
    assert hangman.guess("P") == "_ p p _ _"
    assert hangman.lives == 3
    assert hangman.history == [("p", True)]
    assert hangman.guess("z") == "_ p p _ _"
    assert hangman.lives == 2
    assert hangman.history == [("p", True), ("z", False)]
    assert hangman.guess("p") == "_ p p _ _"
    assert hangman.lives == 2
    assert hangman.history == [("p", True), ("z", False)]
    assert hangman.hint() == "a p p _ _"
    assert hangman.lives == 1
    assert hangman.history == [("p", True), ("z", False), ("a", True)]
    assert hangman.hint() == "a p p _ _"
    assert hangman.lives == 1
    assert hangman.status() == "진행 중"
    assert hangman.wrong_letters() == ["z"]
    assert hangman.guess("e") == "a p p _ e"
    assert hangman.guess("l") == "a p p l e"
    assert hangman.status() == "성공"
    assert hangman.guessed == {"p", "z", "a", "e", "l"}


def test_start_resets_everything():
    hangman.start("hi", 1)
    hangman.guess("x")
    assert hangman.status() == "실패"
    assert hangman.start("yo", 3) is None
    assert hangman.status() == "진행 중"
    assert hangman.lives == 3
    assert hangman.guessed == set()
    assert hangman.history == []
    assert hangman.guess("y") == "y _"


def test_default_lives_is_six():
    hangman.start("cat")
    assert hangman.lives == 6
    for letter in "xyzuvw":
        hangman.guess(letter)
    assert hangman.lives == 0
    assert hangman.status() == "실패"
    assert hangman.wrong_letters() == ["u", "v", "w", "x", "y", "z"]


def test_repeated_wrong_guess_costs_once():
    hangman.start("dog", 3)
    hangman.guess("z")
    hangman.guess("z")
    hangman.guess("Z")
    assert hangman.lives == 2
    assert hangman.guessed == {"z"}
    assert hangman.history == [("z", False)]


def test_hint_reveals_first_unrevealed_in_secret_order():
    hangman.start("banana", 6)
    assert hangman.hint() == "b _ _ _ _ _"
    assert hangman.hint() == "b a _ a _ a"
    assert hangman.hint() == "b a n a n a"
    assert hangman.lives == 3
    assert hangman.status() == "성공"
    assert hangman.history == [("b", True), ("a", True), ("n", True)]
    assert hangman.hint() == "b a n a n a"  # 끝난 게임은 그대로
    assert hangman.lives == 3


def test_hint_skips_already_guessed_letters():
    hangman.start("apple", 6)
    hangman.guess("a")
    hangman.guess("p")
    assert hangman.hint() == "a p p l _"
    assert hangman.lives == 5


def test_hint_needs_at_least_two_lives():
    hangman.start("cat", 2)
    assert hangman.hint() == "c _ _"
    assert hangman.lives == 1
    assert hangman.hint() == "c _ _"
    assert hangman.lives == 1
    assert hangman.history == [("c", True)]
    assert hangman.guess("z") == "c _ _"
    assert hangman.status() == "실패"


def test_after_game_over_nothing_changes():
    hangman.start("ab", 1)
    assert hangman.guess("z") == "_ _"
    assert hangman.status() == "실패"
    assert hangman.guess("a") == "_ _"
    assert hangman.guessed == {"z"}
    assert hangman.history == [("z", False)]
    assert hangman.lives == 0

    hangman.start("ab", 1)
    hangman.guess("a")
    assert hangman.guess("b") == "a b"
    assert hangman.status() == "성공"
    assert hangman.guess("z") == "a b"
    assert hangman.lives == 1
    assert hangman.history == [("a", True), ("b", True)]


def test_wrong_letters_sorted():
    hangman.start("dog", 9)
    for ch in "zqa":
        hangman.guess(ch)
    hangman.guess("o")
    assert hangman.wrong_letters() == ["a", "q", "z"]
    assert hangman.lives == 6
    hangman.start("dog", 9)
    assert hangman.wrong_letters() == []
