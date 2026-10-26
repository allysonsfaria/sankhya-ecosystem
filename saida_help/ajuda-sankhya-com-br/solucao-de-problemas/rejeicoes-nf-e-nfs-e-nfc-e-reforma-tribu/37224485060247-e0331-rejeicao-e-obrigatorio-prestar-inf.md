---
id: "37224485060247"
titulo: "E0331 Rejeição: É obrigatório prestar informações de comércio exterior para as situações de importação de serviços."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224485060247-E0331-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-prestar-informa%C3%A7%C3%B5es-de-com%C3%A9rcio-exterior-para-as-situa%C3%A7%C3%B5es-de-importa%C3%A7%C3%A3o-de-servi%C3%A7os"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:35Z"
rotulos: ["NF-e", "Central de Vendas", "Portal de Vendas", "Importação", "SEFAZ", "Erro", "Comércio Exterior"]
---

# E0331 Rejeição: É obrigatório prestar informações de comércio exterior para as situações de importação de serviços.

**MENSAGEM**

E0331 Rejeição: É obrigatório prestar informações de comércio exterior para as situações de importação de serviços.

**SITUAÇÃO**

A NF-e foi emitida como operação de importação de serviços sem o preenchimento das informações obrigatórias de comércio exterior no documento fiscal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal que apresentou a rejeição.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas)**.**

**(2)** Na grade de **''Itens''**, clique em **''Outras Opções'' (ícone com três pontos)** e selecione a opção **"Declaração de Importação e Adições"**.

**(3)** Clique no botão de inclusão **"+"** para adicionar as informações de importação.

**(4)** Preencha os campos obrigatórios na aba **"Geral"**, incluindo:

- **Número do Documento de Importação**
- **Data de registro da Declaração de Importação**
- **Local de desembaraço**
- **UF do desembaraço**
- **Data do desembaraço aduaneiro**

**OBSERVAÇÃO:** Os campos marcados com asterisco (\*) são de preenchimento obrigatório.

**(5)** Acesse a aba **"Adições de Importação - AD"** e preencha as informações específicas de cada adição, incluindo:

- **Número da adição**
- **Número sequencial do item**
- **Código do fabricante estrangeiro**
- **Valor de desconto**

**(6)** Caso a importação envolva processo de **drawback**, informe o número do processo no campo correspondente.

**(7)** Salve as informações e **aprove a nota** na Sefaz.

**(8)** Gere novamente o lote da NF-e para transmissão. 

**IMPORTANTE:** As informações de importação devem ser registradas **por item** da nota fiscal. Certifique-se de que todos os itens relacionados à importação de serviços possuam os dados de comércio exterior devidamente preenchidos.

**CAUSA**

A rejeição ocorre porque a **Sefaz identifica que se trata de uma operação de importação de serviços**, mas as informações obrigatórias de comércio exterior não foram preenchidas no documento fiscal. Segundo as regras de validação da NF-e, quando há importação de serviços, é **obrigatório informar os dados da Declaração de Importação** e suas respectivas adições, incluindo número do documento, datas, local de desembaraço e demais informações aduaneiras. A ausência desses dados impede a aprovação da nota pela Sefaz.
