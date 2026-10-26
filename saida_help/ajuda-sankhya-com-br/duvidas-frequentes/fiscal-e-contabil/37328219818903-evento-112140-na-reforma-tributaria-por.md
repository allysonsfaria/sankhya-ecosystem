---
id: "37328219818903"
titulo: "Evento 112140 na Reforma Tributária: Por que não aparece no Sankhya e como habilitar corretamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37328219818903-Evento-112140-na-Reforma-Tribut%C3%A1ria-Por-que-n%C3%A3o-aparece-no-Sankhya-e-como-habilitar-corretamente"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-27T13:25:47Z"
rotulos: ["Configuração", "Eventos", "NF-e", "SEFAZ", "TOP", "Reforma Tributária", "Evento 112140", "Fornecimento não realizado com pagamento", "112110 e 112130", "Nota Técnica 2025.002", "112110 – Pagamento Integral", "112130 – Perecimento Perda Roubo ou Furto", "comunicar ao fisco", "Nota de Débito por Pagamento Antecipado", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Evento 112140 na Reforma Tributária: Por que não aparece no Sankhya e como habilitar corretamente

Os eventos da Reforma Tributária são mecanismos de comunicação com a Receita Federal (RFB) e o Comitê Gestor, essenciais para a correta apuração dos novos tributos **(IBS e CBS)** e para a manutenção do direito ao crédito fiscal. No Sankhya, esses eventos devem ser registrados pelo **emitente** ou pelo **destinatário** da NF-e, conforme a ocorrência de um fato específico posterior à emissão do documento fiscal.

Atualmente, o sistema disponibiliza diversos eventos para atender às exigências da **Nota Técnica NT2025.002**, sendo que cada evento possui finalidade específica e deve ser enviado manualmente quando a situação fiscal correspondente ocorrer.

### Eventos disponíveis para o emitente

O emitente da NF-e possui acesso aos eventos através do **"Portal de Vendas"** (Comercial >> Portal de Vendas >> NF-e >> Eventos de NF-e). Os principais eventos disponíveis são:

**• Evento 112110 - Informação de Efetivo Pagamento Integral:** permite ao fornecedor informar o efetivo pagamento integral da operação para liberar o crédito presumido do adquirente. Este evento aplica-se à nota completa e não permite edição de quantidade ou unidade.
**• Evento 112130 - Perecimento, Perda, Roubo ou Furto:** permite ao fornecedor informar quando um bem for objeto de roubo, perda, furto ou perecimento antes da entrega, durante o transporte contratado pelo fornecedor. Este evento permite edição de quantidade e unidade dos itens afetados.
**• Evento 112140 - Fornecimento Não Realizado com Pagamento Antecipado:** este evento tem como finalidade comunicar ao fisco a quantidade de mercadorias não entregues e os valores de impostos (IBS/CBS) correspondentes à parte não fornecida da operação.

### Configuração do evento 112140

É importante esclarecer que o evento **112140** não é habilitado por configurações de alíquotas ou impostos. Ajustes em IBS, CBS ou regras fiscais não fazem o evento aparecer. O critério para disponibilização do evento está diretamente relacionado à natureza da nota fiscal original. Para que o evento fique disponível, a operação original precisa ter sido emitida como uma Nota de Débito específica para Pagamento Antecipado na tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP):

**(1)** Na aba **"NF-e / NFC-e / CF-e"**, configure:

• Campo **"NF-e"**: Selecione **"Nota de Débito"**.
• Campo **"Tipo de Nota Fiscal de Débito"**: Selecione **"Pagamento antecipado"**.

![Imagem 1: (1) Na aba "NF-e / NFC-e / CF-e" , configure: • Campo "NF-e" : Selecione "Nota de Débito" . • Campo "Tipo de Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/37370532070167)

**(2)** Na aba **"Geral"**, certifique-se de que as opções **"A nota fica como pendente"** e **"Copiar liberações quanto faturado"** estejam marcadas.

![Imagem 2: (1) Na aba "NF-e / NFC-e / CF-e" , configure: • Campo "NF-e" : Selecione "Nota de Débito" . • Campo "Tipo de Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/37370532070551)

**(3)** Na aba **"Livro Fiscal"**: No campo **"Atualização de Livro ICMS"**, selecione **"Livro de Saída"** e em **"Atualização do livro de ISS"**, selecione **"Não atualiza"**.

![Imagem 3: (1) Na aba "NF-e / NFC-e / CF-e" , configure: • Campo "NF-e" : Selecione "Nota de Débito" . • Campo "Tipo de Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/37398480484503)

**(4)** Na aba **"Impostos"**, no campo **"Cálculo de ICMS, IPI, ISS, IBS, CBS"**, marque a opção **"Não calcula e não digita"**.

![Imagem 4: (4) Na aba "Impostos" , no campo "Cálculo de ICMS, IPI, ISS, IBS, CBS" , marque a opção "Não calcula e não digita" .](https://ajuda.sankhya.com.br/hc/article_attachments/37398480492439)

### Eventos disponíveis para o destinatário

O destinatário da NF-e possui acesso aos eventos através do **"Portal de Compras"** (Comercial >> Portal de Compras >> NF-e >> Eventos Reforma). Os eventos disponíveis incluem:

• 211110: Solicitação de Apropriação de crédito presumido
• 211120: Destinação de item para consumo pessoal
• 211124: Perecimento, perda, roubo ou furto durante transporte
• 211128: Aceite de débito na apuração por emissão de nota de crédito
• 211130: Imobilização de Item
• 211140: Solicitação de Apropriação de Crédito de Combustível

### Dinâmica de envio dos eventos

A emissão dos eventos não é automática. O fluxo de envio é:
**(1)** Identifique a necessidade do evento conforme a situação fiscal.

**(2)** Acesse o **"Portal de Vendas"** ou **"Portal de Compras"**.

**(3)** Selecione a nota fiscal desejada.

**(4)** Clique no botão **"NF-e"** e escolha a opção **"Eventos de NF-e"**.

**(5)** Escolha o evento, selecione os itens via **"Checkbox"**, ajuste quantidades/unidades quando permitido e confirme o envio.

![Imagem 5: A emissão dos eventos não é automática. O fluxo de envio é: (1) Identifique a necessidade do evento conforme a situação…](https://ajuda.sankhya.com.br/hc/article_attachments/43036368707863)

### Características importantes dos eventos

• **Rastreabilidade:** Cada evento gera um protocolo único e pode ser cancelado individualmente.
• **Edição de quantidade:** Para a maioria dos eventos, é possível editar a quantidade e unidade do item. Alguns, como 112110 e 211128, aplicam-se à nota completa.
• **Impacto Fiscal:** Essencial para liberação de crédito presumido, controle de prazos, cálculo de créditos de bens do ativo e conformidade com a Lei Complementar 214/2025.

Na documentação atual do **Portal de Vendas**, os eventos listados são:

- **112110 — Pagamento Integral**
- **112120 — Importação em ALC/ZFM não convertida em isenção**
- **112130 — Perecimento, Perda, Roubo ou Furto**
- **112150 — Atualização da Data de Previsão de Entrega**

E o **112140 não aparece como evento genérico disponível para qualquer NF-e**: ele depende justamente da condição específica da Nota de Débito por Pagamento Antecipado

**ATENÇÃO:** Somente notas emitidas com uma **"TOP"** configurada exatamente conforme o procedimento descrito permitirão a geração posterior do evento 112140.
