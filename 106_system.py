def title(text):
    
    print('-' * len(text))
    print(text)
    print('-' * len(text))
    
while True:
    title("SISTEMA DE AJUDA PYHELP")
    
    function = input("Função ou biblioteca: ")
    
    if function == "exit":
        break
    
    title(f"Acessing manual of {function}...")
    
    help(function)
