---
id: "41329606659991"
titulo: "PIX Imediato e Checkout (PDV)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:35:16Z"
rotulos: ["Configuração", "PDV", "Financeiro", "Sankhya Checkout", "PIX", "Fintech"]
---

# PIX Imediato e Checkout (PDV)

## Sumário

1. [Descrição da Funcionalidade](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GT74T85D5MWBFS2HT2G)
2. [Pré-requisitos](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GTB3MH2GC1Y0AGP8N50)
3. [Diagrama de Fluxo](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GTGT5WXAF8WVRV0E0WJ)
4. [Jornada de Uso e Configuração](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GTJ1FEX9E0KPF0EYZT5)
5. [Geração e Recebimento do PIX](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GV4KDSBXYHE2S36Q590)
6. [Pontos de Atenção e Sincronização (Checkout)](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GV8C3T24672DPNCBZG9)
7. [Casos de Uso e Solução de Problemas](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GVA9H1W68VAWKMYMPAP)
8. [FAQ – Dúvidas Frequentes](https://sankhya.zendesk.com/knowledge/editor/01KVDZX1AS7QKJ8RP5QW9QPJP0/pt-br?brand_id=360003747033&section_id=31230176583063#h_01KVDZ6GVGX1WFH3VDGWNCT20P)

## [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GT74T85D5MWBFS2HT2G)

O **PIX Imediato** é uma solução **Sankhya Fintech** que permite gerar um QR Code de forma instantânea para recebimentos. No ambiente de varejo, a solução foi desenhada para que tanto o **PDVWeb** quanto o **Sankhya Checkout** se comuniquem diretamente com a API de PIX da Fintech para geração de QR-Code, garantindo a continuidade dos recebimentos após a desativação de APIs legadas (como a V1 do Banco do Brasil).

- **Propósito:** Agilizar o processo de venda no balcão e PDV, gerando dinamicamente o QR Code e garantindo a liquidação automática do título.
- **Valor para o Usuário:** Automação e rapidez no caixa, eliminação de erros manuais de digitação e conciliação instantânea.

## [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GTB3MH2GC1Y0AGP8N50)

Para utilizar o PIX Imediato no Checkout, certifique-se de cumprir os seguintes requisitos:

- **Contratação:** Pacote Básico de serviços Fintech ativo (Pacote Boleto Rápido).
- **Versão ERP:** 4.35b226 ou superior.
- **Versão BFF Financeiro:** 1.20.1 ou superior.
- **Bancos Ativos:** Banco do Brasil, Itaú, Santander ou SICOOB.
- **Permissões:** Sankhya ID ativo e acesso liberado às telas de Contas e Assistente de Melhores Práticas.

## [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GTGT5WXAF8WVRV0E0WJ)

![Imagem 1: 3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/41329606653463)

## [4. Jornada de Uso e Configuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GTJ1FEX9E0KPF0EYZT5)

### Parametrização e Sincronização para o Checkout (PDV)

Para que o PIX fique disponível como forma de pagamento nas frentes de caixa (Checkout), realize os passos a seguir:

1. **Ativação da Conta:** Acesse o cadastro de **Contas** no ERP. Na aba **PIX**, certifique-se de que a opção **"Utiliza PIX PDV"** está marcada para a conta cadastrada na Fintech.
2. **Limpeza de Dados Antigos:**

   > 💡 **OBSERVAÇÃO IMPORTANTE:** Caso a opção já esteja marcada, a parametrização estrutural está correta. Contudo, sugere-se fortemente **limpar e apagar as informações do antigo PIX** (como URLs e Chaves antigas salvas diretamente), garantindo que o cliente tenha guardado esses dados em outro local antes. Isso evita conflitos com os novos parâmetros da Fintech.
3. **Forçar Sincronização:** Estando tudo certo na retaguarda, o sistema irá sincronizar com o checkout. É **fundamental FORÇAR a sincronização inicial** de duas frentes nessa primeira parte:

   - **Da Empresa:** Pois ela estará associada diretamente à conta bancária do usuário.
   - **Da Fintech:** Essencial para puxar e validar os dados corretos do cliente.
4. **Reinicialização do Sistema (Caches):** O Checkout é um produto que opera com banco de dados local (offline), guardando muitos caches para manter a operação rápida.

   - **Ação obrigatória:** Após finalizar todo o processo de parametrização e sincronismo no ERP, **feche o aplicativo do Checkout por completo e abra-o novamente**. Esse procedimento força a limpeza de cache e garante a carga correta da API da Fintech no PDV.

### [GIF animado: Imagem 2: Ação obrigatória: Após finalizar todo o processo de parametrização e sincronismo no ERP, feche o aplicativo do Checkout…](https://ajuda.sankhya.com.br/hc/article_attachments/42312179484567)

Comportamento do sistema quando o pagamento **ainda não foi** processado pelo banco.

### [GIF animado: Imagem 3: Comportamento do sistema quando o pagamento ainda não foi processado pelo banco.](https://ajuda.sankhya.com.br/hc/article_attachments/42312192494743)

Consulta técnica do banco de dados local do Checkout (tabela `tfintech`) validando se os **parâmetros enviados** pelo ERP via API foram gravados corretamente no terminal.

### [GIF animado: Imagem 4: Consulta técnica do banco de dados local do Checkout (tabela tfintech ) validando se os parâmetros enviados pelo ERP…](https://ajuda.sankhya.com.br/hc/article_attachments/42312192495127)

Cenário real de estresse e contingência do operador no PDV offline diante de **instabilidades de rede** (timeouts de comunicação com a API).

## [5. Geração e Recebimento do PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GV4KDSBXYHE2S36Q590)

### No Caixa (Sankhya Checkout):

1. Inicie a venda e lance os produtos no carrinho normalmente.
2. Ao avançar para a tela de **Pagamento**, selecione a opção **[F9] PIX**.
3. O sistema fará a requisição à API da Fintech e abrirá o pop-up **"Pagamento PIX"** contendo o QR Code impresso em tela e a opção de cópia eletrônica.
4. Oriente o cliente a escanear o QR Code exibido.
5. Após o cliente confirmar o pagamento no aplicativo bancário dele, clique no botão **"Verificar pagamento"** para prosseguir.
6. O sistema validará a transação junto à Fintech, fechará o pop-up e avançará para o fechamento e emissão do documento fiscal correspondente (NFC-e / SAT).

## [6. Pontos de Atenção e Sincronização (Checkout)](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GV8C3T24672DPNCBZG9)

- **Comportamento Offline e Cache:** Mudanças feitas no ERP não entram em vigor em caixas abertos. Sempre que houver manutenção de contas, force a sincronização e reinicie o executável do PDV.
- **Validação de Dados Bancários:** O sistema não valida se a agência ou a chave PIX estão corretas junto ao banco no momento do cadastro no ERP. Qualquer caractere incorreto impossibilitará a geração do QR Code no caixa.

## [7. Casos de Uso e Solução de Problemas](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GVA9H1W68VAWKMYMPAP)

### ✅ Cenário 1: Fluxo de Sucesso com Verificação

O operador aciona a forma de pagamento PIX, o QR Code é gerado perfeitamente na tela. O comprador realiza a leitura, o operador clica em "Verificar Pagamento", a transação é liquidada instantaneamente e a NFC-e é emitida com sucesso.

### ❌ Cenário 2: Verificação antecipada (Pagamento não confirmado)

Caso o botão de checagem seja acionado antes da transação ser concluída pelo cliente na instituição bancária, o sistema apresentará a seguinte mensagem de validação:

> `Erro: Pagamento ainda não confirmado. Tente novamente em alguns instantes!`

- **Ação do Operador:** Pressione OK (F12), aguarde o cliente finalizar a transação no celular e clique novamente em "Verificar pagamento".

### ❌ Cenário 3: Tempo limite excedido (Timeout da API)

Instabilidades ou falhas temporárias na rede de internet podem fazer com que o sistema demore a responder e estoure o tempo limite de comunicação.

- **Sintomas:** Exibição de caixas de diálogo contendo alertas como `Tempo limite excedido para buscar dados. Verifique sua conexão` ou erros do tipo `java.util.concurrent.CancellationException`.
- **Ação do Operador:** Verifique se o terminal não perdeu a conexão com a internet. Se a rede estiver estável, feche a janela do PIX que apresentou a falha de comunicação, volte para a tela de formas de pagamento e pressione **[F9] PIX** novamente para forçar uma nova requisição limpa para a API da Fintech.

## [FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41329606659991-PIX-Imediato-e-Checkout-PDV#h_01KVDZ6GVGX1WFH3VDGWNCT20P)

- **O que muda no Checkout com a desativação da API V1 do Banco do Brasil?**

Os clientes não conseguirão mais gerar QR Codes diretamente pelas requisições antigas. A partir desta atualização, as jornadas de varejo no Checkout e no PDVWeb passam a se comunicar de forma transparente com a API unificada da Fintech Sankhya.

- **Cadastrei tudo no ERP mas a opção PIX não aparece ou dá erro de conta no Checkout. O que pode ser?**

Verifique se a flag "Utiliza PIX PDV" foi devidamente marcada no cadastro de contas do ERP, force a sincronização dos dados da "Empresa" e da "Fintech" e certifique-se de que fechou e abriu o aplicativo do Checkout novamente para que as atualizações saiam do cache local.

- **O cliente pagou, mas o caixa travou com erro de Timeout da API. Como proceder?**

Se o cliente teve o valor debitado da conta e o caixa não avançou devido a um timeout na rede **(Cenário 3)**, tente fechar e abrir a requisição. Se a conexão geral de internet caiu, acione a supervisão do estabelecimento para registrar o recebimento na modalidade adequada de contingência e efetuar a posterior conciliação manual no ERP.
