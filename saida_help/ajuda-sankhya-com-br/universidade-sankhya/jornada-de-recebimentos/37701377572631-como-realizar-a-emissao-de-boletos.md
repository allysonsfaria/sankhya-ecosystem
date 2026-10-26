---
id: "37701377572631"
titulo: "Como realizar a emissão de boletos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos"
trilha: "Universidade Sankhya > Jornada de Recebimentos"
atualizado_em: "2026-09-17T01:12:37Z"
rotulos: ["Configuração", "Movimentação Financeira", "Portal de Vendas", "Boleto", "Financeiro", "Emissão"]
---

# Como realizar a emissão de boletos

| Categoria |
| --- |
| [Como funciona o processo de emissão de boletos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17PXVMPAYYQACJ8XZPTSVZ) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17PHS38KW9RQ6P2FKVF1R1) |
| [Quais os riscos de não as utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17PBKJZGNHAY30JQB4JD74) |
| [Vídeo com demonstração prática no Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KFDV71CFDZJC08WBN50VPZD3) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17P44K18H3QD0Z7WNDPWPF) |
| [Tarefa 1: Emissão de boletos no Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17NHNEE1J3J42NA2DBEVV7) |
| [Tarefa 2: Reimpressão de boletos:](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17NPKM0VBNSGEVJ69YENZ1) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701377572631-Como-realizar-a-emiss%C3%A3o-de-boletos#h_01KF17MZMQ2AWC94MS4VW2QBXZ) |

## Emissão de boletos

#### Como funciona o processo de emissão de boletos?

A emissão de boletos é um processo integrado ao ERP Sankhya que permite a geração e impressão de boletos bancários diretamente pelo sistema após registro de uma nota de venda ou lançamento direto no financeiro, eliminando a necessidade de sistemas externos, o que simplifica e agiliza o trabalho. 
Essa integração acelera o registro de receitas, evitando atraso. Além disso, garante que os dados estejam alinhados entre os módulos comercial e financeiro, oferecendo mais precisão e segurança. O procedimento inclui:

1. **Composição do Nosso Número:** Criação de um identificador único para o boleto.
2. **Geração do Código de Barras e Linha Digitável:** Elementos necessários para a cobrança e pagamento.
3. **Integração com o Financeiro:**

   - Durante o lançamento de uma Nota de Venda, o sistema pode gerar automaticamente o boleto.
   - Os dados do boleto são registrados no módulo financeiro, agilizando a gestão das receitas.

#### Quais problemas este recurso resolve?

- **Falta de eficiência operacional:** elimina a necessidade de processos manuais, economizando tempo e recursos.
- **Erros nos dados financeiros:** reduz erros manuais ao sincronizar automaticamente as informações entre o boleto e o financeiro.
- **Dificuldade para os clientes:** resolve atrasos e complicações no acesso aos boletos, tornando os pagamentos mais rápidos e simples.
- **Falta de integração entre módulos:** acaba com a descentralização dos dados, conectando os módulos comercial e financeiro em um único ambiente.

#### Quais os riscos de não as utilizar?

Não utilizar a emissão de boletos integrada no Sankhya pode trazer diversos riscos para a gestão financeira. Um dos principais é a **inconsistência nos dados**, onde informações desconectadas entre os módulos financeiro e comercial podem gerar erros nos registros. Além disso, há o risco de **atrasos na cobrança**, pois a falta de automação pode atrasar a emissão de boletos, comprometendo o fluxo de caixa da empresa.

Outro impacto significativo é a **perda de credibilidade**, já que boletos com erros ou atrasos podem prejudicar a relação com os clientes. Por fim, ocorre o **retrabalho**, pois a emissão manual de boletos exige mais tempo e esforço, resultando em custos operacionais mais elevados.

##### Vídeo com demonstração prática no Sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052444252)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** está passando por uma reorganização em sua área financeira e decidiu automatizar a emissão de boletos para simplificar o processo de cobrança e reduzir erros manuais. Até então, a geração de boletos era feita de forma externa, o que resultava em inconsistências nos registros e atrasos na cobrança.

A gestão estabeleceu um objetivo claro: configurar o sistema para que os boletos sejam gerados automaticamente durante o lançamento de notas de venda e permitir a reimpressão dos boletos diretamente pelo sistema, se necessário.

A equipe ficou encarregada de testar a funcionalidade de emissão de boletos em duas situações:

1. Emissão de boletos durante o lançamento de uma Nota de Venda.
2. Reimpressão de boletos já registrados no sistema.

**Tarefa:** Gere um boleto ao lançar uma Nota de Venda e, em seguida, realize a reimpressão do boleto pela tela de impressão de boletos, validando se as informações estão corretas e registradas conforme o esperado.

##### Tarefa 1: Emissão de boletos no Portal de Vendas

1. **Acessar a tela Portal de Vendas:**

- Vá para Comercial » Consulta » Portal de Vendas.

2. **Localizar a nota de venda:**

   - Utilize os filtros disponíveis para buscar uma nota de venda pendente. Atente-se em buscar pelo tipo de Movimento Nota de Venda.
   - Clique duas vezes sobre a nota para abri-la na Central de Vendas.

     **Emitir o boleto:**
   - Clique no botão com ícone da impressora e selecione **"Imprimir PIX/Boleto"**.
   - Selecione a opção de impressão ou salvar em PDF e salve na máquina.
3. **Validar a integração no Financeiro:**

- Acesse Financeiro » Rotinas » Movimentação Financeira.
- Utilize o filtro “Nr. Único” para localizar o título financeiro correspondente ao boleto gerado.
- Confirme se os dados do boleto estão corretamente vinculados ao título financeiro na aba **Cobrança**.

##### Tarefa 2: Reimpressão de boletos:

1. **Acessar a tela Impressão de Boleto(s):**

- Vá para Financeiro » Relatórios » Impressão de Boleto(s)

2. **Configurar os filtros:**

   - Na barra lateral esquerda, insira os seguintes dados:
   - Número financeiro (referente ao número único)
3. **Preencher os parâmetros do Boleto:**

   - No menu **"Parâmetros Boleto"**, selecione:
   - **Conta Bancária:** Conta configurada para a emissão do boleto.
   - **Modelo de Boleto:** O modelo de cobrança configurado.
   - **Agrupamento de Boleto:** Um título por Boleto
   - Marque a opção **Reimpressão de Boleto(s) (apenas registros com o Nosso Número gerado)** e na opção intervalo, altere para **Títulos da grade.**
4. **Reimprimir o Boleto:**

- Clique no ícone da impressora para **imprimir** e escolha o formato desejado (PDF ou impressão física).
- Verifique a impressão para confirmar que os dados do boleto estão corretos.

#### Correção e Repetição

- Certifique-se de que todos os campos obrigatórios foram preenchidos corretamente ao emitir e reimprimir boletos no sistema.
- Verifique se os valores inseridos estão alinhados com as diretrizes financeiras da empresa e se os títulos financeiros foram gerados corretamente no módulo financeiro.
- Caso o processo não tenha sido concluído conforme esperado, revise as configurações, ajuste os filtros e refaça a emissão ou reimpressão do boleto.
- Para praticar, experimente emitir um boleto para outro cliente ou testar diferentes modelos de cobrança configurados no sistema.
