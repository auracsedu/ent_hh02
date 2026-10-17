"""
문제 3. 행맨

단어 맞히기 게임의 상태를 전역 변수로 관리하는 함수들을 작성하세요. 파일 맨 위에
전역 변수 secret(정답 단어), guessed(지금까지 낸 글자 집합), lives(남은 목숨),
history(낸 글자 기록 리스트)가 선언되어 있습니다.

start(word, lives_count=6)
- 새 게임을 시작합니다. secret 을 word 로, lives 를 lives_count 로 바꾸고,
  guessed 와 history 를 비웁니다. 아무것도 돌려주지 않습니다.
- word 는 소문자 알파벳 한 글자 이상입니다.

guess(letter)
- 한 글자를 추측합니다. 대문자로 들어오면 소문자로 바꿔서 처리합니다.
- 처음 내는 글자면 guessed 에 넣고, history 에 (글자, 맞았는지) 튜플을 붙입니다.
  secret 에 없는 글자면 lives 를 1 줄입니다.
- 이미 낸 글자면 아무것도 바꾸지 않습니다.
- 게임이 이미 끝났으면(status 가 "진행 중" 이 아니면) 아무것도 바꾸지 않습니다.
- 언제나 현재 상태 문자열(아래 참고)을 돌려줍니다.

hint()
- 아직 맞히지 못한 글자 중 secret 에서 가장 앞에 있는 것을 공개합니다. 공개한
  글자는 guessed 에 넣고 history 에 (글자, True) 를 붙이며, 목숨을 1 줄입니다.
- lives 가 1 이하이거나 게임이 끝났으면 아무것도 바꾸지 않습니다.
- 현재 상태 문자열을 돌려줍니다.

status()
- secret 의 모든 글자를 맞혔으면 "성공", 아니고 lives 가 0 이면 "실패", 둘 다
  아니면 "진행 중" 을 돌려줍니다.

wrong_letters()
- 낸 글자 중 secret 에 없는 것들을 정렬한 리스트로 돌려줍니다.

현재 상태 문자열: secret 의 각 글자를 공백 하나로 띄어 쓰되, 아직 낸 적 없는
글자는 "_" 로 가립니다. 예: "a _ _ l e"

예시
    start("apple", 3)
    guess("P")    -> "_ p p _ _"      # lives 3, history [("p", True)]
    guess("z")    -> "_ p p _ _"      # lives 2, history [("p", True), ("z", False)]
    guess("p")    -> "_ p p _ _"      # 이미 낸 글자, 아무 변화 없음
    hint()        -> "a p p _ _"      # a 공개, lives 1
    hint()        -> "a p p _ _"      # lives 가 1 이라 힌트 불가
    status()      -> "진행 중"
    wrong_letters()    -> ["z"]
    guess("e")    -> "a p p _ e"
    guess("l")    -> "a p p l e"
    status()      -> "성공"

힌트
    - secret 과 lives 는 문자열과 정수(불변 객체)라서 함수 안에서 바꾸려면
      global secret, lives 가 필요합니다. 반면 guessed 와 history 는 집합과
      리스트(가변 객체)라 guessed.add(), guessed.clear(), history.append(),
      history.clear() 는 global 없이도 됩니다. 다만 guessed = set() 처럼 새로
      대입하는 순간 global 이 필요해집니다. 이 차이를 이 문제로 확실히 익히세요.
      (교재 2.1 / 2.2 / 3.4)
    - 상태 문자열 만들기: secret 의 글자를 하나씩 보며 guessed 에 있으면 그 글자를,
      없으면 "_" 를 리스트에 모은 뒤 " ".join() 으로 합칩니다. guess 와 hint 가 둘 다
      쓰므로 따로 함수로 빼세요.
    - "모든 글자를 맞혔는지"는 set(secret).issubset(guessed) 한 줄로 확인됩니다.
    - guess 와 hint 맨 앞에서 status() 를 불러 "진행 중" 이 아니면 바로 상태
      문자열을 돌려주세요. 그러면 끝난 게임은 저절로 건드리지 않게 됩니다.
    - hint 에서 공개할 글자: for ch in secret: 로 돌다가 guessed 에 없는 첫 글자에서
      break 하세요.
    - wrong_letters: guessed 에서 set(secret) 을 뺀 차집합을 sorted() 하세요.
"""

secret = ""
guessed = set()
lives = 0
history = []


def start(word: str, lives_count: int = 6) -> None:
    raise NotImplementedError


def guess(letter: str) -> str:
    raise NotImplementedError


def hint() -> str:
    raise NotImplementedError


def status() -> str:
    raise NotImplementedError


def wrong_letters() -> list:
    raise NotImplementedError
