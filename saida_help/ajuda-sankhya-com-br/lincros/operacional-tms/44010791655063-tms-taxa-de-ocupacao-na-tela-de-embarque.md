---
id: "44010791655063"
titulo: "[TMS] - Taxa de ocupação na tela de embarque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010791655063--TMS-Taxa-de-ocupa%C3%A7%C3%A3o-na-tela-de-embarque"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:46:04Z"
rotulos: ["sync_hc", "lincros", "lincros_13433399", "sync_hash_f4191d62b9ea"]
---

# [TMS] - Taxa de ocupação na tela de embarque

**Menu**: Operacional > Cargas > Embarques

**Objetivo**: Como é feito o cálculo da % na coluna ocupação na tela do embarque

## Considerações:

- Possui grupo de veículos cadastrados

Abaixo segue as validações:

1. No embarque acessar a aba 'Documentos';
2. No rodapé verificar o campo 'Taxa Ocup.:';

![Imagem 1: No rodapé verificar o campo 'Taxa Ocup.:';](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963416157/67e495327fa42f57d1a675dcec64/56422EE5FE5D30D2AF7DC509C0C0A475?expires=1791331200&signature=f0a7491289198f1078fbec24630d6508b4443937b06a165163559bcce13e897e&req=dSkhFc1%2Fm4BaXvMW3nq%2BgXC4Br8%2Bi2X%2F%2FEiUlFYEM6w2kwla1aJghTowDWPc%0ACX3mNUVYqvHWbjoUSE70BYb9z0k%3D%0A)

Para que seja exibida a taxa de embarque e a quantidade de cubagem no rodapé dos documentos, no embarque, é necessário que exista um grupo de veículos na ordem de coleta relacionado a este embarque, caso não houver uma ordem de coleta ou não possuir um grupo de veículo na mesma, verificar se o embarque possui uma tabela de frete definida, e verificar se nessa tabela de frete existe valor no campo "Grupo de veículos", conforme exemplos abaixo:

## Na ordem de coleta

![Imagem 2: Na ordem de coleta](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963416163/2a45615c31f098b1a335491ed0a2/AA245A07145F7F4D87B2BEF869071651?expires=1791331200&signature=38f002c539a5cfd6c31af57ba1b8fadc44d7774119e062954a7ff5d7c90492f2&req=dSkhFc1%2Fm4BZWvMW3nq%2BgbwA%2F44fUrLwJ6aFARCHLXebNCTkX3z7AbGIAQB5%0A2%2F6s5ZDv4WDPNzJKpqZ9kNrMsTg%3D%0A)

## Na tabela de frete

![Imagem 3: Na tabela de frete](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963416185/45c7818908a13cc3aa419e0f3f93/F92E5D9DD71A9D057E3E3D0FCD762336?expires=1791331200&signature=4b641d5c9bd58f2d7b68003a54799e30dc9c17f452e0d1e234f450f7fd9da635&req=dSkhFc1%2Fm4BXXPMW3nq%2BgVNgRAzhA4Pi0jogqvmMcPff%2F6h2aU%2FqJLAgjRqP%0Acz2SFTBxGWZLL1inJwuYMzOegw8%3D%0A)

## Exemplo da tela do embarque com a coluna 'ocupação' adicionada

![Imagem 4: Exemplo da tela do embarque com a coluna 'ocupação' adicionada](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963416194/b711895582e9619d9d021064602d/9962AFFBA49E87934AE23697981992B7?expires=1791331200&signature=7e4d309c0e10a110e6efa2c54c31168219824dae7a10a9f0f6be273036c1323a&req=dSkhFc1%2Fm4BWXfMW3nq%2Bga%2FLORHwLdo6UKBYH3iFlpL9r8M5B9Yqs2mzE24m%0A7Rr%2FDt9AECBjbEQj97soTmqTMmc%3D%0A)

## Importante:

A informação da cubagem pode ser alimentada pela nota fiscal ou pode ser considerada a cubagem informada pela transportadora no CTe.

1. NFe - como na estrutura do XML não existe um campo específico para cubagem, pode ser utilizada TF\_CUBAGEM nas informações do contribuinte como já é feito com número e série da pré-nota;

   ![Imagem 5: NFe - como na estrutura do XML não existe um campo específico para cubagem, pode ser utilizada TF_CUBAGEM nas…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963416203/8569e4177021a657f6599c20291e/A5BA421B2E5CED9D1A43CA794BD48499?expires=1791331200&signature=50863d9aa2d5a20ea6c2525e5193fd9243be7d6bb25939faedf08c617a183f4a&req=dSkhFc1%2Fm4NfWvMW3nq%2BgQIBbX6RcN8j9QtpJKOCcwW4LyMqMrQDDTjubk2P%0AU5sw5a2KJMQZrII%2FDxh%2B3M5VsOQ%3D%0A)
2. Considerar da transportadora conforme consta no artigo: [[TMS] - Considerar Peso e Cubagem da Transportadora](https://sankhya.zendesk.com/hc/pt-br/articles/44010791655063).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
