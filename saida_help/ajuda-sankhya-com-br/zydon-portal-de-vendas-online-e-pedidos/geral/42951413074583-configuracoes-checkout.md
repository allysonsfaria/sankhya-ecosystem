---
id: "42951413074583"
titulo: "Configurações - Checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951413074583-Configura%C3%A7%C3%B5es-Checkout"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T14:02:53Z"
rotulos: ["zydon", "sync_hc", "zydon_219372220798", "sync_hash_d03c7f2f42aa"]
---

# Configurações - Checkout

No painel **Configurações → Checkout**, você define **Requisitos de Checkout**: regras que travam ou liberam a finalização do pedido com base na quantidade de itens no carrinho ou no valor total em produtos. É possível aplicar essas regras para todos os clientes ou apenas para clientes e segmentos específicos.

### Pré-requisitos

- Acesso de **Administrador** ao Zydon Admin.

### Como acessar

No menu lateral, clique em **Configurações → Checkout → Requisitos de checkout**.

![Imagem 1: No menu lateral, clique em Configurações → Checkout → Requisitos de checkout .](https://ajuda.sankhya.com.br/hc/article_attachments/42951399215895)

### Requisitos de Checkout

Nesta tela você visualiza todos os requisitos já cadastrados, com **Nome**, **Tipo de condição**, **Mínimo**, **Máximo** e **Status** (Ativo/Inativo).

Para criar um novo, clique em **+ Adicionar**. O formulário é dividido em quatro blocos:

![Imagem 2: Para criar um novo, clique em + Adicionar . O formulário é dividido em quatro blocos:](https://ajuda.sankhya.com.br/hc/article_attachments/42951437198743)

## Geral

Defina o **Nome** do requisito - use algo descritivo, pois é por ele que você vai identificar a regra na listagem depois.

## Condições do requisito

Escolha o **Tipo de condição** que vai determinar quando o pedido pode ser finalizado:

- - **Por quantidade de itens no carrinho** - o pedido precisa ter um número mínimo (e/ou máximo) de itens.
  - **Por valor total em produtos** - o pedido precisa ter um valor mínimo (e/ou máximo) em produtos.

Depois, informe os campos **Mínimo** e **Máximo** correspondentes. Você pode preencher só o mínimo, só o máximo, ou os dois - não é obrigatório definir ambos.

## Clientes

Marque os clientes específicos aos quais esse requisito será aplicado. Use o campo de busca para localizar um cliente pelo nome ou documento, ou marque **Selecionar todos** para aplicar a todos.

> Se nenhum cliente for selecionado, verifique com o time se a regra deve valer para a base toda ou se falta associar os clientes certos - uma regra sem clientes e sem segmentos vinculados pode não ter efeito prático.

## Segmentos

Da mesma forma, marque os **segmentos de clientes** aos quais o requisito se aplica, também com opção de busca e de **Selecionar todos**.

Ao finalizar, use o toggle **Ativo/Inativo** no topo da tela para definir se o requisito já deve valer imediatamente, e clique em **Cadastrar**.

![Imagem 3: Ao finalizar, use o toggle Ativo/Inativo no topo da tela para definir se o requisito já deve valer imediatamente, e…](https://ajuda.sankhya.com.br/hc/article_attachments/42951428958359)

### Gerenciando requisitos existentes

Na listagem, clique no menu de três pontinhos (**⋮**) na coluna **Ações** de um requisito para:

- - **Desativar** (ou **Ativar**, se já estiver inativo) - pausa a regra sem excluí-la.
  - **Excluir** - remove o requisito permanentemente.

> Prefira **Desativar** em vez de **Excluir** quando a pausa for temporária. Assim você mantém o histórico de configuração e evita ter que recriar tudo depois.

### Dicas Extras

- Combine os tipos de condição com clientes e segmentos para criar regras específicas - por exemplo, um pedido mínimo maior para um segmento de clientes com condições comerciais diferenciadas.
- Revise periodicamente os requisitos **Ativos**: regras esquecidas podem bloquear pedidos legítimos no checkout sem que o motivo fique claro para o time de suporte.

### Perguntas Frequentes

**O cliente não conseguiu finalizar o pedido. Como saber se foi bloqueado por um requisito de checkout?** Verifique em **Configurações → Checkout → Requisitos de checkout** se existe alguma regra **Ativa** vinculada ao cliente (diretamente ou pelo segmento dele) cujo mínimo ou máximo não foi atingido pelo pedido.

**Posso ter mais de um requisito ativo ao mesmo tempo?** Sim. É possível cadastrar múltiplos requisitos, inclusive combinando os dois tipos de condição, aplicados a diferentes clientes ou segmentos.

**Dá para aplicar um requisito a todos os clientes de uma vez?** Sim, use a opção **Selecionar todos** nos blocos **Clientes** ou **Segmentos** do formulário.

**Excluí um requisito por engano, é possível recuperar?** Não. A exclusão é permanente - por isso, recomendamos usar **Desativar** em vez de **Excluir** sempre que houver dúvida.
