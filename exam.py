import requests
from bs4 import BeautifulSoup


class SiteManager:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
            return f"Сайт '{url}' добавлен."
        return f"Сайт '{url}' уже есть в списке."

    def list_sites(self):
        return self.sites if self.sites else ["Список сайтов пуст."]


class SiteParser:
    @staticmethod
    def search_keyword(sites, keyword):
        results = []
        for site in sites:
            try:
                response = requests.get(site, timeout=5)
                count = BeautifulSoup(response.text, 'html.parser').get_text().lower().count(keyword.lower())
                results.append((site, count))
            except:
                results.append((site, -1))
        return results


class UserInterface:
    @staticmethod
    def display_menu():
        print("\nМеню:\n1. Добавить сайт\n2. Показать сайты\n3. Искать информацию\n4. Выйти")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)


class SearchApp:
    def __init__(self):
        self.site_manager = SiteManager()
        self.ui = UserInterface()

    def run(self):
        while True:
            self.ui.display_menu()
            choice = self.ui.get_input("Выберите пункт: ")

            if choice == "1":
                url = self.ui.get_input("Введите cсылку сайта: ")
                self.ui.display_message(self.site_manager.add_site(url))

            elif choice == "2":
                self.ui.display_message("\n".join(self.site_manager.list_sites()))

            elif choice == "3":
                if not self.site_manager.sites:
                    self.ui.display_message("Нет сайтов для поиска.")
                    continue
                keyword = self.ui.get_input("Введите ключевое слово: ")
                results = SiteParser.search_keyword(self.site_manager.sites, keyword)
                for site, count in results:
                    message = f"{site}: {'Совпадений' if count >= 0 else 'Ошибка'} {count if count >= 0 else ''}"
                    self.ui.display_message(message)

            elif choice == "4":
                self.ui.display_message("Выход .")
                break

            else:
                self.ui.display_message("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    SearchApp().run()









