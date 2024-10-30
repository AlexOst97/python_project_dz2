from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(bank_account: str) -> str:
    """ Функция, которая обрабатывает информацию о картах и счетах."""
    if 'Счет' in bank_account:
        bank_account_account = get_mask_account(bank_account[-20:])
        return (f'Счет {bank_account_account}')

print(mask_account_card('Счет 73654108430135874305'))