---
id: "10651877852311"
titulo: "Não pode ser utilizada rubrica cuja [natRubr] em S-1010 seja igual a [1801, 9220]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10651877852311-N%C3%A3o-pode-ser-utilizada-rubrica-cuja-natRubr-em-S-1010-seja-igual-a-1801-9220"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:33Z"
rotulos: ["Configuração", "Eventos", "Folha", "Natureza", "eSocial", "#folha", "Erro 1612", "Erro com Rubricas na Rescisão eSocial"]
---

# Não pode ser utilizada rubrica cuja [natRubr] em S-1010 seja igual a [1801, 9220]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19296799468951) MENSAGEM:**

Erro 1612 - Não pode ser utilizada rubrica cuja [natRubr] em S-1010 seja igual a [1801, 9220], desde que mês/ano da data do desligamento ou término ou período de apuração seja maior ou igual XX/XX/XXXX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19296805686935) SITUAÇÃO:**

Ao enviar a rescisão 2299 a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19296799482135) CAUSA:**

Ocorre quando algum código de natureza de rubrica com vigência finalizada está sendo usado em algum evento enviado ao eSocial na folha ou rescisão.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19296799490839) SOLUÇÃO:**

- Acesse o menu Arquivos > Cadastro > Eventos e identifique as rubricas que constam na Folha de Pagamento e que possuem a Natureza 1801, 9220 (geralmente trata-se de eventos de Alimentação).
- Os códigos 1801 e 9220 perderam a validade e não deverão mais ser usados. Assim como algumas outras naturezas de rubricas, de acordo com a data término da Tabela 03 do eSocial.
- Acesse a Tabela 03 - Natureza das Rubricas da Folha de Pagamento e localize um código válido e que corresponda ao evento que estão utilizando.
- Após ajustar o código faça a geração do s-1010 com a retificação dos eventos corrigidos.
- Em seguida, gere também o evento que apresentou o erro inicialmente (S-2299 ou S-1200) e faça o envio.

Caso precise incluir algum código de natureza de rubrica que não consta no sistema, acesse com o usuário SUP.  Somente esse usuário faz a inclusão.
