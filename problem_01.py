"""
문제 1. 단어 줄 바꿈과 정렬

긴 문장을 폭에 맞춰 줄로 나누는 wrap, 나눈 줄을 왼쪽/오른쪽/가운데로 맞추는 align,
양쪽 끝을 맞추는 justify 를 작성하세요.

wrap(text, width=20)
- 단어는 공백으로 구분합니다. 공백이 여러 개 있거나 앞뒤에 붙어 있어도, 결과에서
  단어 사이는 공백 하나로 다시 잇습니다.
- 한 줄에는 단어를 최대한 많이 넣되, 줄의 길이(공백 포함)가 width 를 넘으면
  안 됩니다. 단어 하나가 width 보다 길면 그 단어만으로 한 줄을 씁니다.
- 줄들을 문자열 리스트로 돌려줍니다. 단어가 하나도 없으면 빈 리스트입니다.

align(lines, width, how="left")
- 각 줄을 공백으로 채워 길이를 정확히 width 로 맞춘 새 리스트를 돌려줍니다.
  how 가 "left" 면 뒤에, "right" 면 앞에 공백을 붙입니다. "center" 는 양쪽에
  나눠 붙이되, 홀수 개면 오른쪽에 하나 더 붙입니다.
- width 보다 긴 줄은 그대로 둡니다. lines 는 바꾸지 않습니다.

justify(lines, width)
- 각 줄의 단어 사이 공백을 늘려 줄 길이를 정확히 width 로 맞춘 새 리스트를
  돌려줍니다. 늘릴 공백이 단어 사이에 똑같이 나뉘지 않으면 왼쪽 사이부터 하나씩
  더 줍니다.
- 단어가 하나뿐인 줄과 마지막 줄은 늘리지 않고 뒤에 공백을 붙여 width 로 맞춥니다.
- width 보다 긴 줄은 그대로 둡니다. lines 는 바꾸지 않습니다.

예시
    lines = wrap("the quick brown fox jumps over the lazy dog", 10)
    lines    -> ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
    align(lines, 10, "right")
        -> [" the quick", " brown fox", "jumps over", "  the lazy", "       dog"]
    align(["ab"], 7, "center")    -> ["  ab   "]
    justify(["a b c", "dd e", "f"], 7)    -> ["a  b  c", "dd    e", "f      "]
    justify(["this is an", "example of text", "justification."], 16)
        -> ["this    is    an", "example  of text", "justification.  "]
    wrap("   ")    -> []

힌트
    - wrap: str.split() 은 인자 없이 부르면 공백이 몇 개든 알아서 단어만 떼어 줍니다.
      "지금 만들고 있는 줄"의 단어들을 리스트에 모아 두고, 단어를 하나 더 넣었을 때
      " ".join(현재줄 + [단어]) 의 len 이 width 를 넘으면 지금까지 모은 줄을 결과에
      넣고 새 줄을 시작하세요. 지금 줄이 비어 있으면 단어가 아무리 길어도 일단
      넣습니다. 반복문이 끝난 뒤 마지막 줄을 결과에 넣는 것을 잊지 마세요. 이
      문제에서 가장 흔한 실수입니다.
    - align: 채울 공백 수는 width - len(line) 입니다. 음수면 " " * 음수 는 빈
      문자열이므로 저절로 "그대로" 가 됩니다. center 는 왼쪽에 공백수 // 2,
      오른쪽에 나머지를 붙이세요.
    - justify: 단어를 str.split() 으로 나누고, 사이 개수 = 단어 수 - 1, 넣을 공백
      총수 = width - 글자 수 합 입니다. 사이마다 총수 // 사이개수 개를 넣고, 앞에서부터
      총수 % 사이개수 개의 사이에는 하나씩 더 넣으세요. 조각을 리스트에 모아
      "".join() 으로 합칩니다.
    - "마지막 줄" 은 lines[-1] 입니다. for i in range(len(lines)): 로 돌면서 i 가
      len(lines) - 1 인지로 확인하세요.
"""


def wrap(text: str, width: int = 20) -> list:
    raise NotImplementedError


def align(lines: list, width: int, how: str = "left") -> list:
    raise NotImplementedError


def justify(lines: list, width: int) -> list:
    raise NotImplementedError
