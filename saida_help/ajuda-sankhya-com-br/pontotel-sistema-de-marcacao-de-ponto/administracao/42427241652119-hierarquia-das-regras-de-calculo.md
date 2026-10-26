---
id: "42427241652119"
titulo: "Hierarquia das Regras de Cálculo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427241652119-Hierarquia-das-Regras-de-C%C3%A1lculo"
trilha: "PONTOTEL: Sistema de marcação de ponto > Administração"
atualizado_em: "2026-08-03T12:51:50Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a3328dede1116dd76412528", "sync_hash_19f418956031"]
---

# Hierarquia das Regras de Cálculo

Para que a sua **plataforma de ponto** funcione com máxima eficiência, é essencial compreender como o sistema processa as regras de cálculo quando elas estão presentes em diferentes níveis de cadastro.
Neste artigo, você aprenderá o que é uma regra de cálculo, onde configurá-la e qual a ordem de prioridade que o sistema adota para garantir a **evolução** dos seus processos de RH.

---

## 🧠 O que é uma Regra de Cálculo?

A **Regra de Cálculo** é o "cérebro" das configurações de jornada. É nela que definimos parâmetros essenciais, como:

- Percentuais de horas extras;
- Tolerâncias de atrasos e antecipações;
- Configurações de intervalos e horário noturno;
- Adicional noturno e DSR;
- Customização do espelho de ponto.

É essa regra que garante que os registros dos colaboradores sejam processados de acordo com a legislação e com as políticas internas da sua empresa, trazendo **segurança** e **simplicidade** para o fechamento da folha.

---

## 📍 Onde configurar as regras?

Na **Pontotel**, você tem flexibilidade para personalizar os cálculos em diversos níveis.

### 1. Cadastro de Empregado (Obrigatório)

Este é o local padrão e o único campo **obrigatório** para uma regra de cálculo. Todo colaborador precisa ter uma regra vinculada diretamente em seu cadastro para que o sistema saiba como processar suas horas.

### 2. Outros níveis de cadastro

Você também pode adicionar regras em outros cadastros para atender a exceções ou políticas de grupos. Geralmente, esses campos estão localizados nas **Configurações Avançadas** de cada menu:

- **Local de Trabalho:** Útil para empresas com unidades em cidades diferentes (feriados municipais ou regras sindicais distintas).
- **Escalas:** Quando um grupo específico de trabalho possui regras próprias.
- **Jornadas:** Para aplicar configurações que variam conforme o horário trabalhado.
- **Feriados:** Para definir comportamentos específicos em datas comemorativas.

---

## 🏆 A Hierarquia: Quem vence a "disputa"?

Quando você adiciona uma regra de cálculo em mais de um lugar, o sistema precisa saber qual delas deve prevalecer. Para isso, **a Pontotel** segue uma hierarquia de prioridade.
A regra configurada no nível mais alto da lista abaixo **sempre sobrepõe** as regras que estão nos níveis inferiores. Confira a ordem, do mais forte para o mais básico:

1. **Feriado (Prevalece sobre todas):** Se houver uma regra vinculada a um feriado específico, ela será aplicada ignorando qualquer outra configuração naquele dia.
2. **Jornada:** Caso o dia não seja feriado, o sistema verifica se a jornada que o colaborador está cumprindo possui uma regra própria.
3. **Escala:** Se a jornada não tiver regra, o sistema buscará a configuração definida na Escala do colaborador.
4. **Local:** Não havendo regras nos níveis acima, o sistema aplicará a regra vinculada ao Local de Trabalho do colaborador.
5. **Empregado:** Esta é a regra base. Ela só será aplicada se não houver nenhuma outra regra configurada nos níveis de Feriado, Jornada, Escala ou Local.

![Imagem 1: Empregado: Esta é a regra base. Ela só será aplicada se não houver nenhuma outra regra configurada nos níveis de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/hierarquia-de-regras_120k3ry.png)

---

## 💡 Exemplo Prático

Imagine que um colaborador tem a "Regra Padrão" em seu cadastro (nível 5), mas ele vai trabalhar em um **Feriado** que possui uma regra configurada para pagar 100% de hora extra (nível 1).
Nesse dia, o sistema ignorará a "Regra Padrão" e aplicará a regra do **Feriado**, garantindo que o cálculo seja feito de forma automática e correta.

> 💡 Dicas:

- Sempre que for realizar uma manutenção ou verificação das regras, verifique as "Configurações Avançadas" do cadastro. Manter a hierarquia organizada é o segredo para uma gestão sem esforço e com total confiança nos dados!
- Mantenha sua gestão **simples**: caso sua operação não exija exceções complexas, utilize a regra de cálculo apenas no cadastro do **empregado**. Isso traz mais clareza para o seu dia a dia e garante que o cálculo da jornada seja sempre consistente e fácil de conferir.

---

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
