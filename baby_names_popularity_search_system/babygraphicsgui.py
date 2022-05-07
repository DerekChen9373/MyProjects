import tkinter

def make_gui(top, width, height, names, draw_names, search_names):

    label = tkinter.Label(top, text="Names:")
    label.grid(row=0, column=0, sticky='w')
    entry = tkinter.Entry(top, width=40, name='entry', borderwidth=2)
    entry.grid(row=0, column=1, sticky='w')
    entry.focus()
    error_out = tkinter.Text(top, height=2, width=70, name='errorout', borderwidth=2)
    error_out.grid(row=0, column=2, sticky='w')
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')
    canvas.grid(row=1, columnspan=12, sticky='w')
    space = tkinter.LabelFrame(top, width=10, height=10, borderwidth=0)
    space.grid(row=2, columnspan=12, sticky='w')
    label = tkinter.Label(top, text="Search:")
    label.grid(row=3, column=0, sticky='w')
    search_entry = tkinter.Entry(top, width=40, name='searchentry')
    search_entry.grid(row=3, column=1, sticky='w')
    search_out = tkinter.Text(top, height=2, width=70, name='searchout', borderwidth=2)
    search_out.grid(row=3, column=2, sticky='w')
    entry.bind("<Return>", lambda event: handle_draw(entry, canvas, names, error_out, draw_names))
    search_entry.bind("<Return>", lambda event: handle_search(search_entry, search_out, names, search_names))
    top.update()
    return canvas

def handle_draw(entry, canvas, names, error_out, draw):

    text = entry.get()
    lookups = [name[0].upper() + name[1:].lower() for name in text.split()]  # handles casing
    invalid_names = [name for name in lookups if name not in names]
    lookups = [name for name in lookups if name in names]
    error_out.delete('1.0', tkinter.END)
    if invalid_names:
        if len(invalid_names) == 1:
            out = invalid_names[0] + ' is not contained in the name database.'
        else:
            out = ', '.join(invalid_names) + ' are not contained in the name database.'
        error_out.insert('1.0', out)
    draw(canvas, names, lookups)

def handle_search(search_entry, search_out, names, search):

    target = search_entry.get().strip()
    if target:
        result = search(names, target)
        out = ' '.join(result)
        search_out.delete('1.0', tkinter.END)
        search_out.insert('1.0', out)
