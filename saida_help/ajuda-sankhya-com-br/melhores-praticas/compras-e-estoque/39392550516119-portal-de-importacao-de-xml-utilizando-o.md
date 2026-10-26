---
id: "39392550516119"
titulo: "Portal de Importação de XML: Utilizando o Financeiro do Sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39392550516119-Portal-de-Importa%C3%A7%C3%A3o-de-XML-Utilizando-o-Financeiro-do-Sistema"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-08-10T19:40:30Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "Financeiro", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Portal de Importação de XML: Utilizando o Financeiro do Sistema

Ao importar XMLs de notas fiscais por meio do **Portal de Importação de XML** (Comercial » Arquivo » Consultas » Portal de Importação de XML), o sistema permite definir como será realizada a geração do financeiro da nota.

É possível escolher entre duas opções:

- **Utilizar o financeiro informado no XML:** considera os dados das tags de duplicatas presentes no arquivo XML.
- **Utilizar o financeiro do sistema:** desconsidera as informações de duplicatas do XML e realiza a geração do financeiro conforme as configurações cadastradas no ERP Sankhya.

Este artigo apresenta como configurar e utilizar a opção **"Financeiro do Sistema"**, garantindo que os lançamentos financeiros sejam gerados de acordo com as regras e configurações definidas no ERP Sankhya.

### Configurando o Modelo de Importação de XML

Para que o sistema gere corretamente o financeiro ao escolher a opção **"Usar Financeiro do Sistema"**, é fundamental configurar adequadamente o **"Modelo de Importação de XML"**. 

Acesse a tela **"Preferências da Empresa"** (Comercial » Preferências » Empresa).

Localize a aba **"Modelo de Importação de XML"** e verifique se existe um modelo adequado para o tipo de operação que será realizada.

Caso não exista um modelo apropriado, crie um novo modelo específico para a situação, definindo o **"Tipo de Negociação"** que será utilizado na geração do financeiro. ([Modelo de Notas e Pedidos)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)

Certifique-se de que o **"Tipo de Negociação"** vinculado ao modelo possui as configurações de prazo e parcelas adequadas para suas necessidades.

### Utilizando o financeiro do sistema na importação

Após realizar todas as configurações necessárias, ao importar um XML através do **"Portal de Importação de XML"**, siga os passos:

Realize o vínculo dos produtos e do pedido de compra, se aplicável.

 Na etapa de tratamento de divergências financeiras, selecione a opção **"Usar Financeiro do Sistema"**.

 O sistema carregará automaticamente o **"Tipo de Negociação"** configurado no **"Modelo de Importação de XML"** e gerará os títulos financeiros conforme as regras cadastradas.

 Confira se os valores e vencimentos gerados estão corretos antes de finalizar a importação.

### Observações importantes

- A geração do financeiro pelo sistema considera as configurações definidas no **Tipo de Negociação** e no **Tipo de Operação (TOP)** utilizados na importação. Portanto, é importante garantir que ambos estejam corretamente configurados para a geração do financeiro conforme a operação realizada.
- Para **notas de emissão própria**, o comportamento do Portal de Importação de XML pode ser diferente do aplicado às notas de terceiros. Verifique se as configurações estão adequadas para cada situação.
- **Ajustes manuais:** caso seja necessário realizar ajustes no financeiro após a importação, acesse a tela **"Movimentação Financeira"** (Financeiro Movimentação Financeira) e realize as alterações necessárias nos títulos gerados.
