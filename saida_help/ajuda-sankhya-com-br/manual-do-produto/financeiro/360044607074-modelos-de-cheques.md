---
id: "360044607074"
titulo: "Modelos de Cheques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:41:35Z"
rotulos: ["AJUDA DO SKW", "manual", "Impressão", "Relatórios Formatados", "Relatórios", "Financeiro", "Cheque", "Baixar modelo padrão", "Modelos de Cheques", "Relatório dependente", "br.com.sankhya.fin.modelo.cheque", "Modelos de Cheques manual", "Modelos de Cheque: Criação e download", "Aba Arquivos: Adição de arquivos", "Aba Cheque: Configuração de impressões"]
---

# Modelos de Cheques

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312392012311) Módulo: Financeiro > Relatórios
```

---

Nesta tela, são criados os Modelos de cheques que serão utilizados na Empresa.

[Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#painelprincipal)                                                            [Aba Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#abaarquivos)

[Aba Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#abacheques)                                                               [Aba Contas vinculadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#abacontasvinculadas)

![Imagem 2: Aba Cheques Aba Contas vinculadas](https://ajuda.sankhya.com.br/hc/article_attachments/360082680134)

## Painel Principal

Ao acionar o botão **"Baixar modelos"**, serão apresentadas três opções de baixa:

- **Modelo padrão de cheque:** Será solicitado o download do modelo padrão de impressão de cheques do Sankhya Om;
- **Modelo padrão de cópia (Financeiro):** Será realizado download do modelo padrão de impressão de cheques do Financeiro;
- **Modelo padrão de cópia (Mov. Bancário):** Será realizado download do modelo padrão de impressão de cheques do Movimento Bancário.

Informe o **"Código"** do Modelo de Cheque.

Preencha o campo **"Descrição"** com o nome do Modelo de Cheque.

Cada alteração efetuada no cadastro do Modelo de Cheque será armazenada a data e hora da alteração no campo **"Última Alteração"**.

No campo **"Usuário"** será exibido o nome da pessoa que efetuou a última alteração no Modelo de Cheque.

Se houver necessidade de vincular o Modelo de Cheque a outro Relatório Formatado, informe o código no campo **"Relatório dependente"**. É utilizado, por exemplo, para que no envio de Notas Fiscais por e-mail, seja enviado também o boleto, ou qualquer outro relatório relacionado ao faturamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#top)

## Aba Arquivos

Nesta aba aparecerão os arquivos que farão parte do Modelo de Cheque e que, posteriormente, serão utilizados na [Impressão de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313).

Após realizar a configuração do Relatório Formatado, acione o botão **"Adicionar Arquivo..."** para adicionar o(s) arquivo(s) que será o modelo utilizado para a impressão.

O botão **"Download"** serve para baixar os arquivos já inseridos no Modelo de Cheques.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#top)

## Aba Cheque

![Imagem 3: Aba Cheque](https://ajuda.sankhya.com.br/hc/article_attachments/360082680174)

No campo **"Cópia** **(Financeiro)"**, vincule o Modelo criado para a impressão da Cópia do Cheque.

Preencha o campo **"Cópia (Mov. Bancário)"** com o Modelo criado para a impressão da Cópia do Cheque Mov. Bancário.

Os campos Cópia (Financeiro) e Cópia (Mov. Bancário) serão utilizados quando, na tela [Impressão de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313), aba Parâmetros impressão, a marcação **"Gerar cópia de cheque"** estiver efetuada.

**Nota:** se estes dois campos estiverem informados, o sistema desconsiderará o modelo informado no campo Cópia (Financeiro) e Cópia (Mov. Bancário) e utilizará o indicado nestes.

Nos campos **"Comprimento da linha 1"** e **"Comprimento da linha 2"** são informadas as quantidades máximas de caracteres que poderão ser impressos nas linhas 1 e 2; nestas será impresso o valor do cheque por extenso. Por exemplo: Valor de cheque de R$ 250,00 por extenso: (duzentos e cinquenta reais), ou seja, 48 caracteres.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#top)

## Aba Contas Vinculadas

![Imagem 4: Aba Contas Vinculadas](https://ajuda.sankhya.com.br/hc/article_attachments/360083852413)

O botão **"Vincular conta"** serve para selecionar as contas bancárias que terão o modelo selecionado para impressão do cheque. Ao clicar neste, será aberta a tela de pesquisa da Conta Bancária.

Acione o botão **"Desvincular contas selecionadas"** para selecionar as contas bancárias que não terão o modelo selecionado para Impressão do Cheque. Ao clicar neste, abrirá a tela de pesquisa da Conta Bancária.

**Importante:** o parâmetro **"Campos p/ mod. cheque (TAB.CAMPO,TAB2.CAMPO2,...) - CAMPOSMODCHEQUE"** possibilita configurar, de modo restritivo, quais campos devem ser visualizados no Modelo de Cheque a ser utilizado. Para isto, é necessário preencher o campo **"Texto"** localizado nas configurações do referido parâmetro do seguinte modo:

- Inserir campos e tabelas correspondentes, separando-os por vírgula, conforme modelo estruturado abaixo:

NOMETABELA.NOMECAMPO, NOMETABELA.NOMECAMPO2, NOMETABELA2.NOMECAMPO4.

**Observação:** os campos a serem inseridos devem, necessariamente, considerar uma das tabelas a seguir: **"TGFPAR"**, **"TSIEMP"**, **"TSIBCO"**, **"TGFNAT"**, **"TSICTA"**, **"TGFCTT"**, **"TSIEND"**, **"TSICUS"**, **"TGFVEN"**, **"TGFTOP"** ou a view **"VGFFIN"**. Diante disto, ao considerar a view VGFFIN realize uma consulta verificando os campos mapeados para esta, disponível na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

Para maiores informações acesse [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074-Modelos-de-Cheques#top)
