---
id: "360043863514"
titulo: "Como emitir NFC-e para Consumidor Padrão Identificado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863514-Como-emitir-NFC-e-para-Consumidor-Padr%C3%A3o-Identificado"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:34Z"
rotulos: ["DUVIDANF", "XML", "SEFAZ", "NFC-e", "NFC-e Consumidor Padrão Identificado", "Emissão NFC-E", "Limite SEFAZ", "Identificação de Estrangeiro", "Documentos Eletrônicos", "Consumidor Padrão"]
---

# Como emitir NFC-e para Consumidor Padrão Identificado?

**(1)** Existem na NFCe regras de validação para que o destinatário adquirente seja identificado no DANFE.

**(1)** A identificação do destinatário tem algumas particularidades:

- É opcional, conforme o limite de valor da operação;
- Dependendo do limite de valor, mesmo para o caso de estrangeiro, é necessária a identificação;
- Para qualquer caso, decidindo pela identificação do destinatário, também é opcional a identificação completa do endereço, ou somente a identificação de CPF, CNPJ, ou dados da pessoa física estrangeira.

**(1)** O grupo <dest> do XML é opcional em se tratando de NFC-e e não havendo informação do destinatário não irá constar no XML e nem no DANFE informações sobre o destinatário.

**(1)** Por outro lado, se deseja informar o nome do destinatário (campo xNome que faz parte do grupo dest) é obrigatório informar também o CNPJ ou CPF ou idEstrangeiro, podendo até omitir o grupo <enderDest> que é opcional para a NFC-e.

**(1)** Resumindo:

- Na NFC-e não é informado nada sobre o Destinatário ou é informado somente o CNPJ ou CPF ou idEstrangeiro.
- Se desejar informar mais algum outro dado, por exemplo: nome, IE ou endereço informe também o CNPJ ou CPG ou idEstrangeiro.

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17151935456791) OBSERVAÇÃO:**

Importante lembrar que a SEFAZ estipulou um valor máximo de R$ **10.000,00** (dez mil reais) para uma NFC-e que não possua os dados completos do destinatário (ausência parcial ou total da tag <dest>).

Cada SEFAZ Estadual pode e estipulou valores diferentes para seu estado, então é importante consultar a Legislação Estadual para verificar o valor máximo permitido pela SEFAZ.
