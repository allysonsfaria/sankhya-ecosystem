---
id: "37945359194135"
titulo: "Conceito e eventos de manifestação do destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37945359194135-Conceito-e-eventos-de-manifesta%C3%A7%C3%A3o-do-destinat%C3%A1rio"
trilha: "Universidade Sankhya > Jornada de Manifestação de Destinatário (MD-e)"
atualizado_em: "2026-07-22T14:04:00Z"
rotulos: ["Eventos", "Fiscal", "NF-e", "XML", "SEFAZ", "Documentos Eletrônicos"]
---

# Conceito e eventos de manifestação do destinatário

## MD-e - Manifestação do Destinatário

#### O que é e qual o objetivo deste processo?

O MD-e (Manifestação do Destinatário) é um processo fiscal eletrônico em que o destinatário de uma Nota Fiscal Eletrônica comunica oficialmente à SEFAZ a sua posição em relação à nota emitida para o seu CNPJ. Por meio dele, a empresa pode declarar se apenas tomou ciência da operação, se confirma o recebimento da mercadoria, se desconhece a nota ou se a operação não foi realizada. O objetivo do MD-e é assegurar a posição oficial do destinatário perante o fisco e garantir que cada NF-e emitida contra o seu CNPJ seja tratada de forma adequada.

#### Eventos de Manifestação do Destinatário (MD-e)

As manifestações do destinatário são registradas por meio de eventos eletrônicos, que representam a posição oficial da empresa em relação a uma Nota Fiscal Eletrônica recebida. Cada evento possui uma finalidade específica e deve ser aplicado conforme a situação da operação.

- **Ciência da Operação**
  Utilizada quando a empresa apenas toma conhecimento da NF-e emitida para o seu CNPJ, sem confirmar a operação. Esse evento libera o download do XML e deve ser substituído por uma manifestação conclusiva em até 180 dias.
  **Exemplo:** fornecedor emite uma NF-e, a mercadoria ainda não chegou, mas é preciso acessar o XML para conferência antecipada.
- **Confirmação da Operação**
  Registrada quando a empresa reconhece a operação e confirma o recebimento da mercadoria ou serviço.
  **Exemplo:** a mercadoria é recebida e conferida conforme o pedido, nesse momento, a empresa confirma a operação.
- **Desconhecimento da Operação**
  Aplicada quando a empresa não reconhece a nota fiscal destinada ao seu CNPJ, funcionando como proteção contra emissões indevidas ou fraudulentas.
  **Exemplo:** uma nota aparece vinculada ao CNPJ da empresa, mas não houve negociação.
- **Operação não Realizada**
  Utilizada quando a nota foi emitida, mas a operação não se concretizou, como em casos de recusa de mercadoria ou devolução imediata.
  **Exemplo:** a mercadoria é entregue em desacordo com o combinado e a empresa recusa o recebimento.

#### Quais são os benefícios de realizar a manifestação do destinatário e os riscos de não aplicá-la?

Realizar a manifestação traz benefícios práticos como acesso oficial ao XML da NF-e — essencial para escrituração, auditoria, conferência de mercadorias e integração correta das informações no ERP Sankhya — além de assegurar a rastreabilidade das operações junto à SEFAZ e fortalecer o controle interno.

Por outro lado, não manifestar pode gerar riscos significativos, como o vínculo indevido do CNPJ a operações inexistentes, dificuldades no acesso e armazenamento dos XMLs, vulnerabilidade em auditorias fiscais e até autuações por inconsistências. Isso pode resultar em retrabalho operacional e perda de credibilidade da empresa diante de fornecedores e órgãos reguladores.

#### Entenda o processo

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/901866114)
