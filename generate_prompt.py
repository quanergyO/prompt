import random
from hot_fix import help_generate_prompt


def generate_prompt(words: list) -> str:
    '''
    :param words: all words from db in list
    :return: prompt
    '''
    count_words = len(words)
    index_word = random.randint(0, count_words - 1)
    word = words[index_word]
    prompt_lenght = random.randint(2, 4)
    prompt_lenght = help_generate_prompt(prompt_lenght, len(word))
    index_start = random.randint(0, len(word) - prompt_lenght)
    prompt = word[index_start:index_start+prompt_lenght]
    return prompt


def counter_prompt_coincidences(all_fields: object, prompt: str) -> int and list:
    '''
    :param all_fields: all fields where all_fields.word = word
    :param prompt: prompt
    :return: count_of_matches, id_word_in_db
    '''
    count = 0
    word_ids: list = []
    for field in all_fields:
        if prompt in field.word:
            count += 1
            word_ids.append(field.id)
    print(f'prompt: {prompt}, count: {count}')  # TODO add logguru
    # print(word_ids)                             # TODO add logguru
    return count, word_ids


def is_prompt_fits(number_of_matches: int, total_number_of_words: int, MIN_PERCENT_OCCURRENCES = 15) -> bool:
    '''
    :param number_of_matches:
    :param total_number_of_words:
    :param MIN_PERCENT_OCCURRENCES: default = 15
    :return: True/False
    '''
    percent: float = (float(number_of_matches) / float(total_number_of_words)) * 100
    if round(percent, 1) >= MIN_PERCENT_OCCURRENCES:
        return True
    return False

