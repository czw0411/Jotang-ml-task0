import sys
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

scores = {
    "张三": 88,
    "李四": 92,
    "王五": 79,
    "赵六": 95,
    "钱七": 67,
}

scores_list = [(name, score) for name, score in scores.items()]


def average_score(data):
    if isinstance(data, dict):
        values = list(data.values())
    else:
        values = [score for _, score in data]

    if not values:
        raise ValueError("成绩为空，无法计算平均分")
    return sum(values) / len(values)


def top_student(data):
    items = list(data.items()) if isinstance(data, dict) else list(data)

    if not items:
        raise ValueError("成绩为空，无法找出最高分")
    return max(items, key=lambda pair: pair[1])


names = list(scores.keys())
subjects = ["数学", "英语", "编程"]

A = np.array(
    [
        [88, 76, 90],
        [92, 85, 88],
        [79, 90, 72],
        [95, 70, 96],
        [67, 80, 75],
    ],
    dtype=float,
)

B = np.array(
    [
        [0.5],
        [0.3],
        [0.2],
    ],
    dtype=float,
)

C = A @ B


def main():
    print("=" * 52)
    print("1. 成绩记录（字典）")
    print("=" * 52)
    for name, score in scores.items():
        print(f"    {name}: {score}")

    print()
    print("=" * 52)
    print("2. 平均分与最高分")
    print("=" * 52)
    print(f"    人数   : {len(scores)}")
    print(f"    平均分 : {average_score(scores):.2f}")
    best_name, best_score = top_student(scores)
    print(f"    最高分 : {best_score}  （{best_name}）")

    print()
    print("=" * 52)
    print("3. NumPy 矩阵乘法")
    print("=" * 52)
    print("    矩阵 A:")
    for i, row in enumerate(A):
        print(f"        {names[i]}  {row}")
    print("    矩阵 B:")
    for j, weight in enumerate(B[:, 0]):
        print(f"        {subjects[j]}  {weight}")

    print()
    print("=" * 52)
    print("4. 计算结果与形状")
    print("=" * 52)
    print(f"    A.shape = {A.shape}")
    print(f"    B.shape = {B.shape}")
    print(f"    C.shape = {C.shape}")
    print("    C（每个学生的加权总评）:")
    for name, value in zip(names, C[:, 0]):
        print(f"        {name}  {value:6.2f}")


if __name__ == "__main__":
    main()
