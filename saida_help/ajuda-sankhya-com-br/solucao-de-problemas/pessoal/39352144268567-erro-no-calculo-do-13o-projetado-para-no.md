---
id: "39352144268567"
titulo: "Erro no Cálculo do 13º Projetado para Novembro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352144268567-Erro-no-C%C3%A1lculo-do-13%C2%BA-Projetado-para-Novembro"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:48Z"
rotulos: ["Configuração", "Folha", "Configuração Funcionários", "Erro", "Regra de Cálculo", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no Cálculo do 13º Projetado para Novembro

**MENSAGEM**

O cálculo do 13º salário está sendo projetado apenas até novembro, mesmo após configurar a regra de cálculo para projetar até dezembro.

**SITUAÇÃO**

Ao calcular o 13º salário dos funcionários, o sistema projeta o cálculo apenas até o mês de novembro, não considerando o mês de dezembro, mesmo que a **"Regra de Cálculo"** (Pessoal Arquivos Cadastros Regras de Cálculo) esteja configurada para projetar até dezembro e vinculada corretamente ao sindicato dos funcionários.

**SOLUÇÃO**

Para resolver este problema, siga os passos abaixo:

**(1)**Acesse a tela **"Regra de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo) e verifique se o campo de projeção está configurado para dezembro.

![Imagem 1: (1) Acesse a tela "Regra de Cálculo" (Pessoal+ » Cadastros » Regras de Cálculo) e verifique se o campo de projeção está…](https://ajuda.sankhya.com.br/hc/article_attachments/41054122655639)

**(2)**Confirme se a **"Regra de Cálculo"** correta está vinculada ao **"Sindicato"** Pessoal+ » Cadastros » Sindicato) dos funcionários na tela de cadastro.

![Imagem 2: (2) Confirme se a "Regra de Cálculo" correta está vinculada ao "Sindicato" Pessoal+ » Cadastros » Sindicato) dos…](https://ajuda.sankhya.com.br/hc/article_attachments/41054122656791)

**(3)**Caso as configurações estejam corretas e o problema persista, verifique se há alguma **"Parametrização específica"** no cadastro do funcionário que possa estar sobrescrevendo a regra do sindicato.

**(4)**Recalcule a folha de 13º salário após confirmar todas as configurações.

**CAUSA**

O erro ocorre quando há inconsistência entre as configurações da regra de cálculo e o vínculo com o sindicato, ou quando existe alguma configuração específica no cadastro do funcionário que sobrescreve a regra padrão. Também pode ocorrer se a alteração na regra de cálculo foi feita após o cálculo já ter sido processado, sendo necessário recalcular a folha para aplicar as novas configurações.
