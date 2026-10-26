---
id: "37224442149143"
titulo: "E0318 Rejeição: É obrigatório informar na DPS um item da NBS para casos de exportação de serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224442149143-E0318-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-na-DPS-um-item-da-NBS-para-casos-de-exporta%C3%A7%C3%A3o-de-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-13T22:35:38Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Artigo atualizado KCS", "Código NBS", "Documento de Prestação de Serviço (DPS)", "Exportação de serviços", "Não foi informado o código NBS", "DPS um item da NBS para casos de exportação de serviço", "Legislação da Reforma Tributária", "Código NBS correspondente ao serviço prestado", "Nomenclatura Brasileira de Serviços", "Rejeição E0318", "E0318 Rejeição", "Docs Eletrônicos - KCS", "NBS", "Exportacao"]
---

# E0318 Rejeição: É obrigatório informar na DPS um item da NBS para casos de exportação de serviço.

**MENSAGEM**

E0318 Rejeição: É obrigatório informar na DPS um item da NBS para casos de exportação de serviço.

**SITUAÇÃO**

A rejeição ocorre ao transmitir a Declaração de Prestação de Serviço (DPS) de uma operação de exportação de serviço, na NFS-e Padrão Nacional. O documento foi enviado sem o **código NBS** (Nomenclatura Brasileira de Serviços) no item, e isso bloqueia a emissão da nota e o faturamento.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações >> Cadastros >> Produtos >> Serviços) e localize o serviço que está sendo exportado.

**(2)** Na aba **"Impostos"**, confira o campo **"Código NBS"**:

- **Campo vazio:** preencha com o código NBS do serviço prestado, conforme a tabela oficial da Nomenclatura Brasileira de Serviços.
- **Campo não aparece na tela:** clique na engrenagem da tela, pesquise por "NBS" e adicione o campo à aba "Impostos".
- **Código incorreto:** corrija conforme a tabela NBS vigente.

**(3)** Ainda no cadastro do serviço, acesse a aba **"Configuração por Empresa"**. Se o **"Código NBS"** também estiver preenchido ali, remova-o e mantenha o código somente na aba **"Impostos"**.

**Importante:** o preenchimento nos dois lugares pode fazer o código ser enviado com os últimos dígitos cortados, e a SEFAZ o considera inválido.

**(4)**Acesse a tela **"Cidades"** (Comercial >> Arquivo >> Cadastros >> Cidades) e localize a cidade do emitente. Na aba **"NFS-e"**, marque a opção **"Enviar o Código NBS no JSON"** e salve.

**(5)** Acesse o **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas) e localize a nota rejeitada.

**(6)** Abra a nota e redigite o item: apague a quantidade e informe-a novamente. Assim a nota passa a usar os dados atualizados do cadastro.

**(7)** Gere novamente o lote de envio e transmita o documento.

**CAUSA**

A rejeição vem de uma validação da NFS-e Padrão Nacional: em operações de exportação de serviço, a DPS precisa informar o código NBS do serviço prestado. As principais causas são:

- O campo "Código NBS" está vazio ou incorreto no cadastro do serviço.
- O código está duplicado entre as abas "Impostos" e "Configuração por Empresa", o que corta os dígitos no envio.
- A opção "Enviar o Código NBS no JSON" está desmarcada no cadastro da cidade.
- A nota foi lançada antes da correção do cadastro e não foi atualizada.
