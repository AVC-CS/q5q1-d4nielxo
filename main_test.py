import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # Input: 3 → rows: A / A B / A B C
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'^A$', r'^A B$', r'^A B C$'], lines)


@pytest.mark.T2
def test_main_2():
    # Input: 5 → rows: A / A B / A B C / A B C D / A B C D E
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'^A$', r'^A B C$', r'^A B C D E$'], lines)


@pytest.mark.T3
def test_main_3():
    # Input: 4 → rows: A / A B / A B C / A B C D
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'^A$', r'^A B C$', r'^A B C D$'], lines)


@pytest.mark.T4
def test_main_4():
    # Input: 6 → rows: A / A B / ... / A B C D E F
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'^A$', r'^A B C D$', r'^A B C D E F$'], lines)
