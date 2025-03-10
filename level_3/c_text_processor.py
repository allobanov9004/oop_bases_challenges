"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        return f'text length: {len(self.text)}, total number of words in the text: {len(self.text.split())}'



if __name__ == '__main__':
    a = '''Не следует, однако забывать, что рамки и место обучения кадров позволяет выполнять важные 
                            задания по разработке форм развития. Идейные соображения высшего порядка, а также консультация
                             с широким активом требуют от нас анализа новых предложений. Таким образом консультация с широким 
                            активом требуют определения и уточнения систем массового участия. С другой стороны сложившаяся структура 
                            организации влечет за собой процесс внедрения и модернизации модели развития.'''
    text_ex = TextProcessor(a)
    print(text_ex.to_upper())
    print(text_ex.summarize())

    adv_text_ex = AdvancedTextProcessor(a)
    print(adv_text_ex.to_upper())
    print(adv_text_ex.summarize())
