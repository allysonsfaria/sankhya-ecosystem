---
id: "44012198064663"
titulo: "Como configurar um terminal de atendimento no modo representante?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012198064663-Como-configurar-um-terminal-de-atendimento-no-modo-representante"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:22:54Z"
rotulos: ["sync_hc", "magis5", "magis5_204055239608", "sync_hash_10aab762bc68"]
---

# Como configurar um terminal de atendimento no modo representante?

## O Terminal de Atendimento é utilizado para concretizar as vendas realizadas dentro da plataforma. Essa área é onde ocorre o processo final de uma transação comercial.

---

O **Terminal de Atendimento**, também conhecido como **Caixa** ou **PDV (Ponto de Venda)**, oferece duas modalidades de utilização: **modo loja** e **modo representante**.

No **modo loja**, o Terminal de Atendimento é utilizado quando o cliente está presente para efetuar a compra. Trata-se da forma tradicional de operação em estabelecimentos físicos, como lojas de varejo. Nessa modalidade, os produtos são selecionados, as formas de pagamento são definidas e a venda é concluída na presença do cliente. Todo o processo ocorre de forma imediata, sem a necessidade de aprovação financeira ou procedimentos de expedição. [(Clique aqui para configurar PDV modo loja)](https://sankhya.zendesk.com/hc/pt-br/articles/44012198064663)

No **modo representante**, o Terminal de Atendimento é utilizado por representantes comerciais que atuam em atacados, distribuidoras ou vendas externas. Nessa modalidade, o representante realiza vendas em nome da empresa, mesmo fora do estabelecimento físico. Essa funcionalidade permite emitir pedidos, aplicar descontos, definir condições comerciais e registrar todas as informações relevantes da negociação. Os pedidos gerados no modo representante são processados posteriormente pelo empreendimento.

Portanto, antes de iniciar qualquer venda, é necessário configurar um **Terminal de Atendimento**.

Feito login no Magis5 ERP vá até**"Configurações"**e por fim **"Empresa - Terminais de Atendimento"**

![Imagem 1: Feito login no Magis5 ERP vá até "Configurações" e por fim "Empresa - Terminais de Atendimento"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Nov-07-2025-04-12-04-0340-PM.png?width=329&height=639&name=image-png-Nov-07-2025-04-12-04-0340-PM.png)

Para cadastrar um terminal de atendimento no modo **Representante**, siga as etapas abaixo:

Na tela **Terminais de Atendimento**, preencha os seguintes campos:

![Imagem 2: Na tela Terminais de Atendimento , preencha os seguintes campos:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Nov-14-2025-06-25-27-5644-PM.png?width=688&height=261&name=image-png-Nov-14-2025-06-25-27-5644-PM.png)

- **Descrição:** Informe qual será o nome deste terminal de atendimento. É recomendado que a descrição corresponda ao nome do operador do caixa, uma vez que apenas um operador irá utilizá-lo. **Por exemplo: Cx João Paulo.**
- **IP:**Não é necessário o preenchimento. Este campo é utilizado apenas no terminal de atendimento modo loja. [Como configurar um terminal de atendimento no modo loja?](https://sankhya.zendesk.com/hc/pt-br/articles/44012216144791)

- **Qtd. Vias Impressão:**Informe quantas vias de impressão do cupom não fiscal serão impressas ao finalizar uma venda.

- **ID Externo:**Caso utilize um PDV externo, informe o ID.

- **Acesso:**Selecione **“Ambos”**.
- **Operação Padrão:**É um campo optativo. Por padrão, não é recomendado que selecione nenhuma operação, salvo exceção onde o terminal de atendimento será utilizado para apenas um tipo de venda.
- **Modelo de Impressora:**Informe qual o modelo da impressora que irá imprimir os cupons. **(Se não irá imprimir cupons não é necessário o preenchimento)**

- **Permitir selecionar o tipo de venda via caixa?:**Neste campo é definido a forma que este terminal de atendimento irá trabalhar. Ao selecionar **“Sim”**, é exibido um campo ao lado de ID Externo chamado **“Modo de Vendas”**, onde é possível selecionar: modo loja ou modo representante. Neste caso, selecione **"Modo Depósito"**.

- **Emitir NFC-e?:**Se selecionar **“Sim”**, será obrigatório a emissão do cupom fiscal por este terminal de atendimento. Neste caso, selecione **"Não"**.

- **Exibir Lembrete para trocar de vendedor?:**Considerando que nem todo operador de caixa atua como vendedor, essa configuração é utilizada para lembrar o operador de caixa de alterar o nome do vendedor em cada registro de venda. Caso não seja feita a alteração, todas as vendas serão registradas em nome do operador.

Segue abaixo um exemplo de um caixa configurado:

![Imagem 3: Segue abaixo um exemplo de um caixa configurado:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Nov-14-2025-06-32-32-0091-PM.png?width=688&height=256&name=image-png-Nov-14-2025-06-32-32-0091-PM.png)

Ao lado da aba **“Produtos”**, encontra-se a aba **“Depósitos”**, onde você pode definir de quais depósitos o terminal de atendimento irá descontar os produtos. Para isso, basta selecionar os depósitos desejados e configurar a **ordem de saída** dos itens.

![Imagem 4: Ao lado da aba “Produtos” , encontra-se a aba “Depósitos” , onde você pode definir de quais depósitos o terminal de…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-05-2024-09-35-30-7379-PM.png?width=688&height=167&name=image-png-Sep-05-2024-09-35-30-7379-PM.png)

### UTILIZANDO UM PDV - MODO REPRESENTANTE

Após configurar o terminal de atendimento, é necessário **vincular o representante comercial ao PDV do estabelecimento**, já que o representante não utilizará sempre o mesmo terminal.

Para isso, na tela de **Terminais**, identifique o **ID** do terminal de atendimento cadastrado.

![Imagem 5: Para isso, na tela de Terminais , identifique o ID do terminal de atendimento cadastrado.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-05-2024-09-36-31-8861-PM.png?width=536&height=315&name=image-png-Sep-05-2024-09-36-31-8861-PM.png)

Agora, no módulo de **Usuários**, localize o cadastro do representante que será vinculado ao terminal e insira o **ID do terminal** no campo **“ID Caixa Padrão”**.

![Imagem 6: Agora, no módulo de Usuários , localize o cadastro do representante que será vinculado ao terminal e insira o ID do…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Nov-14-2025-07-13-31-7197-PM.png?width=1323&height=74&name=image-png-Nov-14-2025-07-13-31-7197-PM.png)

Após inserir o ID no campo **“ID Caixa Padrão”**, clique em salvar. 

![Imagem 7: Após inserir o ID no campo “ID Caixa Padrão” , clique em salvar.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Nov-14-2025-07-13-55-8452-PM.png?width=766&height=213&name=image-png-Nov-14-2025-07-13-55-8452-PM.png)

Pronto! Agora o representante poderá utilizar o **PDV – modo representante** em qualquer computador, independentemente do local.

**Observação:** Caso um representante tenha acesso a mais de um estabelecimento, é possível vinculá-lo a todos, desde que, em cada empreendimento, exista um terminal de atendimento devidamente configurado.

**Por exemplo:
![Imagem 8: Observação: Caso um representante tenha acesso a mais de um estabelecimento, é possível vinculá-lo a todos, desde que,…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-05-2024-09-38-10-2854-PM.png?width=1866&height=386&name=image-png-Sep-05-2024-09-38-10-2854-PM.png)**
