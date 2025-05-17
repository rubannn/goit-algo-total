class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додає відповідь до коментаря"""
        if not self.is_deleted:
            self.replies.append(reply)
        else:
            print("Неможливо додати відповідь до видаленого коментаря")

    def remove_reply(self):
        """Видаляє коментар, замінюючи текст та позначуючи його як видалений"""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """Рекурсивно виводить коментар та його відповіді з відступами"""
        if self.is_deleted:
            print("    " * level + "[Видалений коментар]")
        else:
            print("    " * level + f"{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(level + 1)


# Створюємо кореневий коментар
root_comment = Comment("User1", "Це головний коментар")

# Додаємо відповіді до кореневого коментаря
reply1 = Comment("User2", "Відповідь на головний коментар")
root_comment.add_reply(reply1)

reply2 = Comment("User3", "Ще одна відповідь на головний коментар")
root_comment.add_reply(reply2)

# Додаємо відповіді до першої відповіді
reply1_1 = Comment("User1", "Відповідь на першу відповідь")
reply1.add_reply(reply1_1)

reply1_2 = Comment("User4", "Ще одна відповідь на першу відповідь")
reply1.add_reply(reply1_2)

# Додаємо відповідь до відповіді на першу відповідь
reply1_1_1 = Comment("User2", "Глибока відповідь")
reply1_1.add_reply(reply1_1_1)

# Виводимо всю ієрархію
print("Повна ієрархія коментарів:")
root_comment.display()

# Видаляємо один з коментарів
print("\nПісля видалення одного коментаря:")
reply1_1.remove_reply()
root_comment.display()
