import requests
from bs4 import BeautifulSoup

def scrape_problem(contest_id, problem_id):
    url = f"https://atcoder.jp/contests/abc{contest_id}/tasks/abc{contest_id}_{problem_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 問題文と制約の部分を抽出
    problem_statement = ''.join(soup.find('div', {'id': 'task-statement'}).stripped_strings)
    constraints = soup.find('h3', string='制約').find_next('pre').text.strip()

    return problem_statement, constraints

contest_id = input("Enter the contest ID: ")
problem_id = input("Enter the problem ID: ")
problem_statement, constraints = scrape_problem(contest_id, problem_id)

# 英文の部分のみ抽出
start_index = problem_statement.find("Problem Statement")
english_statement = problem_statement[start_index:]

# 改行を挿入
english_statement = english_statement.replace("Sample Input", "\nSample Input")
english_statement = english_statement.replace("Sample Output", "\nSample Output")

# 問題文を分割して表示
statement_parts = english_statement.split("\nSample Input")
for i, part in enumerate(statement_parts):
    if i == 0:
        print(part.strip())
    else:
        print(f"\nSample Input {i}")
        inputs_outputs = part.split("\nSample Output")
        print(inputs_outputs[0].strip())
        print(f"\nSample Output {i}")
        print(inputs_outputs[1].strip())

print("\nConstraints:")
print(constraints)
print("\nThink step by step and write Python code to solve it.")
print("UnionFind should not be used when edges are added or removed.")
print("Please considering the idea of a binary search, memoization and dp and the others.")
print("If the solution is too complicated, please rethink of a simple solution.")
print("説明は日本語で書いて下さい。")

# 追加メッセージ用
'''
TLEします。ほとんど合っているので、パフォーマンスのボトルネックとなっている行を探して下さい。
メモ化やポインタ等を考えてみて下さい。
'''
'''
入力例  が間違っています
'''

