import timeit
import pandas as pd
import numpy as np


class Sort:

    @staticmethod
    def insertionsort(dados, column, ascending=True):
        """
        Ordena um DataFrame usando o algoritmo de Insertion Sort.

        Parâmetros:
            dados (np.matrix): Matriz com os dados.
            column (int): Índice da coluna usada para ordenar a matriz.
            ascending (bool): Se True, ordena de forma crescente; se False, ordena de forma decrescente.

        Retorna:
            np.matrix: Matriz ordenada.
        """
        n = dados.shape[0]  # Número total de linhas na matriz

        # Algoritmo Insertion Sort
        if ascending:
            for j in range(1, n):  # Começar no segundo elemento (índice 1)
                linha_este = dados[j].copy()  # Cópia dos dados correspondentes para preservar o estado
                este = dados[j, column]
                i = j - 1

                # Procura a posição correta para inserir 'este'
                while i >= 0 and dados[i, column] > este:
                    dados[i + 1] = dados[i]  # Atualizar os dados do DataFrame de acordo
                    i -= 1

                dados[i + 1] = linha_este  # Atualizar os dados na nova posição
        else:
            for j in range(1, n):
                linha_este = dados[j].copy()  # Cópia dos dados correspondentes para preservar o estado
                este = dados[j, column]
                i = j - 1

                # Procura a posição correta para inserir 'este' (ordem decrescente)
                while i >= 0 and dados[i, column] < este:
                    dados[i + 1] = dados[i]  # Atualizar os dados do DataFrame de acordo
                    i -= 1

                dados[i + 1] = linha_este  # Atualizar os dados na nova posição
        return dados
    @staticmethod
    def insertion_sort(df, column='Date', ascending=True):
        """
        Manipula o DataFrame e ordena com o Algoritmo Insertion Sort(def insertionsort).

        Parâmetros:
            df (pd.DataFrame): DataFrame com os dados.
            column (str): Nome da coluna pela qual ordenar.
            ascending (bool): Se True, ordena de forma crescente; se False, ordena de forma decrescente.

        Retorna:
            pd.DataFrame: DataFrame ordenado.
        """

        # Garantir que a coluna está no formato datetime para ordenação adequada
        df[column] = pd.to_datetime(df[column])

        # Obter o índice da coluna
        indice_date = df.columns.get_loc(column)

        dados = df.to_numpy()  # Conversão para array numpy melhora a velocidade de manipulação

        #Ordenar os dados com ajuda do algoritmo Insertion Sort
        insertion_data=Sort.insertionsort(dados, indice_date, ascending)

        # Cria um novo DataFrame com os dados ordenados (reconstrói para manter estrutura original)
        df_ordenado = pd.DataFrame(insertion_data, columns=df.columns)

        return df_ordenado

    @staticmethod
    def mergesort(dados, column, ascending=True):
        """
        Ordena um DataFrame usando o algoritmo de Merge Sort.

        Parâmetros:
            dados (np.matrix): Matriz com os dados.
            column (int): Índice da coluna usada para ordenar a matriz.
            ascending (bool): Se True, ordena de forma crescente; se False, ordena de forma decrescente.

        Retorna:
            np.matrix: Matriz ordenada.
        """

        # Caso base: se a matriz tem apenas uma linha ou está vazia
        if dados.shape[0] <= 1:
            return dados  # Retornar a matriz original se já estiver ordenada

        # Calculo do meio da matriz
        meio = dados.shape[0] // 2

        # Divisão da matriz recursivamente até atingir o caso base
        esquerda = Sort.mergesort(dados[:meio], column, ascending)
        direita = Sort.mergesort(dados[meio:], column, ascending)

        # Merge das partes ordenadas
        return Sort.merge(esquerda, direita, column, ascending)

    @staticmethod
    def merge(esquerda, direita, column, ascending):
        """
        Junta duas metades ordenadas de uma matriz NumPy e retorna um array NumPy.

        Parâmetros:
            esquerda (np.matrix): Metade esquerda da matriz.
            direita (np.matrix): Metade direita da matriz.
            column (int): Índice da coluna usada para ordenar a matriz.
            ascending (bool): Se True, ordena de forma crescente; se False, ordena de forma decrescente.

        Retorna:
            np.array: Array NumPy com os dados ordenados.
        """
        aux = [] #Cria lista para armazenar as linhas das matrizes ordenadas
        i = j = 0

        #Correr enquanto a lista auxiliar não tiver as linhas todas
        while i < esquerda.shape[0] and j < direita.shape[0]:
            if ascending:
                if esquerda[i, column] <= direita[j, column]:
                    aux.append(esquerda[i])
                    i += 1
                else:
                    aux.append(direita[j])
                    j += 1
            else:
                if esquerda[i, column] >= direita[j, column]:
                    aux.append(esquerda[i])
                    i += 1
                else:
                    aux.append(direita[j])
                    j += 1

        # Adicionar os elementos restantes a matriz
        if i < esquerda.shape[0]:
            aux.extend(esquerda[i:])
        if j < direita.shape[0]:
            aux.extend(direita[j:])

        # Retornar um array NumPy com os dados ordenados
        return np.array(aux)


    def merge_sort(df, column="Date", ascending=True):
        """
        Manipula o DataFrame e ordena com o Algoritmo Merge Sort(def mergesort).

        Parâmetros:
            df (pd.DataFrame): DataFrame com os dados.
            column (str): Nome da coluna pela qual ordenar.
            ascending (bool): Se True, ordena de forma crescente; se False, ordena de forma decrescente.

        Retorna:
            pd.DataFrame: DataFrame ordenado.
        """
        # Garantir que a coluna está no formato datetime para ordenação adequada
        df[column] = pd.to_datetime(df[column])

        #Obter o índice da coluna
        indice_date = df.columns.get_loc(column)

        # Converter o DataFrame para um array NumPy para operações mais rápidas
        dados = df.to_numpy()

        #Ordenar os dados com o algoritmo Merge Sort
        merge_data = Sort.mergesort(dados, indice_date, ascending)

        #Converter a matriz retornada por merge_data para data frame denovo
        dataframe_merge = pd.DataFrame(merge_data, columns=df.columns)

        return dataframe_merge




# Implementar o TAD Fila ou Queue usando uma representação de lista.
class Queue:
    """Classe que implementa uma fila usando uma lista ."""

    def __init__(self,dim,tipo):
        """Inicializa a fila como uma lista privada vazia.(Metodo construtor)"""
        self.__elements = []# Atributo privado para armazenar os elementos na fila.

    def enqueue(self, elemento):
        """Adiciona um elemento ao final da fila.

        Parâmetros:
            elemento: Elemento que será adicionado ao final da fila.
        """
        self.__elements.append(elemento)

    def is_empty(self):
        """Verifica se a fila está vazia.

        Retorna:
            bool: True se a fila estiver vazia, False caso contrário.
        """
        return len(self.__elements) == 0

    def dequeue(self):
        """Remove o primeiro elemento da fila.

        Levanta:
            ValueError: Se a fila estiver vazia.
        Retorna:
            (int) Elemento removido da fila.
        """
        if self.is_empty():
            raise ValueError('Queue is empty')  # Exceção se não houver elementos na fila.

        return self.__elements.pop(0)  # Remove o primeiro elemento (FIFO).

    def first(self):
        """Retorna o primeiro elemento da fila sem o remover.

        Levanta:
            ValueError: Se a fila estiver vazia.

        Retorna:
            O primeiro elemento da fila.
        """
        if self.is_empty():
            raise ValueError('Queue is empty')  # Exceção para fila vazia.
        else:
            return self.__elements[0]  # Acessa o primeiro elemento.


def encher_fila():
    """Cria uma fila e preenche-a com os dados do DataFrame ordenado.

    Retorna:
        Queue: Fila com os dados do DataFrame.
    """
    queue = Queue()  # Cria um objeto do tipo Queue.

    #Lê o ficheiro CSV e converte-o num Data Frame
    df = pd.read_csv("../attendance.csv", encoding="latin1")

    # Chama a função de ordenação para ordenar os dados do ficheiro.
    # Retorna um DataFrame ordenado pela coluna 'Date'.
    df_sorted=Sort.insertion_sort(df, 'Date', True)

    # Itera sobre as linhas do DataFrame ordenado.
    # `_` é usado como convenção para ignorar o índice da linha, já que só utilizaremos os dados.
    for _, row in df_sorted.iterrows():
        queue.enqueue(row)  # Adiciona a linha atual à fila.

    return queue  # Retorna a fila preenchida.


class Assiduidade:
    """Classe que gere o registo de assiduidade de alunos."""

    def __init__(self):
        """Inicializa um dicionário para armazenar as presenças.

        Atributos:
            dict_assiduidade (dict):
                Chave: Nome do aluno.
                Valor: Lista de datas em que o aluno esteve presente.
        """
        self.dict_assiduidade = {}

    def registo_presencas(self, name, present, date):
        """Regista no dicionário o aluno e a sua data de presença caso ele tenha estado presente nesse dia

        Parâmetros:
            name (str): Nome do aluno.
            present (int): 1 se o aluno esteve presente, 0 caso contrário.
            date (str): Data da presença.
        """
        if present == 1:
            if name not in self.dict_assiduidade:
                self.dict_assiduidade[name] = []  # Cria uma lista vazia para o aluno, se necessário.
            self.dict_assiduidade[name].append(date)  # Adiciona a data à lista de presenças do aluno.

    def obter_presencas(self, nome_aluno):
        """Obtém as datas de presença de um aluno específico.

        Parâmetros:
            nome_aluno (str): Nome do aluno.

        Retorna:
            list: Lista de datas de presença ou uma lista vazia, caso o aluno não exista no registo.
        """
        return self.dict_assiduidade.get(nome_aluno, [])

    def soma_presenças(self):
        """Calcula o aluno com mais e menos presenças e imprime os resultados."""

        if not self.dict_assiduidade:  # Verifica se o dicionário está vazio.
            print("Não há presenças registadas.")
            return

        aluno_max = None  # Inicializa a variável para armazenar o aluno com mais presenças.
        aluno_min = None  # Inicializa a variável para armazenar o aluno com menos presenças.

        for aluno in self.dict_assiduidade.keys():
            # Atualiza o aluno com mais presenças.
            if aluno_max is None or len(self.dict_assiduidade[aluno]) > len(self.dict_assiduidade[aluno_max]):
                aluno_max = aluno
            # Atualiza o aluno com menos presenças.
            if aluno_min is None or len(self.dict_assiduidade[aluno]) < len(self.dict_assiduidade[aluno_min]):
                aluno_min = aluno

        # Imprime os resultados.
        print(f'Aluno com mais presenças: {aluno_max} ({len(self.dict_assiduidade[aluno_max])} presenças)')
        print(f'Aluno com menos presenças: {aluno_min} ({len(self.dict_assiduidade[aluno_min])} presenças)')

    def print_dict(self):
        """ Imprime o dicionário de maneira a haver uma melhor vizualisação. """

        if not self.dict_assiduidade:  # Verifica se o dicionário está vazio.
            print("Não há presenças registadas.")
            return

        for aluno in self.dict_assiduidade.keys():
            print(f'{aluno} :{self.dict_assiduidade[aluno]} presenças')

    def print_presenças(self):
        """ Imprime as presenças de cada aluno """
        if not self.dict_assiduidade:  # Verifica se o dicionário está vazio.
            print("Não há presenças registadas.")
            return


        for aluno in self.dict_assiduidade.keys():
            print(f'{aluno} :{len(self.dict_assiduidade[aluno])} presenças')




def criar_dict_assiduidade():
    """Cria e preenche um dicionário de assiduidade a partir de um ficheiro CSV."""

    # Lê o ficheiro CSV e converte-o num Data Frame
    df = pd.read_csv("../attendance.csv", encoding="latin1")
    # Chama a função de ordenação para ordenar os dados do ficheiro.
    # Retorna um DataFrame ordenado pela coluna 'Date'.
    df_sorted = Sort.merge_sort(df, 'Date', True)

    assiduidade = Assiduidade()  # Cria uma instância da classe Assiduidade.

    for _, linha in df_sorted.iterrows():
        # `_` ignora o índice da linha; `linha` contém os dados da linha atual.
        assiduidade.registo_presencas(linha["Name"], linha["Present"], linha["Date"])#Adiciona ao dicionário

    # Exibe o dicionário de presenças.
    assiduidade.print_dict()

    #Imprime o número de presenças de cada aluna
    #assiduidade.print_presenças()
    
    print('\n')

    # Calcula e imprime o aluno com mais e menos presenças.
    assiduidade.soma_presenças()


# Programa principal para testar as funções acima
if __name__ == '__main__':
    # Lê o arquivo CSV e armazena em um DataFrame
    df = pd.read_csv("../attendance.csv", encoding="latin1")

    # Testa o Insertion Sort em ordem crescente e imprime o resultado
    print(f'Insertion Sort Data Frame (ascending) \n {Sort.insertion_sort(df, "Date", True)}')

    # Testa o Merge Sort em ordem crescente e imprime o resultado
    print(f'Merge Sort Data Frame (ascending) \n {Sort.merge_sort(df, "Date", True)}')

    # Testa o Insertion Sort em ordem decrescente e imprime o resultado
    print(f'Insertion Sort Data Frame (descending) \n {Sort.insertion_sort(df, "Date", False)}')

    # Testa o Merge Sort em ordem decrescente e imprime o resultado
    print(f'Merge Sort Data Frame (descending) \n {Sort.merge_sort(df, "Date", False)}')

    print('\n')

    # Chama a função para criar o dicionário de assiduidade
    criar_dict_assiduidade()

    # Chama a função para encher a fila
    encher_fila()

    # -------------------------------------------------------------------
    # TESTAR OS ALGORITMOS
    # -------------------------------------------------------------------
    print('\n')

    # Testa o tempo de execução do Insertion Sort em ordem crescente
    test_insertion_ascending = timeit.timeit(lambda: Sort.insertion_sort(df, "Date", True), number=11)
    print(f'Teste Insertion (ascending): {test_insertion_ascending}')

    # Testa o tempo de execução do Merge Sort em ordem crescente
    teste_merge_ascending = timeit.timeit(lambda: Sort.merge_sort(df, 'Date', True), number=11)
    print(f'Teste Merge (ascending): {teste_merge_ascending}')

    # Testa o tempo de execução do Insertion Sort em ordem decrescente
    test_insertion_descending = timeit.timeit(lambda: Sort.insertion_sort(df, "Date", False), number=11)
    print(f'Teste Insertion (descending): {test_insertion_descending}')

    # Testa o tempo de execução do Merge Sort em ordem decrescente
    teste_merge_descending = timeit.timeit(lambda: Sort.merge_sort(df, 'Date', False), number=11)
    print(f'Teste Merge (descending): {teste_merge_descending}')

