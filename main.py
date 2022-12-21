from model import Words, Prompts
from generate_prompt import generate_prompt, counter_prompt_coincidences, is_prompt_fits, generate_prompts_list
from app import add_prompt
from telegramm import telegram_send_text
from exceptions import exception_handler
import time


@exception_handler('')
def main():
    all_fields = Words.select()
    prompts = []
    for field in all_fields:
        prompt_lst = generate_prompts_list(field.word)
        for prompt in prompt_lst:
            if prompt in prompts:
                continue
            prompts.append(prompt)
            number_of_matches, id_word_in_db = counter_prompt_coincidences(all_fields, prompt)
            add_prompt(prompt, number_of_matches, id_word_in_db)


if __name__ == '__main__':
    main()
