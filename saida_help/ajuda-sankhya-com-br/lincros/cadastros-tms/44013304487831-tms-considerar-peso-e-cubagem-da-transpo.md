---
id: "44013304487831"
titulo: "[TMS] - Considerar Peso e Cubagem da Transportadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013304487831--TMS-Considerar-Peso-e-Cubagem-da-Transportadora"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:53:58Z"
rotulos: ["sync_hc", "lincros", "lincros_13432704", "sync_hash_b04dc2805587"]
---

# [TMS] - Considerar Peso e Cubagem da Transportadora

**Menu**: Cadastros Gerais > Transportadoras > Transportadora (Empresa)

**Objetivo**: Auxiliar no entendimento da correta utilização da configuração, permitindo que o sistema passe a considerar tanto cubagem como peso informados pela transportadora no CT-e.

**Considerações**:

- Possuir uma transportadora cadastrada no ambiente com CT-es importados;

Ocorre que o sistema possui expressões 'padrões', quando utilizadas estas configurações no cadastro da Transportadora(Empresa) e, caso se faça necessário utilizar uma expressão diferente, deve-se preencher os campos 'Expressão leitura cubagem' e/ou 'Expressão leitura peso'. Importante ressaltar que esta leitura é feita pelo sistema durante o processo de importação do XML do CT-e.

Quando marcada a opção 'Considerar peso do CT-e' no cadastro transportadora (empresa) o sistema irá, por padrão, buscar o campo 'PESO DECLARADO'.

Se, para determinada transportadora se faz necessário ler outro campo, devido à forma com que são emitidos os 'CTes' deve ser preenchido o campo 'Expressão leitura' peso desta forma:
         //\*/infCarga/infQ[tpMed='CAMPO QUE DEVE SER LIDO']/qCarga

A mesma lógica para cubagem, por padrão o sistema irá buscar o '00' onde tudo que for diferente disso, deverá ser preenchido o campo 'Expressão leitura cubagem', conforme texto abaixo:
        //\*/infCarga/infQ[cUnid='CAMPO QUE DEVE SER LIDO']/qCarga

![Imagem 1: A mesma lógica para cubagem, por padrão o sistema irá buscar o '00' onde tudo que for diferente disso, deverá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/44013296030359)

Outro ponto importante a respeito da utilização desta configuração, é que no sistema estas podem ser aplicadas para a empresa através de parâmetros de empresa (considerarCubagemTransportadora e considerarPesoTransportadora), podendo por exemplo, aplicar para a empresa toda e manter false em determinadas transportadoras.

Para mais informações a respeito do funcionamento desta configuração de empresa, entra em contato com o Suporte Lincros, através do e-mail: [atendimento@lincros.com](mailto:atendimento@lincros.com)

**Obs.:** Na configuração da transportadora (empresa) o sistema utiliza um valor como defatult, ou seja, padrão, uma vez que as transportadoras possuem inúmeras formas de descrever. Então sempre, verificar o campo em questão de como está informado no Dacte.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
