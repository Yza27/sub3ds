import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    conn = sqlite3.connect('exemplo.db')
    return conn

# Função para criar a tabela se ela ainda não existir
def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo usuário
def inserir_usuario(login, senha, email, telefone):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (login, senha, email, telefone) VALUES (?, ?, ?, ?)', (login, senha, email, telefone))
    conn.commit()
    conn.close()

# Função para listar todos os usuários
def listar_usuarios():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Função para atualizar os dados de um usuário
def atualizar_usuario(id, login, senha, email, telefone):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET login = ?, senha = ?, email = ?, telefone = ? WHERE id = ?', (login, senha, email, telefone, id))
    conn.commit()
    conn.close()

# Função para deletar um usuário
def deletar_usuario(id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Exemplo de uso das funções
if __name__ == '__main__':
    criar_tabela()

    # Inserir um usuário
    inserir_usuario('user1', 'senha123', 'user1@example.com', '123456789')

    # Listar todos os usuários
    print("Lista de Usuários:")
    usuarios = listar_usuarios()
    for usuario in usuarios:
        print(usuario)

    # Atualizar os dados de um usuário
    atualizar_usuario(1, 'user2', 'novaSenha456', 'user2@example.com', '987654321')

    # Listar todos os usuários novamente para ver a atualização
    print("\nLista de Usuários atualizada:")
    usuarios = listar_usuarios()
    for usuario in usuarios:
        print(usuario)

    # Deletar um usuário
    deletar_usuario(1)

    # Listar todos os usuários após a exclusão
    print("\nLista de Usuários após exclusão:")
    usuarios = listar_usuarios()
    for usuario in usuarios:
        print(usuario)
