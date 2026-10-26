---
id: "42427269470871"
titulo: "I05 - Como criar ou atualizar empregadores em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427269470871-I05-Como-criar-ou-atualizar-empregadores-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:08Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a332857bd5fd861ad9390a1", "sync_hash_f09f9c0fcf77"]
---

# I05 - Como criar ou atualizar empregadores em massa

Sabemos que cadastrar empregadores pode ser uma tarefa que exige tempo, principalmente quando se tem muitos deles para adicionar. Pensando nisso, preparamos este tutorial para você aprender como usar a nossa ferramenta de importação de arquivos em lote, agilizando o processo e garantindo que tudo fique registrado de forma rápida e eficiente. Assim, você evita o trabalho de preencher um a um, e consegue focar no que realmente importa: a gestão das suas equipes!

---

> ⚠️Aviso: Este importador não é aplicável caso sua empresa possua integração de cadastros ativa com outros sistemas, como Sankhya ou similares.

---

## Como baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Empregadores.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Empregadores.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1457sl1.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

---

## Como preencher a planilha modelo

Na planilha, terão 2 abas de navegação: **Criação** e **Atualização**. Os dados deverão ser adicionados a partir da linha 4 da planilha.

### Para cadastrar

![Imagem 3: Para cadastrar](https://storage.crisp.chat/users/helpdesk/website/-/6/5/d/f/65df9c1d74d62800/9607e403-50a3-4af8-8f99-e0a44c_nqwhc.png)

1. Para criar novos cadastros de empregadores, utilize a aba "Criação" da planilha. Nessa aba, insira as informações das empresas que precisam ser incluídas no sistema. Preencha todos os campos necessários, garantindo que as informações estejam corretas para que o cadastro seja realizado com sucesso:

   - **Razão Social:** Esta é a coluna para o nome oficial da empresa, como ela está registrada nos órgãos governamentais. É um campo obrigatório, então certifique-se que o nome esteja correto.
   - **Nome Fantasia:** Aqui você pode adicionar o nome pelo qual a empresa é publicamente conhecida. Este é um campo opcional, então se o nome fantasia for o mesmo da razão social, pode deixar em branco ou repetir, como preferir.
   - **Número de Identificação:** Neste campo obrigatório, você deve inserir o CNPJ, CPF ou CEI do empregador, contendo somente números.
   - **CNO/CAEPF:** Este é um campo opcional e deve ser preenchido apenas se o empregador for brasileiro.
   - **Código:** O código externo de identificação é um campo opcional que pode ser usado para integrar a Pontotel com outros sistemas.
   - **Jurisdição:** Aqui você informa a jurisdição em que o empregador está vinculado no padrão ISO 3166-1 alpha2. Por padrão, será "BR" (Brasil). Este também é um campo opcional.
   - **URL com o Logo:** Se você quiser personalizar o espelho de ponto com a logo da sua empresa, pode inserir a URL da imagem aqui. Este campo é opcional, mas deixa o espelho de ponto com a cara da sua empresa! Também é possível anexar uma imagem do seu computador, editando o cadastro já criado no site Gestão.
2. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.

### Para atualizar

![Imagem 4: Para atualizar](https://storage.crisp.chat/users/helpdesk/website/-/a/4/e/4/a4e4b9ab5d7d6000/4f97d3db-9d93-420b-9a5b-4b93da_1yb22xf.png)

1. Caso queira atualizar um cadastro já existente, utilize a aba "Atualização" da planilha. Nessa aba, insira as informações das empresas que precisam ser ajustadas no sistema.

   - **Número de Identificação**: Este é um campo obrigatório e fundamental para identificarmos qual empregador você deseja atualizar. Ele deve ser preenchido com o CNPJ, CPF ou CEI do empregador, contendo somente números.
   - **CNO/CAEPF**: Este campo é opcional e deve ser preenchido apenas se o empregador for brasileiro. Você pode usá-lo para modificar essa informação. Caso deixe o campo em branco, o campo na plataforma permanecerá como está cadastrado.
   - **Razão Social**: Aqui você pode preencher o nome oficial da empresa como está no Registro Governamental. Este campo deve ser preenchido para identificar a empresa, e não pode ser modificado via importação de planilha.
   - **Nome Fantasia**: Utilize este campo para modificar o nome público como a empresa é conhecida.
   - **Código**: Preencha esta coluna para modificar o código externo de identificação do empregador.
   - **URL com o Logo**: Se precisar atualizar a imagem da logomarca do empregador, é só preencher este campo com a URL do novo logotipo.
   - **Ocultar (S/N)**: Para ocultar o cadastro no sistema, preencha esta coluna com "S" (Sim). Se não deseja ocultar o registro, deixe-o vazio ou preencha com "N".
2. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.

---

## Como fazer o upload da planilha preenchida

1. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 5: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
2. Finalize clicando em **importar.**

   ![Imagem 6: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
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

Agora que você aprendeu como criar e atualizar cadastros de empregadores de forma rápida e eficiente através da importação do I05, o processo de gestão de registros de empresas na plataforma Pontotel se torna muito mais ágil. Ao seguir os passos e garantir que os dados estejam corretamente preenchidos, você evita erros e assegura que todas as informações sejam refletidas com precisão no sistema.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
