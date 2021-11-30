# Nome: Wesley da Silva Ribeiro
# Matrícula: 2019006307

from decimal import *
from datetime import datetime

class View():
    def inicio(self):
        return self.Main_Menu()

    def Main_Menu(self):
        print("MENU")
        print("1. Cadastrar esportes")
        print("2. Consultar pedido")
        print("3. Alterar pedido")
        print("4. Excluir pedido")
        print("5. Sair")
        option = int(input("Escolha uma das opções acima: "))
        return option

    def Coleta_Dados_Pedido(self):
        order_id = input("Digite o identificador do pedido: ")
        customer_id = input("Digite o identificador do cliente: ")
        employee_id = input("Digite o identificador do vendedor: ")
        order_date = input("Digite a data de criação do pedido (AAAA-MM-DD): ")
        required_date = input("Digite a data de fechamento do pedido (AAAA-MM-DD): ")
        shipped_date = input("Digite a data de envio do pedido (AAAA-MM-DD): ")
        freight = input("Digite o valor do frete: ")
        ship_name = input("Digite o local de envio: ")
        ship_address = input("Digite o endereço: ")
        ship_city = input("Digite a cidade do envio: ")
        ship_region = input("Digite a região do envio: ")
        ship_postal_code = input("Digite o CEP: ")
        ship_country = input("Digite o país: ")
        shipper_id = input("Digite o id do endereço de envio: ")
        year, month, day = map(int, order_date.split("-"))
        order_date = datetime(year, month, day)
        year, month, day = map(int, required_date.split("-"))
        required_date = datetime(year, month, day)
        year, month, day = map(int, shipped_date.split("-"))
        shipped_date = datetime(year, month, day)
        pedido = [order_id, customer_id, employee_id, order_date, required_date, shipped_date, freight, ship_name, ship_address, ship_city, ship_region, ship_postal_code, ship_country, shipper_id]
        return pedido

    def Coleta_ID_Pedido(self):
        order_id = int(input("Digite o identificador do pedido: "))
        return order_id

    def Coleta_Dados_Pedido_Update(self, id):
        atributos = {1: 'customerid', 2: 'employeeid', 3: 'orderdate', 4: 'requireddate', 5: 'shippeddate', 6: 'freight', 7: 'shipname', 8: 'shipaddress', 9: 'shipcity', 10: 'shipregion', 11: 'shippostalcode', 12: 'shipcountry', 13: 'shipperid'}
        print("Digite: ")
        print("1. Para alterar o ID do cliente")
        print("2. Para alterar o ID do funcionário")
        print("3. Para alterar a data de criação do pedido")
        print("4. Para alterar a data de fechamento do pedido")
        print("5. Para alterar a data de envio do pedido")
        print("6. Para alterar o valor do frete")
        print("7. Para alterar o local de envio")
        print("8. Para alterar o endereço de envio")
        print("9. Para alterar a cidade de envio")
        print("10. Para alterar a região de envio")
        print("11. Para alterar o CEP de envio")
        print("12. Para alterar o país de envio")
        print("13. Para alterar o ID do endereço de envio")
        opcao = int(input("Escolha uma das opções acima: "))
        valor = input("Digite o novo valor para o atributo: ")
        # Dependendo o valor a ser alterado é feito o cast para o tipo apropriado
        if opcao > 2 and opcao < 6:
            year, month, day = map(int, valor.split("-"))
            valor = datetime(year, month, day)
        elif opcao == 2 or opcao == 13:
            int(valor)
        elif opcao == 6:
            Decimal(valor)
        else:
            str(valor)
        return [id, atributos[opcao], valor]

    def Exibe_Pedido(self, pedido, dados):
        if pedido is not None:
            print()
            print('Dados do pedido')
            print("ID: ", dados[0])
            print("ID do cliente: ", dados[1])
            print("ID do funcionário: ", dados[2])
            print("Data de criação: ", dados[3])
            print("Data de fechamento: ", dados[4])
            print("Data de envio: ", dados[5])
            print("Valor do frete: ", dados[6])
            print("Local de envio: ", dados[7])
            print("Endereço de envio: ", dados[8])
            print("Cidade de envio: ", dados[9])
            print("Região de envio: ", dados[10])
            print("CEP de envio: ", dados[11])
            print("País de envio: ", dados[12])
            print("ID do endereço de envio: ", dados[13])
        else:
            print("Consulta vazia!")

    def Exibe_Validacao(self, validade):
        if validade == None:
            print()
            print('Validação dos dados concluída com sucesso!')
            return True
        elif validade == 'c':
            print()
            print('Validação dos dados incompleta! O customerid informado não é válido!')
            print('A operação foi cancelada!')
            return False
        else:
            print()
            print('Validação dos dados incompleta! O employeeid informado não é válido!')
            print('A operação foi cancelada!')
            return False

    def Exibe_Status(self, status):
        print("\n" + status)