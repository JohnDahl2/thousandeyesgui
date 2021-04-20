
index = 0
size = 2

def _check(self, index, size):
    entry = entries[index]
    next_index = index + 1
    next_entry = self.entries[next_index] if next_index < len(self.entries) else None
    data = entry.get()
    print(len(data))
    if len(data) > size or not data.isdigit():
        self._backspace(entry)
    if len(data) >= size and next_entry:
        next_entry.focus()

def _backspace(self, entry):
    cont = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, cont[:-1])

def get(self):
    return [e.get() for e in self.entries]