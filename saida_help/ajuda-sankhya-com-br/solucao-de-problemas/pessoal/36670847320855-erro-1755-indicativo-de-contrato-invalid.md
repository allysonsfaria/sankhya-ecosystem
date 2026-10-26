---
id: "36670847320855"
titulo: "Erro 1755 - Indicativo de Contrato inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36670847320855-Erro-1755-Indicativo-de-Contrato-inv%C3%A1lido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T19:53:30Z"
rotulos: ["Configuração", "eSocial", "Processo Trabalhista", "Central do eSocial", "Erro", "Indicativo de Contrato inválido", "Há responsabilidade indireta?", "evento S-2500", "Erro 1755", "Processe Trabalhista"]
---

# Erro 1755 - Indicativo de Contrato inválido

**MENSAGEM:**

Erro 1755 - Indicativo de Contrato inválido. Ação sugerida: Quando a Identificação do Contribuinte Responsável Direto for informada, o Indicativo de Contrato deve ser igual a 'N'. 

Elemento: /eSocial/evtProcTrab/ideTrab/infoContr/indContr [S]

**SITUAÇÃO:**

Mensagem de erro apresentada ao tentar realizar o envio do evento S-2500 pela Central do eSocial.

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Processo Trabalhista''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/11592868813719-Processo-Trabalhista) (Pessoal+ » Rotinas Folha » Processo Trabalhista).

**(2)** No campo **''Declarante'',** verifique se a opção **“Há responsabilidade indireta?”** está desativada.

- Se este campo estiver marcado, o erro 1755 será apresentado.

![Imagem 1: Se este campo estiver marcado, o erro 1755 será apresentado.](https://ajuda.sankhya.com.br/hc/article_attachments/36689909916695)

**(3)** Ajuste o campo conforme indicado e **exclua o processo**.

**(4)** Cadastre o processo novamente para que a alteração seja validada.

**CAUSA:**

O erro ocorre porque o campo “Há responsabilidade indireta”  está marcado.

Quando marcado, o sistema entende que deve gerar o evento **S-2500 – Responsabilidade Indireta**, que é utilizado apenas quando há **determinação judicial** **para pagamento por parte de um responsável indireto** (subsidiário ou solidário).
