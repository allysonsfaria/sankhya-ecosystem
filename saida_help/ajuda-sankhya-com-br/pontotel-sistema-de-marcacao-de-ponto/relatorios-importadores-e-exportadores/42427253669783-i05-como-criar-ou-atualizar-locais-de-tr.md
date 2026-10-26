---
id: "42427253669783"
titulo: "I05 - Como criar ou atualizar locais de trabalho em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427253669783-I05-Como-criar-ou-atualizar-locais-de-trabalho-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:07Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_31bf8c1990d4", "pontotel_6a332857a6d60dfc4f1f8d06"]
---

# I05 - Como criar ou atualizar locais de trabalho em massa

Criar ou atualizar locais de trabalho um a um no site Gestão pode demandar bastante tempo. Sabendo disso, criamos uma ferramenta de importação de arquivos em lote, agilizando esse processo e garantindo que tudo fique registrado de forma rápida e eficiente.

---

> ⚠️ Atenção: Este importador não é aplicável caso sua empresa possua integração de cadastros ativa com outros sistemas, como Sankhya ou similares.

---

## Como baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Locais de Trabalho.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Locais de Trabalho.](https://storage.crisp.chat/users/helpdesk/website/-/c/b/4/c/cb4ce352dbfea80/9d1b4dfc-7768-465c-87a3-247d13_49f2pm.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

## Como preencher a planilha modelo

Na planilha, terão 2 abas de navegação: **Criação** e **Atualização**. Os dados deverão ser adicionados a partir da linha 4 da planilha.

### Para cadastrar

![Imagem 3: Para cadastrar](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_x50ioz.png)

Para criar novos locais de trabalho, utilize a aba "Criação" da planilha e preencha todas as colunas indicadas como “Campo obrigatório”. As colunas identificadas como “Campos opcionais” podem ser deixadas em branco, mas caso sejam preenchidas, as informações serão adicionadas ao cadastro. Certifique-se de que os dados informados estejam corretos para garantir o sucesso da importação.

**Campos obrigatórios**:

- **Nome do local:** Nome exato do local de trabalho que será cadastrado.
- **Empregadores (número de identificação):** Número de identificação do empregador vinculado ao local. Pode conter pontuação, como CNPJ.
- **País:** País do local cadastrado, seguindo o padrão internacional (por exemplo, "BR" para Brasil).
- **UF:** Sigla do estado (Por exemplo, "SP" para São Paulo).
- **Cidade:** Nome exato da cidade onde o local de trabalho se situa.

Os demais campos são opcionais. Na segunda linha da planilha há uma explicação sobre o campo e/ou como ele deve ser preenchido.

### Para atualizar

![Imagem 4: Para atualizar](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_52nsrl.png)

Caso queira atualizar um cadastro já existente, utilize a aba "Atualização" da planilha. Nessa aba, insira as informações das empresas que precisam ser ajustadas no sistema. A primeira coluna é de preenchimento obrigatório, e serve para identificar o local de trabalho já cadastrado. As demais colunas devem ser preenchidas com a informaçãoque deseja modificar.
Aqui também é possível entender como preencher o campo com a explicação de cada coluna na segunda linha da planilha.

---

## Como fazer o upload da planilha preenchida

1. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.
2. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 5: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
3. Finalize clicando em **importar.**

   ![Imagem 6: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
4. Aguarde o processo de importação da planilha ser finalizado.
5. Quando o processo for concluído, será gerado um relatório com o feedback da importação. Certifique-se de que o usuário foi criado, atualizado ou desativado.

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

Agora que você aprendeu como criar e atualizar cadastros de locais de trabalho de forma rápida e eficiente através da importação do I05, o processo de gestão de registros de empresas na plataforma Pontotel se torna muito mais ágil. Ao seguir os passos e garantir que os dados estejam corretamente preenchidos, você evita erros e assegura que todas as informações sejam refletidas com precisão no sistema.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
