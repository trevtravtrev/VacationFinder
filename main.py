from vacationfinder import VacationFinder

if __name__ == '__main__':
    vacation = VacationFinder()
    vacation.open_browser()
    vacation.login()
    num_pages = vacation.get_number_of_pages()
