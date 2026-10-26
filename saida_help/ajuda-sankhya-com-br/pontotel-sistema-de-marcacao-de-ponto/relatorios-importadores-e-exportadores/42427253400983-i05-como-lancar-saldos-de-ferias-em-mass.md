---
id: "42427253400983"
titulo: "I05 - Como lançar saldos de férias em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427253400983-I05-Como-lan%C3%A7ar-saldos-de-f%C3%A9rias-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:04Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_8e1519a249d3", "pontotel_6a332855282f16165a2cb964"]
---

# I05 - Como lançar saldos de férias em massa

O importador I05 permite que você cadastre ou atualize os saldos de férias de múltiplos colaboradores de uma só vez, sem precisar acessar um cadastro por vez na plataforma. Para isso, basta preencher a planilha modelo com as informações de cada colaborador e realizar o upload no sistema.

---

## Como acessar o importador e baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Saldo de férias.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Saldo de férias.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_x7ivr1.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

---

## Entendendo a planilha modelo

![Imagem 3: Entendendo a planilha modelo](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_7zxle6.png)

A planilha possui uma aba chamada **Saldo de Férias**, com quatro colunas:

| Coluna | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **PIN empregado** | Obrigatório | PIN de registro de ponto do colaborador, utilizado para identificação no sistema. Pode ser encontrado no cadastro do empregado. |
| **Dia e mês de início do período aquisitivo (dd/mm)** | Obrigatório | Data de início do período aquisitivo referente ao saldo que está sendo lançado. |
| **Saldo período concessivo atual** | Obrigatório | Dias de férias remanescentes no período concessivo em curso. |
| **Saldo período aquisitivo atual** | Opcional | Dias de férias remanescentes do período aquisitivo em curso (período concessivo ainda não iniciado). Se deixado em branco, o sistema calcula automaticamente o valor proporcional aos dias decorridos desde o início do período aquisitivo. |

> 💡 **Dica:** o campo "**Saldo período aquisitivo atual"** pode ser deixado em branco quando você não souber o valor exato. O sistema calculará automaticamente com base na proporcionalidade do período.

---

## Como fazer o upload da planilha preenchida

1. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 4: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
2. Finalize clicando em **importar.**

   ![Imagem 5: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
3. Aguarde o processo de importação da planilha ser finalizado.
4. Quando o processo for concluído, será gerado um relatório com o feedback da importação. Certifique-se de que o usuário foi criado, atualizado ou desativado.

Seguindo todos os passos, asseguramos que o sistema reflita de forma precisa os saldos de férias da equipe, mantendo a gestão de férias transparente e confiável.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
