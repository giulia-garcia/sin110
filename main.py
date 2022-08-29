# Giulia Garcia Castro
# 2020000191

# o jeito correto de importar o numpy (de acordo com a documentação!)
import numpy as np

def entrada(instancia):
  # obtêm o caminho da instância
  caminho = "F:/unifei/sin110/sin110/datasets/" + instancia + '.txt'

  # lê o conteúdo do arquivo da respectiva instância e o armazena em uma matriz do tipo numpy
  matriz = np.loadtxt(caminho)

  # retorna o nome da instância e utiliza o atributo shape para retornar o tamanho da matriz
  return instancia, matriz.shape

def saida(resultado):
  # obtêm o caminho do arquivo e acrescenta o resultado (a = append)
  arquivo = open("F:/unifei/sin110/sin110/resultado.txt", "a+")

  # concatena o resultado no formato "nome_instância qtd_linhas qtd_colunas"
  resultadoCompleto = f'{resultado[0]} {resultado[1][0]} {resultado[1][1]}'

  # mostra o resultado completo na tela
  print(resultadoCompleto)

  # escreve o resultado completo no arquivo (nome da instância + linhas + colunas)
  arquivo.writelines(resultadoCompleto+'\n')

  # fecha o arquivo após a escrita
  arquivo.close()


if __name__=='__main__':
  # o nome da instância é passado como parâmetro para o método no comando de execução
  instancia = input("Insira o nome da instância a ser lida: ")

  # a função de entrada lê o conteúdo do arquivo dessa instância e o armazena numa matriz do tipo numpy
  resultado = entrada(instancia)

  # a função de saída mostra o resultado e o salva no arquivo "resultado.txt"
  saida(resultado)