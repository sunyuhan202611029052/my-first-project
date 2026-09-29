# main.py
def main():
    # 问卷调研数据
    difficulty_list = ["单词记忆", "听力理解", "语法掌握", "口语表达", "阅读长篇文章"]
    count_list = [28, 22, 30, 18, 24]

    total = sum(count_list)
    print("=" * 40)
    print("学生英语学习困难统计报表")
    print("=" * 40)
    print(f"总调研人数：{total}")
    print("-" * 40)

    for name, num in zip(difficulty_list, count_list):
        percent = num / total * 100
        print(f"{name:<12} 人数：{num:>2}  占比：{percent:.2f}%")

    print("=" * 40)
    print("统计完成")

if __name__ == "__main__":
    main()