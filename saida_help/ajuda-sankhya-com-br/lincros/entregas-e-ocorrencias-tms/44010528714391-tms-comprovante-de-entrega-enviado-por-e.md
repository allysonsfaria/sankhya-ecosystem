---
id: "44010528714391"
titulo: "[TMS] - Comprovante de Entrega Enviado por E-mail Não Vincula à Ocorrência (Erro no Nome do Arquivo)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010528714391--TMS-Comprovante-de-Entrega-Enviado-por-E-mail-N%C3%A3o-Vincula-%C3%A0-Ocorr%C3%AAncia-Erro-no-Nome-do-Arquivo"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T18:40:42Z"
rotulos: ["sync_hc", "lincros", "lincros_16540468", "sync_hash_f8a42f823774"]
---

# [TMS] - Comprovante de Entrega Enviado por E-mail Não Vincula à Ocorrência (Erro no Nome do Arquivo)

## 1 - Problema Relatado pelo Cliente

O cliente enviou o comprovante de entrega (canhoto) por e-mail para o endereço de importação configurado, mas o arquivo não apareceu vinculado à respectiva Nota Fiscal na tela de Rastreamento, mesmo com a ocorrência de entrega (código 01) já lançada corretamente no sistema.

---

## 2 - Causa do Problema

O sistema identifica a qual Nota Fiscal e a qual ocorrência um comprovante enviado por e-mail pertence **através do nome do arquivo**, que deve seguir um layout de posições fixas, separado por "\_":

**00000000\_000\_00000000000000\_00\_DDMMYYYY\_HHMM\_nome\_anexo**

| Segmento | Campo | Usado para |
| --- | --- | --- |
| 00000000 | Número NF-e | Localizar a nota fiscal no sistema (junto com Série e CNPJ Emitente) |
| 000 | Série NF-e | Localizar a nota fiscal no sistema |
| 00000000000000 | CNPJ Emitente da NF-e | Localizar a nota fiscal no sistema |
| 00 | Código da Ocorrência | Identificar o tipo de evento (ex: 01 = Entregue) |
| DDMMYYYY | Data da Ocorrência | Localizar a ocorrência específica já lançada nessa NF |
| HHMM | Hora da Ocorrência | Localizar a ocorrência específica já lançada nessa NF |
| nome\_anexo | Texto livre | Apenas identificação do arquivo, não é usado na busca |

Se qualquer um dos campos estruturados (Número, Série, CNPJ Emitente, Código de Ocorrência, Data ou Hora) estiver **incorreto ou não corresponder exatamente aos dados já registrados no sistema**, o vínculo automático falha silenciosamente — o e-mail é recebido, mas o anexo não é associado a nenhuma ocorrência, e não é gerado um erro visível para o cliente.

**Caso confirmado:** em um atendimento, o nome do arquivo estava correto em todos os campos, exceto o de **hora**, que veio como "0000" enquanto a ocorrência real havia sido registrada às "18:00". Essa divergência foi suficiente para impedir o vínculo automático do comprovante.

---

## 3 - Passo a Passo para Resolver o Problema

1. **Confirmar os dados da ocorrência já lançada**

   - Acesse Operacional > Documentos de Despacho > Notas Fiscais, localize a NF e verifique na aba **Ocorrências** o número, série, CNPJ emitente, código e o horário exato do evento registrado.
2. **Conferir o nome do arquivo enviado por e-mail**

   - Compare cada campo do nome do arquivo com os dados reais da NF/ocorrência (tabela acima), com atenção especial a Número/Série/CNPJ (que localizam a nota) e Data/Hora (que localizam o evento certo).
3. **Corrigir e reenviar, se necessário**

   - Ajuste o campo divergente no nome do arquivo e oriente o cliente a reenviar o e-mail.
4. **Vínculo manual (se o reenvio não for possível de imediato)**

   - Acesse Entregas e Ocorrências > Acompanhamento de Entregas, localize a NF/ocorrência e utilize a opção **"Validar comprovante"** ou o diálogo de **Anexo à Ocorrência** para vincular manualmente o arquivo já recebido.

---

## 4 - Resumo do Artigo

Comprovantes de entrega enviados por e-mail são vinculados automaticamente à ocorrência com base no nome do arquivo, que deve seguir o padrão NúmeroNF\_Série\_CNPJEmitente\_CódOcorrência\_DDMMYYYY\_HHMM\_texto. Todos os campos estruturados do nome (Número, Série, CNPJ Emitente, Código de Ocorrência, Data e Hora) precisam corresponder exatamente aos dados já registrados no sistema — qualquer divergência em qualquer um deles impede o vínculo automático do comprovante à ocorrência correspondente, sem gerar erro visível ao cliente.
