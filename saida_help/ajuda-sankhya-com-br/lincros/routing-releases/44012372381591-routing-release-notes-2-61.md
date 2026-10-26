---
id: "44012372381591"
titulo: "[Routing] - Release Notes 2.61"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012372381591--Routing-Release-Notes-2-61"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:26:38Z"
rotulos: ["sync_hc", "lincros", "lincros_13433706", "sync_hash_20372875ce6d"]
---

# [Routing] - Release Notes 2.61

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012372555799)

## Melhorias:

## Relatório de pedágio

Criamos o relatório de pedágio, que permitirá informar os pedágios que cada rota irá passar, juntamente com os valores correspondentes. Esse relatório proporciona maior transparência e controle sobre os custos de pedágio durante o transporte.

Complementando essa entrega, foi adicionada a coluna "IDVPO ANTT" no relatório de pedágios, contendo o número gerado pela ANTT no momento da compra do vale-pedágio via REPOM. Essa informação será utilizada futuramente na emissão do MDF-e conforme exigência da nova regulamentação da ANTT.

## Rota de transferência exportam ao TMS

O Routing agora identifica automaticamente o tipo de conhecimento das notas fiscais nas rotas exportadas para o TMS, utilizando as regras de negócio para definir se o conhecimento será "**Normal**", "**Veículo Adicional**" ou "**Redespacho**". Essa melhoria garante maior assertividade na integração e reduz a necessidade de ajustes manuais.

## Nova opção de filial no cadastro de transportadora

Implementamos a nova função **Filial Transportadora**, que permite a identificação automática do tipo de conhecimento das notas fiscais transportadas.

Com essa melhoria, o sistema agora consegue reconhecer quando uma transportadora atua como **matriz**ou **filial**, e assim classificar corretamente o tipo de conhecimento, seja em rotas de **transferência**ou **lastmile**. Essa identificação é feita com base na associação entre as filiais cadastradas, garantindo mais agilidade e precisão na operação.

![Imagem 2: Com essa melhoria, o sistema agora consegue reconhecer quando uma transportadora atua como matriz ou filial , e assim…](https://ajuda.sankhya.com.br/hc/article_attachments/44012330502679)
