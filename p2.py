# 프로젝트 문제 2번

def problem2(input):
    # 스택을 사용하여 열린 괄호를 추적
    stack = []
    # 추가해야 할 열린 괄호 수
    need_open = 0

    # 입력 힌트
    for char in input:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                need_open += 1

    #최종 결과는 추가해야할 열린 괄호와 닫힌 괄호의 합이다.                    
    result = need_open + len(stack)
    return result

#첫 번째 입력 예시
input = ")))()"
result = problem2(input)

assert result == 3
print("정답입니다.", result)

#두 번째 입력 예시
input = ")(()"
result = problem2(input)

assert result == 2
print("정답입니다.", result)

