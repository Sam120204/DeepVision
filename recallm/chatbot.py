from recall import RecallM

def chatbot():
    # 初始化 RecallM 实例
    recallm = RecallM()
    recallm.reset_knowledge()
    print("欢迎来到 RecallM Chatbot！")
    print("您可以输入问题与RecallM对话，或输入 'exit' 退出")

    # 进入聊天循环
    while True:
        user_input = input("你: ").strip()

        if user_input.lower() == "exit":
            print("再见！")
            break

        # 用户提问
        if user_input:
            # RecallM 处理问题并返回答案
            response = recallm.question(user_input)
            print(f"RecallM: {response}")
            
            # 将用户的提问和系统的回答更新为知识
            knowledge_to_update = f"User asked: {user_input} - RecallM answered: {response}"
            recallm.update(knowledge=knowledge_to_update)
            print("RecallM: 知识已更新！")

    # 关闭数据库连接
    recallm.close()

if __name__ == "__main__":
    chatbot()
