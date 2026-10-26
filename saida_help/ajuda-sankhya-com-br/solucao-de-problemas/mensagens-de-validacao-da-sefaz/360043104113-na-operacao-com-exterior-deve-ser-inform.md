---
id: "360043104113"
titulo: "Na operação com Exterior deve ser informada tag idEstrangeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043104113-Na-opera%C3%A7%C3%A3o-com-Exterior-deve-ser-informada-tag-idEstrangeiro"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:12Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "CFOP", "720", "Rejeição 720: Tag idEstrangeiro Faltando", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Na operação com Exterior deve ser informada tag idEstrangeiro

[720 - Rejeição]: Na operação com exterior deve ser informada tag idEstrangeiro.

### SITUAÇÃO

Esta rejeição ocorre durante a emissão de nota fiscal eletrônica (NF-e ou NFC-e) quando o sistema identifica uma operação com o exterior (idDest = 3 ou CFOP iniciado em 7), porém o campo **"Identificação de estrangeiro"** (idEstrangeiro) não foi preenchido no cadastro do parceiro, impedindo a autorização do documento pela SEFAZ.

### SOLUÇÃO

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros).

- Na aba **"Identificação"**, localize o campo **"Identificação de estrangeiro"** e informe o número do passaporte ou outro documento legal para identificar a pessoa estrangeira.

Após preencher o documento, salve as alterações e transmita a nota fiscal novamente.

**Exemplo da tag gerada:**
`<idEstrangeiro>ABC1234</idEstrangeiro>`

### CAUSA

A legislação fiscal brasileira exige que, em operações com parceiros do exterior, seja informado um código de identificação no XML da nota fiscal. A ausência desta informação no cadastro do parceiro impede a geração da tag no arquivo XML, resultando na rejeição 720.

### OBSERVAÇÕES

- Caso a operação não seja destinada ao exterior, verifique o cadastro de endereço do parceiro da nota e ajuste para um endereço dentro do Brasil.
 - Para mais detalhes técnicos, consulte o [Manual de Orientação do Contribuinte v.6](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=).
