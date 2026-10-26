---
id: "360056763133"
titulo: "Config. Parametros EDI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056763133-Config-Parametros-EDI"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:10:49Z"
rotulos: ["Configuração", "EDI", "Financeiro", "CNAB", "FEBRABAN", "Remessa Bancária", "br.com.sankhya.tim.cfg.ParametrosEDI", "Intercâmbio Eletrônico de Dados (EDI)", "Configuração de Remessa Bancária", "Parâmetros e Configurações EDI"]
---

# Config. Parametros EDI

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311412243863) Módulo: Imobiliária > Configurações      ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311412248855) Versão: a partir da 3.31
```

O Intercâmbio Eletrônico de Dados consiste na integração de informações entre uma determinada entidade e outra. Se tratando de EDI Bancário, temos uma integração entre bancos e empresas (de forma eletrônica), através da troca de arquivos, visando minimizar erros e agilizar o processamento das informações, além de dar mais segurança a todo o processo.

No caso de uma Remessa Bancária, o sistema cria um arquivo de texto simples, contendo todas as informações necessárias para o processamento da cobrança no banco. Essas informações são colocadas em ordem e rastreadas, de acordo com a definição do layout e dos filtros no momento da geração. Já o retorno faz o processo inverso. Baseado em um arquivo fornecido pelo banco, o sistema processa este arquivo e efetua atualizações, conforme configurações realizadas por você, como exemplo, as baixas no financeiro.

Como a integração é feita por arquivos, cada banco deverá fornecer um manual contendo todas as especificações necessárias para a criação do layout.

**![Imagem 3](https://ajuda.sankhya.com.br/hc/article_attachments/16174521194007) Importante:** antes de iniciar a configuração do EDI, tenha em mãos o manual atualizado e saiba qual formato será utilizado na conexão: CNAB ou FEBRABAN, uma vez que, cada modelo apresenta um tamanho de registro diferente.

Através desta tela, você configura os Parâmetros do EDI.

![Imagem 4](https://ajuda.sankhya.com.br/hc/article_attachments/360092847134)

O campo **"Modulo"** será preenchido automaticamente pelo sistema, sendo que, sempre será levado o Módulo Comercial para criar o parâmetro do EDI.

No campo **"Código"**, informe o formatador de remessa previamente cadastrada para fazer os parâmetros.

O campo **"Título"** será preenchido com o nome do título, de acordo com a referência a ser criada no parâmetro.

Na aba **"Parâmetros"**, serão criados os parâmetros e suas ordens para a geração do EDI. Nesta aba, temos os seguintes campos e botões:

O botão **"Configurar Opções"** facilita a criação da ordem e dos parâmetros contidos na aba.

O campo **"Ordem"** armazena a ordem em que o parâmetro será executado.

Informe o **"Nome"** do campo de acordo com o cadastro em sua tabela.

Insira a **"Descrição"** do campo conforme o seu cadastro na tabela.

Selecione o **"Tipo"** de campo, de acordo com sua origem.

Efetue a marcação **"Requerido"** se o campo for do tipo requerido para o processamento.

Caso o campo possua um valor padrão, insira-o no campo **"Valor Padrão"**.

No campo **"Opções"** serão exibidas as opções do campo no momento do cadastro.

Informe a instância de destino no campo **"Nome Instância Dest."**.

E, por fim, informe no campo **"Nro Campo Inst. Destino"** o número do campo da instância de destino.

**Observação:** informe no parâmetro **"Código do Layout polyprint para geração do txt de - TIMCODLAYOUTTXT"** o Código do EDI que será utilizado para a geração do arquivo para o bureau de impressão de boletos.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056763133-Config-Parametros-EDI#top)
