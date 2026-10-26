---
id: "360044278313"
titulo: "Melhores Práticas para Emissão de NF-e pelo Emitente Pessoa Física - Produtor Rural"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044278313-Melhores-Pr%C3%A1ticas-para-Emiss%C3%A3o-de-NF-e-pelo-Emitente-Pessoa-F%C3%ADsica-Produtor-Rural"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:59:07Z"
rotulos: ["DUVIDANF", "Configuração", "NF-e", "SEFAZ", "Disponível desde outubro de 2018", "Necessário e-CPF", "Versão 3.25+ e SanNFE 2.34+", "Documentos Eletrônicos", "Pessoa Física", "Produtor Rural"]
---

# Melhores Práticas para Emissão de NF-e pelo Emitente Pessoa Física - Produtor Rural

**(1)** Conforme estabelecido pelo **Ajuste Sinief 09/2017**e cumprido pela **[Nota Técnica 2018.001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9OYnBfONR2s=)**, a partir de outubro, pessoas físicas poderão emitir Nota Fiscal eletrônica via webservice, identificando-se através de seu CPF. Para usufruir deste recurso, o CPF deve estar vinculado a uma Inscrição Estadual.

**(1)** O principal profissional afetado por esta novidade é o produtor rural. Até então, o agricultor só tinha a opção de emitir Notas Fiscais eletrônicas avulsas, manualmente, através do portal da Sefaz.

**![Imagem 1: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17295190656535) IMPORTANTE:**

Cada estado possui autonomia para recusar esta novidade, mantendo a obrigação de uso da NFA-e (Nota Fiscal Avulsa eletrônica) para os produtores rurais. Em caso de dúvidas, entre em contato com sua Sefaz local.

#### Imagem 2: Prazo de implementação Prazo de implementação

A [Nota Técnica 2018.001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9OYnBfONR2s=) estabelece os seguintes prazos para a implementação da emissão de NF-e com CPF emitente:

- **1º de agosto de 2018**em ambiente de Homologação;
- **1º de outubro de 2018**em ambiente de Produção.

#### Imagem 3: Premissas da NF-e com CPF Emitente Premissas da NF-e com CPF Emitente

Ao emitir uma NF-e informando um CPF emitente, existem algumas particularidades para as quais deve-se estar atento. Confira:

- Na Chave de Acesso, o CPF tomará o lugar do CNPJ do emitente, sendo precedido por zeros, completando 14 posições;

- Será reservada a faixa 920 – 969 do campo Série da NF-e , como forma de identificação do Emitente pessoa física (CPF) para emissão via webservices;

        Configurado em: **Comercial » Arquivo » Cadastros » Tipos de Operação - TOP.** Botão: 'Outras Opções...>>Controle de Numeração'

- A NF-e deverá ser assinada com o Certificado Digital do Emitente, do tipo “e-CPF”;

        O Certificado Digital, devera ser adquirido através das Autoridades Certificadora-AC, credenciada junto ao ['Instituto Nacional de Tecnologia da Informaçao-ITI'](http://www.iti.gov.br/certificado-digital)

- Todas as regras de validação que verificavam apenas um CNPJ de emitente, passam a validar também o CPF do emitente.

- Não será aceita a emissão em EPEC para emitentes pessoa física;

- Não será aceita a emissão de NFC-e para emitentes pessoa física, a seguinte mensagem sera apresentada:

        Empresa do tipo 'Pessoa Física', não pode emitir NFC-e

- Não serão aceitos o cancelamento ou emissão de uma Carta de Correção para emitentes pessoa física, a seguinte rejeição será apresentada:

        Status de retorno: 227- Rejeição: CPF do Emitente difere do CPF do Certificado Digital.

- Não será aceita a utilização da rotina **"Inutilização de Numeração"**, a seguinte mensagem será apresentada:

       "A SEFAZ ainda não aceita inutilização de numeração de notas para empresa do tipo 'Pessoa Física'".

- As regras de validação C02a-08 e C02a-14, que validam se está sendo emitida uma NFe por pessoa física, passam a ser opcionais a critério da UF Autorizadora.
- Será responsabilidade do usuário configurar os impostos adequados a necessidade da emissão da NF-e por emitente com CPF. Nesta nota técnica ainda não constam regras ou validações ref. aos impostos como DIFAL / FCP / ST. Ou seja a configuração deverá ser feita conforme o que já é hoje para uma nota mas com o enfoque de uma pessoa física emitente.
- Implementação feita a partir da versao 3.25 ou superior e SanNFE 2.34 ou superior.
