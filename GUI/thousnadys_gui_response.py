from GUI.thousandeye_gui import MainApp
from api_for_thousandeyes.thousandeyes_agentid import get_agentid
from api_for_thousandeyes.thousandeyes_testid import get_testid
from tkinter import Tk, messagebox
from datetime import datetime, timezone
from logoncredintal.logon import thousandeyes_logon

class function_gui(MainApp):
    def get_list_of_cities(self):
        list_of_cities = get_agentid().reformat_agent_id
        cities = tuple(key['agentName'] for key in list_of_cities)
        return cities

    def get_list_of_test(self):
        list_of_test = get_testid().get_the_data
        test = tuple(key['type'] for key in list_of_test)
        return test

    def TimeStamp(self, year, month, day, hour, minute, zone):
        d1 = datetime.strptime(f"{year} {month} {day} {hour}:{minute} {zone}" , "%y %m %d %I:%M %p")
        return int(d1.replace(tzinfo=timezone.utc).timestamp())

    def retreive_credintails(self):
        return {'username':'Generic', 'testId': 'agent-to-server', 'agentId': 'Singapore', 'start':100, 'end': 200}
        # try:
        #     dt_start = self.TimeStamp(self.entry_start_date_year.get(), self.entry_start_date_month.get(), self.entry_start_date_day.get(),
        #                           self.entry_start_date_hour.get(), self.entry_start_date_minutes.get(), self.entry_start_am_pm.get())
        # except ValueError:
        #     messagebox.showerror("Time Problem", f"The start time was entered incorrectly \n Its M D Y H:M")
        #     return
        # try:
        #     dt_end = self.TimeStamp(self.entry_end_date_year.get(), self.entry_end_date_month.get(), self.entry_end_date_day.get(),
        #                             self.entry_end_date_hour.get(), self.entry_end_date_minutes.get(), self.entry_end_am_pm.get())
        # except ValueError:
        #     messagebox.showerror("Time Problem", f"The end time was entered incorrectly \n Its M D Y H:M")
        #     return
        # return_json = {'username':self.user.get(), 'testId': self.testId.get(), 'agentId': self.agendId.get(), 'start':dt_start, 'end': dt_end}
        # for val in return_json:
        #     if val == '':
        #         messagebox.showerror(f"The {val.keys()} value was not correct")
        # return return_json

    def retrieve_username_and_password(self):
        creditals = self.retreive_credintails()
        data = thousandeyes_logon().credintail
        up = data[creditals['username']]
        creditals['username'] = up['username']
        creditals['authtoken'] = up['authtoken']
        return creditals
    def retrieve_agentid(self):
        creditals = self.retrieve_username_and_password()
        list_of_cities = get_agentid().get_the_data
        for value in list_of_cities:
            if value['agentName'] == creditals['agentId']:
                creditals['agentId'] = value['agentId']
                break
        return creditals
    def retrieve_testid(self):
        credintals = self.retrieve_agentid()
        list_of_test = get_testid().get_the_data
        for value in list_of_test:
            if value['type'] == credintals['testId']:
                credintals['testId'] = value['testId']
                break
        print(credintals)
        return credintals


root = Tk()
function_gui(root)
root.mainloop()