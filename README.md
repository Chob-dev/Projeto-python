# Calculadora de Consumo de Energia - Equipamentos

Um programa Python para cadastrar e gerenciar equipamentos, calculando o tempo total de uso e potência consumida.

##  Funcionalidades

- **Cadastro de Equipamentos**: Registre aparelhos com quantidade, tempo de uso e potência
- **Listagem de Equipamentos**: Visualize todos os equipamentos cadastrados com seus dados
- **Cálculo Automático**: A aplicação calcula automaticamente o tempo total de uso e potência total gasta

##  Como Usar

### Executar o programa

```bash
python Principal.py
```

### Opções disponíveis

1. **Cadastrar Equipamento**
   - Digite o nome do aparelho
   - Informe a quantidade de aparelhos
   - Especifique o tempo de uso (ex: 2h, 5h, 2,5h)
   - Informe a potência de cada aparelho (ex: 300w, 100w)

2. **Listar Equipamentos**
   - Visualize todos os equipamentos cadastrados
   - Se nenhum equipamento for encontrado, será oferecida a opção de iniciar um cadastro

##  Exemplos de Entrada

```
Qual o aparelho? Televisão
Quantos você tem? 2
Quanto tempo você usa os aparelhos? (ex: 2h, 5h, 2,5h) 4h, 3h
Qual a potência de cada aparelho? (ex: 300w, 100w) 100w, 120w
```

##  Arquivos do Projeto

- `Principal.py` - Arquivo principal com as funções de cadastro e listagem
- `relatório.txt` - Arquivo para armazenar relatórios
- `README.md` - Este arquivo

##  Requisitos

- Python 3.6 ou superior

##  Notas

- Os tempos devem ser inseridos separados por ", " (vírgula e espaço)
- A potência deve ser inserida com o sufixo "w" (watts)
- Os valores decimais podem usar "," ou "."
- O programa valida as entradas S/N para continuação de cadastros

##  Autor

Projeto desenvolvido como ferramenta de gerenciamento de equipamentos.
