# 模块：数字工具(number_tools)
# 负责人：hwz（Github：hwz666）
# 说明：作为小组成员，在个人分支 hwz666 上开发的功能模块，演示 Git 分支协同开发流程（master / develop / 个人分支）。

def is_prime(n: int) -> bool:
    """判断一个整数是否为素数。小于2不是素数。"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_list(limit: int) -> list[int]:
    """获取 2 ~ limit 之间所有素数，返回素数列表。"""
    result = []
    for num in range(2, limit + 1):
        if is_prime(num):
            result.append(num)
    return result

if __name__ == "__main__":
    print(f"17 是否素数：{is_prime(17)}")
    print(f"20以内素数：{get_prime_list(20)}")
