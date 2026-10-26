---
id: "39363285089431"
titulo: "Erro no cálculo do FGTS - 2ª parcela do 13º salário não considera periculosidade na base de cálculo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39363285089431-Erro-no-c%C3%A1lculo-do-FGTS-2%C2%AA-parcela-do-13%C2%BA-sal%C3%A1rio-n%C3%A3o-considera-periculosidade-na-base-de-c%C3%A1lculo"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:04Z"
rotulos: ["Configuração", "Eventos", "Folha", "eSocial", "FGTS", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no cálculo do FGTS - 2ª parcela do 13º salário não considera periculosidade na base de cálculo

**MENSAGEM**

O sistema não está considerando o adicional de periculosidade na base de cálculo do FGTS da 2ª parcela do 13º salário de funcionário afastado por acidente de trabalho, embora tenha calculado corretamente na 1ª parcela.

**SITUAÇÃO**

Ao processar a **"2ª parcela do 13º salário"** de funcionário afastado por acidente de trabalho, o sistema calcula o **"FGTS"** considerando apenas o salário base, sem incluir o adicional de **"periculosidade"** (30%) na base de cálculo. Entretanto, na **"1ª parcela"**, o adicional foi corretamente incluído no cálculo do FGTS.

Durante o afastamento por acidente de trabalho, o recolhimento do FGTS é obrigatório e deve considerar todas as parcelas que compõem a remuneração do funcionário, incluindo adicionais como periculosidade, insalubridade e outras médias.

O problema pode estar relacionado a:

- Configuração incorreta do evento de adicional de periculosidade;

**SOLUÇÃO**

Para corrigir o cálculo do FGTS da 2ª parcela do 13º salário, siga os passos abaixo:

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento referente à **periculosidade.**

**(2)** Confirme se está marcado o código "12 - Base de cálculo do FGTS 13º salário"
Importante: Para que o adicional de periculosidade seja considerado na base de FGTS da 2ª parcela do 13º, o evento deve ter a incidência de FGTS configurada como código 12.

**(3)**Clique na aba "Bases de Cálculo"
Verifique se as seguintes bases estão marcadas:
Base 1909 - BASE FGTS 13º SALÁRIO
 ![Imagem 1: (1) Acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento referente à periculosidade. (2)…](https://ajuda.sankhya.com.br/hc/article_attachments/41117306227095)

![Imagem 2: Verifique se as rubricas de incidências do eSocial estão devidamente preenchidas no evento. Acesse a aba "Incidências"…](https://ajuda.sankhya.com.br/hc/article_attachments/41117366862743)
**(4)** Verifique se as rubricas de incidências do eSocial estão devidamente preenchidas no evento. Acesse a aba **"Incidências"** e certifique-se de que as rubricas estão configuradas corretamente.

**(5)** Salve as alterações realizadas no cadastro do evento.

**(6)** Acesse a tela **"Cálculo Mensal"** (Pessoal+ » Rotinas Folha » Cálculos) e recalcule a folha referente à 2ª parcela do 13º salário do funcionário afastado.

**(7)** Após o recálculo, verifique se o valor do FGTS passou a considerar o adicional de periculosidade na base de cálculo.

**(8)** Se necessário, envie o evento **"S-1010"** ao eSocial para atualizar as informações da rubrica alterada.

**CAUSA**

Durante o afastamento por acidente de trabalho, a legislação determina que o FGTS deve ser recolhido sobre a remuneração que o trabalhador estaria percebendo, incluindo todas as parcelas variáveis e adicionais.
