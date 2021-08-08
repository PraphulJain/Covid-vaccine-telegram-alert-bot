# Covid-vaccine-telegram-alert-bot
Python code for a telegram bot to send alerts to you when vaccine slots are available. Also has catching so will request data from the api every 5 minutes and will catch that data so that you won't get the same notifications again on that day. Although you will get a reminder with all the slots available every day at 6am and if there are 10 slots remaining.

### Prerequisites
You need to know how to create a telegram bot by using bot father and how to get it's id and get the chat id where you want to send those alerts.

### Installation
Just clone the repository and install the telegram api package of python by:

Pip:

    pip install python-telegram-bot

Conda:

    conda install -c conda-forge python-telegram-bot

### Setup
1. You need to create your bot on telegram with bot father.
2. Then update the variables in the starting of the code with your bot id, group or your chat id, and the [list of district codes](https://apisetu.gov.in/public/marketplace/api/cowin) you want to search. For getting district codes you need to look at the cowin api website (Instructions below) because I'm too lazy to make the list here.
3. You then need to run the code and if you want me to tell how to run this code then I don't think this is for you. :)

### Getting district codes:
1. Go to the [cowin api website](https://apisetu.gov.in/public/marketplace/api/cowin).
2. Look at the metadata section, go to states api to get the code of your state.
3. Then use the state code to get districts of that state by the district api just below the states api.
4. Now just copy the code.

## Okay bye and enjoy with the spam of vaccine notifications
# Get vaccinated fast!!
