from vacationfinder import VacationFinder
from textfile import TextFile
from sms import SMS

if __name__ == '__main__':
    # grab current number of vacation pages
    vacation = VacationFinder()
    vacation.open_browser()
    vacation.login()
    num_vacations = vacation.get_number_of_pages()
    vacation.driver.quit()
    print(f'{num_vacations} current pages of vacations.')

    # grab previous number of vacation pages
    file = TextFile(vacation.config.get("file_name"))
    previous_num_vacations = file.read_file()
    if previous_num_vacations:
        print(f'{previous_num_vacations} previous pages of vacations')
        if num_vacations > previous_num_vacations:
            print("New vacations have been added.")
            sms = SMS(vacation.config.get('number'), vacation.config.get('carrier'), vacation.config.get('email'), vacation.config.get('password'))
            sms.send('New vacations have been added!')
            print("Text has been sent to phone.")
        else:
            print("No new vacations have been added.")
    else:
        print(f'{vacation.config.get("file_name")} does not exist yet.')

    # write new num_vacations to text file
    file.write_file(str(num_vacations))
    print(f'Wrote current number of vacations ({num_vacations} pages) to {vacation.config.get("file_name")}.')
