from src.sender import handleSender
from src.receiver import handleReceiver

def main():
    choice = "A"
    print(r"""
███████╗ ██████╗ ██████╗ ███████╗███████╗███╗   ██╗
██╔════╝██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║
███████╗██║      ██████╔╝█████╗  █████╗  ██╔██╗ ██║
╚════██║██║      ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
███████║╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝

╔██████╗ ██████╗ ██████╗ ██╗███████╗ ██████╗ 
██╔════╝██╔═══██╗██╔══██╗██║██╔════╝██╔══██╗
██║     ██║   ██║██████╔╝██║█████╗  ██████╔╝
██║     ██║   ██║██╔═══╝ ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║     ██║███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
    """)
    print("This app, copies your screenshots(if it is saved to clipboard) and send it to your second device.")
    while(choice!="S" and choice!="R"):
        choice = input("Are you sender or reciever(S/R) : ")
    if choice=="S":
        handleSender()
    elif choice=="R":
        handleReceiver()
    

if __name__ == "__main__":
    main()