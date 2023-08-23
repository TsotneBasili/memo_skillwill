import json

from diarybook import Diary, DiaryBook
from utils import read_from_json_into_app, write_into_json_from_app
import sys
from authorization import Authorization


class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()
        self.choices = {
            "1": self.show_all_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.sort,
            "5": self.quit
        }

    authorize = Authorization()

    def sort(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            memo_list = []
            for diary in self.diarybook.diaries:
                if self.authorize.current_user == diary.user:
                    memo_list.append(diary.memo)
            if len(memo_list) == 0:
                print("No lists to sort")
            else:
                for memo in sorted(memo_list):
                    print(memo)

    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries")
        else:
            for diary in self.diarybook.diaries:
                if self.authorize.current_user == diary.user:
                    print(f"{diary.id}-{diary.memo} - {diary.tags}")

    def add_diary(self):
        user = self.authorize.current_user
        memo = input("Enter a memo: ")
        tags = input("add tags: ")
        self.diarybook.new_diary(user, memo, tags)
        write_into_json_from_app(user, memo, tags, 'data.json')
        print("Your note has been added")

    def search_diaries(self):
        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        if len(diaries) == 0:
            print("no match found")
        else:
            for diary in diaries:
                print(f"{diary.id}-{diary.memo}")

    def populate_database(self):
        diaries1 = read_from_json_into_app('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)

    def quit(self):
        print("Thank you for using diarybook today")
        sys.exit(0)

    def display_menu(self):
        print("""
        Diary Book Menu:
        
        1. Show diaries
        2. Add diary
        3. Filter using keyword
        4. sort
        5. Quit program
        """)

    def run(self):
        self.authorize.run()
        self.populate_database()
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice) #action = self.choices[choice]
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


if __name__ == "__main__":
    Menu().run()






