from utils import load_question_ids
from scraper import split_data

if __name__ == "__main__":
    all_chunks = load_question_ids()
    for small_question_list in all_chunks:
        split_data(small_question_list)

