---
id: "31053623099287"
titulo: "Erro ao Enviar S1200 | Erro 8 - Grupo 'Informações relativas ao trabalho intermitente' deve ser preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31053623099287-Erro-ao-Enviar-S1200-Erro-8-Grupo-Informa%C3%A7%C3%B5es-relativas-ao-trabalho-intermitente-deve-ser-preenchido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:20Z"
rotulos: ["Grupo", "eSocial", "Folha de Pagamento", "Configuração Funcionários", "deve ser preenchido", "Erro ao Enviar S1200", "Erro 8", "Informações relativas ao trabalho intermitente", "Erro", "Central de Projetos"]
---

# Erro ao Enviar S1200 | Erro 8 - Grupo 'Informações relativas ao trabalho intermitente' deve ser preenchido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31281675636503) MENSAGEM:**

Ao tentar enviar o evento S1200 no eSocial, ocorre o seguinte erro:

**Erro 8 - Grupo 'Informações relativas ao trabalho intermitente' deve ser preenchido. Verifique as condições de preenchimento no leiaute.**

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31281675637399) SOLUÇÃO:**

**Para corrigir o erro, siga os passos abaixo:**

![Imagem 3: Ajuste o regime de jornada do trabalhador no cadastro do colaborador intermitente, alterando para 1 (regido pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/31281675637911) Ajuste o regime de jornada do trabalhador no cadastro do colaborador intermitente, alterando para **1** **(regido pelo horário de trabalho)** ao invés de **2** **(atividade externa, conforme Art. 62 da CLT);**

 

![Imagem 4: Recalcule a folha mensal para considerar corretamente a convocação do trabalhador intermitente;](https://ajuda.sankhya.com.br/hc/article_attachments/31281706468119) Recalcule a folha mensal para considerar corretamente a convocação do trabalhador intermitente;

![Imagem 5: Verifique se a tabela TFPDHTC , que anteriormente não estava sendo alimentada, passou a registrar as informações dos…](https://ajuda.sankhya.com.br/hc/article_attachments/31281706469015) Verifique se a tabela **TFPDHTC**, que anteriormente não estava sendo alimentada, passou a registrar as informações dos dias e horas trabalhados;

![Imagem 6: Bloqueie e libere novamente a folha de pagamento no gerenciador de folhas;](https://ajuda.sankhya.com.br/hc/article_attachments/31281706470167) Bloqueie e libere novamente a folha de pagamento no gerenciador de folhas;

![Imagem 7: Gere o evento S1200 e realize o envio, garantindo que o processamento ocorra com sucesso](https://ajuda.sankhya.com.br/hc/article_attachments/31281675640215) Gere o evento S1200 e realize o envio, garantindo que o processamento ocorra com sucesso

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31281706471703) CAUSA:**

O erro ocorreu devido a uma configuração incorreta do regime de jornada do trabalhador intermitente. O campo **LSTDIAINTERM**, responsável por registrar a lista de dias intermitentes na tabela **TFPS1200**, não foi devidamente preenchido. Isso aconteceu porque, no cadastro do colaborador, o campo **"REGIMEJOR"** estava configurado com o valor **2** **(atividade externa, conforme Art. 62 da CLT)**, em vez de 1 **(regido pelo horário de trabalho)**.
