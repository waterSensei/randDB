from datetime import timedelta
from random import choices

# Define all the sales and installers can choose
Sales = ['Jeffrey', 'William', 'Joe', 'Lawrence', 'Timothy', 'Alma']
Installers = ['Andrew', 'Angel', 'Lucia', 'Marvin']


def randorder(ins_date):
    """Generate random order info

    Args:
        ins_date (date): start date

    Returns:
        dict: Sales, Installer and Installation Date
    """
    sales = choices(Sales, [40, 20, 15, 5, 10, 10])[0]
    installers = choices(Installers, [50, 20, 10, 20])[0]
    randdays = timedelta(days=choices([0, 1, 2], [50, 40, 10])[0])
    # convert date into string ('dd/mm/yyyy')
    ins_date = (ins_date+randdays).strftime("%d/%m/%Y")

    return {'Sales': sales,
            'Installer': installers,
            'InstallationDate': ins_date}
