---
id: "360045109913"
titulo: "Modelos de Nota Fiscal/Duplicatas/Boleto(s)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:08Z"
rotulos: ["manual", "Configuração", "Impressão", "Relatórios Formatados", "MGE", "PARÂMETROS PNOMEUSULOGADO E PCODUSULOGADO", "Modelos", "Modelos de Nota Fiscal/Duplicatas/Boleto(s)", "Nota Fiscal", "TXT", "br.com.sankhya.core.cfg.modelonotafiscal", "Modelos de Nota Fiscal/Duplicatas/Boleto(s) manual", "Boletos", "Duplicatas", "Financeiro", "Cadastro de Modelos de Impressão"]
---

# Modelos de Nota Fiscal/Duplicatas/Boleto(s)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310923172119) Módulo: Configurações > Avançado
```

---

Nesta tela será feito o cadastro de Modelos de Nota Fiscal, Duplicatas e Boletos utilizados na impressão no sistema.

Através desta tela será efetuado o vínculo entre os modelos de impressão do **Sankhya Om** e do MGE.

![Imagem 2: Através desta tela será efetuado o vínculo entre os modelos de impressão do Sankhya Om e do MGE .](https://ajuda.sankhya.com.br/hc/article_attachments/9459986078743)

Para o cadastro é necessário informar:

**Cód. Modelo:** informar o código do modelo, caso a tela esteja configurada para numeração automática, no momento da inserção o campo estará desabilitado.

**Nome:** nome do modelo cadastrado.

**Caminho:** informar o caminho para o diretório onde está o arquivo modelo.

**Tipo Impressora:** informar o tipo de impressora que servirá para a impressão do arquivo.

**Número do relatório modelo:** este campo é responsável por vincular um modelo de relatório formatado ao modelo do título que está sendo cadastrado. No caso do Boleto é necessário vincular o modelo cadastrado na tela Modelos de Boletos, por exemplo. Primeiramente, deve-se configurar o modelo em **Relatórios Formatados**. Efetuada a criação do Relatório formatado, deve-se informá-lo neste campo.

Observação: a impressão em HTML convencional não atende às necessidades do sistema, além de ser não portável. O **Sankhya Om** não tem suporte para impressão de arquivos em HTML, pois existe a opção para impressão gráfica, que é através de modelos importados do iReport.

**Informações Importantes**

- Os arquivos de modelos devem ser hospedados em um diretório específico no mesmo Servidor de Aplicações onde está instalado o **Sankhya Om**.
- Se informado um número do Relatório Modelo para Impressão de boleto/nota/duplicata, este será utilizado para a impressão. Se o usuário trabalha em integração com o MGE e deseja imprimir um modelo formatado neste, informará no campo **"Caminho"** o diretório onde este modelo está abrigado;
- No caso da impressão de nota fiscal poderá ser utilizado o modelo indicado no campo 'Relatório Modelo para Impressão', caso não seja indicado nenhum modelo neste campo, o sistema utilizará o arquivo indicado no campo 'Caminho'. Para isto, o arquivo XXXXXX deverá estar salvo no diretório informado no parâmetro **"Path dos modelos de impressão/e-mail (MGE Web) - SERVDIRMOD"**.
- **Para impressões USB:** Uma vez instalada a impressora, mapeada e configurada corretamente o sistema fará a impressão.
- O **Sankhya Om** não tem suporte para Register (impressões que buscam o caminho no registro do Windows);
- A impressão em HTML convencional não atende às necessidades do sistema, além de ser não portável. O **Sankhya Om** não tem suporte para impressão de arquivos em HTML, pois existe a opção para impressão gráfica, que é através de modelos importados do iReport.
- Os parâmetros **"Nome do Usuário logado - PNOMEUSULOGADO"** e **"Código do Usuário logado para utilização de impressão de notas/pedidos e boletos -PCODUSULOGADO**" se habilitados servem para identificar o usuário logado no momento da impressão dos boletos e das notas.
