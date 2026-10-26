---
id: "44010138326935"
titulo: "[TMS] - Auditoria de Fretes com Correios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010138326935--TMS-Auditoria-de-Fretes-com-Correios"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:31:00Z"
rotulos: ["sync_hc", "lincros", "lincros_17221671", "sync_hash_aa3c16b2e2a6"]
---

# [TMS] - Auditoria de Fretes com Correios

**Menu:** Financeiro > Faturas

## Passo a passo

### Auditora de fretes com correios

- Os **Correios não emitem CT-e**, portanto para fazer a auditoria de fretes foi feita uma adaptação do arquivo de faturas
- A **fatura dos Correios** em formato **txt** é importada no sistema através da importação de EDI ou via e-mail. Este documento entra no sistema como um conhecimento de fretes, ou seja, ao invés de criar uma fatura, é criado um CT-e do tipo Correios onde é possível comparar o Valor cobrado X Valor calculado.
- O vínculo com a NF-e se dá através do **código de rastreio** que está na fatura e o código de rastreio que está no pré-conhecimento

### Modelo EDI

- No cadastro de transportadora (empresa) dos Correios cadastrar o EDI padrão como CORREIOS

![Imagem 1: No cadastro de transportadora (empresa) dos Correios cadastrar o EDI padrão como CORREIOS](https://ajuda.sankhya.com.br/hc/article_attachments/44010138567063)

- Modelo EDI **COB\_CORR**

![Imagem 2: Modelo EDI COB_CORR](https://ajuda.sankhya.com.br/hc/article_attachments/44010109014551)

### EDI COB\_CORR

Esse EDI é extraído do sistema dos Correios. É um arquivo texto que lemos também de forma posicional.

![Imagem 3: Esse EDI é extraído do sistema dos Correios. É um arquivo texto que lemos também de forma posicional.](https://ajuda.sankhya.com.br/hc/article_attachments/44010133168663)

![Imagem 4: Esse EDI é extraído do sistema dos Correios. É um arquivo texto que lemos também de forma posicional.](https://ajuda.sankhya.com.br/hc/article_attachments/44010139381527)

### Cadastros de configurações para importação do EDI COB\_CORR

- Configuração de empresa “**contratoCorreios**” com o número do contrato global

![Imagem 5: Configuração de empresa “ contratoCorreios ” com o número do contrato global](https://ajuda.sankhya.com.br/hc/article_attachments/44010109936919)

- Além das configurações dos Correios preenchidas na plataforma, para efetuar a auditoria deve-se também cadastrar no menu **Cadastros gerais > Configurações da unidade > Parâmetros > Unidade**, a configuração **contratoCorreios**: cada unidade possui um número. Se atentar a **unidade logada**! Caso não esteja em nenhuma será cadastrado na matriz!

![Imagem 6: Além das configurações dos Correios preenchidas na plataforma, para efetuar a auditoria deve-se também cadastrar no…](https://ajuda.sankhya.com.br/hc/article_attachments/44010125134359)

### CT-e com Correios

- A **fatura dos Correios** em formato **txt** é importada no sistema através da importação de EDI ou via e-mail. Este documento entra no sistema como um conhecimento de fretes, ou seja, ao invés de criar uma fatura, é criado um CT-e do tipo Correios onde é possível comparar o Valor cobrado X Valor calculado.
- O vínculo com a NF-e se dá através do **código de rastreio** que está na fatura e o código de rastreio que está no pré-conhecimento. Nesse caso é importante ter o código do rastreio no pré-conhecimento, caso contrario não irá importar
- Criado CT-e com as informações do TXT e com tipo Correios
- CT-e já fica vinculado a Fatura dos correios (criada durante a importação)

  - Número está no EDI
  - A Série são as duas primeiras letras do rastreio + as duas últimas letras

![Imagem 7: A Série são as duas primeiras letras do rastreio + as duas últimas letras](https://ajuda.sankhya.com.br/hc/article_attachments/44010144010647)

![Imagem 8: A Série são as duas primeiras letras do rastreio + as duas últimas letras](https://ajuda.sankhya.com.br/hc/article_attachments/44010171020951)

### Fatura dos Correios

- Ao final é gerado uma fatura com transportadora Correios com os CT-es do tipo correios

![Imagem 9: Ao final é gerado uma fatura com transportadora Correios com os CT-es do tipo correios](https://ajuda.sankhya.com.br/hc/article_attachments/44010140655767)

![Imagem 10: Ao final é gerado uma fatura com transportadora Correios com os CT-es do tipo correios](https://ajuda.sankhya.com.br/hc/article_attachments/44010144760343)

![Imagem 11: Ao final é gerado uma fatura com transportadora Correios com os CT-es do tipo correios](https://ajuda.sankhya.com.br/hc/article_attachments/44010171854743)

### Log de Importação de EDI

- Log de Importação de EDI

  - No Log de importação de EDI fica apresentado os registros e os erros e sucessos de cada linha como qualquer outro layout

![Imagem 12: No Log de importação de EDI fica apresentado os registros e os erros e sucessos de cada linha como qualquer outro layout](https://ajuda.sankhya.com.br/hc/article_attachments/44010172227735)
