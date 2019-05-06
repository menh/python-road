import tkinter
import tkinter.messagebox

def main():
    flag = True

    #change label text
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue','Goodbye, world')
        label.config(text = msg, fg = color)

    # exit
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('tipe', 'exit?'):
            top.quit()

    #create top window
    top = tkinter.Tk()

    #set window size
    top.geometry('240x160')

    #set window title
    top.title('little game')

    #set label object add to top window
    label = tkinter.Label(top, text = 'Hello, world!', font = 'arial -32', fg = 'red')
    label.pack(expand = 1)

    # create button container
    panel = tkinter.Frame(top)

    # create button
    button1 = tkinter.Button(panel, text = 'change', command = change_label_text)
    button1.pack(side = 'left')
    button2 = tkinter.Button(panel, text = 'exit', command = confirm_to_quit)
    button2.pack(side = 'right')
    panel.pack(side = 'bottom')

    # open the main event loop
    tkinter.mainloop()

if __name__ == '__main__':
    main()
