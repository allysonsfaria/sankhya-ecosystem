---
id: "44012664118423"
titulo: "[TMS] - Validações realizadas na importação de DOCCOB - Documento de Cobrança"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012664118423--TMS-Valida%C3%A7%C3%B5es-realizadas-na-importa%C3%A7%C3%A3o-de-DOCCOB-Documento-de-Cobran%C3%A7a"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:19Z"
rotulos: ["sync_hc", "lincros", "lincros_13433395", "sync_hash_93aad7db917b"]
---

# [TMS] - Validações realizadas na importação de DOCCOB - Documento de Cobrança

**Menu**: Operacional > Importação > EDI > Importação

**Objetivo**: Apresentar algumas validações realizadas na importação do arquivo DOCCOB - Documento de Cobrança

**Considerações**:

- O arquivo DOCCOB – Documento de Cobrança é gerada pelas Transportadoras para transmissão às empresas Clientes (Contratantes do frete ou Embarcadoras), visando fornecer uma cópia eletrônica da Nota Fiscal/Fatura de serviço emitida para a cobrança dos serviços de transporte de carga prestados à Embarcadora;
- Essa cobrança deverá seguir os critérios acordados entre as partes em relação ao período de cobrança (semanal, quinzenal, etc.) e em relação ao que cobrar ou não (entregas completas, parciais, etc.).
- O envio dessa mensagem é condicional, pois algumas Embarcadoras não exigem o seu envio/transmissão
- Possuir o arquivo 'DOCCOB' disponibilizado pela transportadora;
- O arquivo 'DOCCOB' deve estar dentro dos padrões Proceda;

O funcionamento do sistema para importação do DOCCOB faz as seguintes validações:

- Primeiramente no cadastro da transportadora disponível no menu: Cadastro Gerais > Transportadoras > Transportadora > Cadastro, o campo 'EDI Padrão' deve estar preenchido;
- O arquivo DOCCOB deve estar dentro dos padrões proceda (em anexo segue o manual com o layout);
- O sistema busca a fatura pelo número, série e empresa presentes no arquivo '.txt';
- Quando encontrado o sistema valida se deve ser usada a alçada de aprovação para validar a fatura;
- Depois de verificado se deve usar a alçada de aprovação o sistema passa para a próxima etapa, validando a situação da fatura;
- Se a fatura estiver aceita, paga ou rejeitada, o sistema não permite a alteração da fatura e encerra a importação com erro;
- Se a fatura estiver conferida, o sistema valida se a validação é a mesma de tela, caso sim, validará de acordo com as configurações de tela, do contrário, retorna falso e não permite alterar a fatura;
- Caso esteja em qualquer outra situação, o sistema permite alterar a fatura e continua a importação normalmente.

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
