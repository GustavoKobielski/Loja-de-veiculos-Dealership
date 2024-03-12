import mysql.connector

# Define a dictionary with the database connection details
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'meu_projeto',
    'auth_plugin':'mysql_native_password'
}

def create_db_connection(db_config):
    """Create a database connection object."""
    connection = mysql.connector.connect(**db_config)
    return connection

# Create the database connection
connection = create_db_connection(db_config)

# Use the connection object to interact with the database
cursor = connection.cursor()



# PASSO A PASSO
# conscessionaria (vendedor, comprador, estoque)

# funcionario
    # nome, idade, cpf, salario

# comprador
    # nome, idade, cpf
    # listar estoque
    # comprar veiculo

# carro
    # marca, modelo, cor, tamanho_roda, portas

# moto
    # marca, modelo, cor, tamanho_roda, cilindrada

# estoque
    # colocar estoque
    # tirar estoque
    # listar estoque

class Concessionaria:
    def __init__(self,nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


class funcionario(Concessionaria):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)

class cliente(Concessionaria):
    def __init__(self, nome, idade, cpf,dinheiro):
        super().__init__(nome,idade,cpf)
        self.dinheiro = dinheiro

    #def comprar_veiculo(self):


    #def listar_veiculo(self):

    #def listar_veiculo_cliente(self):

class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

class carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, portas):
        super().__init__(marca, modelo, ano, cor)
        self.portas = portas

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor} {self.portas}"

class moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, cilindrada):
        super().__init__(marca, modelo, ano, cor)
        self.cilindrada = cilindrada


    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor} {self.cilindrada}"
class Estoque:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self,veiculo):
        insert_query = "INSERT INTO my_table (name, age) VALUES (%s, %s)"
        self.veiculos.append(veiculo)

    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(veiculo)



def check_credentials(cpf, senha):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        query = "SELECT nome FROM funcionario WHERE cpf = %s AND senha = %s"
        cursor.execute(query, (cpf, senha))

        result = cursor.fetchone()
        cnx.close()

        if result:
            return result[0]
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        cnx.close()
        return None

######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################



estoque = Estoque()

print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Conscessionaria")
print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

while True:
    escolha = str(input("Você quer entrar como cliente ou funcionario: "))
    if escolha == "funcionario":
        cpf_funcionario = str(input("Digite seu cpf: "))
        senha_funcionario = input("Digite sua senha: ")
        sim_nao = check_credentials(cpf_funcionario, senha_funcionario)

        if sim_nao: # entrar com login de banco de dados ou senha
            nome_pessoa = check_credentials(cpf_funcionario, senha_funcionario)
            print(f"Olá! , {nome_pessoa}!")

            print("1 - Adicionar Veiculo\n2 - Excluir algum veiculo\n3 - Listar veiculos existentes \n4 - Inicio")
            escolha_func = int(input("Digite qual opção você deseja: "))
            if escolha_func == 1:
                carro_moto = str(input("Você quer adicionar um carro ou uma moto: "))
                if carro_moto == "carro" or carro_moto == "CARRO":
                    car_marca = str(input("Digite a marca do carro: "))
                    car_modelo = str(input("Digite o nome do modelo do carro: "))
                    car_ano = int(input("Digite o ano do carro: "))
                    car_cor = str(input("Digite a cor do carro: "))
                    car_portas = int(input("Digite quantas portas o carro tem: "))
                    carrorr = "carro"
                    nd2 = 0
                    adicionar_query = "INSERT INTO veiculo (tipo, marca, modelo, ano, cor, portas, cilindragem) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(adicionar_query, (carrorr, car_marca, car_modelo, car_ano, car_cor, car_portas, nd2))
                    connection.commit()

                elif carro_moto == "moto" or carro_moto == "MOTO":
                    moto_marca = str(input("Digite a marca da moto: "))
                    moto_modelo = str(input("Digite o nome do modelo da moto: "))
                    moto_ano = int(input("Digite o ano da moto: "))
                    moto_cor = str(input("Digite a cor da moto: "))
                    moto_cilindradas = int(input("Digite quantas cilindradas a moto tem: "))
                    motorr = "moto"
                    nd = 0
                    adicionar_query = "INSERT INTO veiculo (tipo, marca, modelo, ano, cor, portas, cilindragem) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(adicionar_query, (motorr, moto_marca, moto_modelo, moto_ano, moto_cor, nd, moto_cilindradas))
                    connection.commit()

            elif escolha_func == 2:
                id_to_delete = int(input("Qual id dos veiculos você deseja excluir: "))
                delete_query = "DELETE FROM veiculo WHERE id = %s LIMIT 1"
                cursor.execute(delete_query, (id_to_delete,))
                connection.commit()

            elif escolha_func == 3:
                query = "SELECT * FROM veiculo"
                cursor.execute(query)
                rows = cursor.fetchall()

                for row in rows:
                    print("ID: {}, Tipo: {}, Marca: {}, Modelo: {}, Ano: {}, Cor: {}, Portas: {}, Cilindragem : {}".format(*row))


            elif escolha_func == 4:
                print("Voltando ao inicio")

    elif escolha == "cliente":
        nome_cliente = str(input("Diga seu nome: "))
        idade_cliente = int(input("Diga sua idade: "))
        cpf_cliente = int(input("Digite seu cpf: ").replace('.', '').replace('-', '').strip())

        adicionar_query_cliente = "INSERT INTO cliente (nome, idade, cpf) VALUES (%s, %s, CAST(%s AS CHAR))"
        cursor.execute(adicionar_query_cliente, (nome_cliente, idade_cliente, cpf_cliente))
        connection.commit()

        # Add a car or a motorcycle to the client_veiculo table
        compra_cliente = str(input("Você quer comprar um carro ou uma moto: "))

        if compra_cliente == "carro" or compra_cliente == "CARRO":
            query = "SELECT * FROM veiculo WHERE tipo = 'carro'"
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                print("ID: {}, Tipo: {}, Marca: {}, Modelo: {}, Ano: {}, Cor: {}, Portas: {}".format(*row))

            veiculo_id = int(input("Digite o ID do veículo: "))

            # Filter the veiculo table by ID
            query = "SELECT id, tipo, marca, modelo, ano, cor, portas, cilindragem FROM veiculo WHERE id = %s"
            cursor.execute(query, (veiculo_id,))
            veiculo = cursor.fetchone()

            if veiculo:
                # Get the client's ID and CPF
                cliente_id = int(input("Digite o ID do cliente: "))

                # Check if the client ID exists in the client table
                query = "SELECT COUNT(*) FROM cliente WHERE id = %s"
                cursor.execute(query, (cliente_id,))
                result = cursor.fetchone()[0]

                if result > 0:
                    # The client ID exists, so we can proceed with the purchase
                    print("Cliente encontrado!")

                    # Verificar se veiculo não é None
                    if veiculo:
                        # Converter veiculo_id para inteiro
                        veiculo_id = int(veiculo_id)

                        # Excluir as linhas relacionadas com o veículo na tabela cliente_veiculo
                        query2 = "DELETE FROM cliente_veiculo WHERE veiculo_id = %s"
                        cursor.execute(query2, (veiculo_id,))

                        # Inserir o veículo na tabela cliente_veiculo
                        query3 = "INSERT INTO cliente_veiculo(cliente_id, cpf, tipo, marca, modelo, ano, cor, portas, cilindragem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(query3, (
                        cliente_id, cpf_cliente, veiculo[1], veiculo[2], veiculo[3], veiculo[4], veiculo[5], veiculo[6],
                        veiculo[7]))

                        # Excluir o veículo
                        query = "DELETE FROM veiculo WHERE id = %s"
                        cursor.execute(query, (veiculo_id,))

                        connection.commit()

                        print("Compra realizada com sucesso!")
                    else:
                        print("Veículo não encontrado!")
                else:
                    print("Cliente não encontrado!")
            else:
                print("Veículo não encontrado!")

        elif compra_cliente == "moto" or compra_cliente == "MOTO":
            query = "SELECT * FROM veiculo WHERE tipo = 'moto'"
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                print("ID: {}, Tipo: {}, Marca: {}, Modelo: {}, Ano: {}, Cor: {}, Portas: {}".format(*row))

            veiculo_id = int(input("Digite o ID do veículo: "))

            # Filter the veiculo table by ID
            query = "SELECT id, tipo, marca, modelo, ano, cor, portas, cilindragem FROM veiculo WHERE id = %s"
            cursor.execute(query, (veiculo_id,))
            veiculo = cursor.fetchone()

            if veiculo:
                # Get the client's ID and CPF
                cliente_id = int(input("Digite o ID do cliente: "))

                # Check if the client ID exists in the client table
                query = "SELECT COUNT(*) FROM cliente WHERE id = %s"
                cursor.execute(query, (cliente_id,))
                result = cursor.fetchone()[0]

                if result > 0:
                    # The client ID exists, so we can proceed with the purchase
                    print("Cliente encontrado!")

                    # Verificar se veiculo não é None
                    if veiculo:
                        # Converter veiculo_id para inteiro
                        veiculo_id = int(veiculo_id)

                        # Excluir as linhas relacionadas com o veículo na tabela cliente_veiculo
                        query2 = "DELETE FROM cliente_veiculo WHERE veiculo_id = %s"
                        cursor.execute(query2, (veiculo_id,))

                        # Inserir o veículo na tabela cliente_veiculo
                        query3 = "INSERT INTO cliente_veiculo(cliente_id, cpf, tipo, marca, modelo, ano, cor, portas, cilindragem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(query3, (
                            cliente_id, cpf_cliente, veiculo[1], veiculo[2], veiculo[3], veiculo[4], veiculo[5],
                            veiculo[6],
                            veiculo[7]))

                        # Excluir o veículo
                        query = "DELETE FROM veiculo WHERE id = %s"
                        cursor.execute(query, (veiculo_id,))

                        connection.commit()

                        print("Compra realizada com sucesso!")
                    else:
                        print("Veículo não encontrado!")
                else:
                    print("Cliente não encontrado!")
            else:
                print("Veículo não encontrado!")


# FALTA TD DO CLIENTE
# TER CM REMOVER O FUNCIONARIO