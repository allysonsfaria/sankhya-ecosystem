---
id: "39368098565399"
titulo: "Desconto de bloqueio judicial não aplicado na competência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39368098565399-Desconto-de-bloqueio-judicial-n%C3%A3o-aplicado-na-compet%C3%AAncia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:10Z"
rotulos: ["Folha", "Lançamento de Movimento", "Configuração Funcionários", "Pessoal+", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Desconto de bloqueio judicial não aplicado na competência

**MENSAGEM**

O desconto de bloqueio judicial não foi aplicado no cálculo da folha mensal para a matrícula do funcionário.

**SITUAÇÃO**

Ao calcular a folha mensal de um funcionário, o sistema não considerou o desconto referente ao bloqueio judicial, mesmo havendo um lançamento mensal ativo configurado em parcelas. A competência específica foi desconsiderada na sequência de descontos, resultando na ausência do valor.

**SOLUÇÃO**

Para corrigir a ausência do desconto de bloqueio judicial na competência, siga os passos abaixo:

**(1)**Acesse a tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e verifique se existe o lançamento da parcela correspondente à competência em questão para o funcionário.

![Imagem 1: Caso identifique que a parcela está ausente, acesse a aba: Lançamento, ainda na tela: ''Lançamento de movimento'' (…](https://ajuda.sankhya.com.br/hc/article_attachments/41273578943639)

**(2)**Caso identifique que a parcela está ausente, acesse a aba: Lançamento, ainda na tela: ''Lançamento de movimento'' (Pessoal+ » Rotinas Folha » Lançamento de Movimento) na competência desejada e efetue o lançamento da parcela devida (para esta ação, é necessário que o cálculo mensal esteja descartado para o respectivo funcionário). 

![Imagem 2: Realize a importação do lançamento na competência desejada, informando os dados do evento de bloqueio judicial (valor…](https://ajuda.sankhya.com.br/hc/article_attachments/41273558328471)

**(3)**Realize a importação do lançamento na competência desejada, informando os dados do evento de bloqueio judicial (valor da parcela, número da parcela e matrícula do funcionário). Conforme evidenciado acima. 

**(4)** Valide se o lançamento foi inserido corretamente para a competência e salve.

**(5)** Execute novamente o **"Cálculo da Folha Mensal"** para o funcionário e confirme se o desconto de bloqueio judicial foi aplicado com sucesso.

**CAUSA**

O problema ocorre quando o lançamento mensal de uma parcela específica não é registrado no sistema. Como o evento de bloqueio judicial foi configurado como movimento mensal em parcelas, cada competência requer um lançamento individual. Se uma competência não receber o lançamento correspondente, o sistema não consegue identificar o desconto a ser aplicado, fazendo com que aquela parcela seja pulada na sequência de descontos. Isso pode acontecer por esquecimento no processo manual de lançamento das parcelas ou por falha na importação automática dos movimentos mensais.

**Em casos de movimento fixo, para que ocorra o lançamento para competência posterior a atual precisará estar fechada afim de que o evento seja levado ao cálculo.**
