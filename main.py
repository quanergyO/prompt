from model import Words, Prompts
from generate_prompt import generate_prompt, counter_prompt_coincidences, is_prompt_fits
from app import add_prompt
from telegramm import telegram_send_text
from exceptions import exception_handler


@exception_handler('')
def main():
    all_fields = Words.select()
    words: list = []
    for field in all_fields:
        words.append(field.word)
    for _ in range(400000):
        prompt = generate_prompt(words)
        number_of_matches, id_word_in_db = counter_prompt_coincidences(all_fields, prompt)
        if is_prompt_fits(number_of_matches, len(words)):
            all_prompts_fields = Prompts.select()
            prompts = []
            for field in all_prompts_fields:
                prompts.append(field.prompt)
            if prompt in prompts:
                continue
            add_prompt(prompt, number_of_matches, words)
            telegram_send_text(f'ADD PROMPT! prompt: {prompt}, numbers of matches: {number_of_matches}')


if __name__ == '__main__':
    main()
