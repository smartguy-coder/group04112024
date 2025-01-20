from utils.email_sender import send_email, create_welcome_letter


def main():
    data = {
        'age': 60,
        'name': 'Draccula',
        'address': 'Transilvania',
        'hobbies': ['tennis', 'hobbyhorsing'],
        'on_vacation': False
    }
    body = create_welcome_letter(data)
    print(body)

    recipients = ['test_hillel_api_mailing@ukr.net', 'test_hillel_api_mailing@ukr.net']
    send_email(
        recipients,
        mail_subject='About me',
        mail_body=body,
    )


if __name__ == '__main__':
    main()
