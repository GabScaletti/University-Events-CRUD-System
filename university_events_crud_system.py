import os
from colorama import init, Fore
init(autoreset=True)

eventos = [] # Armazena todos os eventos cadastrados

# Classe de eventos e seus respectivos atributos
class Eventos:
    def __init__(self, nome_evento, descrição, data, vagas):
        self.nome_evento = nome_evento
        self.descrição = descrição
        self.data = data
        self.vagas = vagas
        self.participantes = []
        
# Classe de métodos CRUD
class SistemaCrud:
    def __init__(self):
        pass
    
    def cadastrar_eventos(self, nome_evento, descrição, data, vagas):
        """_Cadastra novos eventos à lista de eventos._

        Args:
            nome_evento (_str_): _Nome do evento a ser adicionado._
            descrição (_str_): _Do que se trata o evento._
            data (_str_): _Data do evento (dd/mm/aa)._
            vagas (_int_): _Quantidade de vagas disponíveis._
        """
        
        novo_evento = Eventos(nome_evento, descrição, data, vagas)
        if any(evento.nome_evento == nome_evento for evento in eventos):
            print(Fore.YELLOW + '\nEvento já cadastrado!')
        else:
            eventos.append(novo_evento)
            
    def exibir_eventos(self):
        """_Exibe os eventos e participantes de forma organizada._
        """        
        for index, evento in enumerate(eventos, 1): # enumerate retorna um objeto enumerado, ou seja, com um índice
            print(Fore.GREEN + f'\n{index}. Nome: {evento.nome_evento}',
                    f'\n   Descrição: {evento.descrição}',
                    f'\n   Data: {evento.data}',
                    f'\n   Vagas Disponíveis: {evento.vagas}'
                    )
            print(Fore.GREEN + '\nParticipantes:\n')
            if not evento.participantes:
                print(Fore.RED + '   Não há participants registrados!')
            else:
                for index, participante in enumerate(evento.participantes, 1):
                    print(f'   {index}. {evento.participantes[index - 1]}')
              
    def atualizar_eventos(self, nome_evento):
        """_Atualiza as informações como, descrição, data, quantidade de vagas._

        Args:
            nome_evento (_str_): _Nome do evento que deseja interagir._
        """        
        
        for evento in eventos:
            if nome_evento == evento.nome_evento:
                evento.descrição = input(Fore.YELLOW + '\nQual a nova descrição do evento? ' + Fore.RESET)
                evento.data = input(Fore.YELLOW + '\nQual a nova data do evento? [dd/mm/aa]: ' + Fore.RESET)
                evento.vagas = int(input(Fore.YELLOW + '\nQual a nova quantidade de vagas? [apenas n°]: ' + Fore.RESET))
                return
        print(Fore.RED + '\nEvento não cadastrado!')
    
    def registrar_participantes(self, nome_evento):
        """_Inscreve um participante ao evento desejado._

        Args:
            nome_evento (_str_): _Nome do evento a cadastrar o participante._
        """        
        
        for evento in eventos:
            if nome_evento == evento.nome_evento and evento.vagas > 0:
                evento.participantes.append(input(Fore.YELLOW + '\nQual o nome do participante a se inscrever? ' + Fore.RESET))
                evento.vagas -= 1
                print(Fore.GREEN + '\nParticipante inscrito com sucesso!')
                return
            elif nome_evento == evento.nome_evento and evento.vagas <= 0:
                print(Fore.RED + '\nSinto muito, vagas esgotadas!')
                return
        print('\nEvento não cadastrado!')

    def remover_participantes(self, nome_evento, nome_participante):
        """_Remove um participante do evento desejado._

        Args:
            nome_evento (_str_): _Nome do evento._
            nome_participante (_str_): _Nome do participante a ser removido do evento._
        """        
        
        for evento in eventos:
            if nome_evento == evento.nome_evento:
                if nome_participante in evento.participantes:
                    evento.participantes.remove(nome_participante)
                    evento.vagas += 1
                    print(Fore.GREEN + '\nParticipante removido com sucesso!')
                    return
                else:
                    print(Fore.RED + '\nParticipante não registrado no evento!')
                    return
        print('\nEvento não encontrado')

    def excluir_eventos(self, nome_evento):
        """_Exclui um evento._

        Args:
            nome_evento (_str_): _Nome do evento a ser excluído._
        """        

        for index, evento in enumerate(eventos):
            if nome_evento == evento.nome_evento:
                del eventos[index]
                print(Fore.GREEN + '\nEvento excluído com sucesso!')
                return
        print(Fore.RED + '\nEvento não cadastrado!')
                
# Classe de métodos para o sistema de Eventos
class SistemaDeEventos:
    def __init__(self):
        self.usuário_logado = None

    def limpar_tela(self):
        """_Limpa a tela do terminal._
        """        
        
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause(self):
        """_Pausa entre as execuções, controlado pelo usuário._
        """        
        
        input(Fore.BLUE + '\nAperte ENTER para continuar...')

    def exibir_usuários(self):
        """_Exibe todos os usuários disponíveis para login._
        """        
        
        print(Fore.BLACK + '\n{:=^30}'.format('Usuários'))
        print(
            '1. Coordenador',
            '\n2. Aluno/participante'
        )
        print(Fore.BLACK + '{:=^30}'.format('Usuários'))

    def exibir_opções_coordenador(self):
        """_Exibe as funções que o usuário "coordenador" possui._
        """        
        
        print(Fore.BLACK + '\n{:=^30}'.format('MENU'))
        print(
            '1. ➕ Cadastrar evento ',
            '\n2. 🔁 Atualizar informações',
            '\n3. 👁️  Exibir eventos',
            '\n4. 🗑️  Excluir evento'
            '\n5. 👤 Trocar de usuário',
            '\n0. 💀 Encerrar programa'
        )
        print(Fore.BLACK + '{:=^30}'.format('MENU'))

    def exibir_opções_aluno(self):
        """_Exibe as funções que o usuário "aluno" possui._
        """        
        
        print(Fore.BLACK + '\n{:=^30}'.format('MENU'))
        print(
            '1. 👁️  Exibir eventos',
            '\n2. ✅ Registrar-se',
            '\n3. ❌ Remover registro',
            '\n4. 👤 Trocar de usuário',
            '\n0. 💀 Encerrar programa'
        )
        print(Fore.BLACK + '{:=^30}'.format('MENU'))

    def processar_usuário(self, option):
        """_Processa o login escolhido pelo usuário._
        """        
        
        if option == 1:
            self.usuário_logado = 'coordenador'
            return True
        elif option == 2:
            self.usuário_logado = 'aluno/participante'
            return True
        else:
            print(Fore.RED + '\nOpção inválida, tente novamente!')
            return False

    def usuário_atual(self):
        """_Exibe o usuário logado no sistema._
        """        
        
        print(Fore.CYAN + f'\nUsuário atual: {Fore.RESET}{self.usuário_logado}')

    def processar_crud_coordenador(self, option):
        """_Processa a função de "coordenador" escolhida pelo usuário._

        Args:
            option (_int_): _Função que o usuário deseja executar._
        """        
        
        if option == 1: # Cadastra eventos com suas informações
            SistemaCrud().cadastrar_eventos(
                input(Fore.YELLOW + 'Qual o nome do evento a cadastrar? ' + Fore.RESET),
                input(Fore.YELLOW + '\nExplique com poucas palavras do que se trata o evento: ' + Fore.RESET),
                input(Fore.YELLOW + '\nQuando vai acontecer o evento? [dd/mm/aa]: ' + Fore.RESET),
                int(input(Fore.YELLOW + '\nQuantas vagas o evento vai possuir? [apenas números]: ' + Fore.RESET))
            )
        elif option == 2: # Atualiza as informações do evento (desc., data, vagas)
            SistemaCrud().atualizar_eventos(input(Fore.YELLOW + '\nQual evento será atualizado? ' + Fore.RESET))
        elif option == 3: # Exibir eventos disponíveis
            if not eventos:
                print(Fore.RED + 'Nenhum evento cadastrado!')
            else:
                SistemaCrud().exibir_eventos()
        elif option == 4:
            if not eventos:
                print(Fore.RED + '\nNão há eventos cadastrados!')
            else:
                SistemaCrud().excluir_eventos(input(Fore.YELLOW + '\nQual o evento a ser excluído? ' + Fore.RESET))
        elif option == 5: # Trocar de Usuário (logar com outro usuário)
            print(Fore.RED + '\nDesconectando...')
            return
        elif option == 0: # Encerra o programa
            self.limpar_tela()
            print(Fore.RED + 'Você desejou encerrar o programa 💀')
            exit()
        else:
            print(Fore.RED + '\nOpção inválida, tente novamente!')

    def processar_crud_aluno(self, option):
        """_Processa a função de "aluno" escolhida pelo usuário._

        Args:
            option (_int_): _Função que o usuário deseja executar._
        """        
        
        if option == 1: # Exibir eventos disponíveis
            if not eventos:
                print(Fore.RED + 'Nenhum evento cadastrado!')
            else:
                SistemaCrud().exibir_eventos()
        elif option == 2: # Inscrever aluno ao evento desejado
            if not eventos:
                print(Fore.RED + '\nNão há eventos cadastrados!')
            else:
                SistemaCrud().registrar_participantes(input(Fore.YELLOW + '\nQual o nome do evento que deseja se registrar? ' + Fore.RESET))
        elif option == 3: # Remover cadastro do aluno do evento inscrito
            SistemaCrud().remover_participantes(input(Fore.YELLOW + '\nQual o evento você deseja remover seu registro? ' + Fore.RESET),
                                                    input(Fore.YELLOW + '\nQual o nome que você registrou no evento? ' + Fore.RESET))
        elif option == 4: # Trocar de Usuário (logar com outro usuário)
            print(Fore.RED + '\nDesconectando...')
            return
        elif option == 0: # Encerrar programa
            self.limpar_tela()
            print(Fore.RED + 'Você desejou encerrar o programa 💀')
            exit()
        else:
            print('\nOpção inválida, tente novamente!')

    def executar_sistema(self):
        """_Inicia o programa._
        """        
        
        self.limpar_tela()
        while True:
            self.exibir_usuários()
            login = int(input(Fore.YELLOW + '\nQual usuário deseja logar? [apenas números]: ' + Fore.RESET))
            self.limpar_tela()
            if self.processar_usuário(login):
                if login == 1:
                    while True:
                        self.usuário_atual() # Exibe o usuário atual (coordenador)
                        self.exibir_opções_coordenador()
                        user_input = int(input(Fore.YELLOW + '\nO que deseja fazer? [apenas números]: ' + Fore.RESET))
                        self.limpar_tela()
                        self.processar_crud_coordenador(user_input)
                        if user_input == 5:
                            break
                        self.pause()
                        self.limpar_tela()
                    self.pause()
                elif login == 2:
                    while True:
                        self.usuário_atual() # Exibe o usuário atual (aluno/participante)
                        self.exibir_opções_aluno()
                        user_input = int(input(Fore.YELLOW + '\nO que deseja fazer? [apenas números]: ' + Fore.RESET))
                        self.limpar_tela()
                        self.processar_crud_aluno(user_input)
                        if user_input == 4:
                            break
                        self.pause()
                        self.limpar_tela()
                    self.pause()
                break
        self.executar_sistema()

# Dá início ao sistema
SistemaDeEventos().executar_sistema()
