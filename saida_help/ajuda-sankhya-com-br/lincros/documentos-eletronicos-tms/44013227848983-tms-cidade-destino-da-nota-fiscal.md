---
id: "44013227848983"
titulo: "[TMS] - Cidade Destino da Nota fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013227848983--TMS-Cidade-Destino-da-Nota-fiscal"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:50:59Z"
rotulos: ["sync_hc", "lincros", "lincros_13432832", "sync_hash_b75028bd7c8c"]
---

# [TMS] - Cidade Destino da Nota fiscal

**Menu**: Documentos Eletrônicos > NF-es

**Objetivo**: Auxiliar no entendimento da validação do destino informado no arquivo XML de NF-es (Notas Fiscais Eletrônicas)

**Considerações**:

- É necessário ter o arquivo XML da nota fiscal em questão;

Durante o processo de importação o sistema faz a validação do campo 'CEP Destino' e também do código IBGE informado (cMun) do XML da Nota Fiscal, conforme exemplo abaixo:

![Imagem 1: Durante o processo de importação o sistema faz a validação do campo 'CEP Destino' e também do código IBGE informado…](https://ajuda.sankhya.com.br/hc/article_attachments/44013228048279)

Sendo os campos:

<CEP> = CEP
<cMun> = Código IBGE do Município

Ocorre que, o sistema valida o código IBGE informado e assume o município o qual o mesmo pertence como destino do documento no TMS.

No exemplo acima, o CEP pertence ao município de Piracicaba/SP, todavia, o código IBGE informado no campo 'cMun' pertence à 'Nova Odessa/SP', que por sua vez, será preenchida como destino do respectivo documento.

Se os campos 'CEP' e 'cMun' estiverem divergentes o sistema leva em consideração ao que estiver no campo 'cMun'. Caso no campo 'CEP' estiver com CEP inválido, o sistema irá lançar com o nome do Estado na nota fiscal.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
