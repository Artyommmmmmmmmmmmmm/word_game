import random

class WordGenerator:
    def __init__(self):
        # Слова по уровням сложности
        self.word_pools = {
            1: ['cat', 'dog', 'sun', 'car', 'book', 'house', 'tree', 'fish', 'bird', 'hand'],
            2: ['python', 'mouse', 'phone', 'table', 'chair', 'green', 'black', 'water', 'fire', 'earth'],
            3: ['keyboard', 'monitor', 'program', 'guitar', 'puzzle', 'dragon', 'knight', 'magic', 'sword', 'shield'],
            4: ['algorithm', 'skeleton', 'dungeon', 'treasure', 'victory', 'journey', 'battle', 'monster', 'legend', 'hero'],
            5: ['programming', 'adventure', 'challenge', 'experience', 'knowledge', 'strength', 'courage', 'destiny', 'eternal', 'mystical']
        }

    def get_random_word(self, level):
        """Получение случайного слова для уровня"""
        # ИСПРАВЛЕНО: Защита от выхода за пределы
        level = min(max(level, 1), 5)  # Ограничиваем уровень от 1 до 5
        pool = self.word_pools[level]
        return random.choice(pool)

    def get_word_difficulty(self, word):
        """Определение сложности слова"""
        return len(word)
    
    def get_words_by_level(self, level):
        """Получение всех слов определенного уровня"""
        level = min(max(level, 1), 5)
        return self.word_pools[level].copy()
    
    def add_word(self, level, word):
        """Добавление нового слова в пул"""
        if level in self.word_pools and word not in self.word_pools[level]:
            self.word_pools[level].append(word)
            return True
        return False
    
    def get_level_count(self, level):
        """Получение количества слов на уровне"""
        level = min(max(level, 1), 5)
        return len(self.word_pools[level])