---
id: "42427234900759"
titulo: "I05 - Como cadastrar ou atualizar escalas em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427234900759-I05-Como-cadastrar-ou-atualizar-escalas-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:05Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a33285626811e03efe0995a", "sync_hash_e870258be587"]
---

# I05 - Como cadastrar ou atualizar escalas em massa

A ferramenta de importação em lote da Pontotel permite cadastrar várias escalas de trabalho de uma só vez, facilitando a gestão em empresas com grande volume de funcionários e escalas. O processo é feito por meio do Importador i05, que utiliza uma planilha modelo para realizar os lançamentos de forma rápida, segura e padronizada.

---

> ⚠️Aviso: Este importador não é aplicável caso sua empresa possua integração de cadastros ativa com outros sistemas, como Sankhya ou similares.

---

## Como baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Escalas de Trabalho.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Escalas de Trabalho.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1umnrge.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

---

## Como preencher a planilha modelo

![Imagem 3: Como preencher a planilha modelo](https://storage.crisp.chat/users/helpdesk/website/-/8/d/c/d/8dcdaae1a9d6a800/83bac443-cd10-4979-b033-753ec3_19qev2z.png)

1. Preencha as colunas corretamente:
   - Nome: Nome único para identificar a escala no sistema.
   - Esquema (Dias Trabalho): Informe o número de dias consecutivos de trabalho no ciclo da escala.
   - Deve ser preenchido com um número inteiro, por exemplo: 5.
   - Esquema (Dias Folga): Informe o número de dias consecutivos de folga no ciclo da escala. Também deve ser preenchido com um número inteiro.
   - Jornada primeiro dia da escala: Nome da jornada a ser aplicada no primeiro dia do ciclo de trabalho da escala. O nome deve corresponder exatamente a uma jornada já cadastrada no sistema.
   - Jornada segundo dia da escala: Mesmo princípio da coluna anterior, mas agora sendo a jornada para o segundo dia da escala.

> 🚨Importante:

- Caso esteja cadastrando uma escala que possua mais de dois dias em seu ciclo (como 5 dias de trabalho e 2 de folga, por exemplo), é necessário preencher as colunas opcionais com o nome das jornadas correspondentes a cada dia. Assim, a escala será montada corretamente para todo o período desejado.
- Existem outras colunas opcionais que preenchem campos específicos da escala. Consulte a linha 2 da planilha para entender como preenchê-las corretamente caso haja necessidade.

2. Depois de preencher a planilha, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.

---

## Como fazer o upload da planilha preenchida

1. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 4: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
2. Finalize clicando em **importar.**

   ![Imagem 5: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
3. Aguarde o processo de importação da planilha ser finalizado.
4. Quando o processo for concluído, será gerado um relatório com o feedback da importação. Certifique-se de que o usuário foi criado, atualizado ou desativado.

---

## 🆕 Novidade: limpeza de campos opcionais via importador I05

O importador I05 agora permite **remover informações opcionais já cadastradas** diretamente pela planilha, sem precisar de ajuste manual na plataforma.
Para isso, basta utilizar a palavra reservada **`<APAGAR>`** na célula correspondente ao campo que deseja limpar, dentro da aba **Atualizar** da planilha.
**Como funciona:**

- **Célula em branco:** o sistema interpreta como "não alterar". O valor existente é mantido.
- **`<APAGAR>` em campo opcional:** o sistema remove o valor cadastrado naquele campo.
- **`<APAGAR>` em campo obrigatório:** a importação retorna uma mensagem de erro. Campos obrigatórios não podem ser apagados.

> 💡 Dica: essa funcionalidade está disponível apenas na aba Atualizar da planilha do I05. Utilize com atenção para não remover informações de forma não intencional.

---

A importação em lote de escalas é a forma mais eficiente de criar rotinas de trabalho para grandes equipes, economizando tempo e reduzindo riscos de erro manual.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
