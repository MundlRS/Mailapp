class Mail:
    def __init__(self,uid,date, from_, to,cc,bcc,subject,text,flag):
        self.uid = uid
        self.date = date
        self.from_ = from_
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.subject = subject
        self.text = text
        self.flag = flag

    def returnStringforTextBrowserInbox(self):
        if len(self.cc) == 0 and len(self.bcc) == 0:
            return f"Zeit: {self.date}\nVon: {self.from_}\nAn: {', '.join(self.to)}\n\nBetreff: {self.subject}\n\n\n{self.text}"
        elif len(self.cc) >= 1 and len(self.bcc) == 0:
            return f"Zeit: {self.date}\nVon: {self.from_}\nAn: {', '.join(self.to)}\ncc: {', '.join(self.cc)}\n\nBetreff: {self.subject}\n\n\n{self.text}"
        elif len(self.cc) == 0 and len(self.bcc) >= 1:
            return f"Zeit: {self.date}\nVon: {self.from_}\nAn: {', '.join(self.to)}\nbcc: {', '.join(self.bcc)}\n\nBetreff: {self.subject}\n\n\n{self.text}"
        else:
            return f"Zeit: {self.date}\nVon: {self.from_}\nAn: {', '.join(self.to)}\ncc: {', '.join(self.cc)}\nbcc: {', '.join(self.bcc)}\n\nBetreff: {self.subject}\n\n\n{self.text}"

    def returnStringForListWidget(self):
        return f"Datum/Zeit: {self.date}\nVon: {self.from_}\nAn: {', '.join(self.to)}\nBetreff: {self.subject}\n"

    def originallyMessage(self):
        return f"\n\n----Ursprüngliche Nachricht----\n_____________________________________\nZeit: {self.date}\nVon:{self.from_}\nAn: {', '.join(self.to)}\ncc: {', '.join(self.cc)}\nBetreff: {self.subject}\n\n{self.text}"