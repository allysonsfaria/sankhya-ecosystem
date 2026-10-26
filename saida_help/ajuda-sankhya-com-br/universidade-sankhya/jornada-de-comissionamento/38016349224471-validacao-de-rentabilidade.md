---
id: "38016349224471"
titulo: "Validação de rentabilidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38016349224471-Valida%C3%A7%C3%A3o-de-rentabilidade"
trilha: "Universidade Sankhya > Jornada de Vendas > Jornada de Comissionamento"
atualizado_em: "2026-07-22T14:02:23Z"
rotulos: ["Configuração", "Portal de Vendas", "Comissão", "Preferências", "Financeiro", "Comercial"]
---

# Validação de rentabilidade

## Como validar a rentabilidade do pedido após o cálculo de comissão

#### Qual o objetivo de calcular a comissão com percentual fixo?

O cálculo de comissão com percentual fixo tem como finalidade simplificar a remuneração da equipe comercial, utilizando uma taxa única aplicada a todas as vendas — independentemente do produto, forma de pagamento ou volume negociado. Esse modelo padronizado torna o entendimento mais fácil para o vendedor, reduz dúvidas e torna a apuração mais ágil, confiável e operacionalmente segura.

#### Quais problemas este recurso resolve?

- Erros recorrentes na aplicação de múltiplos percentuais;
- Dificuldade dos vendedores em entender as regras de comissionamento;
- Divergências internas por interpretações diferentes do cálculo;
- Conferências repetitivas e retrabalhos manuais desnecessários;
- Baixa previsibilidade no valor final a ser pago em comissões.

#### Quais os riscos de não calcular a comissão com percentual fixo?

Ignorar a aplicação de um percentual fixo pode gerar insegurança na equipe de vendas e comprometer a credibilidade do modelo de remuneração. A complexidade excessiva no cálculo pode abrir margem para erros, questionamentos e retrabalhos constantes, além de dificultar o controle financeiro e a previsibilidade dos custos com comissões. Isso impacta diretamente a motivação da equipe e a eficiência do processo como um todo.

#### Cenário de aplicação

**Contexto:** A Axis Ltda está revisando seu modelo de remuneração variável para tornar o processo mais claro e eficiente. Após ouvir feedbacks da equipe comercial e identificar inconsistências no cálculo das comissões, a empresa decidiu simplificar suas regras, buscando maior transparência e agilidade na apuração. Agora, é hora de estruturar o novo modelo e garantir que ele esteja alinhado aos objetivos da organização.

**Tarefa:** Siga as orientações indicadas para definir o comissionamento com percentual fixo.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Preferências”**
   **Menu:** Configuração  »  Avançado  »  Preferências

- No campo de busca **“Chave ou descrição e tecle ENTER”**, busque o parâmetro **PERCCOMISSAO**;
- Informe o percentual de comissão no campo **“Número Decimal**”, como 5,00, por exemplo;
- Clique no botão “**Salvar**”.
  **Importante!** Esta configuração define o percentual de comissão que será aplicado nas movimentações de venda habilitadas para cálculo de comissão.

2. Acesse a tela **“Gerente On-Line GOL”**
   **Menu:** Comercial  »  Gerente  »  Gerente On-Line - GOL

- No canto superior direito da tela, clique no botão “**Configurações**”;
- No menu lateral esquerdo, selecione “**Margem de Contribuição**”;
- Na seção **“Comissão”**, marque a flag e selecione a opção **“Fixa”**;
- Clique no botão “**Salvar**”.
  **Importante!** Esta configuração informa qual cálculo de comissão foi aplicado nas movimentações de venda, permitindo que os resultados sejam refletidos corretamente nas análises gerenciais.

3. Acesse a tela **“Portal de Vendas”**
   **Menu:** Comercial  »  Consulta  »  Portal de Vendas

- Lance uma nota de venda e informe o vendedor para que as parametrizações realizadas nos passos anteriores sejam refletidas no sistema.

**Atenção!** Caso o cadastro do vendedor contenha uma Fórmula Comissão com regras diferentes das configurações gerais, essa fórmula será priorizada.

#### Correção e repetição

- Revise os registros para confirmar se os valores e percentuais estão corretos;
- Garanta que os lançamentos foram realizados de forma adequada e estão devidamente alinhados com os objetivos do processo;
- Caso haja erro no registro ou na alocação dos valores, refaça a atividade seguindo o passo a passo novamente.
