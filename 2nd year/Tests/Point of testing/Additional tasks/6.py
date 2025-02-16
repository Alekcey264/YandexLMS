from yandex_testing_lesson import strip_punctuation_ru


def strip_punctuation_ru_test():
    test_cases = [
        ("Привет, как дела?", "Привет как дела"),
        ("Это тест. Слова разделены, ! знаками препинания...", "Это тест Слова разделены знаками препинания"),
        ("Слова-содержащие дефисы", "Слова-содержащие дефисы"),
        ("", ""),
        ("!!!", ""),
        ("Здравствуйте! Как ваши дела? Всё хорошо.", "Здравствуйте Как ваши дела Всё хорошо"),
        ("Это пример: слова, содержащие-разные знаки.", "Это пример слова содержащие-разные знаки"),
        ("Слово - это слово.", "Слово это слово"),
    ]
    
    for input_val, correct_output_val in test_cases:
        if strip_punctuation_ru(input_val) != correct_output_val:
            print('NO')
            return
    print('YES')
    return


strip_punctuation_ru_test()