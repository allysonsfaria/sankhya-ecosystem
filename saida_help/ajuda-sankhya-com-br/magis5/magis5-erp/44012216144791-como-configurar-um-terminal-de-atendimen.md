---
id: "44012216144791"
titulo: "Como configurar um terminal de atendimento no modo loja?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012216144791-Como-configurar-um-terminal-de-atendimento-no-modo-loja"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:22:09Z"
rotulos: ["sync_hc", "magis5", "magis5_204048109113", "sync_hash_75a295d894fb"]
---

# Como configurar um terminal de atendimento no modo loja?

## O Terminal de Atendimento é utilizado para concretizar as vendas realizadas dentro da plataforma. Essa área é onde ocorre o processo final de uma transação comercial.

---

O **Terminal de Atendimento**, também conhecido como **caixa** ou **PDV (Ponto de Venda)**, pode ser utilizado em duas modalidades: **modo loja** e **modo representante**.

**- Modo Loja:**
Neste modo, o terminal é utilizado quando o cliente está presente para efetuar a compra, sendo a operação típica de **lojas físicas**.
O processo inclui a **seleção de produtos**, definição das **formas de pagamento** e conclusão da venda **imediatamente**, sem necessidade de aprovação adicional do financeiro ou do processo de expedição.

**- Modo Representante:**
Destinado a **representantes comerciais** que atuam em **atacados, distribuidoras ou vendas externas**.
O representante pode realizar **vendas em nome da empresa**, mesmo fora do estabelecimento físico, emitindo **pedidos, aplicando descontos, definindo condições comerciais** e registrando informações relevantes para a negociação.
Os pedidos realizados neste modo são **processados posteriormente pelo empreendimento**.

[(Clique aqui para configura PDV modo representante)](https://ajuda.magis5.com.br/magis5-erp-como-configurar-um-terminal-de-atendimento-no-modo-representante?hsLang=pt-br)

💡 **Importante:** Antes de iniciar qualquer venda, é necessário **configurar um terminal de atendimento**.

Feito login no Magis5 ERP vá até **"Configurações"** e por fim **"Empresa - Terminais de Atendimento"**

![Imagem 1: Feito login no Magis5 ERP vá até "Configurações" e por fim "Empresa - Terminais de Atendimento"](https://ajuda.sankhya.com.br/hc/article_attachments/44012183763735)

Na tela de **"Terminais de Atendimento"**, preencha os campos a seguir:

![Imagem 2: Na tela de "Terminais de Atendimento" , preencha os campos a seguir:](https://ajuda.sankhya.com.br/hc/article_attachments/44012194534039)

- **Descrição:** Informe qual será o nome deste terminal de atendimento. Ex: **"Caixa + Nome do usuário"**

- **IP:** Informe o IP do computador que será utilizado pelo terminal de atendimento. Não é necessário ser o IP real da máquina; também é possível utilizar um IP genérico, como 192.192.192.192.

- **Qtd. Vias Impressão:** Informe quantas vias do cupom não fiscal devem ser impressas ao finalizar uma venda.

- **ID Externo:** Caso utilize um PDV externo, informe o ID.

- **Acesso:** Selecione **“Ambos”**.
- **Operação Padrão:** Por padrão, não é recomendado selecionar nenhuma operação. Use somente em casos excepcionais, quando o terminal de atendimento será dedicado a um único tipo de venda.
- **Modelo de Impressora:** Informe o modelo da impressora que será utilizada para imprimir os cupons.

- **Permitir selecionar o tipo de venda via caixa?**

  Define como este terminal de atendimento irá operar.

  - Se selecionar **"SIM"** será exibido o campo "**Modo de Vendas"**, onde você deve escolher **"Modo loja"** ou **"Modo Representante"**
  - Neste caso, selecione **"Modo loja"**.

- **Emitir NFC-e?:** Se selecionar **"SIM"**, a emissão do cupom fiscal será obrigatória neste terminal de atendimento.

- **Exibir Lembrete para trocar de vendedor?:** Esta configuração ajuda a lembrar o operador de caixa a alterar o nome do vendedor em cada venda. Caso não seja feita a alteração, todas as vendas serão registradas em nome do operador.

A seguir, um exemplo de como um caixa configurado

![Imagem 3: A seguir, um exemplo de como um caixa configurado](https://ajuda.sankhya.com.br/hc/article_attachments/44012208910871)

Ao lado da aba **"Produtos"**, está a aba **"Depósitos"**, onde é possível configurar de quais depósitos este terminal de atendimento irá retirar os produtos. Para isso, selecione os depósitos desejados e defina a ordem de saída dos produtos.

![Imagem 4: Ao lado da aba "Produtos" , está a aba "Depósitos" , onde é possível configurar de quais depósitos este terminal de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012131718807)

Após concluir todas as configurações, clique em **"Salvar"** para registrar as alterações.

### UTILIZANDO UM PDV - MODO LOJA

**O cadastro de um terminal de atendimento pode ser realizado em qualquer computador, desde que o usuário possua as permissões necessárias.**

No entanto, é obrigatório inserir no computador correspondente ao terminal o mesmo IP informado durante o cadastro.

Para isso, acesse o menu **Configurações → Configurações Gerais → PDV → IP do Caixa**, insira o IP da máquina e clique em **Salvar**.

![Imagem 5: Para isso, acesse o menu Configurações → Configurações Gerais → PDV → IP do Caixa , insira o IP da máquina e clique em…](https://ajuda.sankhya.com.br/hc/article_attachments/44012180271255)

**Observação:** Caso o usuário realize a limpeza dos arquivos temporários do computador, as configurações serão apagadas. Nesse caso, será necessário configurá-las novamente, pois o sistema exibirá a mensagem **“Caixa não configurado”**.
