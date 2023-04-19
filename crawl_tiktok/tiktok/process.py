from __init__ import *
from model import *

def add_account(url_tiktok, count_live):
    try:
        session = Session()
        account_new = account(url_tiktok=url_tiktok, count_live = count_live)
        session.add(account_new)
        session.commit()
        return True
    except Exception as ex:
        pass
    return False


def get_all_account(phone_number= False, check = True):
    try:
        session = Session()
        accounts = session.query(account).filter(account.check == check).all()
        if phone_number:
            accounts = session.query(account).filter(account.phone_number != None).all()
        return accounts
    except Exception as ex:
        return []

def update_account(url_tiktok, text_user_subtitle, text_user_bio, text_other_links, count_follower, text_phone_numbers, text_fb, check):
    try:
        session = Session()
        account_up = session.query(account).filter_by(url_tiktok=url_tiktok).first()
        account_up.user_subtitle = text_user_subtitle
        account_up.user_bio = text_user_bio
        account_up.spanlink = text_other_links
        account_up.count_flower = count_follower
        account_up.phone_number = text_phone_numbers
        account_up.url_facebook = text_fb
        account_up.check = check
        session.commit()
        return True
    except Exception as ex:
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f'UPDATE_ACCOUNT {url_tiktok, text_user_subtitle, text_user_bio, check} {ex} \n')
    return False

def update_phone_number_account(url_tiktok, phone_number):
    try:
        session = Session()
        account_up = session.query(account).filter_by(url_tiktok=url_tiktok).first()
        if phone_number is None:
            account_up.phone_number = phone_number
        if phone_number in  account_up.phone_number:
            pass
        session.commit()
        return True
    except Exception as ex:
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f'UPDATE_ACCOUNT {url_tiktok, phone_number} {ex} \n')
    return False

def update_link_phone_account(url_tiktok, phone_number, url_facebook):
    try:
        session = Session()
        account_up = session.query(account).filter_by(url_tiktok=url_tiktok).first()
        account_up.phone_number = phone_number
        account_up.url_facebook = url_facebook
        session.commit()
        return True
    except Exception as ex:
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f'UPDATE_ACCOUNT {url_tiktok, phone_number, url_facebook} {ex} \n')
    return False
   