from random import randrange, choice
import names


def randcli():
    """Generate random client info

    Returns:
        dict: client's first name, last name, mobile and email address
    """
    fname = names.get_first_name()
    lname = names.get_last_name()
    phone = '04'+str(randrange(100000000))
    # Random email domain (gmail, hotmail, yahool or client's last name)
    email = fname.lower()+lname.lower() + \
        choice(['@gmail.com', '@hotmail.com',
               '@yahoo.com', '@'+lname.lower()+'.com'])

    return {'FirstName': fname,
            'LastName': lname,
            'Mobile': phone,
            'Email': email}
