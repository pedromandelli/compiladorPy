# Trabalho de Compiladores

## INE5622 - Introdução a Compiladores

### Descrição
Feito por Pedro Balconi Mandelli \
O projeto consiste em um analisador léxico e sintático para uma linguagem de programação simplificada. O analisador léxico identifica e classifica os tokens presentes no código fonte, o analisador sintático faz a análise da estrutura gramatical do programa, verificando se está de acordo com as regras definidas na gramática da linguagem.

### Execução do projeto
1 - Execute o comando ```make run FILE=nomedoarquivo.lcc``` colocando o nome arquivo que você quer analisar, por exemplo: ```make run FILE=program1.lcc```. Se nenhum arquivo for determinado, o programa fará a analise do arquivo padrão: `entrada.lcc` \
2 - Utilize o comando ```make clean``` para limpar o ambiente

### Considerações
Os arquivos solicitados para entregar no trabalho são 'program1.lcc', 'program2.lcc' e 'program3.lcc'. \
Os outros arquivos são exemplos fornecidor pelo professor.
A tabela de reconhecimento sintática foi construida preenchendo uma planilha e transformada em um dicionário, seguindo os passos vistos na disciplina e recomendados nas instruções do trabalho.

### Sobre a estrutura do Programa
Como visto no exemplo na segunda página das notas da disciplina: https://drive.google.com/file/d/1LdAY8zMZot-NJuf9GVWefleyl_WD9Mp4/view?usp=sharing, o programa foi construido de forma que a entrada é passada para o analisador léxico e o analisador sintático solicita o próximo token para o análisador léxico, análisa o token, e caso não encontre erros, continua até chegar no token final do arquivo. \
Caso o análisador léxico encontre um erro, a execução será interrompida, indicando o token, junto com a linha e coluna de onde ele ocorre. \
Caso o análisador sintático encontre um erro, a execução será interrompida, os tokens reconhecidos e a tabela de símbolos gerada até o momento do erro seram impressos, além disso, é mostrada a forma sentencial, o símbolo não terminal mais a esquerda e o token de entrada.



