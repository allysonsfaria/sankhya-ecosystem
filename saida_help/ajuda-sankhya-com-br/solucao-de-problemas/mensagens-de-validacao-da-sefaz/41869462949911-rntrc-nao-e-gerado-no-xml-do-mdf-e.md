---
id: "41869462949911"
titulo: "RNTRC não é gerado no XML do MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41869462949911-RNTRC-n%C3%A3o-%C3%A9-gerado-no-XML-do-MDF-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T13:26:14Z"
rotulos: ["MDF-e", "Configuração", "SEFAZ", "Transporte", "Docs Eletrônicos - KCS", "RNTRC", "Veículo da empresa", "RNTRC não é gerado no XML do MDF-e", "RNTRCFROTAPROP", "Enviar RNTRC da empresa para frota própria", "Documentos Eletrônicos"]
---

# RNTRC não é gerado no XML do MDF-e

**MENSAGEM:**

RNTRC não é gerado no XML do MDF-e

**SOLUÇÃO:**

**(1)** Verifique se o parâmetro **''RNTRCFROTAPROP''** - **''Enviar RNTRC da empresa para frota própria?''** está ativo.

**(2)** Acesse **Configurações » Cadastros » Veículos » aba Propriedades** e confira o estado da flag **"Veículo da empresa"** para o veículo utilizado na viagem.

**(3)** Com base no estado da flag, confirme onde o RNTRC deve estar cadastrado:

- Flag **marcada** → cadastre/confira o RNTRC em **Configurações » Cadastros » Empresas » aba Naturezas**.
- Flag **desmarcada** → cadastre/confira o RNTRC em **Configurações » Cadastros » Veículos » aba Propriedades**.

**(4)** Valide o RNTRC no Portal da ANTT:

- <https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/>

**(5)** Gere novamente o XML do MDF-e em **Comercial » Rotinas » Viagens de Transporte (MDF-e)** e confirme se o grupo de tags do RNTRC foi incluído.

**OBSERVAÇÃO:**

O RNTRC é único por empresa. A SEFAZ trata essa informação como opcional, mas quando enviada, é validada — se estiver inválida ou não encontrada por conta da flag mal configurada, a emissão pode ser rejeitada (erros 681 ou similares).

**CAUSA:**

O sistema não decide de onde buscar o RNTRC com base no "tipo de frota" isoladamente, ele segue a flag **"Veículo da empresa"**, marcada no cadastro do veículo (Configurações » Cadastros » Veículos » aba Propriedades):

- **Flag marcada**: o sistema busca o RNTRC **apenas** no cadastro da Empresa (Configurações » Cadastros » Empresas » aba Naturezas), mesmo que o veículo tenha um RNTRC próprio preenchido.
- **Flag desmarcada**: o sistema busca o RNTRC **apenas** no cadastro do próprio Veículo.

Se o RNTRC estiver preenchido no cadastro errado em relação ao estado dessa flag, o sistema simplesmente não o encontra, mesmo com o parâmetro ''RNTRCFROTAPROP'' ativo e o dado aparentemente correto em algum dos dois cadastros.
