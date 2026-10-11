# -*- coding: utf-8 -*-
"""
模块：问候功能（greeting）
负责人：王铭伟 (GitHub: wumeiwei)
说明：作为小组成员，在个人分支 wumeiwei 上开发的功能模块，
      演示 Git 分支协同开发流程（master / develop / 个人分支）。
"""


def greet(name: str) -> str:
    """返回一句中文问候语。"""
    if not name:
        return "你好，陌生人！"
    return f"你好，{name}！欢迎加入 Git 团队协作。"


def add(a: int, b: int) -> int:
    """一个最简单的求和函数，用于演示提交与合并。"""
    return a + b


if __name__ == "__main__":
    print(greet("王铭伟"))
    print("1 + 2 =", add(1, 2))
