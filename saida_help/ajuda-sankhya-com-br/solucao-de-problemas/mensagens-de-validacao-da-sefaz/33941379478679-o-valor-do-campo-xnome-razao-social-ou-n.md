---
id: "33941379478679"
titulo: "O valor do campo Xnome (Razão Social ou Nome do emitente) informado não é válido - (NFC-e Consumidor Padrão)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33941379478679-O-valor-do-campo-Xnome-Raz%C3%A3o-Social-ou-Nome-do-emitente-informado-n%C3%A3o-%C3%A9-v%C3%A1lido-NFC-e-Consumidor-Padr%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-08-03T20:11:47Z"
rotulos: ["Configuração", "Parceiro", "XML", "SEFAZ", "NFC-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "informado não é válido", "Erro", "O valor do campo Xnome", "- (NFC-e Consumidor Padrão)", "(Razão Social ou Nome do emitente)"]
---

# O valor do campo Xnome (Razão Social ou Nome do emitente) informado não é válido - (NFC-e Consumidor Padrão)

**SITUAÇÃO:**

Ao tentar emitir uma **NFC-e** (Nota Fiscal de Consumidor Eletrônica), o sistema apresenta uma mensagem de erro relacionada à geração do XML, especificamente pela presença indevida da tag **<dest>**, que só deve ser gerada em situações específicas.

**SOLUÇÃO:**

**(1)**  **Verifique o parceiro informado na nota:** confirme se é um consumidor final sem CPF/CNPJ, geralmente cadastrado como **"Consumidor Não Identificado"**.

**(2)**  Configure corretamente o parceiro padrão da NFC-e:

- Acesse a tela **"Empresa"** (Comercial» Preferências» Empresa) e selecione a empresa correspondente;
- Clique na aba **"Documentos Fiscais Eletrônicos"**, sub aba **"NFC-e",** e no campo **"Parceiro Padrão da NFC-e"** e selecione o parceiro cadastrado como ''**Consumidor Final padrão (sem identificação)''.**

**Observações**:

- O parceiro Consumidor Final padrão (sem identificação) da nota deve ser o mesmo da configuração do parceiro padrão da empresa.
- Se a venda for para um cliente identificado (com CPF ou CNPJ), o sistema poderá gerar a tag **<dest>**, desde que os dados estejam completos e válidos.
- **Devolução de NFC-e :** Quando for necessário realizar a devolução de uma NFC-e (Nota Fiscal de Consumidor Eletrônica), deve-se emitir uma **NF-e (Nota Fiscal Eletrônica)** de devolução. Além disso, para a emissão da NF-e de devolução, é indispensável que o parceiro (cliente) esteja devidamente identificado com um **CPF ou CNPJ válido**. Essa informação é obrigatória para a validação fiscal do documento e para que a devolução seja autorizada pela SEFAZ.

**CAUSA:**

O erro ocorre quando o **"parceiro (cliente)"** utilizado na venda não corresponde ao **"Parceiro Padrão da NFC-e"** configurado no sistema. Dessa forma, o sistema entende que a nota deve conter dados de destinatário, gerando a tag **<dest>**, o que pode ser inválido em determinadas condições da NFC-e.
