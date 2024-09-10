text = """Перші комп'ютери займали цілі кімнати, і їх обчислювальна потужність була значно меншою, ніж сучасних смартфонів. Проте ці машини стали основою для розвитку всіх сучасних технологій. З кожним роком технології ставали дедалі компактнішими та потужнішими, що призвело до революції у світі інформаційних технологій. Сьогодні ми живемо в епоху, де смартфони та ноутбуки є невід'ємною частиною нашого повсякденного життя."""

# 1. Переводимо текст у нижній регістр
lower_text = text.lower()

# 2. Знаходимо індекс першого входження слова 'технологій'
index_of_word = text.find("технологій")

# 3. Перетворюємо текст у формат Title Case (кожне слово з великої літери)
title_text = text.title()

# Виведення результатів
print("Текст у нижньому регістрі:\n", lower_text)
print("\n Індекс першого входження слова 'технологій':", index_of_word)
print("\n Текст у форматі Title Case:\n", title_text)
