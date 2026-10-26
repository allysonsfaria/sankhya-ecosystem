---
id: "7054805037719"
titulo: "Campo 50- Índice do saldo salário para horista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7054805037719-Campo-50-%C3%8Dndice-do-saldo-sal%C3%A1rio-para-horista"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:30:14Z"
rotulos: ["Configuração", "Relatórios", "Folha", "#EnviadoAndreza", "TRCT Portaria Revogada: Modelo ainda usado", "Configuração do Sistema: Atualizar relatórios definir valores em dias ou horas", "Salário Horista: Marcado valor em dias; desmarcado valor em horas", "Pessoal+", "TRCT"]
---

# Campo 50- Índice do saldo salário para horista

#### ![Imagem 1: Breve explicação](https://ajuda.sankhya.com.br/hc/article_attachments/42310211029271) Breve explicação

O TRCT (Termo de Rescisão de Contrato de Trabalho) possui um leiaute previsto anteriormente na Portaria n.º 1.057/2012 que foi revogada pela Portaria n.º 671, no art. 400, LXXV. Apesar da revogação da portaria que levava as configurações do TRCT, os sindicatos continuam utilizando o modelo definido na mesma para validação do documento nas homologações de rescisão, nos casos necessários.

Diante disso, não foi implementado a alteração das palavras no leiaute do TRCT e sim a alteração dos valores apresentados no índice do campo 50-Saldo Salário para o funcionário horista, podendo ser parametrizado se no documento será apresentado o valor em horas ou em dias, conforme configuração abaixo.

#### ![Imagem 2: Configuração no sistema](https://ajuda.sankhya.com.br/hc/article_attachments/42310132450327) Configuração no sistema

**2.1 Local: Pessoal+ >> Configurações >> Painel de Configurações>>Atualizar relatórios da base.**

O usuário **deverá** atualizar os relatórios da base quando atualizar a versão do sistema para a 4.12. Após, não será mais necessário atualizar para essa implementação especificamente.

![Imagem 3: O usuário deverá atualizar os relatórios da base quando atualizar a versão do sistema para a 4.12. Após, não será mais…](https://ajuda.sankhya.com.br/hc/article_attachments/16481583078679)

**2.2 Local: Pessoal+ >> Cadastros >> Regras de Cálculo >> TRCT>>Configurações**

![Imagem 4: 2.2 Local: Pessoal+ >> Cadastros >> Regras de Cálculo >> TRCT>>Configurações](https://ajuda.sankhya.com.br/hc/article_attachments/16481583080599)

**Marcado:** leva no índice do campo 50- Saldo salário o valor em dias

**Desmarcado:** comportamento atual levando no índice do campo 50- Saldo Salário o valor em horas

#### ![Imagem 5: Exemplos](https://ajuda.sankhya.com.br/hc/article_attachments/42310211032727) Exemplos

**3.1 Tipo salário Horista e marcado para trazer o valor em dias.**

![Imagem 6: 3.1 Tipo salário Horista e marcado para trazer o valor em dias.](https://ajuda.sankhya.com.br/hc/article_attachments/16481583084951)

![Imagem 7: 3.1 Tipo salário Horista e marcado para trazer o valor em dias.](https://ajuda.sankhya.com.br/hc/article_attachments/16481583087767)

![Imagem 8: 3.1 Tipo salário Horista e marcado para trazer o valor em dias.](https://ajuda.sankhya.com.br/hc/article_attachments/16481591044375)

![Imagem 9: 3.1 Tipo salário Horista e marcado para trazer o valor em dias.](https://ajuda.sankhya.com.br/hc/article_attachments/16481591046935)

####

**3.2 Tipo salário Horista e desmarcado trazendo o valor em horas (Comportamento atual do sistema).**

![Imagem 10: 3.2 Tipo salário Horista e desmarcado trazendo o valor em horas (Comportamento atual do sistema).](https://ajuda.sankhya.com.br/hc/article_attachments/16481591047703)

![Imagem 11: 3.2 Tipo salário Horista e desmarcado trazendo o valor em horas (Comportamento atual do sistema).](https://ajuda.sankhya.com.br/hc/article_attachments/16481591049623)

![Imagem 12: 3.2 Tipo salário Horista e desmarcado trazendo o valor em horas (Comportamento atual do sistema).](https://ajuda.sankhya.com.br/hc/article_attachments/16481591051671)

![Imagem 13: 3.2 Tipo salário Horista e desmarcado trazendo o valor em horas (Comportamento atual do sistema).](https://ajuda.sankhya.com.br/hc/article_attachments/16481583101207)

Cálculo do índice das horas trabalhadas: horas semanais X semanas no mês/30\* dias trabalhados na referência (44\*5)/30\*8=58,67 arredondando para 59 horas trabalhadas na referência.

**Observação:** para os outros tipos de salário o valor retornado permanecerá em dias, não sendo necessário a parametrização.
