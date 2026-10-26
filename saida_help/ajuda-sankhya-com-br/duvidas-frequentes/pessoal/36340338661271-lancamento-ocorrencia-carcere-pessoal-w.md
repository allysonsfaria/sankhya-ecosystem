---
id: "36340338661271"
titulo: "Lançamento ocorrência Cárcere - Pessoal + / W 2"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36340338661271-Lan%C3%A7amento-ocorr%C3%AAncia-C%C3%A1rcere-Pessoal-W-2"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:11Z"
rotulos: ["Lançamento", "Configuração", "Ocorrências", "Folha", "Afastamento", "Pessoal +", "Pessoal+", "ocorrência", "Cárcere", "W 2", "licença cárcere", "trabalhista"]
---

# Lançamento ocorrência Cárcere - Pessoal + / W 2

O afastamento por licença cárcere ocorre quando o empregado é preso ou detido por determinação judicial sem condenação definitiva, ou seja, enquanto o processo continua em andamento.

A CLT não possui um artigo específico sobre “licença cárcere”, mas esse afastamento é tratado como suspensão do contrato de trabalho.

O fundamento está no art. 471 da CLT, que garante que o empregado não perde o vínculo empregatício em situações de suspensão ou interrupção do contrato.

Assim, o contrato de trabalho permanece suspenso durante todo o período de prisão preventiva, temporária ou provisória.

#### Consequências trabalhistas:

- Não há pagamento de salário durante o período de afastamento.
- Não há recolhimento de FGTS, uma vez que o contrato permanece suspenso.
- O período de afastamento não conta para aquisição de férias, 13º salário ou demais benefícios.
- Após a soltura, o empregado pode retornar às suas atividades normalmente, desde que o vínculo empregatício não tenha sido rescindido.

#### Configurações necessárias

**(1)** **Cadastre a ocorrência:**

- Na tela **''Pessoal+''** (Rotinas Folha» Ocorrências» Cadastro):

![Imagem 1: Na tela ''Pessoal+'' (Rotinas Folha» Ocorrências» Cadastro):](https://ajuda.sankhya.com.br/hc/article_attachments/36343910920727)![Imagem 2: Na tela ''Pessoal+'' (Rotinas Folha» Ocorrências» Cadastro):](https://ajuda.sankhya.com.br/hc/article_attachments/36343910922903)

**(2)** **Configure o evento padrão:**

- Na tela **''Pessoal+''**, aba **''Eventos'';**

**Observação:** O código do evento pode variar conforme a configuração de cada cliente.

![Imagem 3: Observação: O código do evento pode variar conforme a configuração de cada cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/36343910925591)![Imagem 4: Observação: O código do evento pode variar conforme a configuração de cada cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/36340338647831)![Imagem 5: Observação: O código do evento pode variar conforme a configuração de cada cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/36340361629207)![Imagem 6: Observação: O código do evento pode variar conforme a configuração de cada cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/36340338648727)

- **Fórmula:**

(@F\_COMPOSICAOSALARIOFOLHA / &DiaDivSalBase) \* FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'2',&TIPFOL)

FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'2', &TIPFOL)

**(3)** **Registre a ocorrência:**

- Na tela **''Pessoal+''** (Rotinas Folha» Ocorrências» Lançamento):

  Informe o código da empresa, habilite a seleção no canto superior direito, escolha o card do colaborador desejado e clique no ícone **“+”** para lançar a ocorrência.

![Imagem 7: Informe o código da empresa, habilite a seleção no canto superior direito, escolha o card do colaborador desejado e…](https://ajuda.sankhya.com.br/hc/article_attachments/36343937769623)

- Em seguida, selecione a ocorrência conforme o código e opção de cada empresa:

![Imagem 8: Em seguida, selecione a ocorrência conforme o código e opção de cada empresa:](https://ajuda.sankhya.com.br/hc/article_attachments/36343910928791)

- Após essa etapa, será aberto um pop-up para preenchimento das informações do afastamento. É necessário informar corretamente a Data de Início e a quantidade de dias em Dias de afastamento previstos. Ao preencher esses dois campos, a Data de retorno prevista será preenchida automaticamente pelo sistema.

**Observação:** A Data de Término só deve ser registrada quando o funcionário efetivamente retornar às suas atividades.

![Imagem 9: Observação: A Data de Término só deve ser registrada quando o funcionário efetivamente retornar às suas atividades.](https://ajuda.sankhya.com.br/hc/article_attachments/36343937772183)![Imagem 10: Observação: A Data de Término só deve ser registrada quando o funcionário efetivamente retornar às suas atividades.](https://ajuda.sankhya.com.br/hc/article_attachments/36343937773591)

**(4)**  Após confirmar o lançamento, o sistema irá atualizar a "Situação" do funcionário na tela de **"Configuração Funcionários"** (Pessoal+» Cadastros):

![Imagem 11: (4) Após confirmar o lançamento, o sistema irá atualizar a "Situação" do funcionário na tela de "Configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/36343910931735)

**(5)** **Cálculos:**

- Acesse a tela **''Pessoal+''** (Rotinas Folha» Cálculos):

![Imagem 12: Acesse a tela ''Pessoal+'' (Rotinas Folha» Cálculos):](https://ajuda.sankhya.com.br/hc/article_attachments/36343910932759)![Imagem 13: Acesse a tela ''Pessoal+'' (Rotinas Folha» Cálculos):](https://ajuda.sankhya.com.br/hc/article_attachments/36343910933527)![Imagem 14: Acesse a tela ''Pessoal+'' (Rotinas Folha» Cálculos):](https://ajuda.sankhya.com.br/hc/article_attachments/36340361638935)![Imagem 15: Acesse a tela ''Pessoal+'' (Rotinas Folha» Cálculos):](https://ajuda.sankhya.com.br/hc/article_attachments/36343937780119)
