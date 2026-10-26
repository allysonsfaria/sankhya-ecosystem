---
id: "44013071112599"
titulo: "[TMS] - Número do documento de cobrança deve ser maior que 0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013071112599--TMS-N%C3%BAmero-do-documento-de-cobran%C3%A7a-deve-ser-maior-que-0"
trilha: "Lincros > TMS > Importação EDI - TMS"
atualizado_em: "2026-10-05T19:47:16Z"
rotulos: ["sync_hc", "lincros", "sync_hash_d6b7661f659a", "lincros_13432976"]
---

# [TMS] - Número do documento de cobrança deve ser maior que 0

**Menu**: Operacional > Importação > EDI > Importação
**Objetivo:** Arquivo EDI com padrão DOCCOB (fatura) ao ser importado retorna erro 'Número do documento de cobrança deve ser maior que 0'

**Considerações:**         - Possuir um arquivo EDI no padrão DOCCOB;
 

Os arquivos EDI a ser importado para dentro do TMS apresentam erro na tela de log de importação do EDI:

![Imagem 1: Menu : Operacional > Importação > EDI > Importação Objetivo: Arquivo EDI com padrão DOCCOB (fatura) ao ser importado…](https://ajuda.sankhya.com.br/hc/article_attachments/44013091081239)

Essa mensagem de importação sempre irá aparecer quando no arquivo EDI o número da fatura não estiver informado! Para validação pode ser acessado o log da importação desse arquivo pelo caminho; Operacional > Importação > EDI > Log e ao localizar o log do arquivo em questão deve ser acessado o campo 'Conteúdo' e deve ser acessado a linha '4' e verificar se o campo 'Número do documento de cobrança' está com uma sequência de 0, conforme registro de tela abaixo:

![Imagem 2: Essa mensagem de importação sempre irá aparecer quando no arquivo EDI o número da fatura não estiver informado! Para…](https://ajuda.sankhya.com.br/hc/article_attachments/44013054607639)

Ao validar que a importação do EDI está com esse mesmo comportamento, deve ser reportada a transportadora para que a mesma posso corrigir informando no arquivo EDI o número da fatura.

**Obs**.: Link explicando mais sobre as informações obrigatórias e os layout padrões Proceda: [TMS] - Layouts dos arquivos padrões Proceda.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
