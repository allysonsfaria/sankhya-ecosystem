---
id: "42427268616343"
titulo: "E01 - Como gerar o exportador com o registro de pontos dos empregados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427268616343-E01-Como-gerar-o-exportador-com-o-registro-de-pontos-dos-empregados"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:00Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_13d790ddea1f", "pontotel_6a332852e448e05ba5b05278"]
---

# E01 - Como gerar o exportador com o registro de pontos dos empregados

O **E01** é um arquivo de exportação com os registros de ponto dos colaboradores em um período determinado, acompanhado do número do PIS de cada um. Ele é direcionado principalmente para integração com softwares de folha de pagamento, servindo como base para o processamento das marcações fora da plataforma Pontotel.

---

## Como acessar

1. No menu de navegação do site Gestão, clique em **Relatório e importações**.
2. Na seção "exportações", escolha a opção: **E01 - Registro de pontos de todos os empregados**.

![Imagem 1: Na seção "exportações", escolha a opção: E01 - Registro de pontos de todos os empregados .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_rllyg.png)

---

## Como configurar os filtros e gerar o relatório

1. Antes de gerar o arquivo, configure os filtros conforme a necessidade. Todas as opções estão disponíveis na parte central da tela.

![Imagem 2: Antes de gerar o arquivo, configure os filtros conforme a necessidade. Todas as opções estão disponíveis na parte…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_57ikt4.png)

### Filtro por grupo de colaboradores

Na parte superior, você pode escolher como segmentar os colaboradores incluídos na exportação. As abas disponíveis são:

- **Locais de trabalho**: filtra pelos locais cadastrados na plataforma.
- **Empregadores**: filtra pelo CNPJ/empregador vinculado ao colaborador.
  Selecione a aba desejada e escolha o(s) registro(s) correspondentes no campo abaixo.

### Período

Defina o intervalo de datas que deseja exportar. No campo **Período**, você pode escolher entre opções pré-definidas ou selecionar **Customizado** para informar manualmente as datas de **início** e **fim** do período.

### Filtro de empregado

No campo **Filtro de empregado**, defina se deseja incluir **todos** os colaboradores ou aplicar um filtro específico, como apenas ativos ou apenas demitidos.

### Envio por e-mail

Se preferir receber o arquivo diretamente no e-mail, marque a opção **Enviar os resultados do relatório por e-mail**. O arquivo será enviado para o endereço vinculado ao seu usuário na plataforma.

2. Com os filtros configurados, clique em **Gerar arquivo** para iniciar a exportação.

> 💡 Dica: o botão "Gerar arquivo beta" gera uma versão alternativa do mesmo relatório, com melhorias em andamento. Utilize-o caso o time de suporte oriente nesse sentido.

3. Após o processamento, o arquivo será disponibilizado para download ou enviado por e-mail, conforme a opção escolhida.

---

## Sobre o arquivo gerado

O E01 é exportado em formato de texto (`.txt`), com registros em largura fixa. Cada linha representa uma batida de ponto de um colaborador, contendo informações como o número do PIS e o horário da marcação. Esse formato é compatível com os principais softwares de folha de pagamento do mercado.

![Imagem 3: O E01 é exportado em formato de texto ( .txt ), com registros em largura fixa. Cada linha representa uma batida de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_k8svdm.png)

---

Se precisar de auxílio ou tiver dúvidas sobre a exportação do E01, entre em contato com o nosso time pelo Chat integrado na plataforma ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700)!
