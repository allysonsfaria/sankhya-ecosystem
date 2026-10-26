---
id: "42951210185111"
titulo: "Cadastro de Clientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951210185111-Cadastro-de-Clientes"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:56:51Z"
rotulos: ["zydon", "sync_hc", "zydon_213266016937", "sync_hash_2190e12630d6"]
---

# Cadastro de Clientes

O Cadastro de Clientes concentra todos os dados dos seus compradores B2B: CPF/CNPJ, endereços, contatos, limite de credito, grupo de pagamento e vendedores associados. E o ponto de partida para vender no seu portal B2B.

## Pré-requisitos

Acesso ao Zydon Admin com permissão para gerenciar clientes e vendedores.

## Onde encontrar

No menu lateral do Zydon Admin, clique em Clientes e vendedores e depois em Clientes.

## Entendendo a lista de clientes

![screenshot-1786990747348-9](https://ajuda.sankhya.com.br/hc/article_attachments/42951221152023)

No topo da tela, três cards resumem sua carteira: Total de clientes (todos os cadastrados), Com acesso vinculado (clientes que já possuem usuário para logar no portal) e Sem acesso vinculado (clientes ainda sem convite de acesso enviado).

A tabela Lista de clientes traz, entre outras, as colunas Nome, E-mail, Segmento, Status, Erro de Webhook, Tipo (Física/Jurídica), CPF/CNPJ, Inscrição Estadual, Telefone, Celular, Vendedor Preferencial, Empresa Padrão, Vendedores, Endereços e Contatos. Use Filtrar e Colunas para personalizar a visualização, ou Buscar para localizar um cliente específico.

Você também pode clicar em Importar para cadastrar vários clientes de uma vez via planilha.

## Criando um novo cliente

Clique em Adicionar, no canto superior direito da lista, para abrir o formulário de cadastro. Preencha as seções abaixo (todas ficam disponíveis no menu Acesso rápido, a esquerda do formulário):

![screenshot-1786990716710-7](https://ajuda.sankhya.com.br/hc/article_attachments/42951221297943)

## Informações básicas

Preencha o Nome/Razão social e escolha o Tipo de pessoa (Física ou Jurídica), que define se o campo exibido será CPF ou CNPJ. Complete também Identidade (RG ou Inscrição Estadual), E-mail, Telefone, Celular, a Empresa preferencial (caso sua operação tenha mais de uma empresa) e o Segmento do cliente.

![screenshot-1786990725383-8](https://ajuda.sankhya.com.br/hc/article_attachments/42951221390615)

## Crédito

Ative Habilitar credito para este cliente se ele puder comprar com pagamento a prazo. As regras gerais de limite de credito (bloqueio ou permissão de excesso, controle automático ou externo) são definidas em Configurações > Clientes e vendedores > Credito.

## Contatos

Clique em Adicionar contato para cadastrar os responsáveis pela empresa (nome, telefone, e-mail), garantindo que a comunicação chegue a pessoa certa.

## Endereços

Clique em Adicionar endereço para cadastrar matriz, filiais ou centros de distribuição. Esses endereços são usados para entrega, cobrança e emissão de documentos fiscais - e um cliente pode ter vários.

## Grupo de pagamento

Selecione quais grupos de pagamento (conjuntos de formas de pagamento previamente cadastradas) estarão disponíveis para este cliente, personalizando as opções de acordo com as politicas comerciais da sua empresa.

## Vendedores

Associe vendedores da sua empresa ao cliente, marcando as caixas correspondentes. Eles poderão visualizar e atender o cliente dentro do sistema, além de acompanhar pedidos, negociações e histórico.

- **Vendedor Preferencial**: clique no ícone de estrela ao lado de um vendedor para defini-lo como preferencial. Cada cliente pode ter apenas um vendedor preferencial, o que garante um atendimento mais próximo e personalizado.

![screenshot-1786990687440-4](https://ajuda.sankhya.com.br/hc/article_attachments/42951210736663)

## Campos especiais

Preencha aqui informações adicionais sobre o cliente que não existem nas tabelas nativas. Esses campos precisam ser criados antes em Configurações > Configurações avançadas > Atributos, selecionando a entidade Clientes.

Dica: se você integra a Zydon com um ERP, os clientes são sincronizados automaticamente - não e necessário cadastra-los manualmente.

## Perguntas frequentes

## Onde configuro as regras gerais de limite de crédito?

Em Configurações > Clientes e vendedores > Credito, onde você define se o sistema deve bloquear ou permitir pedidos que ultrapassem o limite, e se o controle e feito automaticamente pelo Zydon ou por um ERP externo.

## Como faço para o cliente acessar o portal B2B?

O cadastro em si não cria acesso. Na lista de clientes, verifique o card Sem acesso vinculado e use as configurações de Acessos para enviar um convite e permitir que o cliente crie seu próprio login no portal.

**[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)**
