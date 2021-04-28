from gui.frame import MainApp
from tkinter import messagebox
from datetime import datetime, timezone

class function(MainApp):
    def TimeStamp(self, year, month, day, hour, minute, zone):
        return int(datetime.strptime(f"{year} {month} {day} {hour}:{minute} {zone}" , "%y %m %d %I:%M %p").replace(tzinfo=timezone.utc).timestamp())
    def retreive_credintails(self):
        try:
            dt_start = self.TimeStamp(self.entry_start_date_year.get(), self.entry_start_date_month.get(), self.entry_start_date_day.get(),
                                  self.entry_start_date_hour.get(), self.entry_start_date_minutes.get(), self.entry_start_am_pm.get())
        except ValueError:
            messagebox.showerror("Time Problem", f"The start time was entered incorrectly \n Its M D Y H:M")
            return
        try:
            dt_end = self.TimeStamp(self.entry_end_date_year.get(), self.entry_end_date_month.get(), self.entry_end_date_day.get(),
                                    self.entry_end_date_hour.get(), self.entry_end_date_minutes.get(), self.entry_end_am_pm.get())
        except ValueError:
            messagebox.showerror("Time Problem", f"The end time was entered incorrectly \n Its M D Y H:M")
            return
        return_json = {'username': self.retrieve_username, 'authtoken': self.retrieve_authtoken,
                       'agentId': self.retrieve_agentid,'testId':self.retrieve_testid, 'start':dt_start, 'end': dt_end}
        map(lambda x: messagebox.showerror(f"The {x.keys()} value was not correct") if x == '' else None, return_json)
        return return_json
    @property
    def retrieve_username(self):
        return self.usernames[self.user.get()]['username']
    @property
    def retrieve_authtoken(self):
        return self.usernames[self.user.get()]['authtoken']
    @property
    def retrieve_agentid(self):
        return next(filter(lambda x : x if self.agentId.get() == x['agentName'] else '', self.agentId_list))['agentId']
    @property
    def retrieve_testid(self):
        return next(filter(lambda x: x if self.testId.get() == x['type'] else '', self.testId_list))['testId']