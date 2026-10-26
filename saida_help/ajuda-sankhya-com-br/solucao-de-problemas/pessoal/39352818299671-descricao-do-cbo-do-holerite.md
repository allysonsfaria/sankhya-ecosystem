---
id: "39352818299671"
titulo: "Descrição do CBO do holerite"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352818299671-Descri%C3%A7%C3%A3o-do-CBO-do-holerite"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:54Z"
rotulos: ["Configuração", "Relatórios", "Preferências", "eSocial", "Folha de Pagamento", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Descrição do CBO do holerite

A descrição da CBO (Classificação Brasileira de Ocupações) está sendo exibida no holerite dos funcionários, e é necessário apresentar apenas o código da ocupação ou impedir sua exibição, conforme a configuração desejada.

### Situação

Ao imprimir o holerite, o sistema apresenta tanto o "Número do CBO" quanto a "Descrição completa da ocupação". Em alguns cenários, a empresa opta por não exibir essa descrição para simplificar a visualização do documento ou evitar questionamentos dos colaboradores.

A CBO (Classificação Brasileira de Ocupações) é uma informação obrigatória que deve estar vinculada ao cargo ou função do colaborador no sistema. Por padrão, quando a CBO está cadastrada, sua descrição pode aparecer no holerite do funcionário.

A forma como a informação é apresentada depende das configurações do sistema e do modelo de impressão utilizado pelo holerite.

### Causa

A exibição da descrição no holerite ocorre em função de dois fatores:

- Configuração do parâmetro **FPUTILIZACBO**;
- Modelo de relatório utilizado para impressão do holerite.

Quando a empresa utiliza um relatório personalizado, a forma de exibição da CBO pode ter sido definida diretamente na personalização, fazendo com que alterações nos parâmetros do sistema não tenham efeito.

### Solução

(1)** Verifique se o holerite utiliza um relatório personalizado**

Antes de realizar qualquer alteração, confirme com a equipe de TI ou com o responsável técnico se o holerite utiliza um modelo de impressão personalizado.

Importante: caso exista uma personalização, as alterações descritas neste artigo podem não surtir efeito, pois a apresentação da CBO poderá estar definida diretamente no relatório.

**(2)** **Configure o parâmetro responsável pela exibição da CBO**

Acesse a tela **Preferências** e localize o parâmetro FPUTILIZACBO.

Defina o parâmetro para utilizar a CBO do Cargo ou da Função, conforme a parametrização adotada pela empresa.

Quando o parâmetro permanecer sem preenchimento, o sistema deixará de apresentar a informação da CBO no holerite.

**(3)** **Gere um novo holerite**

Após salvar a alteração, gere novamente o holerite e valide se a informação está sendo apresentada conforme o esperado.

**(4)** Realize um **"Teste de impressão"** do holerite para validar que apenas o código do CBO está sendo exibido.

### Observações importantes

#

- A informação da CBO continua sendo obrigatória para atendimento às exigências do eSocial, independentemente da forma como é apresentada no holerite.
- Caso o holerite utilize um relatório personalizado, a alteração deverá ser realizada por um profissional com conhecimento em personalização de relatórios.
- Se o holerite não for personalizado e a alteração do parâmetro **FPUTILIZACBO** não produzir o comportamento esperado, abra um chamado para o suporte especializado informando que:
  - o relatório é nativo; e
  - a alteração do parâmetro não resolveu o problema.
