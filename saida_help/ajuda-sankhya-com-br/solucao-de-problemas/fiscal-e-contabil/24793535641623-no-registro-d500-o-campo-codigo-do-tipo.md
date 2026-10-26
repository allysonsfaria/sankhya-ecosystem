---
id: "24793535641623"
titulo: "No registro D500, o campo \"CODIGO DO TIPO DE ASSINANTE\", não está sendo preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24793535641623-No-registro-D500-o-campo-CODIGO-DO-TIPO-DE-ASSINANTE-n%C3%A3o-est%C3%A1-sendo-preenchido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-08-13T13:16:55Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Preferências", "\"CODIGO DO TIPO DE ASSINANTE\"", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# No registro D500, o campo "CODIGO DO TIPO DE ASSINANTE", não está sendo preenchido

**MENSAGEM:**

No registro D500, o campo 24 "CODIGO DO TIPO DE ASSINANTE", não está sendo preenchido.

**SOLUÇÃO:**

Existem duas formas de informar o código de assinante, são elas:

- **Automática**, conforme configuração das preferências da empresa;
- **Manual**, no momento do lançamento da nota informa-se o código na aba imposto;

Nesse contexto, na tela **"Empresa"**(Caminho: Comercial » Preferências » Empresa), aba **"Livros Fiscal",** existem o campo **"Cód.Tipo de Assinante"**e a opção **"Assinante Informado na Central?". Assim:**

**(1)** Quando a opção Assinante Informado na Central estiver **desmarcada**, o sistema pegará o número informado no campo Cód.Tipo de Assinante do tipo de assinante e o informará em seu correspondente no Pedido/Nota.

**(1)** Se a opção Assinante Informado na Central estiver **marcada**, o sistema trará o campo para Central de Notas sem preenchimento. Estes campos serão visualizados em conformidade ao que for configurado no menu Comercial » Configuração » Configurador de layout da nota.

**Observação:** Estes dados são de responsabilidade do usuário.

**Importante:** Além de informá-los na Configuração do Layout da Nota é necessário também que a top utilizada para o lançamento tenha o código do modelo de Nota Fiscal igual a 20 ou 21.
