---
id: "360044110694"
titulo: "Valor do campo \"Cód. Tipo de Assinante\" deve estar entre 1 e 6"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110694-Valor-do-campo-C%C3%B3d-Tipo-de-Assinante-deve-estar-entre-1-e-6"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:17Z"
rotulos: ["#PUBLIFER", "#revisadojunior", "CORE_E00913", "Configuração", "Fiscal", "NF-e", "Preferências", "Solução: Configure o campo na tela \"Empresa\" com valores de 1 a 6.", "Ajuste: Atualize notas antigas via banco de dados ou reemita com a configuração correta.", "Erro: Valor de \"Cód. Tipo de Assinante\" fora do intervalo 1 a 6.", "Erro"]
---

# Valor do campo "Cód. Tipo de Assinante" deve estar entre 1 e 6

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16647259453591) MENSAGEM:**

[CORE\_E00913]:  Valor do campo "Cód.Tipo de Assinante" deve estar entre 1 e 6.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16647281489047) SOLUÇÃO:**

![Imagem 3: Verifique na tela "Empresa" (Caminho de acesso: Comercial » Preferências), aba 'Livros Fiscais' » Nota Fiscal de…](https://ajuda.sankhya.com.br/hc/article_attachments/16647281500439) Verifique na tela **"Empresa"** (Caminho de acesso: Comercial » Preferências), aba 'Livros Fiscais' » Nota Fiscal de Comunicação/Telecomunicação" » **Cód.Tipo de Assinante:**

![Imagem 4: Verifique na tela "Empresa" (Caminho de acesso: Comercial » Preferências), aba 'Livros Fiscais' » Nota Fiscal de…](https://ajuda.sankhya.com.br/hc/article_attachments/14765535470743)

![Imagem 5: Defina esse campo de acordo com a necessidade da empresa, com uma das opções abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16647259466647) Defina esse campo de acordo com a necessidade da empresa, com uma das opções abaixo:

1 - Comercial/Industrial
2 - Poder Público
3 - Residencial/Pessoa física
4 - Público
5 - Semi-Público
6 - Outros

Quando a opção**"Permite informar Assinante na Central?"** estiver desmarcada, o sistema pegará o número informado no campo **"Cód.Tipo de Assinante"**do tipo de assinante e o informará em seu correspondente no Pedido/Nota.

Se a opção Permite informar Assinante na Central? estiver marcada, o sistema trará o campo para Central de Compras e Central de Vendas sem preenchimento para o usuário informá-lo. Estes campos serão visualizado em conformidade ao que for disposto no[Configurador de Layout da Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)

**Nota:** Estes dados são de responsabilidade do usuário/empresa.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16647281506839) IMPORTANTE:**

Para as notas lançadas antes da configuração feita na empresa, será necessário ajuste via banco de dados, setando a informação na tabela. Ou, relançar as notas, setando a marcação "Permite informar Assinante na Central" e preencher o campo ao efetuar o lançamento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16647281511575)CAUSA:**

Mensagem retornada quando realizada a emissão/lançamentos de notas com Modelo de Documento 20 ou 21 e não informado o Cód.Tipo de Assinante.
