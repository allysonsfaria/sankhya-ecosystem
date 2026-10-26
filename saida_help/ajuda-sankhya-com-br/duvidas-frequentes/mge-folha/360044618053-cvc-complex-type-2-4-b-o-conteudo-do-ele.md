---
id: "360044618053"
titulo: "cvc-complex-type.2.4.b: O conteúdo do elemento 'infoMV' não está completo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044618053-cvc-complex-type-2-4-b-O-conte%C3%BAdo-do-elemento-infoMV-n%C3%A3o-est%C3%A1-completo"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:58Z"
rotulos: ["Configuração", "eSocial", "Configure INSS outras fontes", "Informe CNPJ e categoria", "Registre eventos corretamente", "Erro", "Remuneração", "Múltiplo Vínculo"]
---

# cvc-complex-type.2.4.b: O conteúdo do elemento 'infoMV' não está completo

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16806993654295) MENSAGEM :**

cvc-complex-type.2.4.b: O conteúdo do elemento 'infoMV' não está completo. Era esperado um dos '{"https://www.esocial.gov.br/schema/evt/Remun/v02\_04\_02".remunOutrEmpr}'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16807002867479) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: MGEPessoal » Arquivos » Funcionários, aba: "Remuneração Outras Empresas"](https://ajuda.sankhya.com.br/hc/article_attachments/16806993672855)  Acesse: MGEPessoal » Arquivos » Funcionários, aba: **"Remuneração Outras Empresas"**

1.1 - Informe o tipo de desconto INSS

[ ] 1-Contribuição descontada pela Empresas
[ ] 2-Contribuição descontada por outra empresa sobre valor menor que o teto
[ ] 3-Contribuição descontada por outra Empresa sobre valor do teto

1.2 - Informe os dados da outra empresa (CNPJ e Cod. Categoria).

![Imagem 4: Acesse: MGEPessoal » Arquivos » Eventos . selecione o evento: 505-**Base INSS Outras Fontes.*** - Aba "Propriedades" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16807002881047) Acesse: MGEPessoal » Arquivos » Eventos. selecione o evento: 505-\*\*Base INSS Outras Fontes.\*\*\* - Aba **"Propriedades"**, Campo **"Identificação do evento"** (\*):[178 - Evento de remuneração outras empresas.]

![Imagem 5: Acesse: MGEPessoal » Lançamentos » Movimentação por Funcionário ou MGEPessoal » Arquivos » Eventos Fixos por…](https://ajuda.sankhya.com.br/hc/article_attachments/16806993693079) Acesse: MGEPessoal » Lançamentos » Movimentação por Funcionário **ou** MGEPessoal » Arquivos » Eventos Fixos por Funcionários.

Crie um registro para o evento 505, como o valor da base da Outra Empresa.
Nesse momento abrirá um pop-up para selecionar o CNPJ responsável pelo pagamento (esse antes era informado no cadastro do funcionário). Em seguida, informe também o valor recolhido de INSS da outra empresa no Evento 506-\*\*INSS RETIDO OUTRAS FONTES\*\*\*.

Ao calcular a folha do funcionário serão feitas as deduções corretamente e, ao enviar ao E-social, serão separadas corretamente as verbas da empresa e do múltiplo vinculo.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16807002894743) CAUSA:**

Ocorre quando o funcionário tem múltiplos vínculos e é preciso estar devidamente configurada a dedução na outra empresa no qual possui vinculo.
