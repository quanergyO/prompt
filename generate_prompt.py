import random
from hot_fix import help_generate_prompt


def generate_prompts_list(word: str) -> list:
    '''
    :param word:
    :return: list of prompts
    '''
    prompt_list = []
    for i in range(0, len(word) - 1):
        prompt_list.append(word[i] + word[i + 1])
    for i in range(0, len(word) - 2):
        prompt_list.append(word[i] + word[i + 1] + word[i + 2])
    for i in range(0, len(word) - 3):
        prompt_list.append(word[i] + word[i + 1] + word[i + 2] + word[i + 3])
    return prompt_list


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

