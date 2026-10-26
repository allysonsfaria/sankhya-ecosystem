---
id: "44013518955287"
titulo: "TMS - Configuração para envio dos anexos no e-mail de ordem de coleta ao transportador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013518955287-TMS-Configura%C3%A7%C3%A3o-para-envio-dos-anexos-no-e-mail-de-ordem-de-coleta-ao-transportador"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T20:00:14Z"
rotulos: ["sync_hc", "lincros", "lincros_13432061", "sync_hash_a552998093c8"]
---

# TMS - Configuração para envio dos anexos no e-mail de ordem de coleta ao transportador

## 1 - Problema Relatado pelo Cliente

Cliente gostaria que o e-mail da ordem de coleta, que é encaminhado do TMS para o transportador quando é clicado no botão "Enviar" dentro da ordem de coleta, ou quando a ordem de coleta é criada automaticamente por agendamento, seja enviado à transportadora contendo alguns documentos em anexo, como as DANFE das NF-e da Coleta, XML das NF-e, arquivo NOTFIS etc.

---

## 2 - Passo a Passo para Resolver o Problema

1º Acesse a tela de edição de cadastro de transportadora através do caminho: Cadastros gerais > Transportadoras > Transportadora (empresa) > Cadastro e procure por uma transportadora desejada, exemplo:

![Imagem 1: 1º Acesse a tela de edição de cadastro de transportadora através do caminho: Cadastros gerais > Transportadoras >…](https://ajuda.sankhya.com.br/hc/article_attachments/44013529436055)

2º Ao localizar a transportadora desejada, clique em seu "Código" e navegue até o final da página, na aba chamada "Configuração dos anexos da ordem de coleta", você vai se deparar com esta tela, conforme exemplo abaixo:

![Imagem 2: 2º Ao localizar a transportadora desejada, clique em seu "Código" e navegue até o final da página, na aba chamada…](https://ajuda.sankhya.com.br/hc/article_attachments/44013550065431)

Essa aba, registrar toda as possibilidades de arquivos que você pode encaminhar no e-mail de ordem de coleta, vou explicar oque cada um deles realiza:

1. **Relatório Espelho ordem de coleta:**Encaminha como anexo no E-mail o espelho da ordem de coleta.
2. **NOTFIS:**Encaminha como anexo o arquivo EDI NOTFIS, o padrão que o TMS usa é o 3.0, mas podemos ajustar para o 5.0.
3. **Relatório Espelho de pré-conhecimento:**Encaminha como anexo o espelho do pré-conhecimento.
4. **Relatório agendamento de notas não entregues:**Encaminha como anexo no E-mail um relatório com NF-es que possuem um agendamento de entrega mas não foram entregues ainda.
5. **Notas fiscais:**Encaminha como anexo no E-mail um arquivo ZIP com todos os XMLs de NF-es caso houver XML.
6. **Relatório Minuta de despacho (somente com o módulo Portaria):**Encaminha como anexo no E-mail um relatório contendo a minuta de despacho, funciona apenas com o módulo pátio e portaria do TMS contrato.
7. **Danfe**: Encaminha como anexo no E-mail um arquivo ZIP com as DANFEs das NF-es vinculadas a ordem de coleta, necessário ativar o parâmetro: enviarEspelhoDANFeOrdemColeta, essa parametrização é ativada apenas pelo time de suporte.
8. **Arquivos anexados:** Encaminha como anexo no E-mail todos os arquivos contidos no campo "Anexos" do TMS, a seguir eu mostro onde esse campo fica dentro da ordem de coleta:
9. ![Imagem 3: Arquivos anexados: Encaminha como anexo no E-mail todos os arquivos contidos no campo "Anexos" do TMS, a seguir eu…](https://ajuda.sankhya.com.br/hc/article_attachments/44013529626519)

3º Ao finalizar as suas escolhas do que deseja encaminhar no e-mail de ordem de coleta, clique em "Salvar" na tela de edição do cadastro de transportadora. Agora, toda vez que uma ordem de coleta for enviada ao transportador seja pelo botão "Enviar" dentro da ordem de coleta e ou quando a ordem de coleta é criada automaticamente, os anexos será encaminhados de acordo com as flags marcadas acima.
