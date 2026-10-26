---
id: "360044607134"
titulo: "Modelos de Boleto(s)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134-Modelos-de-Boleto-s"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:41:40Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios", "Relatório Dependente", "Boleto", "Financeiro", "configuração de impressão de boleto", "impressão de boleto", "Modelos de Boletos", "br.com.sankhya.fin.modelo.boleto", "Modelos de Boleto(s) manual", "Criar e baixar modelos de boletos", "Vincular modelo à Conta para impressão", "Usar iReport e cadastrar no sistema"]
---

# Modelos de Boleto(s)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312424613783)Módulo: Financeiro > Relatórios
```

---

Por meio desta tela, você pode criar um modelo de boleto ou baixar o modelo padrão do sistema, que poderá ser alterado conforme sua necessidade.

O modelo do boleto, é diretamente buscado pela tela de impressão. Contudo, quando a impressão for feita pela [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), este modelo terá de ser vinculado a um modelo de impressão, porque assim, ele ficará vinculado à Conta.

![Imagem 2: O modelo do boleto, é diretamente buscado pela tela de impressão. Contudo, quando a impressão for feita pela Central -…](https://ajuda.sankhya.com.br/hc/article_attachments/4421276405271)

**Importante:** o novo modelo deverá ser criado no iReport, antes de ser adicionado a esta tela.

Para realizar a criação do modelo nessa tela, bastará você clicar no botão ![Imagem 3: Para realizar a criação do modelo nessa tela, bastará você clicar no botão "Cadastrar Relatório (F8)" no painel de…](https://ajuda.sankhya.com.br/hc/article_attachments/16372404162455) **"Cadastrar Relatório [F8]"** no painel de controle e identificar o novo registro através dos campos:

O campo **"Código"** será gerado automaticamente pelo sistema.

No campo **"Descrição"** insira a identificação do registro fornecida.

Informe no campo **"Categoria"** um grupo em que o modelo se enquadre. Este campo pode ser alimentado manualmente no ato do cadastro, ou seja, não é necessário um cadastro prévio para seu preenchimento. À medida que novas categorias são inseridas, estas serão apresentadas no espaço Categoria localizado no Painel de Filtros.

O campo **"Última** **Alteração"** é preenchido de forma automática pelo sistema, exibindo a data e hora de criação do novo registro. Este campo serve pra consultas futuras.

O sistema automaticamente registrará o nome e o **"Usuário"** logado responsável pela criação ou alteração do modelo.

O campo **"Id da tela"** é utilizado para relacionar o atual relatório formatado com sua respectiva tela, onde será utilizado para impressão.

Caso haja necessidade de vincular outro modelo de Relatório Formatado, você deverá informá-lo no campo **"Relatório dependente"**. É utilizado, por exemplo, para que no envio de Notas Fiscais por e-mail, seja enviado também o boleto, ou qualquer outro relatório relacionado ao faturamento.

Através do campo **"Fonte de Dados"**, você define qual o banco de dados que será acessado para execução dos relatórios formatados.

Referente ao campo **"Nome do anexo no envio de e-mail"**, na utilização da rotina de Impressão de Boletos, ao enviar um boleto por e-mail, caso a marcação **"Anexar Nota Fiscal"** esteja assinalada, o sistema envia o documento por e-mail com o nome **"Nota\_fiscal\_8522.pdf"**, onde **"8522"** se refere ao número da nota. Informando este campo, o texto aqui inserido substituirá o termo Nota\_Fiscal\_.

Além dos botões padrões do painel, a tela possui os botões ![Imagem 4: Além dos botões padrões do painel, a tela possui os botões "Visualizar Relatório" e "Agendar Relatório" .](https://ajuda.sankhya.com.br/hc/article_attachments/16372424822679) **"Visualizar Relatório"** e  **"Agendar Relatório"**.

Por meio do botão ![Imagem 5: Por meio do botão "Outras Opções..." , pode-se baixar os modelos de cobrança "Boleto" , "Pix Cobrança" e "Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/16372424826007) **"Outras Opções..."**, pode-se baixar os modelos de cobrança **"Boleto"**, **"Pix Cobrança"** e **"Boleto Hibrido (com QRCode)"**.

**Observação:** o modelo de boleto híbrido atenderá tanto o Banco do Brasil híbrido quanto o Banco Itaú híbrido.

Além disso, será possível realizar o download dos modelos fechados do Banco Itaú e do Banco do Brasil no [Sankhya Place](https://ajuda.sankhya.com.br/hc/pt-br/articles/4422517129623-Sankhya-Place). 

O botão ![Imagem 6: O botão "Baixar Modelo Padrão" contém os modelos padrões de boleto para download. Como já informado, estes modelos…](https://ajuda.sankhya.com.br/hc/article_attachments/16372462494871) **"Baixar Modelo Padrão"** contém os modelos padrões de boleto para download. Como já informado, estes modelos poderão ser alterados.

Após salvar o cabeçalho com as informações sobre o novo registro, adicione o novo arquivo configurado pelo iReport. Isto será feito através do botão **"Adicionar Arquivo..."** da aba **"Arquivos"**:

![Imagem 7: Após salvar o cabeçalho com as informações sobre o novo registro, adicione o novo arquivo configurado pelo iReport .…](https://ajuda.sankhya.com.br/hc/article_attachments/4421276414359)

**Observação:** o sistema aceitará apenas arquivos no formato **".jrxml"**. Também através do botão Adicionar Arquivo... você pode adicionar mais de um arquivo para cada modelo.

O botão **"Download"** só ficará habilitado após a adição de um arquivo. Em caso de perda do modelo original, você pode resgatar o mesmo através do download, tanto para alteração no arquivo quanto para conferência dos dados.

**Observação:** a pré-visualização de um boleto deve ser realizada na tela [Impressão de Boletos(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-).

---

![Imagem 8: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16372424828055) Acesse também:

[Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[Impressão de boletos pela Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599634).
