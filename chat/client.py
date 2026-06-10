import socket
import threading
from tkinter import Button, Entry, Text, Tk, simpledialog


class Chat:
    def __init__(self):

        HOST = '127.0.0.1'
        PORT = 55556
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        login = Tk()
        login.withdraw()

        self.window_loaded = False
        self.ativo = True

        self.name = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        self.room = simpledialog.askstring('sala', 'Digite a sala que deseja entrar!', parent=login)

        thread = threading.Thread(target=self.conecta)
        thread.start()
        self.window()

    def window(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title('Chat')

        self.box_text = Text(self.root)
        self.box_text.place(relx=0.05, rely=0.01, width=700, height=600)

        self.send_menssage = Entry(self.root)
        self.send_menssage.place(relx=0.05, rely=0.8, width=500, height=20)

        self.btn_send = Button(self.root, text='Enviar', command=self.sendMessage)
        self.btn_send.place(relx=0.7, rely=0.8, width=100, height=20)
        self.root.protocol("WM_DELETE_WINDOW", self.close)


        self.root.mainloop()

    def close(self):
        self.root.destroy()
        self.client.close()

    def conecta(self):
        while True:
            recieved = self.client.recv(1024)
            if recieved == b'SALA':
                self.client.send(self.room.encode())
                self.client.send(self.name.encode())
            else:
                try:
                    self.caixa_texto.insert('end', recieved.decode())
                except:  # noqa: E722
                    pass


    def sendMessage(self):
        message = self.send_message.get()
        self.client.send(message.encode())

chat = Chat()