from models.email import IMAPConnection
from controller.caller import Caller
from config.configuration import*
import imaplib 
from models.logc import Log
import time 

def main():
    Log.info('Listening...')
    while True:
        settings = appconfig['CALL']
        attempts = settings['attempts']
        time.sleep(int(app_settings['interval']))
        try:
            mail_handling = IMAPConnection()
            mail_handling.login()
            new_emails = mail_handling.fetcher()
        
        except Exception as err:
            Log.warning("ErrorType : {}, Error : {}".format(type(err).__name__, err))
            continue

        if new_emails:
            Log.info('new email')

            for key, value in settings.items():
                if 'phone' in key:
                    retry = 0
                    request = 0

                    while retry != attempts: 
                        caller = Caller()
                        response = caller.calling(phone=settings[key])

                        if response == 'accepted':
                            request = 1
                            break

                        elif response == 'not accepted':
                            break

                        elif response == 'not received':
                            Log.info('retrying...')
                            retry += 1

                        elif response == 'call failed':
                            Log.info('retrying...')
                            retry += 1

                    if request == 1:
                        break
    

if __name__ == '__main__':
    app_settings = appconfig['APP']
    main()

