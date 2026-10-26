---
id: "42951233690263"
titulo: "Como configurar a Integração Zydon ↔ Omie"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951233690263-Como-configurar-a-Integra%C3%A7%C3%A3o-Zydon-Omie"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:57:28Z"
rotulos: ["zydon", "sync_hc", "sync_hash_ea9edd02d9f9", "zydon_213266907433"]
---

# Como configurar a Integração Zydon ↔ Omie

A **integração Zydon ↔ Omie** conecta o seu portal B2B ao ERP Omie, sincronizando automaticamente produtos, clientes, estoque, vendedores e pedidos entre os dois sistemas — eliminando retrabalho e mantendo seus dados sempre atualizados.

Ideal para **distribuidores, atacadistas e indústrias** que usam o Zydon como canal de vendas e o Omie para gestão fiscal e operacional.

## Pré-requisitos

- Conta ativa no Zydon com acesso de **Administrador**
- Conta no Omie com acesso ao **Portal do Desenvolvedor**
- **App Key** e **App Secret** gerados no Portal do Desenvolvedor Omie

## Benefícios da integração

- Dados consistentes entre portal B2B e ERP, sem digitação duplicada
- Estoque sincronizado em tempo real
- Pedidos enviados automaticamente ao Omie
- Cálculo de impostos em tempo real no checkout (CBS, COFINS, ICMS, IPI, PIS)
- Configuração granular do que deve ou não sincronizar

## Como instalar a integração

1. **Acessar o App Center**
   No menu lateral esquerdo do Zydon, clique em **App Center → Aplicativos**. Na barra de busca, digite **Omie** e clique em **Instalar**.
   ![Imagem 1: Acessar o App Center No menu lateral esquerdo do Zydon, clique em App Center → Aplicativos . Na barra de busca, digite…](https://ajuda.sankhya.com.br/hc/article_attachments/42951196901399)
2. **Configurar os Webhooks no Omie**
   No Portal do Desenvolvedor Omie, cadastre a URL de webhook exibida na tela de configuração do plugin. Inscreva os seguintes eventos:
   - **clientefornecedor.\*** — inclusão, alteração e exclusão de clientes/fornecedores
   - **localestoque.\*** — inclusão, alteração e exclusão de locais de estoque
   - **produto.\*** — inclusão, alteração, exclusão e movimentação de estoque
   - **vendedor.\*** — inclusão, alteração e exclusão de vendedores![Imagem 2: vendedor.* — inclusão, alteração e exclusão de vendedores](https://ajuda.sankhya.com.br/hc/article_attachments/42951197166871)
3. **Inserir as credenciais**
   De volta ao Zydon, informe a **App Key** e o **App Secret** gerados no Portal do Desenvolvedor Omie e clique em **Conectar**. Após a validação, a integração estará ativa.
   ![Imagem 3: Inserir as credenciais De volta ao Zydon, informe a App Key e o App Secret gerados no Portal do Desenvolvedor Omie e…](https://ajuda.sankhya.com.br/hc/article_attachments/42951197438103)

## O que a integração sincroniza

### Produtos (Omie → Zydon)

Produtos do Omie são sincronizados automaticamente via webhook (inclusão, alteração, exclusão).

- **Campos:** descrição, código, EAN, peso bruto, valor unitário, unidade, marca e status
- **Variações** são detectadas e sincronizadas automaticamente como variações no Zydon
- Produtos excluídos ou inativados no Omie são desativados no Zydon
- **Sincronização manual:** aba Produtos → selecione os itens → **Sincronizar**

### Clientes (Omie → Zydon)

Clientes e fornecedores do Omie são sincronizados como Parceiros Comerciais. O roteamento depende das **tags** configuradas no Omie:

- Tag **"Cliente"** → sincronizado como **Parceiro Comercial**
- Tag **"Transportadora"** → sincronizado como **Método de Entrega**
- Ambas as tags → sincronizado como **ambos**
- Sem tag → **ignorado** (não sincronizado)

### Vendedores (Omie → Zydon)

- **Campos:** nome, e-mail e status (ativo/inativo)
- Vendedores inativados no Omie são desativados no Zydon automaticamente

### Locais de Estoque (Omie → Zydon)

- Depósitos do Omie são sincronizados como locais de estoque no Zydon
- O endereço é obtido automaticamente do cadastro da empresa no Omie

### Categorias de Produto — opcional (Omie → Zydon)

- Famílias de produto do Omie → categorias no Zydon
- Habilite nas configurações do plugin: opção **"Sincronizar categorias"**

### Estoque (Omie → Zydon)

- O estoque é sempre **sobrescrito** no Zydon com o valor atual do Omie (não soma nem subtrai)
- Controle por **produto + local de estoque**
- **Sincronização manual:** Configurações → aba Estoque → **Buscar Estoque**

### Pedidos (Zydon → Omie)

- Pedidos realizados no Zydon são enviados automaticamente ao Omie
- Se o cliente não existir no Omie, a integração cria o cadastro automaticamente
- Se o pedido tiver transportadora sincronizada, o frete é adicionado ao pedido no Omie
- **Regra "Somente Pagos":** quando ativada, apenas pedidos com status **Pago** são enviados

### Cálculo de Impostos em tempo real (Zydon → Omie)

- Durante o checkout, o Zydon consulta o Omie para calcular CBS, COFINS, ICMS, IPI, PIS e demais tributos
- O resultado é retornado imediatamente para exibição no checkout (fluxo síncrono)

## Configurações do plugin

### Produtos

- **Auto-criar produtos:** novos produtos no Omie são criados automaticamente no Zydon
- **Auto-atualizar produtos:** alterações no Omie são refletidas no Zydon

### Clientes

- **Auto-criar clientes:** novos clientes no Omie são criados automaticamente no Zydon
- **Auto-atualizar clientes:** alterações no Omie são refletidas no Zydon

### Vendedores

- **Auto-criar vendedores** e **Auto-atualizar vendedores**

### Locais de Estoque

- **Auto-criar locais de estoque**, **Auto-atualizar locais de estoque**
- **Auto-atualizar estoque:** movimentações no Omie atualizam o saldo no Zydon
- **Buscar Estoque:** força a sincronização manual de todos os produtos

### Pedidos

- **Somente pagos:** envia ao Omie apenas pedidos com status Pago
- **Cenário de Impostos, Categoria, Conta Corrente e CFOP:** configurações fiscais aplicadas aos pedidos

## Acompanhando os pedidos

A tela de **Pedidos Realizados** exibe 4 cards de status no topo: **Total, Pendentes, Sincronizados** e **Com Erro**. Clique em qualquer card para filtrar a listagem.

Pedidos com status **Erro** exibem um botão de **Reenviar** — clique para reprocessar após verificar o detalhe do erro.

> **💡 Dica:** antes de ativar a integração em produção, teste com um produto e um cliente para validar que os webhooks estão configurados corretamente no Portal do Desenvolvedor Omie. Webhooks faltando são a causa mais comum de falhas de sincronização.

## Perguntas frequentes

**Os clientes sem tag no Omie não aparecem no Zydon — por quê?**
Registros sem a tag "Cliente" ou "Transportadora" são ignorados pela integração. Adicione a tag correta no cadastro do Omie e sincronize manualmente.

**O estoque do Zydon está com valor errado após a sincronização.**
O estoque é sobrescrito pelo valor do Omie, não acumulado. Verifique o saldo no Omie e, se correto, use o botão **Buscar Estoque** nas configurações para forçar a sincronização.

**Um pedido ficou com status Erro — o que fazer?**
Clique no ícone de erro para ver o detalhe, corrija a causa (ex.: dados fiscais faltando, CNPJ do cliente não preenchido) e clique em **Reenviar**.

**Posso sincronizar apenas algumas entidades e deixar outras desativadas?**
Sim — cada entidade (Produtos, Clientes, Vendedores, Locais de Estoque, Categorias) tem suas próprias opções de auto-criar e auto-atualizar nas configurações do plugin. Desative as que não deseja sincronizar.

---

### 🚀 Quer Zydon e Omie 100% sincronizados? Teste grátis por 15 dias!

[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)
