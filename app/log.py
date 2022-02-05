def add_log(file: str = './app/logs.txt', **kwargs):
    """Añade un log en un archivo

    Args:
        file (str): archivo sobre el que se escriben los registros
        **kwargs: Es posible darle cualquier valor para que
            en el archivo de texto se escriban

    Ejemplo:
        >>> add_log(nombre='Carlos', celular='123456')
        
        Se vera en el archivo logs.txt:

        nombre: Carlos, celular:123456,;
    """
    with open(file, 'a') as f:
        for key, value in kwargs.items():
            f.write(f'{key}: {value},')
            f.write(' ')
        f.write(';\n')