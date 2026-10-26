---
id: "44010529217815"
titulo: "[TMS] - Erro na importação de CT-e por duplicidade de numeração com CT-e de Serviço da transportadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010529217815--TMS-Erro-na-importa%C3%A7%C3%A3o-de-CT-e-por-duplicidade-de-numera%C3%A7%C3%A3o-com-CT-e-de-Servi%C3%A7o-da-transportadora"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:40:46Z"
rotulos: ["sync_hc", "lincros", "lincros_16528123", "sync_hash_ab49915c4dc6"]
---

# [TMS] - Erro na importação de CT-e por duplicidade de numeração com CT-e de Serviço da transportadora

**Menu**: Operacional > Importação > CT-e > Importação

**Objetivo**: Entender por que a importação de um CT-e é bloqueada com as mensagens "CT-e com situação inválida para importação (cancelado ou anulado)" ou de duplicidade, mesmo quando o documento não foi cancelado pelo cliente, e como solicitar a correção.

**Considerações**:

- A transportadora emitiu um CT-e do tipo **Serviço** usando o mesmo número e série de um CT-e **Eletrônico** já existente na base;
- O sistema identifica um CT-e pela combinação **Número + Série + Emitente (transportadora)**. Ao encontrar um registro de CT-e de Serviço já ocupando essa combinação, o sistema entende que o documento já existe e bloqueia a entrada do CT-e Eletrônico real;
- A mensagem de erro varia conforme a situação do CT-e de Serviço conflitante:
- **Anulado** → "CT-e com situação inválida para importação (cancelado ou anulado)"
- **Ativo** → erro de duplicidade

**Causa comum**: falha da transportadora no envio do EDI/arquivo (por exemplo, troca de sistema de emissão), que gera indevidamente um registro de CT-e de Serviço com a mesma numeração de um CT-e Eletrônico real.

**Como identificar**:

1. Acesse Documentos eletrônicos > CT-es (ou o relatório de Conhecimentos de frete) e filtre pelo número do CT-e rejeitado;
2. Verifique se existe mais de um registro para o mesmo número/série, de tipos diferentes (CT-e Eletrônico e CT-e de Serviço), emitidos pela mesma transportadora;
3. Confirme a situação do registro do tipo Serviço (Ativo ou Anulado) para entender qual mensagem é esperada.

**Como resolver**:

- Esse ajuste não está disponível para o cliente via sistema — a tela de cadastro do CT-e de Serviço é restrita ao perfil Transportador e não expõe exclusão/edição de número e série para esse cenário;
- A correção (ajuste da série do CT-e de Serviço conflitante) precisa ser feita pela equipe Lincros diretamente na base;
- Após o ajuste, reimporte o XML do CT-e afetado. Se a nota fiscal vinculada já estiver "Finalizada", será necessário reabri-la (botão "Reabrir" na tela de edição da nota) antes da reimportação.

**Como solicitar**: abra um chamado com o suporte Lincros informando:

- Número e série do CT-e de Serviço conflitante;
- Transportadora emissora;
- Print da mensagem de erro na importação.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
