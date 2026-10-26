---
id: "360044222853"
titulo: "A nota 'XXXXXX' possui movimentações de caixa. Pode ser excluída somente pelo Gerente da Central de Atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044222853-A-nota-XXXXXX-possui-movimenta%C3%A7%C3%B5es-de-caixa-Pode-ser-exclu%C3%ADda-somente-pelo-Gerente-da-Central-de-Atendimento"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:20Z"
rotulos: ["#criadoRoger", "CORE_E01835", "Configuração", "Segurança", "Movimentação Financeira", "Financeiro", "Restrição na exclusão", "Autorização do gerente", "Permissões de acesso", "Central de Atendimento"]
---

# A nota 'XXXXXX' possui movimentações de caixa. Pode ser excluída somente pelo Gerente da Central de Atendimento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17175702396183) MENSAGEM:**

[CORE\_E01835]: A nota 'X' possui movimentações de caixa. Pode ser excluída somente pelo Gerente da Central de Atendimento.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17175718430615) SOLUÇÃO:**

![Imagem 3: A mensagem é apresentada para restringir a exclusão de registros financeiros movimentados através da uma conta Caixa.…](https://ajuda.sankhya.com.br/hc/article_attachments/17175702402327) A mensagem é apresentada para restringir a exclusão de registros financeiros movimentados através da uma conta Caixa. Sendo essa exclusão permitida apenas por 'Usuários' que tenham seus acessos definidos como Gerente.

![Imagem 4: Dessa forma, o recomendado é uma sintonia interna, solicitando ao gestor do financeiro que esse procedimento seja…](https://ajuda.sankhya.com.br/hc/article_attachments/17175702405783) Dessa forma, o recomendado é uma sintonia interna, solicitando ao gestor do financeiro que esse procedimento seja realizado pelo seu usuário, com a sua autorização.

![Imagem 5: Caso seja definido que essa liberação ocorrerá para outros usuários, solicite que o usuário responsável por liberação…](https://ajuda.sankhya.com.br/hc/article_attachments/17175702407703) Caso seja definido que essa liberação ocorrerá para outros usuários, solicite que o usuário responsável por liberação de acessos em sua empresa, realize a liberação abaixo:

- Tela 'Usuários' >> Aba 'Segurança' >> **Gerente dos Portais [MARCADO]**

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17175702412311) CAUSA:**

Mensagem apresentada ao tentar excluir um lançamento que gerou movimentações de caixa, por um usuário que não possua permissões de acesso definidas com o controle 'Gerente dos portais'.
