---
id: "360044110594"
titulo: "Código inválido. Utilizar código da \"Tabela de Códigos de Ajustes da Apuração do ICMS\" da UF do informante"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110594-C%C3%B3digo-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-C%C3%B3digos-de-Ajustes-da-Apura%C3%A7%C3%A3o-do-ICMS-da-UF-do-informante"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:24Z"
rotulos: ["#PUBLIFER", "#revisadojunior", "Configuração", "Fiscal", "NF-e", "SEFAZ", "ICMS", "Impostos", "CORE_E01946", "Código ICMS inválido", "Revise ajustes ICMS", "Regenere o arquivo"]
---

# Código inválido. Utilizar código da "Tabela de Códigos de Ajustes da Apuração do ICMS" da UF do informante

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16594977377047) MENSAGEM:**

Código inválido. Utilizar código da "Tabela de Códigos de Ajustes da Apuração do ICMS" da UF do informante. O 3º caractere deste código deve ser = Zero.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16594977386391) CAUSA:**

Mensagem apresentada quando enviado um 'Código de Ajuste da Apuração do ICMS' que difere do previsto na 'Tabela de Códigos de Ajustes da Apuração do ICMS'.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16594977379351) SOLUÇÃO:**

![Imagem 4: Na tela "Ajuste da Apuração de ICMS e ICMS ST", revise as informações inseridas para os 4 campos abaixo, que são os…](https://ajuda.sankhya.com.br/hc/article_attachments/16594977381655) Na tela **"Ajuste da Apuração de ICMS e ICMS ST",** revise as informações inseridas para os 4 campos abaixo, que são os responsáveis pela geração do campo **"COD\_AJ\_APUR"** do Registro E111:

![Imagem 5: Na tela "Ajuste da Apuração de ICMS e ICMS ST", revise as informações inseridas para os 4 campos abaixo, que são os…](https://ajuda.sankhya.com.br/hc/article_attachments/15185418573975)

**(1)** Campo **"UF"**:

Os dois primeiros caracteres (UF) referem-se à 'Unidade da Federação' do estabelecimento. O sistema obtém esta informação a partir do cadastro da Empresa.

**(1)** Campo **"Tipo Imposto"**:

O terceiro caractere refere-se à apuração própria ou da substituição tributária, em que:
0 - ICMS e
1 - ICMS ST.

**(1)** Campo **"Tipo Apuração":**

O quarto caractere refere-se à **utilização** e identificará o campo a ser ajustado:
0 - Outros débitos;
1 - Estorno de créditos;
2 - Outros créditos;
3 - Estorno de débitos;
4 - Deduções do imposto apurado.
5 - Débito especial.

**(1)** Campo **"Tipo de Ajuste**":

Os quatro caracteres seguintes, **sequência**, iniciando-se por 0001 deverá ser referente a identificação do tipo de ajuste deixando sempre um código genérico para a possibilidade de outras ocorrências não previstas.

![Imagem 6: Realizado os devidos ajustes, faça uma nova geração do arquivo e teste a validação.](https://ajuda.sankhya.com.br/hc/article_attachments/16595022218903) Realizado os devidos ajustes, faça uma nova geração do arquivo e teste a validação.
