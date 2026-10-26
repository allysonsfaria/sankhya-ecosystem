---
id: "44013447563287"
titulo: "[TMS] Integração Correios com tabela de frete para valores e prazos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013447563287--TMS-Integra%C3%A7%C3%A3o-Correios-com-tabela-de-frete-para-valores-e-prazos"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:58:19Z"
rotulos: ["sync_hc", "lincros", "lincros_13432419", "sync_hash_5ace2aef6b61"]
---

# [TMS] Integração Correios com tabela de frete para valores e prazos

**1. Problema Relatado pelo Cliente:** O cliente deseja automatizar a busca de valores de preço, prazo e ocorrências dos Correios, evitando a necessidade de cadastros manuais de  várias tabelas de fretes como é feito habitualmente com as demais transportadoras. Além disso, o cliente quer obter os valores dos diferentes serviços prestados pelos Correios, como Sedex, Sedex10, PAC, etc.

1. ## Cadastrar Tabela de Fretes:

Acesse: Cadastros Gerais > Transportadoras > Negociações > Tabelas de frete.

Cadastre uma tabela de frete com a transportadora 'ECT EMP BRAS DE CORREIOS E TELEGRAFOS' e uma rota 'Brasil x Brasil' com faixa de peso de "0" ao infinito ou utilize a faixa de peso que queira que essa tabela fique disponível, exemplo: 0 a 50 quilos

Aplicar filtros para rotas específicas, se necessário. Exemplo de preenchimento:

![Imagem 1: Aplicar filtros para rotas específicas, se necessário. Exemplo de preenchimento:](https://ajuda.sankhya.com.br/hc/article_attachments/44013474464407)

## Informar Serviço do Correios na Tabela de Frete:

No modal da tabela de frete, informe o serviço do Correios (PAC, Sedex, etc).

![Imagem 2: No modal da tabela de frete, informe o serviço do Correios (PAC, Sedex, etc).](https://ajuda.sankhya.com.br/hc/article_attachments/44013437694743)

## Criar Tabelas para Cada Modal:

É necessário criar uma tabela com cada modal, caso o cliente utilize mais opções de serviço do Correios;

![Imagem 3: É necessário criar uma tabela com cada modal, caso o cliente utilize mais opções de serviço do Correios;](https://ajuda.sankhya.com.br/hc/article_attachments/44013474674327)

Após clicar em "Salvar" o mesmo modal precisa ser adicionado na aba "Restrições de busca" como atendido:

![Imagem 4: Após clicar em "Salvar" o mesmo modal precisa ser adicionado na aba "Restrições de busca" como atendido:](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1962970996/401eb6cc7d977d7e083e38802c3c/7D8E0CCAB65A63CA3176A43D931C3E51?expires=1791331200&signature=7cb850e069bfd9167aa583e9ee488fcda37d685a5ca09ebf4a186226b658b05f&req=dSkhFMB5nYhWX%2FMW3nq%2BgSCyIOI19pb1eWJA5oRl7f2Oa9%2FLwjqwoQEpimk7%0AT2pVW4F5hbpbUZmEarZHA9aXMc4%3D%0A)

## Premissas para cálculo de preço e prazo:

Informação de login e senha cadastrados;

Ativação da integração habilitada;

Tabela de fretes por serviço Correios (PAC, Sedex e etc.);

Rota Brasil x Brasil ou detalhada;

Componente em generalidades (Valor Correios);

Deferimento de tabela;

Tabela de fretes com período vigente dentro da data atual;

Adicionar restrição com o modal atendido;

## Componente valor correios:

Na aba de generalidades é necessário informar um componente de frete chamado "Valor correios" responsável pela busca dos valores de fretes e prazos na base dos correios.

Exemplo de preenchimento:

![Imagem 5: Exemplo de preenchimento:](https://ajuda.sankhya.com.br/hc/article_attachments/44013468840471)

## Prazo

O Lincros pode buscar o prazo com base em uma tabela de prazo padrão para Correios, cadastrada manualmente ou buscar automaticamente pelo webservice, para esta segunda opção solicitar ao suporte a habilitação do serviço (gratuito).

Parâmetro de empresa a ser ativado: **buscarPrazoEntregaCorreios**= true
Parâmetros de empresa só podem ser configurados por usuários Lincros, desta forma, solicite que o suporte técnico esteja configurando este parâmetro em sua empresa.
