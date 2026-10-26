---
id: "44392758019479"
titulo: "Lentidão ao gerar o PDF ou Envio por e-mail"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44392758019479-Lentid%C3%A3o-ao-gerar-o-PDF-ou-Envio-por-e-mail"
trilha: "Solução de Problemas > Erros Internos"
atualizado_em: "2026-10-20T18:33:17Z"
---

# Lentidão ao gerar o PDF ou Envio por e-mail

**Mensagem**

A geração do PDF da nota demora dezenas de segundos (por exemplo, de 30 a 50 segundos por nota), e o envio da nota e do boleto por e-mail também fica lento.

**Situação**

O sistema demora muito para responder ao salvar ou visualizar o PDF da nota no  **"Portal de Vendas"** , ao enviar a nota (NF-e ou NFS-e) ou o boleto por e-mail, no faturamento ou manualmente, e ao baixar o PDF da nota pela API.

Reiniciar o sistema não resolve. Em geral, a demora acontece só nas notas de uma mesma TOP ou de um mesmo tipo de documento, e as demais geram o PDF normalmente.

**Solução**

Esse comportamento está relacionado ao **modelo de impressão personalizado** configurado para o documento. Siga os passos abaixo para confirmar a causa e encaminhar a correção.

Na tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros), abra a TOP da nota que está demorando e anote o modelo de impressão informado. Para NFS-e, por exemplo, é o campo **"Mod. Imp. NFS-e"**.
 Na tela **"Modelos de Nota Fiscal/Duplicatas/Boleto(s)"** (Configurações » Avançado), localize esse modelo e anote o **"Número do relatório modelo"**. Abra esse relatório na tela **"Modelo de Impressão (Nota/Pedido)"**. Se ele não aparecer lá, use a tela **"Relatórios Formatados"** (Configurações » Avançado). É nesse relatório que fica o arquivo .jrxml. Veja se ele é personalizado, ou seja, se foi criado ou alterado pela sua empresa, por um consultor ou por um parceiro. No DANFE de NF-e, o relatório é o indicado no campo **"Relatório formatado do DANFE"**, nas Preferências da Empresa.
 Acesse a tela **"Monitor de Consultas"** (Configurações » Avançado) e clique em **"Iniciar monitoramento"**.
 Com o mesmo usuário e no mesmo navegador, sem sair do sistema, gere o PDF de uma nota lenta pelo **"Portal de Vendas"**. Depois volte ao monitor, clique em **"Parar monitoramento"** e em seguida em **"Baixar arquivos de Log"**.
 Abra o arquivo **Monitor\_Consulta.log**, que vem dentro do .zip baixado, e procure a consulta com o maior tempo. O tempo aparece no início de cada consulta, como **"tempo: 45000 (ms)"**. Lembre que 1.000 ms equivalem a 1 segundo. Logo abaixo aparecem o SELECT executado e, em  **Params**, o número único da nota. Se a consulta mais demorada for a do modelo, a causa está confirmada.
 Encaminhe o modelo e o arquivo de log para revisão de quem criou o modelo: consultor de implantação, TI da empresa ou parceiro. O Service Desk não faz alterações ou correções em modelos personalizados, mas continua à disposição para os recursos padrão do sistema.

**(7)** Depois da correção, repita o monitoramento com a mesma nota e compare o tempo da consulta.

**Causa**

O PDF é montado a partir de um modelo (arquivo .jrxml) que contém uma consulta ao banco de dados. O sistema guarda o modelo pronto na memória, mas executa essa consulta a cada PDF gerado, por isso reiniciar não resolve. **O mesmo modelo é usado no Portal de Vendas, no e-mail da nota, no e-mail do boleto e na API.** O e-mail do boleto leva o PDF da nota anexado. Por isso, se a consulta estiver pesada, todos esses pontos ficam lentos juntos. No faturamento de muitas notas, a demora de cada PDF se soma.
