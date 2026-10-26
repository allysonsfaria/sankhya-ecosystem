---
id: "42951119772439"
titulo: "Configurações - Clientes e Vendedores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951119772439-Configura%C3%A7%C3%B5es-Clientes-e-Vendedores"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:53:06Z"
rotulos: ["zydon", "sync_hc", "zydon_213266012803", "sync_hash_7d40c19c159b"]
---

# Configurações - Clientes e Vendedores

Como gerenciar ações disponíveis para clientes e vendedores

Personalize quais ações estarão disponíveis nos menus de contexto para **clientes e vendedores**. Essas configurações ajudam a adaptar os fluxos operacionais e garantir maior controle sobre os registros dentro do Zydon Admin.

## Como acessar

1. No menu lateral do Zydon Admin, clique em **Configurações**.
2. Em seguida, selecione a seção **Clientes e vendedores**.

![Imagem 1: Em seguid a, selecione a seção Clientes e vendedores .](https://ajuda.sankhya.com.br/hc/article_attachments/42951073399063)

## Clientes

## Ações de Tabela

Nesta tela, é possível definir quais ações estarão disponíveis para os clientes.

**Ações disponíveis para pedido**

- - Confirmar pedidos
  - Editar dados do pedido
  - Repetir pedido, gerando um novo pedido idêntico
  - Imprimir o resumo do pedido
  - Anexar documentos ou arquivos (ex: contrato, autorização)
  - Compartilhar link de pagamento (ativação opcional)

**Ações disponíveis para orçamento**

- - Editar o orçamento, antes da aprovação final
  - Gerar pedido a partir de um orçamento

**Ações disponíveis para financeiro**

- - Imprimir boleto para pagamento
  - Enviar comprovante
  - Download da Nota Fiscal Eletrônica (PDF)
  - Download do arquivo XML da Nota Fiscal
  - Copiar código de barras do boleto
  - Pagamento com QRCode

![Imagem 2: Pagamento com QRCode](https://ajuda.sankhya.com.br/hc/article_attachments/42951120080407)

## Vendedores

## Geral

Defina quais **clientes o vendedor poderá visualizar e atender**, configurando a regra de listagem de clientes. As opções são:

- - **Mostrar clientes vinculados ao vendedor**
    O vendedor verá apenas os clientes conectados a ele e poderá realizar pedidos para qualquer um desses clientes.
  - **Mostrar clientes vinculados ao vendedor preferencial**
    Exibe apenas os clientes com vínculo preferencial com o vendedor.
  - **Mostrar todos os clientes**
    Lista todos os clientes cadastrados, permitindo pedidos para qualquer um, mesmo sem vínculo.

![Imagem 3: Mostrar todos os clientes Lista todos os clientes cadastrados, permitindo pedidos para qualquer um, mesmo sem vínculo.](https://ajuda.sankhya.com.br/hc/article_attachments/42951103432727)

## Ações de Tabela

Assim como na configuração para clientes, é possível definir as ações disponíveis para os **vendedores** em seus respectivos menus de contexto.

**Ações disponíveis para pedido**

- - Confirmar pedidos
  - Editar dados do pedido
  - Repetir pedido
  - Imprimir o resumo do pedido
  - Anexar documentos ou arquivos
  - Compartilhar link de pagamento

**Ações disponíveis para orçamento**

- - Editar o orçamento, antes da aprovação final
  - Gerar pedido a partir de um orçamento

**Ações disponíveis para financeiro**

- - Imprimir boleto para pagamento
  - Enviar comprovante
  - Download da Nota Fiscal Eletrônica (PDF)
  - Download do arquivo XML da Nota Fiscal
  - Copiar código de barras do boleto
  - Pagamento com QRCode

![Imagem 4: Pagamento com QRCode](https://ajuda.sankhya.com.br/hc/article_attachments/42951088752407)

## Crédito

## Geral

A seção Credito, dentro de Configurações > Clientes e vendedores, define como o limite de credito dos clientes será controlado e como o sistema deve se comportar quando um pedido ultrapassar o limite disponível.

**Permitir ultrapassar limite de credito**

Define o comportamento do sistema quando um cliente tenta realizar um pedido que ultrapassa o limite de credito disponível. Escolha entre:

- - Bloquear ao atingir o limite: impede que o cliente finalize pedidos com pagamento a prazo quando o valor do pedido ultrapassar o limite de credito disponível.
  - Permitir exceder o limite: permite que pedidos a prazo sejam realizados mesmo quando o limite disponível for ultrapassado.

**Controle de limite de credito**

Define se o controle do valor utilizado do limite de credito será realizado automaticamente pelo Zydon ou por um sistema externo, como um ERP. Ative o toggle Habilitar controlar limite automaticamente pelo Zydon para que o próprio Zydon calcule e atualize o limite disponível a cada pedido; desative caso o controle de credito já seja feito no seu ERP ou outro sistema externo, evitando duplicidade de calculo.

![Imagem 5: Define se o controle do valor utilizado do limite de credito será realizado automaticamente pelo Zydon ou por um…](https://ajuda.sankhya.com.br/hc/article_attachments/42951120383127)

Dica: se o cliente usa formas de pagamento a vista (sem prazo), essas configurações de limite de credito não se aplicam - elas valem apenas para pedidos com pagamento a prazo.

---

Se tiver dúvidas sobre essas configurações ou qualquer outra funcionalidade do Zydon Admin, entre em contato com nossa equipe de suporte.

---

[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)
