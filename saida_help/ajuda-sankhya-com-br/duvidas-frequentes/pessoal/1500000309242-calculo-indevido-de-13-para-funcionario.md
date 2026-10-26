---
id: "1500000309242"
titulo: "Cálculo indevido de 13° para funcionário afastado por auxilio doença"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000309242-C%C3%A1lculo-indevido-de-13-para-funcion%C3%A1rio-afastado-por-auxilio-doen%C3%A7a"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:25:39Z"
rotulos: ["#criadoRoger", "Configuração", "Funcionários", "Ocorrências", "Folha", "#validadoRayssa", "13° indevido para afastado", "Desmarcar opção 'Direito ao 13°'", "Recalcular Folha", "FGTS", "Pessoal+", "Artigo atualizado KCS", "Sankhya RH - KCS", "MGE Pessoal"]
---

# Cálculo indevido de 13° para funcionário afastado por auxilio doença

O sistema está calculando indevidamente o 13º salário para funcionários afastados, mesmo quando esses colaboradores estão afastados durante todo o período aquisitivo, gerando valores indevidos para situações como serviço militar, auxílio-doença, aposentadoria por invalidez ou cárcere.

### SOLUÇÃO

Para correção, siga os passos abaixo de acordo com a sua versão do sistema:

**Para clientes com o MGE Pessoal**

Acesse o registro de ocorrências em (MGE Pessoal >> Lançamentos >> Histórico do Funcionário >> Registro de Ocorrências). Informe a empresa, funcionário e em seguida localize o histórico da ocorrência:
![Imagem 1: Acesse o registro de ocorrências em (MGE Pessoal >> Lançamentos >> Histórico do Funcionário >> Registro de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000349582)

Acesse o histórico de ocorrências em (MGE Pessoal >> Lançamentos >> Histórico do Funcionário >> Histórico de Ocorrências). Localize o histórico da ocorrência e identifique na parte afastamento a causa.
![Imagem 2: Acesse o histórico de ocorrências em (MGE Pessoal >> Lançamentos >> Histórico do Funcionário >> Histórico de…](https://ajuda.sankhya.com.br/hc/article_attachments/14820020353175)

Acesse o cadastro de afastamento em (MGE Pessoal >> Arquivos >> Cadastros >> Códigos de afastamento). Verifique o código de afastamento vinculado ao funcionário e **"Desmarque"** a opção **"Direito ao décimo terceiro"**. Caso trate-se de aposentadoria por incapacidade permanente, verifique se o campo **"Descrição FGTS"** está vinculado à opção **"19"**.
![Imagem 3: Acesse o cadastro de afastamento em (MGE Pessoal >> Arquivos >> Cadastros >> Códigos de afastamento). Verifique o…](https://ajuda.sankhya.com.br/hc/article_attachments/14820050560791)

**Para clientes com Pessoal+**

Acesse o cadastro de ocorrências em (Pessoal+ >> Rotinas Folha >> Ocorrências). Verifique o código de afastamento que está vinculado ao funcionário e **"Desmarque"** a opção **"Direito ao décimo terceiro"**.
![Imagem 4: Acesse o cadastro de ocorrências em (Pessoal+ >> Rotinas Folha >> Ocorrências). Verifique o código de afastamento que…](https://ajuda.sankhya.com.br/hc/article_attachments/360101457933)

Acesse o cadastro de afastamento do Pessoal+ em (Pessoal+ >> Cadastros >> Código de Afastamento). Certifique-se de que o campo **"Descrição FGTS"** .
![Imagem 5: Acesse o cadastro de afastamento do Pessoal+ em (Pessoal+ >> Cadastros >> Código de Afastamento). Certifique-se de que…](https://ajuda.sankhya.com.br/hc/article_attachments/14820075754775)

Certifique-se de que, no cadastro de afastamento, o campo **"Calcula 13º Salário"** esteja desmarcado para que o sistema não considere os meses de afastamento no cálculo dos avos.

Após os ajustes, calcule novamente o 13º para o funcionário em questão. 

**OBS: Esse processo acima precisa ser realizado para todos os afastamento que não da direito a 13º salário.**

### CAUSA

O cálculo indevido ocorre porque o **código de afastamento** estava configurado com a opção **"Direito ao 13º"** marcada, fazendo com que o sistema considere os meses de afastamento como válidos para o cálculo dos avos do 13º salário, mesmo para colaboradores que não possuem tal direito. Adicionalmente, a ausência de preenchimento correto no campo **"Descrição FGTS"** pode impactar o reconhecimento da natureza do afastamento.
